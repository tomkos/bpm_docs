# setWSRRDefinitionAsDefault command

Any WSRR definition in the cell that was previously set
to be default will no longer be the default. If no definition can
be found with that name, or the target object and name are both supplied
but conflict, an exception will be thrown.

```
$AdminTask help SIBXWSRRAdminCommands
```

The setWSRRDefinitionAsDefault command
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
The setWSRRDefinitionAsDefault command does not
write to a log file, but the wsadmin scripting client always writes
a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
setWSRRDefinitionAsDefault
-name definitionName
```

## Parameters

## Example

```
wsadmin>AdminTask.setWSRRDefinitionAsDefault( ['-name', 'mydefName'] )
```