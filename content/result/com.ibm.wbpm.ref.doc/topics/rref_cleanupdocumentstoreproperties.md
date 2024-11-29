<!-- image -->

# cleanupDocumentStoreProperties command

To run a process that uses the Basic Case Management
feature to manage documents and folders, you must have installed the
Basic Case Management feature from a previous release.

The cleanupDocumentStoreProperties command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

The following conditions
must be met:

- The command must be run on the deployment manager node.
- One or more application cluster members must be running.
- The command must be run in connected mode. Do not specify the wsadmin
-conntype none option.
- You must connect to the deployment manager with a user ID that
has WebSphere Application Server operator privileges.

## Location

Start the wsadmin scripting client from the
profile\_root/bin directory of the deployment manager
profile. The cleanupDocumentStoreProperties command does not write to a log file,
but the wsadmin scripting client always writes a
profile\_root/logs/wsadmin.traceout log file where you will
find exception stack traces and other information.

## Syntax

```
cleanupDocumentStoreProperties
-containerAcronym container\_acronym
-serverName server\_name
-nodeName node\_name
-clusterName cluster\_name
-deName deployment\_environment\_name
```

## Required parameters

You must specify the -clusterName parameter,
or the -deName parameter, or both the -serverName and -nodeName parameters.
As an alternative to specifying those parameters, you can run the
command on a target object of type BPMDeploymentEnvironment, ServerCluster,
or Server.

## Output

- For each property property that is removed
from a case folder type case\_type, the property
name and the case type name are reported.CWTDS2052I: The property 'property' was removed from the case type 'case\_type'.Otherwise,
if there are no properties to delete, the command outputs the following
message:CWTDS2054I: There was no property to be deleted from any case type.
- For each property property that is removed
from a document type document\_type, the property
name and the document type name are reported.CWTDS2053I: The property 'property' was removed from the document type 'document\_type'.Otherwise,
if there are no properties to delete, the command outputs the following
message:CWTDS2055I: There was no property to be deleted from any document type.
- For each property template property\_template that
is deleted, the property template name is reported.CWTDS2049I: The property template 'property\_template' was deleted.Otherwise,
if there are no property templates to delete, the command outputs
the following message:CWTDS2050I: No property template was deleted.

## Examples

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.cleanupDocumentStoreProperties(['-nodeName', 'myNodeName', '-serverName', 'myServerName', '-containerAcronym', 'MYAPP'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.cleanupDocumentStoreProperties(['clusterName', 'myClusterName', '-containerAcronym', 'MYAPP'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.cleanupDocumentStoreProperties(['-deName', 'myDeName', '-containerAcronym', 'MYAPP'])
```

The
following Jython example uses the cleanupDocumentStoreProperties command
to remove unused properties for the MYAPP application
for a specified server target object:

```
wsadmin -user admin -password admin -lang jython
wsadmin>server = AdminConfig.getid('/Cell:/Node:myNodeName/Server:myServerName')
wsadmin>AdminTask.cleanupDocumentStoreProperties(server, ['-containerAcronym', 'MYAPP'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>cluster = AdminConfig.getid('/Cell:/ServerCluster:myClusterName')
wsadmin>AdminTask.cleanupDocumentStoreProperties(cluster, ['-containerAcronym', 'MYAPP'])
```