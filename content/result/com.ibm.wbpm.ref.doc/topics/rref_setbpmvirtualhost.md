# setBPMVirtualHost command

The setBPMVirtualHost command is run
using the AdminTask object of the wsadmin scripting client.

## Prerequisites

The following conditions must
be met:

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
The setBPMVirtualHost command does not write to
a log file, but the wsadmin scripting client always writes a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
setBPMVirtualHost
[-de deployment\_environment\_name]
-name virtual\_host\_name
[-transportProtocol virtual\_host\_transport\_protocol]
[-hostname virtual\_host\_hostname]
[-port virtual\_host\_port]
[-uriPrefix virtual\_host\_URI\_prefix]
```

## Parameters

If the port parameter value is -1 or
the actual default port number for the specified protocol, the port
number is not included in the generated URL. For example, the generated
URL would be https://my\_host/ProcessCenter rather
than the URL https://my\_host:443/ProcessCenter.

## Examples

- The following Jython example uses the setBPMVirtualHost command
to reset the existing value for the uriPrefix parameter:AdminTask.setBPMVirtualHost( [ '-name', 'myVirtualHost', '-uriPrefix' ] )
- The following Jython example uses the setBPMVirtualHost command
to create or update a virtual host:wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.setBPMVirtualHost(['-de', 'De1', '-name', 'myVirtualHost', '-transportProtocol', 'https', '-hostname', 'myHostName', '-port', '9443', '-uriPrefix', 'myURIPrefix'])
wsadmin>AdminConfig.save()When the virtual host created
by the above command syntax is used in the Workflow Center web
module lookup, the following URL is the result:
https://myHostName:9443/myURIPrefix/ProcessCenter
- The following Jython example uses the setBPMVirtualHost command
to update the host name to myHostName and removes
any previously set port value:wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.setBPMVirtualHost(['-de', 'De1', '-name', 'myVirtualHost', '-hostname', 'myHostName', '-port'])
wsadmin>AdminConfig.save()