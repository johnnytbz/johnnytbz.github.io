# -*- coding: utf-8 -*-

import logging
import requests
import os
import time
# import urlparse
from urllib.parse import urlparse
from urllib.parse import urlsplit
from urllib import parse
from pyquery import PyQuery as pq
import re
import urllib3


def generateHeaders():
    headersBrower = '''
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding:gzip, deflate, br
Accept-Language:en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
Connection:keep-alive
User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36
    '''

    headersMap = dict()
    for item in headersBrower.splitlines():
        item = str.strip(item)
        if item and ":" in item:
            (key, value) = item.split(":", 1)
            headersMap[str.strip(key)] = str.strip(value)

    return headersMap

# if wiki need login checking, using webbrowse visit wiki, when login then you can get this account cookie information. cookie JSESSIONID
def genereateCookies():
    cookieString = "usertour={\"uid\":\"EOIAZHT\",\"tour_popup\":true}; NSC_TMAC=/cgi/tmlogin; AWSUSER_ID=awsuser_id1627549980316r7635; citrix_ns_id=AAA760NAYTvNlAQAAAAAADv-VisRdPaPJ1Y2O9Z8Ng96phK8eW1jSv6VQ_WONjXBOw==b0dAYQ==-8AeR4v5TZ8Vvz_CjWl8NMeYuBg=; citrix_ns_id_.internal.ericsson.com_/_wat=AAAAAAUkp8PEaeRCZDKeNbnVcGTz0j6c9zu9ff0bAm8iiK8tCXYrd9aF_eBFSiJv6ao7_gqn_jJ_IaClJrXZ8prmuUGJ&; target=HTTP://cpistore.internal.ericsson.com/elex?id=21146; SMSESSION=LOGGEDOFF; NSC_BOD1=AAAIQgAAEIACBsU9gtEbGzJw5UyYlgVcH-5WeplRoMG0G93FmjEZJ6DSgzbeuCiz8qwN684wyMwoZA4ZfnBljpinp-ihRCxnbUR7hKU4mTVO-QluNdNFInGIeum7ML_5rj3dnJ53yo-eqU37M2itR6RTLQ6dPafn1nFY3rHAMqajya3rhR6E8jHkWlV7cZ6_958_D2fAeAhCAAAQgAAEIQAACEIAABMYpgUJGjImQqfZUJY2MmTVrVjJmjNalDn51YFypBXzLNWPUFNA7IekCu_ZA3Vk0t7HNWfzVmAVJmDH2mi75FvBVIyU8leat53qdMmvZ9c5G5s5F-bbFmjGmvV04_ZFjwigPw0ejePQW4lGmTCGjRNNVA8rc1tykqdsf_o9W7xzMXZnKMWPMtLJwmvm46J2aeEAAAhCAAAQgAAEIQAACEIDA-CcQZ8So8TIa7qaUqBlj1lCJMjiKrfpSppnERcaYRVx14L7z_90kHw2eyzEZ8k3zKcZ80PMxUSxR05HsOyJpOaJuwax3elLjxn7kS9PerxKvTSTL5rmrPFMmfOtpzacQD3sxZa17vVtU1MLD-dLJ952WwY6MUUY8IAABCEAAAhCAAAQgAAEIQAACSiCfEbN3715njRjdqjFjomOqeVelxCNjzPQcNR_0VsY6HafUx0jNmMuX_uQYMFoGvZWzTs2JeiRtxmieekvqrhlPONN19DbZWiaNDtl1_-bs1KAIPmbxX70bk_KsxkOjYfT23Bopo3ciCpsdhYwSU-ZCiw7nSyffd8pAb5WuEVfKUG_BzQMCEIAABCAAAQhAAAIQgAAEIFDIiNHv9VHsfkkQ_fKXvyyJrRmjBf7z5T97d8z5r__e6hgOpZ7ISM2YYo9Xw0GNh6gonkLGgDmnfFEsevei5-atFuVw9vivzSEFt38YvugYOGo6vP2TNwruX6kd7DV_wtPDzPQz5RL1yMfB7G_XS1Q6hfLQ8u39jx2OGZPPZDP5sYUABCAAAQhAAAIQgAAEIACB8U2gVIOl1P0rRU_NmESnKWlBz38wLJ3_vNwZNOt6KaVGd9iD9rApEAYRNU3pT5_-UfQuSGpmxN0CWafQ_ORbzzr7JGXGaPSGlkFvv13KQ02Hg-0vO8euv6lddLpTNR5qpOnCu1rmMPcoznaZzN2j1Hg6__6w_ZX3-r29_c5ttTX9KDOmUB6a0K8Pv-9E72gEz-D-d7y0eQEBCEAAAhCAAAQgAAEIQAACE4tAucZKuceNhG5VzBgt4KlDA07EiQ68dVqOLqR68ezvAtOW1HTQ6BGNqki_6d8NaKRmjOavd1DSvNUcUKPALEqr2w9PnpUt31zrlE8H9UmbMWpwxE2ViqtMe70ZXaD21w; NSC_BODY=&ct=dGV4dC9wbGFpbg&bWVzc2FnZT0lNUIlN0IlMjJjaGFubmVsJTIyJTNBJTIyJTJGbWV0YSUyRmhhbmRzaGFrZSUyMiUyQyUyMnZlcnNpb24lMjIlM0ElMjIxLjAlMjIlMkMlMjJzdXBwb3J0ZWRDb25uZWN0aW9uVHlwZXMlMjIlM0ElNUIlMjJjcm9zcy1vcmlnaW4tbG9uZy1wb2xsaW5nJTIyJTJDJTIyd2Vic29ja2V0JTIyJTVEJTdEJTVE; _mkto_cross=true; _cs_mk=0.26495654912380395_1632275295219; _gcl_au=1.1.273301302.1632275295; _mkto_trk=id:891-BLC-619&token:_mch-ericsson.com-1632275301862-19931; _cs_c=2; _fbp=fb.1.1632275302776.452451720; datadome=Gow3~T6mqNWwOe6lv3qpZCmVzrHJZOCKJvf8KT59rKpn28PbXq44MlcktqYzQrFmsaL0IAW_8Fx~iPVY2auAUeyO8kdcmP1FistTH-ZygW; _ga_J8ZRWS5V63=GS1.1.1632275295.1.0.1632276169.0; _ga_G9EF4FD5HD=GS1.1.1632390436.14.1.1632390544.0; _gaexp=GAX1.2.Occzhr5OTtCC9hsOKEcPGg.18951.1; iv=d1259316-4a55-46ac-bdfe-eb94c428f61e; _cs_id=09c48d57-2273-a56e-cb56-fe2257520e70.1632275301.2.1632452228.1632452204.1.1666439301810; _ga=GA1.2.533103167.1623729070; _ga_0WL62SDVS3=GS1.1.1632452199.1.1.1632452235.24; seraph.confluence=770415590:8ea77baef77a18f3f6cf559b7aeb549cff4d595a; confluence.list.pages.cookie=list-content-tree; balance=DC_use; JSESSIONID=D2FE6423D3B4A29B2BF98E168C61E873.node1; AWSSESSION_ID=awssession_id1634308576315r510"
    cookieMap1 = {}
    for item in cookieString.split(";"):
        item = str.strip(item)
        if item and "=" in item:
            (key, value) = item.split("=", 1)
            cookieMap1[str.strip(key)] = str.strip(value)

    return cookieMap1



