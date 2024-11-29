# Monitoring MBeans with JConsole

1 Start JConsole by using a script.
    - Example Linux script (filename.sh)#!/bin/bash
################################################################
# This script is assumed to run on the same host where the BPM 
# server is running.
# Change the variable( $HOST, $PROFILE\_NAME, $WAS\_VER, $PORT...) 
# if your environment is different
################################################################

PROFILE\_NAME=StandAloneProfile
WAS\_VER=8.5.0
PORT=2809

HOST=$(hostname)
WAS\_HOME=$HOME/main/deploy2/AppServer
JAVA\_HOME=$WAS\_HOME/java

PROFILE\_HOME=$WAS\_HOME/profiles/$PROFILE\_NAME
BPM\_HOME=$WAS\_HOME
PROVIDER=-Djava.naming.provider.url=corbaname:iiop:$HOST:$PORT

PROPs\_HOME=$PROFILE\_HOME/properties

FILE\_SAS=$PROPs\_HOME/sas.client.props
FILE\_SSL=$PROPs\_HOME/ssl.client.props

CLIENTSAS=-Dcom.ibm.CORBA.ConfigURL=file://$FILE\_SAS
CLIENTSSL=-Dcom.ibm.SSL.ConfigURL=file://$FILE\_SSL

echo "sas file: $FILE\_SAS"
echo "ssl file: $FILE\_SSL"

PROPs=
PROPs="$PROPs $CLIENTSAS"
PROPs="$PROPs $CLIENTSSL"
PROPs="$PROPs $PROVIDER"
echo $PROPs

CLASSPATH=
CLASSPATH=$CLASSPATH:$JAVA\_HOME/lib/tools.jar
CLASSPATH=$CLASSPATH:$BPM\_HOME/runtimes/com.ibm.ws.admin.client\_$WAS\_VER.jar
CLASSPATH=$CLASSPATH:$BPM\_HOME/runtimes/com.ibm.ws.ejb.thinclient\_$WAS\_VER.jar
CLASSPATH=$CLASSPATH:$BPM\_HOME/runtimes/com.ibm.ws.orb\_$WAS\_VER.jar
CLASSPATH=$CLASSPATH:$BPM\_HOME/plugins/javax.j2ee.management.jar
CLASSPATH=$CLASSPATH:$JAVA\_HOME/lib/jconsole.jar

URL=service:jmx:iiop://$HOST:$PORT/jndi/JMXConnector

JARS=$(echo $CLASSPATH |sed s/:/\ /g)

FILE\_SETUPCMD=$PROFILE\_HOME/bin/setupCmdLine.sh

#detect the require file:
for file in $FILE\_SAS $FILE\_SSL $JARS
do 
    if [ ! -e $file ]
	then
	echo "file doesn't exist: $file"
	exit
    fi
done

#exit
. $FILE\_SETUPCMD

$JAVA\_HOME/bin/java -classpath $CLASSPATH $PROPs  sun.tools.jconsole.JConsole $URL
    - Example windows script (filename.bat)@echo off
REM ############################################################
REM # This script is assumed to run on the same host where the 
REM # BPM server is running.
REM # Change the variable( HOST, PROFILE\_NAME, WAS\_VER, PORT...)
REM # if your environment is different
REM ############################################################

set PROFILE\_NAME=
set WAS\_VER=8.5.0
set PORT=2809

set HOST=

REM ************************************************************
REM PD\_HOME is the Process Designer installation path, to reference 
REM to the properties file for connection.
REM ************************************************************
set PD\_HOME=
set JAVA\_HOME=

REM ******************************************************************
REM BPM\_HOME is a directory that stores the necessary jar files copied 
REM from the server
REM ******************************************************************
set BPM\_HOME=
set PROVIDER=-Djava.naming.provider.url=corbaname:iiop:%HOST%:%PORT%

set PROPs\_HOME=%PD\_HOME%/resources

set FILE\_SAS=%PROPs\_HOME%/sas.client.props
set FILE\_SSL=%PROPs\_HOME%/ssl.client.props

set CLIENTSAS=-Dcom.ibm.CORBA.ConfigURL=file:///%FILE\_SAS%
set CLIENTSSL=-Dcom.ibm.SSL.ConfigURL=file:///%FILE\_SSL%

echo "sas file: %FILE\_SAS%"
echo "ssl file: %FILE\_SSL%"

set PROPs=%CLIENTSAS%
set PROPs=%PROPs% %CLIENTSSL%
set PROPs=%PROPs% %PROVIDER%

echo "props: " %PROPs%

REM *******************************************************************************
REM the following jar files in the directory of BPM\_HOME should be copied 
REM from the server 
REM *******************************************************************************
set CLASSPATH=%JAVA\_HOME%\lib\jconsole.jar
set CLASSPATH=%CLASSPATH%;%JAVA\_HOME%\lib\tools.jar
set CLASSPATH=%CLASSPATH%;%BPM\_HOME%\com.ibm.ws.admin.client\_%WAS\_VER%.jar
set CLASSPATH=%CLASSPATH%;%BPM\_HOME%\com.ibm.ws.ejb.thinclient\_%WAS\_VER%.jar
set CLASSPATH=%CLASSPATH%;%BPM\_HOME%\com.ibm.ws.orb\_%WAS\_VER%.jar
set CLASSPATH=%CLASSPATH%;%BPM\_HOME%\javax.j2ee.management.jar

set URL=service:jmx:iiop://%HOST%:%PORT%/jndi/JMXConnector

REM FILE\_SETUPCMD=$PROFILE\_HOME/bin/setupCmdLine.sh

REM $FILE\_SETUPCMD
echo "class path: "  %CLASSPATH%

REM %JAVA\_HOME%\bin\java -classpath %JAVA\_HOME%/lib/jconsole.jar;
REM                 %java\_home%/lib/tools.jar sun.tools.jconsole.JConsole %URL%
REM %JAVA\_HOME%\bin\java -classpath %CLASSPATH% sun.tools.jconsole.JConsole %URL%
%JAVA\_HOME%\bin\java -classpath %CLASSPATH% %PROPs% sun.tools.jconsole.JConsole %URL%
2. In the MBeans tab, locate ProcessMonitor and navigate
to the server that you want.
3. You can see the MBeans operations that are available. Choose the
operation that you want to run, enter parameter values, and click
the operation to run it.