# updateDocumentStoreApplication command

If you configured IBM® Business Automation Workflow to
use an external Enterprise Content Management server, then this command
does not apply.

The updateDocumentStoreApplication command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

The following conditions must
be met:

- The command must be run on the deployment manager node.
- Run the command in either local or connected mode.
- When running the command in connected mode, you must specify a
user ID that has WebSphere Application Server operator and deployer
privileges.

Before running this command, review Updating the BPM document store application.

## Location

Start the wsadmin scripting client
from the deployment\_manager\_profile/bin directory
on either Workflow Server or Workflow Center. The updateDocumentStoreApplication command
does not write to a log file, but the wsadmin scripting client always
writes a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
updateDocumentStoreApplication
-serverName server\_name
-nodeName node\_name
-clusterName cluster\_name
-deName deployment\_environment\_name
```

## Required parameters

You must specify the -clusterName parameter,
or the -deName parameter, or both the -serverName and -nodeName parameters.
As an alternative to specifying any parameters, you can invoke the
command on a target object of type BPMDeploymentEnvironment, ServerCluster,
or Server.

## Examples

The updateDocumentStoreApplication can
be run in either local mode or connected mode.

```
wsadmin -conntype none -lang jython
```

```
wsadmin -user admin -password admin -lang jython
```

The
examples that follow are based on the assumption that you are running
in connected mode.

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.updateDocumentStoreApplication(['-nodeName', 'myNodeName', '-serverName', 'myServerName'])
wsadmin>AdminConfig.save()
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.updateDocumentStoreApplication(['-clusterName', 'myClusterName'])
wsadmin>AdminConfig.save()
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.updateDocumentStoreApplication(['-deName', 'myDeName'])
wsadmin>AdminConfig.save()
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>server = AdminConfig.getid('/Cell:/Node:myNodeName/Server:myServerName')
wsadmin>AdminTask.updateDocumentStoreApplication(server)
wsadmin>AdminConfig.save()
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>cluster = AdminConfig.getid('/Cell:/ServerCluster:myClusterName')
wsdmin>AdminTask.updateDocumentStoreApplication(cluster)
wsadmin>AdminConfig.save()
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>de = AdminConfig.getid("/Cell:/BPMCellConfigExtension:/BPMDeploymentEnvironment:myDeName/")
wsadmin>AdminTask.updateDocumentStoreApplication(de)
wsadmin>AdminConfig.save()
```