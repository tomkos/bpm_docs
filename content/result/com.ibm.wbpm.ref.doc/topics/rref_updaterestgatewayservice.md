# updateRESTGatewayService command

This command updates the
REST Gateway service when the deployment manager is running so that
REST services are configured and enabled. The deployment of the REST
services is performed automatically in a stand-alone server profile.
For other types of configurations, the REST Services administrative
console page or the updateRESTGatewayService allows
you to configure REST services for all of your product's widgets in Business Space.

The updateRESTGatewayService command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- Run the command on the deployment manager node.
- If the deployment manager is stopped, use the -conntype
none option to run the command in disconnected mode.
- If the deployment manager is running, you must connect with a
user ID that has WebSphere® Application
Server administrator privileges. Do not use the wsadmin -conntype
none option.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
updateRESTGatewayService 
-clusterName cluster\_name
-nodeName node\_name
-serverName server\_name
-enable true | false
[-type name\_of\_service\_type -version name\_of\_version]
```

## Parameters

## Example

```
wsadmin -user admin -password admin -lang jython 

wsadmin>AdminTask.updateRESTGatewayService( [ '-clusterName', 'cluster1',
'-type', '{com.ibm.bpm}TimeTable', '-version', '6.2.0.0', '-enable', 'true' ] )
```