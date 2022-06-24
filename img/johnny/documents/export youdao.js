var exported = {}
function warn(obj) {console.warn(obj)}
function error(obj) {console.error(obj)}
function send_contextmenu(obj) {

var rect = obj.getClientRects()[0]
var evObj = document.createEvent('MouseEvents');
evObj.initMouseEvent('contextmenu',true,true,window,1,0,0,rect.left,rect.top,false,false,false,false,0,null);
obj.dispatchEvent(evObj);
}
function scrol(obj, y){

var evt = document.createEvent('MouseEvents');
evt.initEvent('wheel', true, true);
evt.deltaY = +y;
var element = obj;
element.dispatchEvent(evt);
}
var pages = $('.file-item .title');
function download_page(index) {

if (index >= pages.length) {
    newpages = $('.file-item .title');
    if (newpages.length > pages.length) {
        pages = newpages
        error('导出下一页，总数:'+index)
    } else {
        error('导出结束，总数:'+index)
    }
}
var obj = pages[index]
var top = obj.getClientRects()[0].top
if (top>500) {
    scrol($('.abstract-mode')[0], 300)
}
var that = $(obj)
var title = $.trim(that.text());
if (exported[title]) return;
console.warn(index+' 导出:'+title)
send_contextmenu(obj)
setTimeout(function(){
    var action = $.trim($($('.menu-li .menu-label')[6]).text())
    if (action == '导出为Word') $('.menu-li .menu-label')[6].click()
    else error(action +' 不支持')
    index++
    download_page(index)
},3000)
}
function start() {

warn('开始导出，总数：' + pages.length)
download_page(0)
}
start()