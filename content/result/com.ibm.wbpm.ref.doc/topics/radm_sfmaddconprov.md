# addSCMConnectivityProvider command

A connectivity provider is a logical partition of the
ESB that is exposed via the Service Connectivity Management Protocol.
It defines the target (server or cluster) to which proxy gateway modules
will be deployed when a Service Federation Management group proxy
is created on that connectivity provider. It also defines properties
that will be used for proxy targets created on those group proxies.

```
print AdminTask.help('SCMAdminCommands')
```

The addSCMConnectivityProvider command
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
The addSCMConnectivityProvider command does not
write to a log file, but the wsadmin scripting client always writes
a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
addSCMConnectivityProvider
-name connectivityProviderName
-node nodeName -server serverName
-cluster clusterName
-proxyHostHTTP httpHost
-proxyPortHTTP httpPort
-proxyHostHTTPS httpsHost
-proxyPortHTTPS httpsPort
[-description connectivityProviderDescription]
[-contact contactName]
[-organization organizationName]
[-location locationName]
[-authAlias alias]
[-repertoire sslConfig]
```

## Parameters

## Examples

The following Jython example adds
a connectivity provider named myProvider associated
with server server1 on node cpNode where
web service clients access that server directly:

```
wsadmin>AdminTask.addSCMConnectivityProvider( ['-name', 'myProvider, 
'-node', 'cpNode', '-server', 'server1, '-proxyHostHTTP', 'webserver.example.com', 
'-proxyPortHTTP, '80', '-proxyHostHTTPS', 'webserver.example.com', 
'-proxyPortHTTPS', '443' ])
```

The following Jython
example adds a connectivity provider named myScalableProvider associated
with cluster cpCluster where web service clients
access servers in that cluster via a web server:

```
wsadmin>AdminTask.addSCMConnectivityProvider( ['-name', 'myScalableProvider',
'-cluster', 'cpCluster', '-proxyHostHTTP', 'webserver.example.com', 
'-proxyPortHTTP', '80', '-proxyHostHTTPS', 'webserver.example.com', 
'-proxyPortHTTPS', '443'] )
```

The following Jython
example demonstrates the use of the optional parameters to specify
additional information that will appear in the Service Federation
Management console and for connecting to the service registry securely:

```
wsadmin>AdminTask.addSCMConnectivityProvider( ['-name', 'myScalableProvider',
'-cluster', 'cpCluster', '-proxyHostHTTP', 'webserver.example.com', 
'-proxyPortHTTP', '80', '-proxyHostHTTPS', 'webserver.example.com', 
'-proxyPortHTTPS', '443', '-description', 'My Connectivity Provider', 
'-contact', 'Contact Name', '-organization', 'Owning Organization', 
'-location', 'ESB location', '-authAlias', 'REGISTRY\_AUTH\_ALIAS', 
'-repertoire', 'REGISTRY\_SSL\_CONFIG'] )
```