# modifyWSRRDefinition command

The modifyWSRRDefinition command is
a multi-step command, in which the steps define the type of connection
definition and the specific properties. You can specify only one step,
because a WSRR definition can have only one connection definition.
You specify the object to be modified, either as a target object or
by a name parameter. If there is a conflict between the target object
and the name parameter, or if a definition cannot be found, you will
see an error message.

```
$AdminTask help SIBXWSRRAdminCommands
```

The modifyWSRRDefinition command
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
The modifyWSRRDefinition command does not write
to a log file, but the wsadmin scripting client always writes a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
modifyWSRRDefinition
-name definitionName
-newName newdefName
-description defDescription
-defaultCacheExpiryTimeout timeout
```

## Parameters

## Steps

Only one step can be specified or
you will see an error message. Select the step that matches the connection
of the definition.

To modify the properties for a web service
connection associated with the WSRR definition, you can specify values
for the registry URL and the authentication alias, as in this example:

The default connection has a default registry
URL and no authentication alias or repertoire (SSL configuration).

## Example

```
wsadmin>AdminTask.modifyWSRRDefinition( ['-name', 'MydefName', '-newName', 'newdefName', 
    '-description', 'my\_new\_description', 
    '-defaultCacheExpiryTimeout', '300', 
    '-WSConnection ',['-registryUrl', 'http://localhost:9084', '-authAlias', 'NEW\_AUTH\_ALIAS', '-repertoire', NEW\_SSL\_CONFIG']] )
```