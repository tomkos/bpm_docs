# modifySCMConnectivityProvider command

The modifySCMConnectivityProvider command
changes the details of a connectivity provider, given its name or
target object.

Specify the object to be modified, either as
a target object or by a name parameter. If the target object does
not represent a connectivity provider, or a connectivity provider
does not exist with the given name, an exception is thrown.

```
print AdminTask.help('SCMAdminCommands')
```

The modifySCMConnectivityProvider command
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
The modifySCMConnectivityProvider command does
not write to a log file, but the wsadmin scripting client always writes
a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
modifySCMConnectivityProvider
-name connectivityProviderName | target
[-proxyHostHTTP httpHost]
[-proxyPortHTTP httpPort]
[-proxyHostHTTPS httpsHost]
[-proxyPortHTTPS httpsPort]
[-description connectivityProviderDescription]
[-contact contactName]
[-organization organizationName]
[-location locationName]
[-authAlias alias]
[-repertoire sslConfig]
```

## Parameters

## Example

The following example modifies the
description and registry security settings for the connectivity provider myProvider:

```
wsadmin>AdminTask.modifySCMConnectivityProvider(
['-name', 'myScalableProvider', '-description', 'Newdescription',
'-authAlias', 'NEW\_REGISTRY\_AUTH\_ALIAS', 
'-repertoire', 'NEW\_REGISTRY\_SSL\_CONFIG'])
```