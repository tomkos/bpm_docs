# Configuring WebSphere Application
Server
logging for Case Builder and the
Business Automation Workflow API
application

## About this task

You can use the logging settings in the WebSphere Application
Server administrative console to
redirect the logs to the Business Automation Workflow log location.

To access the settings in the administrative console, click
Troubleshooting > Logs and
trace, and select your server name.

## Procedure

To configure logging options for Case Builder and the Business Automation Workflow API
application:

- Redirect the log:
    1. Click Diagnostic Trace and click the Runtime
tab.
    2. In the File Name field, change the value to
installation\_path/IBM/CaseManagement/logs.
- Redirect the main application server logs:

1. Click JVM logs and click the Runtime
tab.
2. In the File Name fields, change the path before the /SystemOut.log and
/SystemErr.log file names to the Business Automation Workflow log location.
For example, use
installation\_path/IBM/CaseManagement/logs/SystemOut.log and
installation\_path/IBM/CaseManagement/logs/SystemErr.log.
- Change the logging level: Case Builder components havethe Message and Trace Levels set to info by default. Reset these componentsto audit or warning to prevent filling log files tooquickly. Under the com.ibm.acm.* component, select the com.ibm.acm.sold.* node to set theMessage and Trace Levels settings for all the Case Builder components.

1. From the WebSphere Application
Server
administrative console, click Logging and
Tracing > server > Change log detail
levels.
2. Change the logging levels as needed.