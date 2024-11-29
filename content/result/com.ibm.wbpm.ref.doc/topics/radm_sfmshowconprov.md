# showSCMConnectivityProvider command

The showSCMConnectivityProvider command
returns a list of all the parameters for a connectivity provider,
given its name or target object.

An exception is thrown if a
connectivity provider is not found with the name that you specify,
or if the target object does not represent a connectivity provider.

```
print AdminTask.help('SCMAdminCommands')
```

The showSCMConnectivityProvider command
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
The showSCMConnectivityProvider command does not
write to a log file, but the wsadmin scripting client always writes
a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
showSCMConnectivityProvider
-name connectivityProviderName | target
```

## Parameters

## Example

```
wsadmin>AdminTask.showSCMConnectivityProvider( ['-name', 'myProvider'] )
```