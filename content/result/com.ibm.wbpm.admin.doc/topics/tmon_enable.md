<!-- image -->

# Enabling monitoring of business process and human task events

## Before you begin

## About this task

## Procedure

1. Open the administrative console.
2. To enable business process events for the Human Task Manager,
click Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab under Business
Process Manager, expand Business Process Choreographer,
ensure that the boxes for Enable Common Event Infrastructure
Logging, Enable audit logging,
and Enable task history are selected. If the
check boxes are not selected, then you must select them and restart
the server.
3. To enable business process events for the Business Flow
Manager, click Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab under Business
Process Manager, expand Business Process Choreographer,
click Business Flow Manager. In the section State
Observers, ensure that the boxes for Enable
Common Event Infrastructure Logging and Enable
audit logging are selected. If the check boxes are not
selected, then you must select them and restart the server.
4. If you had to select any of the boxes, then you must restart
the cluster for the changes to take effect.