# getBPMVirtualHost command

The getBPMVirtualHost command is run
using the AdminTask object of the wsadmin scripting client.

## Prerequisites

The following conditions must
be met:

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
The getBPMVirtualHost command does not write to
a log file, but the wsadmin scripting client always writes a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
getBPMVirtualHost
-de deployment\_environment\_name
-name virtual\_host\_name
```

## Parameters

## Examples

```
wsadmin -user admin -password admin -lang jython
wsadmin>vh = AdminTask.getBPMVirtualHost(['-de', 'De1', '-name', 'myVirtualHost'])
wsadmin>print AdminConfig.show( vh )
```