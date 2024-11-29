# Capturing javacore

## Capturing javacore

A javacore dump, or a
thread dump as it is also called, is one of the primary problem determination
documents that an application server creates.

1 Use wsadmin to produce a javacore in the Profile directory: Note: The braces, [] around the AdminControl queryNames commandare part of the command, and not used to signify optional parametersas is the case for braces around host, port and user. The processname: server1 may need to be change to fit your configuration.
    1. For Windows:<PROFILE\_DIR>\bin\wsadmin.bat [-host host\_name] [-port port\_number]
[-user userid -password password] -c
"$AdminControl invoke [$AdminControl queryNames WebSphere:name=JVM,process=server1,*]
dumpThreads"
    2. For UNIX (IBM JDKs):<PROFILE\_DIR>>/bin/wsadmin.sh[-host host\_name] 
[-port port\_number] [-user userid -password password] -c
"\$AdminControl invoke [\$AdminControl queryNames WebSphere:name=JVM,process=server1,*]
dumpThreads"
2 A signal can be sent to the server process:

1 Windows:A launchscript must be used to start the server process to allow the signalto be passed to the process. This does require special setup beforestarting the server.
    1. <PROFILE\_DIR>\bin\startServer.bat server1 -script SERVER1.bat
    2. b.	SERVER1.batThe server process will start in a command window.
You will need to check the logs to verify that the server has successfully
started since the intermediate JVM process which usually starts the
server process is not used.
    3. <CTRL><BREAK>Issue a <CTRL><BREAK> into the command
window where the server process is running. A javacore will be produced.
2. UNIX (all JDKs): kill -3 <pid>Where <pid> is the process
id of the WebSphere® Process
Server. For IBM JDKs a javacore
will be produced in the <PROFILE\_DIR>directory. 
For non-IBM
JDKs, a thread dump will be written to the native\_stdout.log.
3 An alternative method to dumping a windows core file is to usejvmdump. This does not require special setup before starting theserver. However, it does require a special executable file from theJVM team. The jvmdump.exe program can be requested by sending a noteto jvmcookbook@uk.ibm.com. The advantage of this method is additionalinformation can be obtained about native code being executed withinJVM. The format of the dump differs from the IBM javacores. For more details about the jdumpview utility consult the Diagnostics Guide for the IBM Developer Kit and Runtime Environment, Java™ Technology Edition, Version5.0.

This does not require special setup before starting the
server. However, it does require a special executable file from the
JVM team. The jvmdump.exe program can be requested by sending a note
to jvmcookbook@uk.ibm.com. The advantage of this method is additional
information can be obtained about native code being executed within
JVM. The format of the dump differs from the IBM javacores.

- jvmdump.exe <PID>
- <WAS\_HOME>>\java\jre\bin\jextract.exe <core.name.dmp>
- <WAS\_HOME>\java\jre\bin\jdumpview.exe
    - set dump <core.name.dmp>.zip
    - display threadDisplays the current executing thread at the
time of the dump
    - c.	display thread *Display all of the threads from the dump.

For more details about the jdumpview utility consult the Diagnostics Guide for the IBM Developer Kit and Runtime Environment, Java™ Technology Edition, Version
5.0.