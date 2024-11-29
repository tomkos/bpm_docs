# setExternalNavigator command

The setExternalNavigator command is run by using the AdminTask object of the
wsadmin scripting client.

## Prerequisites

The following conditions must be met:

- In clustered environments, the command must be run on the deployment manager node. In
non-clustered environments, the command must be run on the stand-alone server.
- If the deployment manager or stand-alone server is stopped, use the wsadmin -conntype
none option to run the command in disconnected mode (which is the recommended mode for this
command).

## Location

Start the wsadmin scripting client from the
profile\_root/bin directory. The
setExternalNavigator command does not write to a log file, but the wsadmin
scripting client always writes a
profile\_root/logs/wsadmin.traceout log file where you find
exception stack traces and other information.

## Syntax

```
setExternalNavigator
[-de deployment\_environment\_name]
-icnUrl external\_ICN\_server\_URL 
-icnAdminUser external\_ICN\_admin\_user 
-icnAdminPassword external\_ICN\_admin\_password
[-workflowWebServerURL web\_server\_URL] 
[-publicIcnURL public\_ICN\_URL]
```

## Parameters

```
Access to ... from origin 'https://myhostname.x.y.z:9444' has been blocked by CORS policy: The 'Access-Control-Allow-Origin' header has a value 'https://myHostName.x.y.z:9444' that is not equal to the supplied origin.
```

An optional parameter that configures the access URL of the IBM Business Automation
Workflow server from the external
IBM Content
Navigator
server. If it is not specified, the first application cluster member URL is used. Hence, it is
required when the IBM Business Automation
Workflow
server is accessed through a web server such as the IBM HTTP Server (IHS), load balancer, or virtual
IP. The URL format is https://baw\_web\_server\_host:baw\_web\_server\_port.

For example, https://icn\_web\_server\_host:9443/navigator

## Example

```
wsadmin -connType none -lang jython
wsadmin>print AdminTask.setExternalNavigator (['-de', 'De1', '-icnURL', 'https://icnserver:9443/navigator', '-icnAdminUser', 'ICNAdminUser', '-icnAdminPassword', 'adminpassword'])
wsadmin>AdminConfig.save()
```

```
wsadmin -connType none -lang jython
wsadmin>print AdminTask.setExternalNavigator (['-de', 'De1', '-icnURL', 'https://icnserver:9443/navigator', '-icnAdminUser', 'ICNAdminUser', '-icnAdminPassword', 'adminpassword', '-workflowWebServerURL', 'https://bawhttpserver:443'])
wsadmin>AdminConfig.save()
```