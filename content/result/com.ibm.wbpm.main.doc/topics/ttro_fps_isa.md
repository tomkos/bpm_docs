# Collecting problem report data for Process Federation Server with
IBM Support Assistant Data Collector

## Before you begin

## About this task

## Procedure

To run the data collector, complete the following steps:

1 Ensure that your Java environment is configured correctly:
    1. Verify that your Java runtime environment is at level
1.5 or higher.
    2 Verify that the location of the Java runtime environmentis included in your PATH environment setting. If the location is notincluded in your path, set the JAVA\_HOME variableto point to the Java runtime environment.
        - For example, if you have a Java Development
Kit installed at C:\jre1.5, use the command: SET JAVA\_HOME=C:\jre1.5
        - For example, if you are using the bash shell
and you have a Java Development Kit installed at /opt/jre15,
use the command: export JAVA\_HOME=/opt/jre15
2 Start the script from a command window. The IBM Support Assistant Data Collector starts in consolemode.

1. Go to the directory where you downloaded the IBM Support
Assistant Data Collector to.
2 Run the following command:
    - isadc.bat
    - isadc.shTip: Ensure
that the script is executable file. If necessary, use the following
command to change the file permissions:  chmod 755 isadc.sh
3 Create a response file. You can specify your own file name for response.txt . Answer the console prompts as appropriate for yourenvironment.

- isadc.bat -record response.txt
- isadc.sh -record response.txt

Answer the console prompts as appropriate for your
environment.

4 Run the tool using a response file. The response file is a plain text file.You can edit it to modify values. For example, you can use the fileon another computer after adjusting the response file values to reflectsettings for the local computer. Remember that sensitive information,such as user names and passwords, might be stored in the responsefile. Manage the file carefully, to prevent unauthorized access toimportant information. Some data collection sessions requireinteraction with the user, and thus are not suitable for the silentcollection option. For example, IBM Support might ask you to reproducea problem during data collection, in order to collect log and tracefiles. In this case, silent collection cannot record and reproduceall steps.

- isadc.bat response.txt
- isadc.sh response.txt

The response file is a plain text file.
You can edit it to modify values. For example, you can use the file
on another computer after adjusting the response file values to reflect
settings for the local computer.

Remember that sensitive information,
such as user names and passwords, might be stored in the response
file. Manage the file carefully, to prevent unauthorized access to
important information.

Some data collection sessions require
interaction with the user, and thus are not suitable for the silent
collection option. For example, IBM Support might ask you to reproduce
a problem during data collection, in order to collect log and trace
files. In this case, silent collection cannot record and reproduce
all steps.

5. Stop the data collector by typing the quit option in console
mode.