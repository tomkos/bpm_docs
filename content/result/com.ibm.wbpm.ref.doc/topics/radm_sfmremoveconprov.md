# removeSCMConnectivityProvider command

The removeSCMConnectivityProvider removes
a connectivity provider that has been named or supplied as a target
object. An exception is thrown if there are still proxy gateway modules
deployed to the target server or cluster representing group proxies
created on this connectivity provider. The group proxies should be
removed via the Service Federation Management console or, if the connectivity
provider is no longer managed by the console, the proxy gateway modules
should be manually removed by the IBM® Business Automation Workflow administrator.

Specify
the object to be removed either as a target object or by a name parameter.

```
print AdminTask.help('SCMAdminCommands')
```

The removeSCMConnectivityProvider command
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
The removeSCMConnectivityProvider command does
not write to a log file, but the wsadmin scripting client always writes
a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
removeSCMConnectivityProvider
-name connectivityProviderName | target
```

## Parameters

## Example

```
wsadmin>AdminTask.removeSCMConnectivityProvider( ['-name', 'myProvider'] )
```