# correctDocumentStoreInstanceAuthorization command

If you switch to an external ECM server, your Business Automation Workflow and external
ECM environments have a shared user registry configured. Business Automation Workflow will
print warnings into the SystemOut.log file of the application cluster
when it cannot authorize users on content artifacts because the users
or groups are not available in the shared user registry. There can
be several reasons for users or groups not being shared:

- The users or groups are defined in a file-based repository. In
this case, no correction can be made.
- The users or groups are defined in a Lightweight Directory Access
Protocol (LDAP) user repository, but the LDAP repository is not consistently
connected to the two systems. For example, the base entry is not the
same or different LDAP search filters are used.

You can correct the LDAP connection settings to enable users
and groups to be shared. After correcting the connection settings,
you can run the correctDocumentStoreInstanceAuthorization command
to update the case and BPD instances or the team instances with the
correct authorization information for the users and groups.

## Prerequisites

The correctDocumentStoreInstanceAuthorization command
is run using the AdminTask object of the wsadmin scripting client.
The following conditions must be met:

- The command must be run on the deployment manager node.
- One or more application cluster members must be running.
- Run the command in connected mode. Do not specify the wsadmin
-conntype none option.
- You must connect to the deployment manager with a user ID that
has WebSphere Application Server operator privileges.

## Location

Start the wsadmin scripting client
from the profile\_root/bin directory
of the deployment manager profile.
The correctDocumentStoreInstanceAuthorization command
does not write to a log file, it directly responds with a message.
However, the wsadmin scripting client always writes a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
correctDocumentStoreInstanceAuthorization
-serverName server\_name
-nodeName node\_name
-clusterName cluster\_name
-deName deployment\_environment\_name
-instanceID instance\_ID
-teamID team\_ID
```

## Parameters

You must specify the -clusterName parameter,
or the -deName parameter, or both the -serverName and -nodeName parameters.
As an alternative to specifying any parameters, you can invoke the
command on a target object of type BPMDeploymentEnvironment, ServerCluster,
or Server.

You must also specify
one of the following parameters:

- -instanceID
- -teamID

## Examples

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.correctDocumentStoreInstanceAuthorization(['-nodeName', 'myNodeName', '-serverName', 'myServerName', '-instanceID', myInstanceID])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.correctDocumentStoreInstanceAuthorization(['-nodeName', 'myNodeName', '-serverName', 'myServerName', '-teamID', myTeamID])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.correctDocumentStoreInstanceAuthorization(['-clusterName', '-instanceID', myInstanceID])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.correctDocumentStoreInstanceAuthorization(['-clusterName', 'myClusterName', '-teamID', myTeamID])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.correctDocumentStoreInstanceAuthorization(['-deName', 'myDeName', '-instanceID', myInstanceID])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.correctDocumentStoreInstanceAuthorization(['-deName', 'myDeName', '-teamID', myTeamID])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>server = AdminConfig.getid('/Cell:/Node:myNodeName/Server:myServerName')
wsadmin>AdminTask.correctDocumentStoreInstanceAuthorization(server, ['-instanceID', myInstanceID])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>cluster = AdminConfig.getid('/Cell:/ServerCluster:myClusterName')
wsadmin>AdminTask.correctDocumentStoreInstanceAuthorization(cluster, [['-instanceID', myInstanceID])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>de = AdminConfig.getid('/Cell:/BPMCellConfigExtension:/BPMDeploymentEnvironment:myDeName/')
wsadmin>AdminTask.correctDocumentStoreInstanceAuthorization(de, ['-teamID', myTeamID])
```