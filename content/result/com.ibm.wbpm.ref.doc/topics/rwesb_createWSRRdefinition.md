# createWSRRDefinition command

The createWSRRDefinition command is
a multistep command in which the steps define the type of connection
definition and its specific properties. You can specify only one step,
because a WSRR definition can have only one connection definition.

```
$AdminTask help SIBXWSRRAdminCommands
```

The createWSRRDefinition command
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
The createWSRRDefinition command does not write
to a log file, but the wsadmin scripting client always writes a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
createWSRRDefinition
-name definitionName
-connectionType WEBSERVICE
-defaultCacheExpiryTimeout timeout
[-description defDescription]
```

## Parameters

## Steps

## Examples

```
wsadmin>AdminTask.createWSRRDefinition( ['-name', 'mydefName', '-description', my description',
		 	'-defaultCacheExpiryTimeout', '300', '-connectionType', 'WEBSERVICE'] )
```

```
wsadmin>AdminTask.createWSRRDefinition( ['-name', 'mydefName', '-description', my description', 
    '-defaultCacheExpiryTimeout', '300', '-connectionType', 'WEBSERVICE', 
    '-WSConnection ', ['-registryUrl', 'http://localhost:9080', '-authAlias', 'AUTH\_ALIAS1', '-repertoire', 'SSL\_CONFIG1']] )
```

```
wsadmin>AdminTask.createWSRRDefinition( ['-name', 'defName', '-description', my description', 
    '-defaultCacheExpiryTimeout', '300', '-connectionType', 'WEBSERVICE', 
    '-WSConnection', [ ["" AUTH\_ALIAS1  ""] ]] )
```