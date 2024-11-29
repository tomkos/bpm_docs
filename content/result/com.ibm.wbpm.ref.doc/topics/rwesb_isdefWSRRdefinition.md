# isDefaultWSRRDefinition command

```
$AdminTask help SIBXWSRRAdminCommands
```

The isDefaultWSRRDefinition command
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
The isDefaultWSRRDefinition command does not write
to a log file, but the wsadmin scripting client always writes a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
isDefaultWSRRDefinition
-name definitionName
```

## Parameters

## Example

```
wsadmin>AdminTask.isDefaultWSRRDefinition( ['-name', 'MydefName'] )
```

## Note on interactive usage

```
wsadmin>AdminTask.isDefaultWSRRDefinition('-interactive')
Check if a WSRR definition is the default  

Check if a WSRR definition is the default  

Target WSRR definition: 
Name (name): testDefinition  

Check if a WSRR definition is the default  

F (Finish) 
C (Cancel)  

Select [F, C]: [F] F 
WASX7278I: Generated command line: 
AdminTask.isDefaultWSRRDefinition('[-name testDefinition ]') 
'true'
```