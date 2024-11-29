<!-- image -->

# Working with scripts

## About this task

IBM® Integration
Designer includes
the capability for working with projects other than modules and libraries.
It also includes the following batch files that you can use to invoke
Ant scripts for running IBM Integration
Designer builds:

- runAnt.bat
- runAntWID.bat

These files are located in the WID\_home\bin directory
(where WID\_home is the installation path of IBM Integration
Designer).

It
is recommended that you use the runAntWID.bat file. This file is similar
to the runAnt.bat file, but the runAntWID.bat file sets up the classpath
to help avoid potential problems when building IBM Integration
Designer projects.

If
you are using the Linux operating system and the JAVA\_HOME environment
variable has not been set, the IBM Integration
Designer JVM
is automatically used by the runAntWID.sh file. However, if JAVA\_HOME
has been set, you will need to change it to point to the IBM Integration
Designer JVM
by referencing the following directory:

Integration\_Designer\_installation\_path/jdk

For
example:

/opt/ibm/IntegrationDesigner/v8.5/jdk

Follow
these steps to create and run an Ant script.

## Procedure

1 Generate an encrypted password. As discussed in the Overview of testing with Ant scripts in headless IBM Integration Designer , an encrypted passwordis not required. However, if you are sharing your script and wantto keep the password confidential then an encrypted password is recommended.A utility is provided for you to generate the encrypted password.
    1. In the <installdir>\bin directory,
edit runAntWidSecurity, add a password and
save the file.
    2. Run runAntWidSecurity to generate
your encrypted password.
2 Create a script. The following sample is an indicationof the type of script you might create. The script beginswith a list of properties, which is an effective way of using variablesthat can be changed rather than using hard-coded values. The propertiesprovide information on your CVS userid, password, the CVS stream,modules required and so on. The script then checks out modulesfrom the Concurrent Versions System (CVS) system and then importsthe modules into IBM IntegrationDesigner .Once inside, the modules are deployed to a server and run. Yourencrypted password should be used as the password for your server. Anumber of these tasks are standardAnt tasks which are well-known to users who work with Ant in Eclipse . However, some special taskshave been added for WebSphere Integration Edition. They are describedin Additional Ant tasks . CVSalso has some CVS commands that you should know if yourscript will be extracting files from a CVS repository. <project name="Automated Test Case Run" basedir="." default="run"> <property name="password" value="mypassword"/> <property name="user" value="myuserid"/> <property name="module" value="OrderEntry"/> <property name="testp" value="OrderTest"/> <property name="testfile" value="OrderTest.xml"/> <property name="url" value="http://localhost:9080/OrderTestWeb/TestServlet"/> <property name="cvsroot" value=":pserver:${user}:${password}@cvs.mycorporation.com:/cvs/wid/wbit\_comptest"/> <property name="extract.dir" value="F:\Program Files\IBM\WID61\workspacetestscript"/> <property name="cvs.stream" value="HEAD"/> <property name="log.filename" value="./cvsextract"/> <target name="checkout"> <cvs cvsroot="${cvsroot}" cvsrsh="ssh" dest="${extract.dir}" package="TestCase/${module}" command="export -r ${cvs.stream} -d ${module}" output="${log.filename}m.log" quiet="true"/> <cvs cvsroot="${cvsroot}" cvsrsh="ssh" dest="${extract.dir}" package="TestCase/${testp}" command="export -r ${cvs.stream} -d ${testp}" output="${log.filename}t.log" quiet="true"/> </target> <!-- checking out from CVS does not make modules visible to eclipse, need to import those projects now --> <target name="importProject" depends="checkout"> <importProject projectName="${module}"/> <importProject projectName="${testp}"/> </target> <target name="build" depends="importProject"> <projectBuild projectName="${module}"/> <projectBuild projectName="${testp}"/> </target> <target name="deploy" depends="build"> <wid.deploy projectName="${module}" userid="admin" password="{xor}PjsyNjE=" profile="wps" connectionType="SOAP" port="8880"/> <wid.deploy projectName="${testp}"/> </target> <target name="run" depends="deploy"> <get dest="${testfile}" src="${url}"/> <wid.undeploy projectName="${module}"/> <wid.undeploy projectName="${testp}"/> </target></project> Several other examples of scripts areavailable:

