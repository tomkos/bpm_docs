# showBPMExternalECM command

The showBPMExternalECM command is
run by using the AdminTask object of the wsadmin scripting client.

## Prerequisites

The following conditions
must be met:

- In a network deployment environment, run the
command on the deployment manager node. In a single-server environment,
run the command on the stand-alone server.
- If the deployment manager or stand-alone server is stopped, use
the wsadmin -conntype none option to run the command
in disconnected mode (which is the recommended mode for this command).
- If the deployment manager or stand-alone server is running, you
must connect with a user ID that has WebSphere Application Server
configurator privileges. Do not use the wsadmin -conntype
none option.

## Location

Start the wsadmin scripting client
from the profile\_root/bin directory.
The showBPMExternalECM command does not write to
a log file, but the wsadmin scripting client always writes a profile\_root/logs/wsadmin.traceout log
file where you find exception stack traces and other information.

## Syntax

```
showBPMExternalECM
[-de deployment\_environment\_name]
```

## Parameters

## Examples

```
wsadmin -user admin -password admin -lang jython
wsadmin>print AdminTask.showBPMExternalECM(['-de', 'De1'])
```