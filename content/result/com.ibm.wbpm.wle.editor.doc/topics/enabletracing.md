# Enabling error logging in the desktop Process Designer (deprecated)

## Traces and logs

Error logs and traces can be located in a number of different places within the Process Designer installation
directory. You can find java.util.log in the main directory where Process Designer is installed. Other
logs are located in the
<ProcessDesignerInstallationDirectory>\workspace\metadata directory.

You
can use the information in these logs to troubleshoot a problem. If
you need to contact IBM Support, submit these logs to get the problem
resolved faster.

## Enabling
java.util.logging

To enable logging for java.util.logging
messages, follow these steps:

1. Close Process Designer.
2. Navigate to the main Process Designer installation
directory.
3. Open TraceSettings.properties. Uncomment the
line for the classes that you want to trace.
4. Restart Process Designer,
recreate the problem and examine the java.util.log file
for errors. The java.util.log file is located in
the Process Designer installation
directory.