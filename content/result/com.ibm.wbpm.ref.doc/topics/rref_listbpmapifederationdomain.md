# listBPMApiFederationDomains command

This command lists all federation
domains that exist for a server or a cluster. The Federation API allows
you to display processes and tasks created in Process Designer and
Integration Designer in the same task list. The Federation API is
automatically configured with your product as part of the REST Services
Gateway application. If you want to change that configuration for
your environment with multiple deployment targets, use wsadmin commands
to create and manage federation domains.

## Prerequisites

The following conditions
must be met:

- The command must be run on the deployment manager node.
- If the deployment manager is stopped, use the wsadmin
-conntype none option to run the command in disconnected
mode.
- If the deployment manager is running, you must connect with a
user ID that has WebSphere Application Server monitor privileges.
Do not use the wsadmin -conntype none option.

## Location

Start the wsadmin scripting client
from the deployment\_manager\_profile/bin directory.
The listBPMApiFederationDomains command does not
write to a log file, but the wsadmin scripting client always writes
a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Target object

Scope at which the federation
domain is to be administered. The target object can be used instead
of the nodeName, serverName and clusterName parameters.

## Required parameters

## Examples

```
AdminTask.listBPMApiFederationDomains('[-nodeName myNode -serverName
 myServer]')
```