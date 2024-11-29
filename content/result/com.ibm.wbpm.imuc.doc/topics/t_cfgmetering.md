# Capturing metrics for monitoring concurrent users and
activities

You can capture metrics to monitor usage for the IBM® Business Automation Workflow Concurrent User
license option. You can audit and report on concurrent users, and the number of Workflow and
Content activities.

Business Automation Workflow also supports
the use of the IBM License Metric
Tool,
which can discover the software that is installed in your infrastructure, help to analyze the
consumption data, and generate reports.

For concurrent users, the metering agent records the number of users that are logged in within a
15-minute period.

- BPMN processes (BSDs):
    - User Tasks, System Tasks, and Decision Tasks
    - No scripts or sub-processes
    - Multi-instance loops fire multiple end events
- Service flows:

- Content Integration Tasks, Service Tasks, and Decision Tasks
- No Script Tasks
- BPEL processes:

- Invoke, Script, and Human Task activities
- Mediation Flows:

- All steps are counted

## About this task

You must run two commands (MeteringConfig and
MeteringAgent) to enable WebSphere® Application
Server security auditing and generate the audit logs for
user-based license compliance.

The MeteringConfig command enables the WebSphere Application
Server Auditing Facility, which then generates the audit
logs for measuring concurrent user metrics and activities. For more
information about the Auditing Facility, see Auditing the security infrastructure in the WebSphere Application
Server documentation.

The MeteringAgent starts a thread to analyze the audit log changes and sends
the information to the IBM FileNet System Manager to ensure compliance with the license entitlement.
The IBM
FileNet® System Manager
monitors the number of users who access ECM products and provides both real time and historical
usage information. It also generates files for the IBM License Metric
Tool.

```
dmgr\_profile/logs/metering/BinaryAudit\_cell\_name\_dmgr\_name\_dmgr.log
node\_profile/logs/metering/BinaryAudit\_\_cell\_name\_node\_name\_nodeagent.log
node\_profile/logs/metering/BinaryAudit\_\_cell\_name\_node\_name\_app\_server\_name.log
```

```
install\_root/logs/metering/ActivitiesMetricLog\_server\_name.log
```

## Procedure

1. Stop the deployment environment.
2 To capture metrics, run a command to enable the WebSphere ApplicationServer Auditing Facility: The WebSphere ApplicationServer Auditing Facility is configured with the following settings: For information about event type filters, see Creating security auditing event type filters .
    - To capture metrics for concurrent
users:install\_root/bin/MeteringConfig -enableConcurrentUserMetrics -profile dmgr\_profile
    - To capture metrics for number of
activities:install\_root/bin/MeteringConfig -enableActivityMetrics -profile dmgr\_profile
    - To capture metrics for both concurrent users and number of
activities:install\_root/bin/MeteringConfig -enableAllMetrics -profile dmgr\_profile
    - This event type filter specifies the type of auditable security events.

Event Name
Outcome of Event

SECURITY\_AUTHN
SUCCESS
    - Default values are used for the audit service provider and audit event factory.

For information about event type filters, see Creating security auditing event type filters.

3. Restart the deployment environment.
4 Start the metering agent to analyze the audit log files from the WebSphere ApplicationServer Auditing Facility and send the information to theFileNet SystemManager to ensure compliance with licenseentitlement.

1. Get the FileNet System
Manager (formerly
Performance Clearinghouse) configuration properties sample file and modify the file to specify the
values for your environment. The sample is in
install\_root/util/metering/pchConfig.properties. 
Customize the behavior of the
listener by using the parameters shown in the following table. For more information about these
parameters, see Listener configuration parameters.

Property
Default Value
Description

port\_number
322775
The primary TCP port number on which the first instantiated listener (called the primary
listener) listens for connections from managers.

secondary\_port
OS defined
When this parameter is defined, secondary listeners attempt to bind to the specified port
number, then that number plus 1, plus 2, and so on, until they successfully bind to a port. 

output\_interval
900 (15 minutes)
The aggregation interval in seconds. 

output\_count
96
The maximum number of summary blocks that are written to the summary log file before it is
closed and a new log is opened.

 Manage the user history queue by using the properties shown in the following table. For
more information about these properties, see IBM System Dashboard for Enterprise Content Management Listener
configuration.

Property
Default Value
Description

filenet.pch.ILMT.MAX\_HISTORY
2500000
The maximum number of User History Queue records to store in the listener buffers. 

filenet.pch.ILMT
enabled | disabled
Enable or disable the IBM License Metric
Tool
collection of metrics.

filenet.pch
enabled | disabled
Enable or disable the entire listener data collection and network services.
2 Run the MeteringAgent command on each computer that has one or moreBusiness Automation Workflow nodes. MeteringAgent -pchConfigFile pchConfig.properties -profile profile\_root /profile\_name where profile\_name is one of the profile names in thecell.The agent monitors all audit logs under that profile in the same cell. Important: The agent can use a long-running command to monitor the logs, for example thenohup command on Linux or by registering the command as a service on Windows. Formore information about MeteringAgent.bat command, see MeteringAgent command-line utility Make sure the computer that the agentruns on has the correct time, or the logs might not be accurate.

```
MeteringAgent -pchConfigFile pchConfig.properties -profile profile\_root/profile\_name
```

    - nohup MeteringAgent -start -pchConfigFile /opt/pchConfig.properties -profile DmgrProfile > /opt/meteringAgent.log 2>&1 &
    - <install\_root>\bin\MeteringAgent.bat -start -pchConfigFile c:\pchConfig.properties -profile DmgrProfile
Note: The Windows command shown here is a long-running command, refer to the Microsoft Windows
documentation here for more details.
5. While the metering agent is running, schedule the IlmtCollector
script to run (for example, once a day) to save the data for the concurrent user and activity  metrics that are collected. For instructions,
see Collecting license compliance records in the FileNet P8
Platform documentation.

## What to do next

## Related information

- Monitoring concurrent users and activities
- MeteringConfig command-line utility
- MeteringAgent command-line utility