<!-- image -->

# Changing the configured logging infrastructure, using the administrative
console

## About this task

Choices made on the Configuration tab are activated the
next time the cluster is started. The chosen settings remain in effect
whenever the cluster is restarted.

Make changes
to the configuration, as follows:

## Procedure

1 Display the Business Flow Manager or Human TaskManager pane.
    1. Click Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer.
    2 Choose one of the following options:
        - For BPEL processes, click Business Flow Manager.
        - For human tasks, click Human Task Manager.
2. On the Configuration tab, in the
General Properties section, select the logging to be enabled. 
The
state observers are independent of each other:
Enable Dynamic Event Framework logging
Select this check box to enable event emission that is based on
the Dynamic Event Framework.
Enable audit logging
Select this check box to store the audit log events in the audit
trail tables of the Business Process Choreographer database.
Enable task history
 This option is only available for the Human Task Manager. Select
this check box to display task history data in Business Space, or
to retrieve task history data using the Task Instance History Representational State Transfer (REST) interface.
3 Accept the change.

1. Click OK.
2. In the Messages box, click Save.

## Results

## What to do next

<!-- image -->