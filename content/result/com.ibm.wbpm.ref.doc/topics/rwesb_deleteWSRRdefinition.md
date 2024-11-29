# deleteWSRRDefinition command

If the definition cannot be found, or the name and target
object are both supplied but conflict, an exception is thrown. This
command deletes the default WSRR definition only if it is the only
definition in the cell. If there are other definitions present in
the cell, the command fails and you must change the default to another
WSRR definition before the current one can be deleted.

```
$AdminTask help SIBXWSRRAdminCommands
```

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
The deleteWSRRDefinition command does not write
to a log file, but the wsadmin scripting client always writes a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
deleteWSRRDefinition
-name definitionName
```

## Parameters

## Example

```
wsadmin>AdminTask.deleteWSRRDefinition( ['-name', 'MydefName'] )
```