def save_file(url, path):
    if os.path.exists(path):
        logging.debug("exist path=" + path)
        return

    logging.debug("save %s to %s" % (url, path))

    logging.debug("start get " + url)
	
    proxies={
    'http':'www-proxy.lmera.ericsson.se:8080',
    'https':'www-proxy.lmera.ericsson.se:8080'
    }

    urllib3.disable_warnings()
    resp = requests.get(url, timeout=1000, headers=generateHeaders(), cookies=genereateCookies(), stream=True,verify=False,proxies=proxies)

    if resp.status_code  == 200:
        try:
            with open(path, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                f.close()

            logging.debug("save file " + path)

            time.sleep(3)
        except FileNotFoundError:
            print("Sorry! We don't find.")
            pass          
    else:
        print("error ", resp.status_code)

def parse_host_pageId_fromurl(url):
    # r = urlsplit(url)

    # # print(type(r.scheme),type(r.netloc),type(r.port))

    # # if r.port == None :
    # host = r.scheme + "://" + r.netloc
    # # else :
    #     # host = r.scheme + "://" + r.netloc + ":" + str(r.port)

    # params=parse.parse_qs(r.query,True)
    # print(params)
    # pageId = params["pageId"]

    # return (host, pageId[0])

    print("!!!parse:",url)
    r = urlsplit(url)
    host = r.scheme + "://" + r.netloc
    proxies={
    'http':'www-proxy.lmera.ericsson.se:8080',
    'https':'www-proxy.lmera.ericsson.se:8080'
    }
    urllib3.disable_warnings()	
    resp = requests.get(url, timeout=1000, headers=generateHeaders(), cookies=genereateCookies(), stream=True, verify=False, proxies=proxies)
    if resp.status_code == 200:
        reg=re.compile(r"(?<=pdfpageexport.action\?pageId=)\d+")
        match=reg.search(resp.text)
        if match:
            print("ID:",match.group(0))
            return (host,match.group(0))
            

    print("error ", "cannot find pageID for download in url:", url )
    return 



def get_sub_pages_url(parentUrl):
    print("!!!parentUrl",parentUrl)

    url = "%s/plugins/pagetree/naturalchildren.action?decorator=none&excerpt=false&sort=position&reverse=false&disableLinks=false&expandCurrent=false&hasRoot=true&pageId=%s&treeId=0&startDepth=0" % parse_host_pageId_fromurl(parentUrl)
    print("!!!get_sub_pages_url",url)
    proxies={
    'http':'www-proxy.lmera.ericsson.se:8080',
    'https':'www-proxy.lmera.ericsson.se:8080'
    }
    urllib3.disable_warnings()	
    resp = requests.get(url, timeout=1000, headers=generateHeaders(), cookies=genereateCookies(), stream=True,verify=False,proxies=proxies)

    if resp.status_code == 200:
        doc = pq(resp.text)
        links = []

        for a in doc.find("a").items():
            text = a.text().strip()
            if a.attr("href") and text:
                links.append({
                    "title" : text.encode("utf-8"),
                    "href" : parse.urljoin(parentUrl, a.attr("href"))
                })
        print("links:",links)
        return links

    else :
        logging.error("failed get url %s status_code=%d " % (url, resp.status_code))

    return []

def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)
    return new_title

