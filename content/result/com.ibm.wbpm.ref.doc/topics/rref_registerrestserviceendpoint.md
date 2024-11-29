# registerRESTServiceEndpoint command

This command registers the
REST service endpoints so that Business Space is properly
connected to widgets for your product. This command registers the
endpoints of the REST services that are in the same cell as Business Space.

The registerRESTServiceEndpoint command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- Run the command on the deployment manager node.
- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- You must connect with a user ID that has WebSphere® Application Server administrator
privileges.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
registerRESTServiceEndpoint 
-clusterName cluster\_name
-businessSpaceClusterName name\_of\_business\_space\_cluster
-serverName name\_of\_rest\_services\_server
-nodeName name\_of\_rest\_services\_node
-businessSpaceServerName name\_of\_business\_space\_server
[-appName name\_of\_provider\_application]
[-name name\_of\_rest\_service]
[-type name\_of\_service\_type]
[-version name\_of\_version]
[-webModuleName name\_of\_web\_module]
```

## Parameters

```
<tns:Endpoint>
    <tns:id>{com.ibm.bpm}SCA</tns:id>
    <tns:type>{com.ibm.bpm}SCA</tns:type>
    <tns:version>6.2.0.0</tns:version>
    <tns:url>/rest/sca/v1</tns:url>
    <tns:description>Location backend SCA REST Services
 for Module Administration widgets and Service Monitoring widget
</tns:description>
  </tns:Endpoint>
```

## Example

```
wsadmin -user admin -password admin -lang jython 
wsadmin>AdminTask.registerRESTServiceEndpoint( [ '-clusterName',
'name\_of\_rest\_services\_cluster', '-businessSpaceClusterName',
'name\_of\_business\_space\_cluster' ] )
```