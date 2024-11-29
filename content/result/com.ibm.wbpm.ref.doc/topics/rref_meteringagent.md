# MeteringAgent command-line utility

The MeteringAgent analyzes the audit log changes and sends the information to
the FileNet System
Manager, a performance monitoring tool for
enterprise content management (ECM) products. It monitors the number of users who access ECM
products and provides both real-time and historical usage information. It uses the
IlmtReporter script to generate comma-separated values (CSV) files and IBM
Software License Metric Tag (.slmtag) files that can be read by the IBM License Metric
Tool agent.

Because the agent must keep monitoring the logs, make it a long-running command, for example by
using the nohup command on Linux or registering the command as a service on
Windows.

Run the MeteringAgent command on each computer that has one or more managed
nodes.

## Prerequisites

- You must have run the MeteringConfig command to start the WebSphere Application
Server Auditing Facility.
- The deployment environment must be running.
- The computer that the agent runs on must have the correct time. Otherwise, data collection might
not be accurate.

## Location

The MeteringAgent command-line utility is in the
install\_root\_/bin directory.

The command log is in
install\_root\_/logs/metering/MeteringAgent.timestamp.log.

## Syntax

```
install\_root\_/bin/MeteringAgent
-pchConfigFile pchConfig.properties
-profile deployment\_manager\_profile
```

```
dmgr\_profile/logs/metering/BinaryAudit\_cell\_name\_dmgr\_name\_dmgr.log
node\_profile/logs/metering/BinaryAudit\_\_cell\_name\_node\_name\_nodeagent.log
node\_profile/logs/metering/BinaryAudit\_\_cell\_name\_node\_name\_app\_server\_name.log
```

When the DEF listener is enabled, the activity metrics
log is created in
install\_root\_/logs/metering/ActivityMetricLog.server\_name.log.

## Parameters

You can find a sample file in
install\_root/util/metering/pchConfig.properties. Modify the
file to specify the values for your environment.

| Property        | Default Value    | Description                                                                                                                                                                           |
|-----------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| port\_number     | 322775           | The primary TCP port number on which the first instantiated listener (called the primary listener) listens for connections from managers.                                             |
| secondary\_port  | OS defined       | When this parameter is defined, secondary listeners attempt to bind to the specified port number, then that number plus 1, plus 2, and so on, until they successfully bind to a port. |
| output\_interval | 900 (15 minutes) | The aggregation interval in seconds.                                                                                                                                                  |
| output\_count    | 96               | The maximum number of summary blocks that are written to the summary log file before it is closed and a new log is opened.                                                            |

| Property                     | Default Value      | Description                                                                        |
|------------------------------|--------------------|------------------------------------------------------------------------------------|
| filenet.pch.ILMT.MAX\_HISTORY | 2500000            | The maximum number of User History Queue records to store in the listener buffers. |
| filenet.pch.ILMT             | enabled | disabled | Enable or disable the IBM License Metric Tool collection of metrics.               |
| filenet.pch                  | enabled | disabled | Enable or disable the entire listener data collection and network services.        |

## Examples

- nohup MeteringAgent -start -pchConfigFile /opt/pchConfig.properties -profile DmgrProfile > /opt/meteringAgent.log 2>&1 &
- <install\_root>\bin\MeteringAgent.bat -start -pchConfigFile c:\pchConfig.properties -profile DmgrProfile

## What to do next