def export_wiki(wiki_title, wiki_page_url, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
	
    print("!!!Export:",wiki_page_url)
    export_url = "%s/spaces/flyingpdf/pdfpageexport.action?pageId=%s" % parse_host_pageId_fromurl(wiki_page_url)
    print(dir,'',wiki_title)
    wiki_title=validateTitle(wiki_title)
    wiki_title = wiki_title.replace(" ", "")
    save_file(export_url, dir + "/" + wiki_title + ".pdf")

    subpages = get_sub_pages_url(wiki_page_url)
    if subpages :
        parentdir = dir + "/" + wiki_title
        if parentdir.find('Iota/Aboutus')>=0 or parentdir.find('Iota/Architectureandsystemdesign')>=0 :
            pass
        else :
            for subpage in subpages :
                export_wiki(str(subpage["title"],encoding = "utf8"), subpage["href"], parentdir)


logging.basicConfig(level=logging.DEBUG)

# modify generateHeaders and genereateCookies setting first
wiki_page_url = "https://eteamspace.internal.ericsson.com/display/IoTA/IoT+Accelerator+Home"
wiki_title = "Iota"
# wiki_page_url = "https://eteamspace.internal.ericsson.com/display/IoTA/Solution+Descriptions"
# wiki_title = "SolutionDescriptions"
dir = "C:/backup"
export_wiki(wiki_title, wiki_page_url, dir)
