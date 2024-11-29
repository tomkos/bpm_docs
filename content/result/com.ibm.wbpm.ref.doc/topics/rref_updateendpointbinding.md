# updateEndpointBindingsOnPortal command

This command creates references
to the Representational State Transfer (REST) endpoints on the WebSphere Portal application
server. Business Space and product-specific endpoint reference entries
must be created so that Business Space works properly in the WebSphere Portal environment.
Business Space widgets are registered as iWidgets with WebSphere Portal by a bulk import using
the WebSphere Portal-specific
widget catalog file with your product. The catalog XML file is available
at the root of the product web archive (WAR) file. Each product has
a different context root. This command works only for the resource
environment provider named WP Mashup Endpoints.

The updateEndpointBindingsOnPortal command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- Install WebSphere Portal
V7.0.0.1 or later, configure Business Space and REST services for
your product, and configure SSL and SSO.
- Make sure that the remote WebSphere Portal
server is started.
- Run the command on the deployment manager node.
- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- Run the command from your product deployment manager, but make
sure to designate the user name and the password for the WebSphere Portal administrator user ID.
- You must connect to the remote WebSphere Portal
deployment manager with a user ID that has WebSphere Application Server administrator
privileges for WebSphere Portal.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
updateEndpointBindingsOnPortal 
-serverName WebSphere\_Portal\_server\_name
 -nodeName WebSphere\_Portal\_node\_name
 -clusterName WebSphere\_Portal\_cluster\_name
 -host server\_IP\_or\_host -port SOAP\_port
 -user WebSphere\_Portal\_admin\_ID
 -password WebSphere\_Portal\_admin\_password
 -endpointBindingDirectoryName directory\_containing\_endpoints\_files
```

## Parameters

## Examples

```
wsadmin -user admin -password admin -lang jython 

wsadmin>AdminTask.updateEndpointBindingsOnPortal( [ '-nodeName', 'Portal\_node\_name',
 '-serverName', 'WebSphere\_Portal', '-endpointBindingDirectoryName',
 'directory\_containing\_endpoints\_files', '-host',
 'Portal\_server\_IP\_or\_host', '-port', 'Portal SOAP\_port\_default\_10025',
 '-user', 'Portal\_admin\_ID', '-password', 'Portal\_admin\_password' ] )
```

```
wsadmin -user admin -password admin -lang jython 

wsadmin>AdminTask.updateEndpointBindingsOnPortal( [ '-nodeName', 'Portal\_node\_name',
 '-serverName', 'WebSphere\_Portal', '-endpointBindingDirectoryName',
 'directory\_containing\_endpoints\_files', '-host', 'DMGR\_IP\_or\_host',
 '-port', 'DMGR\_SOAP\_port\_default\_8879', '-user', 'DMGR\_admin\_ID',
 '-password', 'DMGR\_admin\_password' ] )
```