---
layout: post
title: robot framework test case
subtitle: How to run robot-tests Windows 10 locally
tags: [technology]
comments: true
---

This is a simple robot test case, you can run in your laptop locally. As your first step in exploring robot framework.

## what is robotframework?
Robot framework is a generic open source automation framework.
[https://robotframework.org/](https://robotframework.org/)

## how to install

### 1.Install Git
Download and install Git-2.9.0-64-bit.exe from https://github.com/git-for-windows/git/releases. 

~~~
When launching Git Bash, Git CMD and Git GUI in Windows 10 it has been observed that for some users the current working directory becomes H:\ instead of C:\Users\<your user name>\. To correct that do the following:

1.Launch Windows Explorer.
2.Navigate to the folder containing the Git Bash, Git CMD and Git GUI shortcuts, e.g. C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Git\.
3.Right-click Git Bash and select Properties.
4.Select the Shortcut tab.
5.Modify the Target field to contain only: "C:\Program Files\Git\git-bash.exe"
6.Modify the Start in field to contain: %USERPROFILE%
7.Click OK, Continue and Yes to confirm the modification.
8.Repeat the steps for Git CMD and Git GUI.

Also add environment variable HOME in Windows 10 as follows:
1.Launch Control Panel (Press the Windows button to the bottom left → Windows System → Control Panel → System and Security → System → Advanced system settings → Environment Variables)
2.In the 'User variables ...' section press 'New ...'.
3.Enter HOME as variable name.
4.Enter %USERPROFILE% as variable value and press the OK button.
~~~

### 2.Install Python

**Warning:** Do NOT install Python 3.X. The Robot Framework does not have support for Python 3.X.
{: .box-warning}

Download and install python-2.7.9.amd64.msi from https://www.python.org/downloads/. 

In the install wizard ensure to explicitly select "Will be installed on local harddrive" for both "pip" and "Add python.exe to Path". If you accidently forget that you'll have to either unistall Python and then reinstall it, or manually install pip and set the Windows PATH environment variable by adding C:\Python27;C:\Python27\Scripts if that's where you installed python.

#### Python install verification
Test from command line Python is properly installed and PATH settings are working.
~~~
python --version
Python 2.7.9
~~~


### 3.Install pip

For Windows pip is included by default in Python 2.7.9 and later. 
So if you during Python installation selected "Will be installed on local harddrive" for "pip" then the only thing needed is to run the following (remember the proxy settings) in the Windows Command Prompt where Command Prompt must be run as administrator:
~~~
python -m ensurepip
~~~
#### pip install verification
~~~
pip --version
pip 1.5.6 from C:\Python27\lib\site-packages (python 2.7)
~~~


### 4.Install Robot Framework
Install the Robot Framework using PIP which works (remember the proxy settings).

{: .box-warning}
**Warning:**For Windows users there is also windows installer available at http://code.google.com/p/robotframework/wiki/Installation#Windows_installer (e.g. robotframework-2.9.1.win-amd64.exe), although Python package manager is preferred to be used installing all Robot Framework related software.

{: .box-warning}
**Warning:**For Windows users the Command Prompt should be launched as administrator for the following command(s) to run successfully.
~~~
pip install robotframework==3.0.2
~~~

#### Verification
Verify Robot Framework is installed successfully by running the following:
~~~~
pybot --version
Robot Framework 3.0.2 (Python 2.7.9 on win32)
~~~~


### 5.Install Robot Framework libraries
#### 5.1. Install the Selenium2Library and httplibrary for web testing
Install the Robot Framework Selenium2Library using Python package manager (remember the proxy settings).

{: .box-warning}
**Warning:**For Windows users the Command Prompt should be launched as administrator for the following command(s) to run successfully.
~~~
pip install decorator==4.0.10
pip install selenium==2.53.6
pip install --no-deps robotframework-selenium2library==1.8.0
pip install waitress==0.9.0
pip install beautifulsoup4==4.4.1
pip install WebOb==1.6.1
pip install six==1.10.0
pip install --no-deps webtest==2.0.21
pip install --no-deps robotframework-httplibrary==0.4.2
~~~
In order to run tests with multiple browsers environment, selenium needs browser specific configurations as outlined in the following sub-chapters.

### 5.2 Install/configure Firefox

Download and install Firefox Setup 46.0.1.exe from https://www.mozilla.org/en-US/firefox/releases/ (64-bit). 
If you intend to use a more recent Firefox release, you will probably have to download and install Mozilla GeckoDriver (geckodriver-v0.19.1-win64.zip) from http://www.seleniumhq.org/download/. Click on the version number and then click on geckodriver-v0.19.1-win64.zip. Extract it in C:\Python27\. 

### 5.3 Install/configure Chrome
### 5.3.1 Install Chrome
Download and install Google Chrome from https://www.google.com/chrome/.

It's not possible to download and install a particular Chrome version. The latest version is the only version available which is automatically installed when downloaded. Because of that there is no point in specifying here a particular Chrome version to download/install.

### 5.3.2 Configure Chrome
Disable automatic Chrome updates in order to have a stable test environment by launching Windows Task Scheduler (Start → All Programs → Accessories → System Tools → Task Scheduler) and disable the following jobs.

![Crepe](/img/docker/image2018-7-25_15-55-50.png)

Launch Task Manager (Start → Windows Administrative Tools → Task Scheduler) and terminate the two processes indicated above in the Task Scheduler screenshot.

And to be on the safe side, rename folder ...
~~~
C:\Program Files (x86)\Google\Update
~~~
... to ...
~~~
C:\Program Files (x86)\Google\Update2
~~~

### 5.3.3 Install chromedriver
Download and install chromedriver_win32.zip (version 2.35) from http://www.seleniumhq.org/download/ (click on the "Google Chrome Driver" link) and extract it in C:\Python27\. 

{: .box-warning}
**Warning:**No 64-bit version of the Google Chrome Driver is available for Windows, but the 32-bit version has been verified to work with the 64-bit version of Google Chrome. Even though not verified, it's likely to believe that the 32-bit version of Google Chrome works too with the 32-bit Google Chrome Driver if ever needed.


### 6.using chinese repositries
~~~
python -m pip install robotframework==3.0.2 -i http://pypi.douban.com/simple/
python -m pip install decorator==4.0.10 -i http://pypi.douban.com/simple/
python -m pip install selenium==2.53.6 -i http://pypi.douban.com/simple/
python -m pip install --no-deps robotframework-selenium2library==1.8.0 -i http://pypi.douban.com/simple/
python -m pip install waitress==0.9.0 -i http://pypi.douban.com/simple/
python -m pip install beautifulsoup4==4.4.1 -i http://pypi.douban.com/simple/
python -m pip install WebOb==1.6.1 -i http://pypi.douban.com/simple/
python -m pip install six==1.10.0 -i http://pypi.douban.com/simple/
python -m pip install --no-deps webtest==2.0.21 -i http://pypi.douban.com/simple/
python -m pip install --no-deps robotframework-httplibrary==0.4.2 -i http://pypi.douban.com/simple/
python -m pip install suds==0.4 -i http://pypi.douban.com/simple/
python -m pip install --no-deps robotframework-sudslibrary==0.8 -i http://pypi.douban.com/simple/
python -m pip install cx-Oracle==7.0.0 -i http://pypi.douban.com/simple/
python -m pip install requests==2.6.0 -i http://pypi.douban.com/simple/
python -m pip install robotframework-requests==0.4.5 -i http://pypi.douban.com/simple/
python -m pip install ecdsa==0.13 -i http://pypi.douban.com/simple/
python -m pip install pycrypto==2.6 -i http://pypi.douban.com/simple/
python -m pip install --no-deps paramiko==1.15.2 -i http://pypi.douban.com/simple/
python -m pip install --no-deps robotframework-sshlibrary==2.1.2 -i http://pypi.douban.com/simple/
python -m pip install jsonpointer==1.10 -i http://pypi.douban.com/simple/
python -m pip install --no-deps jsonpatch==1.14 -i http://pypi.douban.com/simple/
python -m pip install docutils==0.12 -i http://pypi.douban.com/simple/
python -m pip install future==0.16.0 -i http://pypi.douban.com/simple/
python -m pip install --no-deps robotframework-imaplibrary==0.3.0 -i http://pypi.douban.com/simple/
python -m pip install kafka-python==1.4.6 -i http://pypi.douban.com/simple/
python -m pip install --no-deps robotframework-kafkalibrary==0.0.2 -i http://pypi.douban.com/simple/
python -m pip install lxml==3.4.4 -i http://pypi.douban.com/simple/
python -m pip install pyasn1==0.1.9 -i http://pypi.douban.com/simple/
python -m pip install --no-deps scp==0.10.2 -i http://pypi.douban.com/simple/
python -m pip install wget==3.2 -i http://pypi.douban.com/simple/
python -m pip install robotframework-pabot==0.45 -i http://pypi.douban.com/simple/
python -m pip install pyotp==2.3.0 -i http://pypi.douban.com/simple/
python -m pip install PyJWT==1.7.1 -i http://pypi.douban.com/simple/
python -m pip install elasticsearch==7.0.5 -i http://pypi.douban.com/simple/
python -m pip install urllib3==1.25.6 -i http://pypi.douban.com/simple/
python -m pip install websocket==0.2.1 -i http://pypi.douban.com/simple/
python -m pip install websocket-client==0.56.0 -i http://pypi.douban.com/simple/
python -m pip install robotframework-databaselibrary==0.8.1 -i http://pypi.douban.com/simple/
python -m pip install pymongo==3.5.1 -i http://pypi.douban.com/simple/
python -m pip install --no-deps robotframework-mongodblibrary==0.3.4 -i http://pypi.douban.com/simple/
~~~

## how to run test case

robot test file save as hello.robot
~~~
*** Settings ***
Documentation     Example using the space separated format.
Library           OperatingSystem

*** Variables ***
${MESSAGE}        Hello, world!

*** Test Cases ***
My Test
    [Documentation]    Example test.
    Log    ${MESSAGE}
    My Keyword    ${CURDIR}

Another Test
    Should Be Equal    ${MESSAGE}    Hello, world!

*** Keywords ***
My Keyword
    [Arguments]    ${path}
    Directory Should Exist    ${path}
~~~

run this command in CMD
~~~
pybot hello.robot
~~~

![Crepe](/img/docker/robot_test_01.png)

and you can check report on log.html

![Crepe](/img/docker/robot_test_02.png)


