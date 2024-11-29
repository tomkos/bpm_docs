# Taking workflow servers offline

## Before you begin

Ensure you have administrative access to the Workflow Center repository to take servers offline. For more
information, see Granting access to the Workflow Center repository.

## About this task

## Procedure

1 On the online Workflow Server , perform one of thefollowing actions:
    - If you are using wsadmin commands, set the heartbeat interval to -1. For more information, see
Customizing the Workflow Server settings used to connect to Workflow Center.
    - If you are using the admin console, select Use server offline. For more
information, see Using the administrative console to customize the Workflow Server settings used to connect to Workflow Center.
2. Ensure your changes are saved and synchronized with the nodes.
3. Restart the Workflow Server deployment
environment.
4. Click the Servers tab in Process Designer.
5. For the server that you want to take offline, click Take Server Offline
and confirm your selection.
6. For the server that you just took offline, click Remove Offline Server
and confirm your selection.

## Results