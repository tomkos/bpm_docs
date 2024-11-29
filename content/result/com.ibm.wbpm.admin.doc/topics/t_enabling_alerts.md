# Disabling and enabling the checking of BPM alerts

## Before you begin

The following conditions must be met:

- The setBPMProperty command must be run on the deployment manager node.
- If the deployment manager is stopped, use the wsadmin -conntype none option to
run the command in disconnected mode.
- If the deployment manager is running, you must connect with a user ID that has WebSphere
Application Server configurator privileges. Do not use the wsadmin -conntype none
option.

## About this task

IBM® Business Automation
Workflow uses
a WCCM custom property to control whether the system checks that alert
definitions have triggered alerts. If the ProcessServer.AlertDefinitionsStatusEnabled property
does not exist or if it is true, the system checks the condition in
the alert definition to see whether it is true and thus triggers an
alert. If you are not sure about current behavior, use the getBPMProperty command
to confirm whether the property exists and if it does, what value
it has.

Disabling the checking of BPM alerts is a significant
action to take because it affects all of the alert definitions. An
alternative option is to check how often the getAlertDefinitionsStatus API
is called. Try to reduce the number of calls to the minimum needed
to properly monitor a specific artifact when you create an alert implementation.

## Procedure

Use the setBPMProperty command to
set the ProcessServer.AlertDefinitionsStatusEnabled WCCM
custom property.

- To disable the checking of BPM alert status, set the property
value to false. When the property
is false, the system does not check whether the artifacts that are
being monitored have passed the threshold value. Calls using the getAlertDefinitionsStatus API
result in the CWTBG0600E error message. The error
message says that status checking for alert definitions has been disabled.
- To enable the checking of BPM alert status, set the property
value to true, which is the default value.
Alternatively, delete the property by using the deleteBPMProperty command.