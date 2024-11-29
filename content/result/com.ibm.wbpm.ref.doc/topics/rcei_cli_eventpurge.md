# eventpurge command-line utility

## Prerequisites

If WebSphere® security is enabled, your user ID must
be mapped to the eventAdministrator role to delete events.

## Syntax

```
eventpurge
-seconds seconds |  -end end\_time
[-group event\_group]
[-severity severity]
[-extensionname extension\_name]
[-start start\_time]
[-size size]
```

## Parameters

The end time of the group of events you want to delete. Only events generated before the
specified time are deleted. The end\_time value must be specified in the XML
dateTime format (CCYY-MM-DDThh:mm:ss ). For example, noon on 1 January 2006 in
Eastern Standard Time would be 2006-01-01T12:00:00-05:00.

This parameter is required if you do not specify the -seconds parameter.

## Examples

```
eventpurge -group "All events" -severity 20 -seconds 600
```