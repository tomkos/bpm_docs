# Updating desktop IBM
Process Designer
(deprecated)

## About this task

## Procedure

1. Uninstall the current instance of desktop Process Designer by using Installation Manager or the
Uninstall icon on the Start menu.
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
5 Run one of the following commands to update desktop Process Designer . Use the same command that you usedto install desktop Process Designer . Default location (C:\IBM\ProcessDesigner\v8.5 ) Different location If the location has spaces in the directory name, put the whole location in quotation marks. The following examples show how to install to a different location.
    - installProcessDesigner\_admin.bat
    - installProcessDesigner\_nonadmin.bat
    - installProcessDesigner\_admin.bat
installLocation
    - installProcessDesigner\_nonadmin.bat
installLocation
    - installProcessDesigner\_admin.bat D:\IBM\PD
    - installProcessDesigner\_admin.bat "D:\Process Designer\"

## Results

Installation messages are recorded in the file
%TEMP%\IBMProcessDesignerInstall.log, where the %TEMP%
variable is typically set to C:\Documents and
Settings\current\_user\_name\Local Settings\Temp.