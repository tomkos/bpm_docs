# Installing the desktop IBM
Process Designer
(deprecated)

## About this task

## Procedure

1. From the machine you intend to install desktop Process Designer on, open
Workflow Center. Note the
host and port in its URL.
2. In the following URL, replace WORKFLOW\_CENTER\_HOST and
WORKFLOW\_CENTER\_PORT with the host and port you use to access Workflow Center. 
 https://WORKFLOW\_CENTER\_HOST:WORKFLOW\_CENTER\_PORT/ProcessCenter/repository/com.lombardisoftware.repository.Repository/downloadDesigner?platform=win&url=https://WORKFLOW\_CENTER\_HOST:WORKFLOW\_CENTER\_PORT
3. Open the URL in a browser to download the desktop Process Designer and extract
the contents of the IBM Process Designer.zip file to a temporary directory on
your file system.
4. Open a command window and change to the
directory where you extracted the contents of the IBM Process
Designer.zip file. Important: If
you are running Windows, start your command prompt
by right-clicking and selecting Run as administrator.
5 Run one of the following commands to install the desktop Process Designer . If you are inthe Administrators group on Windows, you can install usingthe admin command. If you are not an administrative user, or if you want to install to your ownusername without administrative privileges, install using the nonadmin command. Default location (C:\IBM\ProcessDesigner\v8.5 ) Different location If the location has spaces in the directory name, put the whole location in quotation marks. The following examples show how to install to a different location.
    - installProcessDesigner\_admin.bat
    - installProcessDesigner\_nonadmin.bat
    - installProcessDesigner\_admin.bat
installLocation
    - installProcessDesigner\_nonadmin.bat
installLocation
    - installProcessDesigner\_admin.bat D:\IBM\PD
    - installProcessDesigner\_admin.bat "D:\Process Designer\"

## Results

## What to do next

- The SSL certificate does not have revocation information, which may lead to warnings in someversions of Internet Explorer. To resolve this issue, disable the certificate revocation in Internet Explorer:
    1. Go to Internet Explorer > Tools > Internet options.
    2. Click the Advanced tab.
    3. From the Security section, deselect Check for server certificate
revocation.
    4. Restart Internet Explorer and desktop Process Designer.
- The signer certificate is not trusted by the browser. To resolve this issue, install the signer
certificate into your Windows trust store.Note: Make sure
that you select the top-level signer certificate from the certification tree.

- Recovering from an out of memory exception while installing desktop Process Designer (deprecated)

On some systems, downloading IBM Process Designer might fail because of insufficient memory.

## Related tasks

- Updating IBM Process Designer

## Related information

- Process Designer window is blank