# Modifying the size and location of Case Builder CBE log files

## About this task

- icm/icm\_casebuildercbe%g.log
- icm/icmcbe%g.log

The icm path is relative to the profile directory of your
application server. For example, the path might be /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/icm.

IBM® Business Automation
Workflow configuration editor sets the
-DICMCBELogFilePattern=icm/icmcbe%g.log property during the Deploy Case Manager API task. This
setting redirects the content-logged entries that otherwise would go into
icm\_casebuildercbe%g.log file to the icmcbe%g.log file
resulting in one log file instead of two log files. You can modify this property to change the
location of the log file.

## Procedure

To modify log file options for the CBE log files:

- Modify the log file location and generate one log fileinstead of two log files:
    1. In the WebSphere® Application
Server administration
console, add the ICMCBELogFilePattern property to the Java™ Virtual Machine (JVM) configuration settings.
Click Application servers > server > Process definition > Java Virtual Machine.
    2. In the Generic JVM arguments field,
modify the ICMCBELogFilePattern property to create a single log file.
In the following example, a single log file (icmcbe%g.log) is created
in the system temporary directory (%t, for the /tmp
directory on AIX®, Linux®, or Linux on system Z):
-DICMCBELogFilePattern=%t/icmcbe%g.log

If you prefer, you can direct the logging to a specific folder, such as
/icm/logs. For example, specify
-DICMCBELogFilePattern=/icm/logs/icmcbe%g.log (for AIX, Linux, or Linux on system Z) or
-DICMCBELogFilePattern=C:\icm\logs\icmcbe%g.log (for Windows).
Restriction: WebSphere Application
Server does not create folders for you. The folder that you
specify for the log files must already exist. For example, if you direct the log files to the
C:\icm\logs\ folder, you must ensure that the icm\logs
folder exists on the C: drive.
    3. Save your changes and restart WebSphere Application
Server.
When
you use Case Builder to copy
a solution, for example, the log files are written in the location
that you specified. Using icmcbe%g as the sample
file name, the first log file is named icmcbe0.log,
followed by the icmcbe1.log, and so on.
- Modify the maximum size of the log files:

1. In the WebSphere Application
Server administration
console, add the ICMCBELogMaxSize property to the Java Virtual Machine
(JVM) configuration settings. Click Application
servers > server > Process
definition > Java Virtual Machine.
2. In the Generic JVM arguments field,
modify the ICMCBELogMaxSize property to control the maximum size of
the log, in bytes.
By default, the maximum log file size is 500 MB (524288000 bytes). In the
following example, the maximum log file size is 500
MB:
 -DICMCBELogMaxSize=524288000
3. Save your changes and restart WebSphere Application
Server. When the log file reaches
a size of 5 MB, it is renamed from icmcbe0.log to icmcbe1.log,
and a new log file is started with the name icmcbe0.log.
- Modify the maximum number of log files:

1. In the WebSphere Application
Server administration
console, add the ICMCBELogCount property to the Java Virtual Machine
(JVM) configuration settings. Click Application
servers > server > Process
definition > Java Virtual Machine.
2. In the Generic JVM arguments field,
modify the ICMCBELogCount property to control the maximum number of
logs.
By default, the maximum number of logs is 5. In the
following example, the maximum number of logs is 5:
-DICMCBELogCount=5
3. Save your changes and restart WebSphere Application
Server. When five log files
are written and the newest log file reaches the maximum log file size, the oldest log file is
deleted.
- Change the logging level for IBM Business AutomationWorkflow API and Case Builder CBE files:

1. From the WebSphere Application
Server administrative
console, click Logging and Tracing > server > Change
log detail levels.
2. Under the com.ibm.casemgmt.* component, select the com.ibm.casemgmt.cbe
node and set the message and trace levels as needed.
The
default logging level is info. Select No Logging
to disable logging, or change the settings to audit or warning to
prevent filling log files too quickly.
3. Save your changes and restart WebSphere Application
Server.