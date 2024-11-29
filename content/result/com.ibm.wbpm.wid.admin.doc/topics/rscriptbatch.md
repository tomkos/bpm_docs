<!-- image -->

# Example of a batch file to launch a script

The runAntWid batch file or shell script provided in IBM® Integration
Designer in the <installdir>\bin directory is used to launch
your script, which is passed as a parameter to it. You will need to
edit one line of this batch file as it indicates the path and name
of your workspace. The following example shows that the workspace
to be used with your Ant script is workspacefortesting.
Note that the workspace must be qualified with an absolute path.

```
@echo off
setlocal
set BASE\_DIR=%~dp0
set VMARGS=-Xms512m -Xmaxf0.1 -Xminf0.05 -Xmx1024m -Xgcpolicy:gencon -Xscmx96m -Xshareclasses:singleJVM,keep -XX:MaxPermSize=512M -Xss2048k -Dsun.java2d.noddraw=true:java

set JAVA\_HOME=%BASE\_DIR%..\eclipse\jdk
@if not exist "%JAVA\_HOME%\jre\bin" set JAVA\_HOME=%BASE\_DIR%..\jdk
@if not exist "%JAVA\_HOME%\jre\bin" echo ERROR: JAVA\_HOME must point to Java installation containing jre\bin
@if not exist "%JAVA\_HOME%\jre\bin" goto done

:startup
set STARTUP\_JAR="%BASE\_DIR%..\startup.jar"
@if not exist %STARTUP\_JAR% set STARTUP\_JAR="%BASE\_DIR%..\eclipse\startup.jar"
@if not exist %STARTUP\_JAR% echo ERROR: Unable to locate Eclipse startup.jar
@if not exist %STARTUP\_JAR% goto done

:workspace
if not $%WORKSPACE%$==$$ goto check
REM #######################################################
REM ##### you must edit the "WORKSPACE" setting below #####
REM #######################################################
REM *********** The location of your workspace ************
set WORKSPACE=F:\Program Files\IBM\WID61\workspacefortesting

:check
REM ************* The location of your workspace *****************
if not exist "%WORKSPACE%" echo ERROR: incorrect workspace=%WORKSPACE%, edit this runAnt.bat and correct the WORKSPACE envar
if not exist "%WORKSPACE%" goto done

:run
@echo on
"%JAVA\_HOME%\jre\bin\java.exe" %VMARGS% -Dwtp.autotest.noninteractive=true -cp %STARTUP\_JAR% org.eclipse.core.launcher.Main -application com.ibm.etools.j2ee.ant.RunAnt -data "%WORKSPACE%"  %*
@if %ERRORLEVEL% EQU 0 goto done
@if %ERRORLEVEL% EQU 13 echo runAnt BUILD FAILED.
@if %ERRORLEVEL% EQU 13 goto done
@if %ERRORLEVEL% EQU 15 echo WORKSPACE is already BEING USED.
@if %ERRORLEVEL% EQU 15 goto done
@if %ERRORLEVEL% EQU 23 echo totally clean (UNINITIALIZED) workspace, it is now setup.  will rerun...
@if %ERRORLEVEL% EQU 23 goto run
@echo runAnt FAILED? (return code %ERRORLEVEL%)
:pause
@pause

:done
```