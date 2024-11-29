# MeteringConfig command-line utility

To measure the number of activities that are running, the
MeteringConfig command also creates a dynamic event framework (DEF) listener to
capture the execution events.

The concurrent user and activity metrics logs are analyzed by the
metering agent. See the MeteringAgent command.

For more information about the Auditing Facility, see Auditing the security infrastructure in the WebSphere Application
Server documentation.

## Prerequisites

- The deployment environment must be stopped.

## Location

The MeteringConfig command-line utility is in the
install\_root\_/bin directory.

The command log is in
install\_root\_/logs/metering/MeteringConfig.timestamp.log.

```
dmgr\_profile/logs/metering/BinaryAudit\_cell\_name\_dmgr\_name\_dmgr.log
node\_profile/logs/metering/BinaryAudit\_\_cell\_name\_node\_name\_nodeagent.log
node\_profile/logs/metering/BinaryAudit\_\_cell\_name\_node\_name\_app\_server\_name.log
```

When the DEF listener is enabled, the activity metrics
log is created in
install\_root\_/logs/metering/ActivityMetricLog.server\_name.log.

## Syntax

```
install\_root\_/bin/MeteringConfig
[-enableConcurrentUserMetrics | -disableConcurrentUserMetrics]|
[-enableActivityMetrics | -disableActivityMetrics] |
[-enableAllMetrics | -disableAllMetrics]
-profile deployment\_manager\_profile
```

## Parameters

## Examples

```
MeteringConfig -enableConcurrentUserMetrics -profile dmgr\_profile
```

```
MeteringConfig -disableAllMetrics -profile dmgr\_profile
```

## What to do next