# showWSRRDefinition command

An exception is thrown if the name you specify does
not have a definition, or if the target object and the name do not
match.

```
$AdminTask help SIBXWSRRAdminCommands
```

The showWSRRDefinition command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- The command must be run on the deployment manager node.
- If the deployment manager is stopped, use the wsadmin
-conntype none option to run the command in disconnected
mode.
- If the deployment manager is running, you must connect with a
user ID that has WebSphere Application Server configurator privileges.
Do not use the wsadmin -conntype none option.

## Location

Start the wsadmin scripting client
from the deployment\_manager\_profile/bin directory.
The showWSRRDefinition command does not write to
a log file, but the wsadmin scripting client always writes a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
showWSRRDefinition
-name definitionName
```

## Parameters

## Example

```
wsadmin>AdminTask.showWSRRDefinition( ['-name', 'mydefName'] )
```