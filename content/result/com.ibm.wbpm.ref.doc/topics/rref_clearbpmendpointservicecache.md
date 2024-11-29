# clearBPMEndpointServiceCache command

The Business Automation Workflow endpoint
service reads and caches its configuration settings during the server
start up process. If you enable endpoint service tracing com.ibm.bpm.endpoint.*=all during
server runtime for problem determination, then the resulting traces
do not contain the initial computation of the URLs. To ensure the
URL computation for the endpoint service is part of the endpoint service
trace, run the clearBPMEndpointServiceCache command
to reset the endpoint service caches after enabling the com.ibm.bpm.endpoint.*=all trace.

After
the URL cache has been cleared, the trace contains the computation
of the URLs. If you change the endpoint service configuration, you
need to synchronize the configuration changes to the managed nodes
and restart the cluster members.

The clearBPMEndpointServiceCache command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

The following conditions must
be met:

- The command must be run on the deployment manager node.
- The wsadmin admin scripting client must be invoked in connected
mode and the user must have WebSphere Application Server operator
privileges.

## Location

Start the wsadmin scripting client
from the deployment\_manager\_profile/bin directory.
The clearBPMEndpointServiceCache command does not
write to a log file, but the wsadmin scripting client always writes
a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
clearBPMEndpointServiceCache
```

## Parameters

The clearBPMEndpointServiceCache command
does not have any parameters and it does not return a result.

## Examples

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.clearBPMEndpointServiceCache()
```