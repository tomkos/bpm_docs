# BPMClearWSICache command

Use this command when there is an incompatible change
in the web service provider's WSDL definitions of operations, parameters,
and other elements but the web service integration uses the same WSDL
URL or endpoint. The command removes the cached WSDL and XSD metadata
model data for a specific web service integration or for all web service
integrations. In the Workflow Server environment,
the BPMClearWSICache command is a convenient alternative
to restarting the server or cluster, which also clears the cache.
Because the new WSDL definitions load when the cache is repopulated,
ensure that you run this command or restart the server or cluster
before the web service consumer invokes the provider.

Run the BPMClearWSICache command
by using the AdminTask object of the wsadmin scripting
client.

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- Use the BPMClearWSICache command in connected
mode from Workflow Server.
In a network deployment environment, you must run this command on
the node that contains the application cluster member that handles Workflow Server applications.
Do not run this command from the deployment manager profile. Tip: If you are using a SOAP connection, the command can take
longer to complete than the specified SOAP timeout value. Although
the command continues to run until it is finished, you might see a
read timed out exception (java.net.SocketTimeoutException).
To prevent this exception, set a higher value for the com.ibm.SOAP.requestTimeout property
in the profile\_root/properties/soap.client.props file.
- You must be an administrator.

## Location

Start the wsadmin scripting client
from the custom\_profile/bin directory.

## Syntax

```
BPMClearWSICache
-wsdlURL URL
```

## Parameters

## Examples

- Clear the cache of all web service definitions:wsadmin -conntype SOAP -port 8080 -host PS1.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMClearWSICache ('[-wsdlURL all]')

- Clear the cache of a specific web service definition:wsadmin -conntype SOAP -port 8080 -host PS1.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMClearWSICache ('[-wsdlURL http://servername:8088/mockWS\_Hello\_V2SoapSoapBinding?WSDL]')