The script begins
with a list of properties, which is an effective way of using variables
that can be changed rather than using hard-coded values. The properties
provide information on your CVS userid, password, the CVS stream,
modules required and so on.

The script then checks out modules
from the Concurrent Versions System (CVS) system and then imports
the modules into IBM Integration
Designer.
Once inside, the modules are deployed to a server and run.

Your
encrypted password should be used as the password for your server.

A
number of these tasks are standard
Ant tasks which are well-known to users who work with Ant in Eclipse. However, some special tasks
have been added for WebSphere Integration Edition. They are described
in Additional Ant tasks. CVS
also has some CVS commands that you should know if your
script will be extracting files from a CVS repository.

```
<project name="Automated Test Case Run" basedir="." default="run">
   <property name="password" value="mypassword"/>
   <property name="user" value="myuserid"/>
   <property name="module" value="OrderEntry"/>
   <property name="testp" value="OrderTest"/>
   <property name="testfile" value="OrderTest.xml"/>
   <property name="url" value="http://localhost:9080/OrderTestWeb/TestServlet"/>
   <property name="cvsroot" value=":pserver:${user}:${password}@cvs.mycorporation.com:/cvs/wid/wbit\_comptest"/>
   <property name="extract.dir" value="F:\Program Files\IBM\WID61\workspacetestscript"/>
   <property name="cvs.stream" value="HEAD"/>
   <property name="log.filename" value="./cvsextract"/>

   <target name="checkout">
      <cvs cvsroot="${cvsroot}" cvsrsh="ssh" dest="${extract.dir}" package="TestCase/${module}" command="export -r ${cvs.stream} -d ${module}" output="${log.filename}m.log" quiet="true"/>
      <cvs cvsroot="${cvsroot}" cvsrsh="ssh" dest="${extract.dir}" package="TestCase/${testp}" command="export -r ${cvs.stream} -d ${testp}" output="${log.filename}t.log" quiet="true"/>
   </target>
   
   <!-- checking out from CVS does not make modules visible to eclipse, need to import those projects now -->
   <target name="importProject" depends="checkout">
      <importProject projectName="${module}"/>
      <importProject projectName="${testp}"/>
   </target>
   
   <target name="build" depends="importProject">
      <projectBuild projectName="${module}"/>
      <projectBuild projectName="${testp}"/>
   </target>
   
   <target name="deploy" depends="build">
      <wid.deploy projectName="${module}" userid="admin" password="{xor}PjsyNjE=" profile="wps" connectionType="SOAP" port="8880"/>
      <wid.deploy projectName="${testp}"/>
   </target>
   
   <target name="run" depends="deploy">
      <get dest="${testfile}" src="${url}"/>
      <wid.undeploy projectName="${module}"/>
      <wid.undeploy projectName="${testp}"/>
   </target>
</project>
```

- Creating a script for test cases that rarely change
- Creating a script for test cases that change frequently
- Creating a script for test cases stored in a CVS repository, which
is similar to the one shown.
3 If you have referenced some proprietary environment variablesin the test suite editor for a component test project, test suite,or test case, and you want to define the environment variables inthe servlet URL, you can use the following syntax: http://myHost:9080/MyTestWeb/TestServlet?DRUG=drug%20claim&AMOUNT=100&DATE=2011-07-05 Inthe example, there are three environment variable definitions appendedto the end of the URL. Each definition must be separated by an ampersand(&) character. In the URL, the escape code %20 isused to encode a space because the URL does not allow certain ASCIIcharacters. In the example, the three environment variablesthat are defined are:

```
http://myHost:9080/MyTestWeb/TestServlet?DRUG=drug%20claim&AMOUNT=100&DATE=2011-07-05
```

In
the example, there are three environment variable definitions appended
to the end of the URL. Each definition must be separated by an ampersand
(&) character. In the URL, the escape code %20 is
used to encode a space because the URL does not allow certain ASCII
characters.

