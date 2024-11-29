# maintainDocumentStoreTrace command

If you configured IBM® Business Automation Workflow to
use an external Enterprise Content Management server, then this command
does not apply. The equivalent procedure in FileNet P8 Platform is
in the topic Troubleshooting.

## Prerequisites

The following conditions must
be met:

- The command must be run on the deployment manager node.
- One or more application cluster members must be running.
- Run the command in connected mode. Do not specify the wsadmin
-conntype none option.
- You must connect to the deployment manager with a user ID that
has WebSphere Application Server operator privileges.

Before running this command, review Managing tracing for the BPM document store.

## Location

Start the wsadmin scripting client from the
profile\_root/bin directory of the deployment manager
profile. The maintainDocumentStoreTrace command does not write to a log file, but
the wsadmin scripting client always writes a
profile\_root/logs/wsadmin.traceout log file where you will
find exception stack traces and other information.

## Syntax

```
maintainDocumentStoreTrace
-serverName server\_name
-nodeName node\_name
-clusterName cluster\_name
-deName deployment\_environment\_name
-disable componentName|all
-enable componentName|all
-list
```

## Parameters

You must specify the -clusterName parameter,
or the -deName parameter, or both the -serverName and -nodeName parameters.
As an alternative to specifying any parameters, you can invoke the
command on a target object of type BPMDeploymentEnvironment, ServerCluster,
or Server.

You must also specify
one or more of the following parameters:

- -disable
- -enable
- -list

Any changes are effective immediately and no additional
save operation needs to be performed.

The following components
are included in the BPM document store:

- API
- AsynchronousProcessing
- AuditDisposition
- CBR
- CFSDaemon
- CFSImportAgent
- CodeModule
- ContentCache
- ContentStorage
- Database
- EJB
- Engine
- Error
- Events
- FixedContentProvider
- GCD
- Handler
- Metadata
- Publish
- Replication
- Search
- Security
- SSI
- Sweep
- ThumbnailGeneration
- WSI

## Examples

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreTrace(['-nodeName', 'myNodeName', '-serverName', 'myServerName', '-list'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreTrace(['-nodeName', 'myNodeName', '-serverName', 'myServerName', '-enable', 'componentName' | 'all'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreTrace(['-nodeName', 'myNodeName', '-serverName', 'myServerName', '-disable', 'componentName' | 'all'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreTrace(['-clusterName', 'myClusterName', '-list'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreTrace(['-clusterName', 'myClusterName', '-enable', 'componentName' | 'all'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreTrace(['-clusterName', 'myClusterName', '-disable', 'componentName' | 'all'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreTrace(['-deName', 'myDeName', '-list'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreTrace(['-deName', 'myDeName', '-enable', 'componentName' | 'all'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.maintainDocumentStoreTrace(['-deName', 'myDeName', '-disable', 'componentName' | 'all'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>server = AdminConfig.getid('/Cell:/Node:myNodeName/Server:myServerName')
wsadmin>AdminTask.maintainDocumentStoreTrace(server, ['-enable', 'componentName' | 'all'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>cluster = AdminConfig.getid('/Cell:/ServerCluster:myClusterName')
wsadmin>AdminTask.maintainDocumentStoreTrace(cluster, ['-enable', 'myComponentName' | 'all'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>de = AdminConfig.getid("/Cell:/BPMCellConfigExtension:/BPMDeploymentEnvironment:myDeName/")
wsadmin>AdminTask.maintainDocumentStoreTrace(de, ['-list'])
```