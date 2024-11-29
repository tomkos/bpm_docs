# configureBPMTransportSecurity command

Traditional: 
Use the configureBPMTransportSecurity command
to list and toggle HTTPS protocol enforcement for a set of Business Automation Workflow URLs.

```
AdminTask.setBPMProperty(['-de', 'De1', '-name', 'ProcessServer.MarkCookiesSecureOnSecureConnections', '-value', 'false'])"
```

The configureBPMTransportSecurity command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

This command reconfigures
web deployment descriptors and then redeploys affected applications.
As a result, the following conditions must be met:

1. In a network deployment environment, run the
command on the deployment manager node. In a single-server environment,
run the command on the stand-alone server.
2. Stop all servers in your deployment environment. In an ND topology,
this includes the deployment manager and the node agents.
3. Run the command in disconnected mode by using the wsadmin
-conntype none option.
4. Restart all servers in your deployment environment to pick up
the configuration changes.

## Location

Start the wsadmin scripting client
from the profile\_root/bin directory.
The configureBPMTransportSecurity command does
not write to a log file, but the wsadmin scripting client always writes
a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

```
[3/15/17 13:07:50:879 CST] 00000041 annotations 
W com.ibm.ws.amm.scan.context.ScannerContextImpl getInputDataForClass 
Failed to open resource [ org/apache/struts/taglib/bean/StrutsTag.class ]
from module [ webviewer.war ]
```

## Syntax

```
configureBPMTransportSecurity
[-de deployment\_environment\_name]
-apps configuration\_scope
-transportSecurity configuration\_mode
```

## Parameters

- productREST: REST APIs provided by Business Automation Workflow.
- productSOAP: SOAP APIs provided by Business Automation Workflow.
- customSOAP: SOAP web services in custom (.twx) applications.
- bspace:
Web applications related to Business Space and Heritage Process Portal.Restriction: Heritage Process Portal is
deprecated.
- 201612: All other changes that are relative
to cumulative fix 2016.12.
- 18001: IBM® Content
Navigator and case management features
introduced in 24.x.

- list: Display the current configuration.
- httpsonly: Switch the transport-guarantee
setting to CONFIDENTIAL to enforce a redirect to HTTPS.
- allowhttp: Switch the transport-guarantee
setting to NONE to allow non-secure HTTP traffic. If you enable non-secure
HTTP and access any of the browser-targeted web user interfaces using
an HTTP URL, you need to ensure that URLs pointing to Business Automation Workflow are calculated
using an HTTP prefix to avoid mixed content in the browsers. The useHTTPSURLPrefixes flag
determines the protocol of self-referential URLs in case no other
strategy is configured, as described in the topic Configuring Secure Sockets Layer (SSL) communication in a network deployment environment.

## Examples

```
print AdminTask.configureBPMTransportSecurity( [ '-de', 'De1', '-apps', 'productREST', '-transportSecurity', 'allowhttp'] )
```

```
print AdminTask.configureBPMTransportSecurity( [ '-de', 'De1', '-apps', 'productSOAP', '-transportSecurity', 'httpsonly'] )
```

```
print AdminTask.configureBPMTransportSecurity( [ '-de', 'De1', '-apps', 'customSOAP', '-transportSecurity', 'httpsonly'] )
```

```
print AdminTask.configureBPMTransportSecurity( [ '-de', 'De1', '-apps', '201612', '-transportSecurity', 'list'] )
```

```
wsadmin> print AdminTask.configureBPMTransportSecurity( [ '-de', 'De1', '-apps', 'productREST', '-transportSecurity', 'allowhttp'] )
wsadmin> AdminTask.configureSingleSignon('-requiresSSL false')
wsadmin> for server in AdminUtilities.convertToList(AdminTask.listServers( '-serverType APPLICATION\_SERVER' )):
wsadmin>     for cookie in AdminUtilities.convertToList(AdminConfig.list('Cookie', server)):
wsadmin>         AdminConfig.modify(cookie, [['secure','false']])
wsadmin>
wsadmin> AdminConfig.save()
```

In this example, the
fourth line must be indented one level and the fifth line must be
indented two levels. You should use at least one blank for each level.
The sixth line is a required empty line to end the loop and you can
just press the Enter key.