# maintainDocumentStoreAuthorization command

## Prerequisites

If you configured IBM® Business Automation Workflow to
use an external Enterprise Content Management server, this command
can still be used to assign permissions to a user with the EmbeddedECMTechnicalUser
role. Security configuration for other users and groups is handled
by the FileNet P8 Platform. See Update object store with new users and groups.

By
default, the user who is resolved by the EmbeddedECMTechnicalUser BPM document store role
is the only user authorized to manage the domain and the default object
store. The command ensures that the last remaining user or group cannot
be removed.

The maintainDocumentStoreAuthorization command
is run by using the AdminTask object of the wsadmin scripting client.

The
following conditions must be met:

- The command must be run on the deployment manager node.
- One or more application cluster members must be running.
- Run the command in connected mode. Do not specify the wsadmin
-conntype none option.
- You must connect to the deployment manager with a user ID that
has WebSphere Application Server operator privileges.

Before you run this command, review Administering the technical user for the BPM document store.

If you change the technical user then a change to the
application settings of IBM\_BPM\_DocStoreAdmin is required to allow
the new technical user to access the IBM Administrative Console for
Content Platform Engine.

## Location

Start the wsadmin scripting client from the
profile\_root/bin directory of the deployment manager
profile. The maintainDocumentStoreAuthorization command does not write to a log
file. It directly responds with a message. However, the wsadmin scripting client always writes a
profile\_root/logs/wsadmin.traceout log file where you find
exception stack traces and other information.

## Syntax

```
maintainDocumentStoreAuthorization
-serverName server\_name
-nodeName node\_name
-clusterName cluster\_name
-deName deployment\_environment\_name
-add distinguished\_name
-remove distinguished\_name
-list
```

## Parameters

You must specify the -clusterName parameter,
or the -deName parameter, or both the -serverName and -nodeName parameters.
As an alternative to specifying any parameters, you can invoke the
command on a target object of type BPMDeploymentEnvironment, ServerCluster,
or Server.

You must also specify
one of the following parameters:

- -add
- -remove
- -list

## Examples

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreAuthorization(['-nodeName', 'myNodeName', '-serverName', 'myServerName', '-list'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreAuthorization(['-nodeName', 'myNodeName', '-serverName', 'myServerName', '-add', 'user\_ID' | 'group\_ID'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreAuthorization(['-nodeName', 'myNodeName', '-serverName', 'myServerName', '-remove', 'user\_ID' | 'group\_ID'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreAuthorization(['-clusterName', 'myClusterName', '-list'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreAuthorization(['-clusterName', 'myClusterName', '-add', 'user\_ID' | 'group\_ID'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreAuthorization(['-clusterName', 'myClusterName', '-remove', 'user\_ID' | 'group\_ID'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreAuthorization(['-deName', 'myDeName', '-list'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreAuthorization(['-deName', 'myDeName', '-add', 'user\_ID' | 'group\_ID'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreAuthorization(['-deName', 'myDeName', '-remove', 'user\_ID' | 'group\_ID'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>server = AdminConfig.getid('/Cell:/Node:myNodeName/Server:myServerName')
wsadmin>AdminTask.maintainDocumentStoreAuthorization(server, '[-add user\_ID | group\_ID]')
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>cluster = AdminConfig.getid('/Cell:/ServerCluster:myClusterName')
wsadmin>AdminTask.maintainDocumentStoreAuthorization(cluster, ['-add', 'user\_ID' | 'group\_ID'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>de = AdminConfig.getid('/Cell:/BPMCellConfigExtension:/BPMDeploymentEnvironment:myDeName/")
wsadmin>AdminTask.maintainDocumentStoreAuthorization(de, ['-add', 'user\_ID' | 'group\_ID'])
```

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreAuthorization('[-nodeName Node1 -serverName server1 -list]')
```

```
Authorization on the domain for the BPM document store\r\nCWTDS2034I: Access is granted to the BPM document store domain
'uid=deadmin,o=defaultWIMFileBasedRealm' with access mask '459,267'
Authorization on the object store for the BPM document store\r\nCWTDS2035I: Access is granted to the BPM document
store object store 'uid=deadmin,o=defaultWIMFileBasedRealm' with access mask '838,205,440'
```