In the example, the three environment variables
that are defined are:

- DRUG: "drug claim"
- AMOUNT: 100
- DATE: 2011-07-05
4. Once you have your script, you need to edit the runAntWid batch
file or shell script to point to the correct workspace. runAntWid is
found in the <installdir>\bin directory. In
this sample, the workspace is workspacetestscript.
Note that the workspace is fully qualified to indicate drive and path
(or home and path on a Linux system). @echo off
setlocal
set BASE\_DIR=%~dp0
set VMARGS=-Xms512m -Xmaxf0.1 -Xminf0.05 -Xmx1024m -Xgcpolicy:gencon -Xscmx96m -Xshareclasses:singleJVM,keep -XX:MaxPermSize=512M -Xss2048k

set JAVA\_HOME=%BASE\_DIR%..\eclipse\jdk
@if not exist "%JAVA\_HOME%\jre\bin" set JAVA\_HOME=%BASE\_DIR%..\jdk
@if not exist "%JAVA\_HOME%\jre\bin" echo ERROR: JAVA\_HOME must point to Java installation containing jre\bin
@if not exist "%JAVA\_HOME%\jre\bin" goto done

:startup
set STARTUP\_JAR="%BASE\_DIR%..\startup.jar"
@if exist "%BASE\_DIR%..\eclipse.exe" goto im

for /f "delims= tokens=1" %%c in ('dir /B /S /OD "%BASE\_DIR%..\eclipse\plugins\org.eclipse.equinox.launcher\_*.jar"') do set STARTUP\_JAR=%%c
goto checkstartup

:im
for /f "delims= tokens=1" %%c in ('dir /B /S /OD "%BASE\_DIR%..\plugins\org.eclipse.equinox.launcher\_*.jar"') do set STARTUP\_JAR=%%c

:checkstartup
@if not exist "%STARTUP\_JAR%" echo ERROR: Unable to locate Eclipse startup.jar
@if not exist "%STARTUP\_JAR%" goto done

:workspace
if not $"%WORKSPACE%"$==$$ goto check
REM #######################################################
REM ##### you must edit the "WORKSPACE" setting below #####
REM #######################################################
REM *********** The location of your workspace ************
set WORKSPACE=X:\MyWorkspace

:check
REM ************* The location of your workspace *****************
if not exist "%WORKSPACE%" echo ERROR: incorrect workspace=%WORKSPACE%, edit this runAntWid.bat and correct the WORKSPACE envar
if not exist "%WORKSPACE%" goto done

:run
@echo on
"%JAVA\_HOME%\jre\bin\java.exe" %VMARGS% -Dwtp.autotest.noninteractive=true -cp "%STARTUP\_JAR%" org.eclipse.core.launcher.Main -application com.ibm.wbit.comptest.ant.RunAntWid -data "%WORKSPACE%"  %*
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

:doneAs an alternative to modifying the script, you
can set the workspace environment variable. For example: set
WORKSPACE=G:\workspacefinaltest.
See Example of a batch file to launch a script for another similar
example of a batch file.
5. Next create a batch file or shell script
that will launch your script as a parameter to the runAntWid batch
file. Although you can launch the script yourself from a command window,
in most cases it is convenient to create a batch file or shell script
and have your operating system launch your script late at night when
computer time is available. In our example, runAntWid is
launched and the script it runs, doAll.xml, is found
in the testscript directory on e: drive.
pushd f:\Program Files\IBM\WID61\bin
runAntWid -buildfile e:\testscript\doAll.xml
popd
The batch file is a convenience. You could also run
the script from a command window by typing runAntWid -buildfile <directory>
6. Run the batch file or shell script or, much more likely,
use the operating system's services to run it for you at a convenient
time. This is, of course, the biggest advantage of using scripts:
the scripts can be run at times convenient to you such as nights and
weekends.
7. Examine the pass/fail results in the returned XML file.
This file will be placed in the same directory as defined in your
script. See Example of an XML output file,
which shows an example of the type of output you should expect.