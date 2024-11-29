# startDocumentStoreMigration command

The startDocumentStoreMigration command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

The following conditions must
be met:

- The command must be run on the deployment manager node.
- One or more application cluster members must be running.
- Run the command in connected mode. Do not specify the wsadmin
-conntype none option.
- You must connect to the deployment manager with a user ID that
has WebSphere Application Server operator privileges.

Before running this command, you should review the task topic
"Migrating document attachments to the BPM document store."

## Location

In clustered environments, start the wsadmin scripting client from the
profile\_root/bin directory of the deployment manager
profile. The startDocumentStoreMigration command does not write to a log file,
but the wsadmin scripting client always writes a
profile\_root/logs/wsadmin.traceout log file where you will
find exception stack traces and other information.

## Syntax

```
startDocumentStoreMigration
-serverName server\_name
-nodeName node\_name
-clusterName cluster\_name
-deName deployment\_environment\_name
[-keepFailedDocuments true|false]
```

## Parameters

You must specify the -clusterName parameter,
or the -deName parameter, or both the -serverName and -nodeName parameters.
As an alternative to specifying any parameters, you can invoke the
command on a target object of type BPMDeploymentEnvironment, ServerCluster,
or Server.

## Examples

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.startDocumentStoreMigration(['-nodeName', 'myNodeName', '-serverName', 'myServerName'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.startDocumentStoreMigration(['-clusterName', 'myClusterName'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.startDocumentStoreMigration(['-deName', 'myDeName'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>server = AdminConfig.getid('/Cell:/Node:myNodeName/Server:myServerName')
wsadmin>AdminTask.startDocumentStoreMigration(server)
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>cluster = AdminConfig.getid('/Cell:/ServerCluster:myClusterName')
wsadmin>AdminTask.startDocumentStoreMigration(cluster)
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>de = AdminConfig.getid("/Cell:/BPMCellConfigExtension:/BPMDeploymentEnvironment:myDeName/")
wsadmin>AdminTask.startDocumentStoreMigration(de)
```