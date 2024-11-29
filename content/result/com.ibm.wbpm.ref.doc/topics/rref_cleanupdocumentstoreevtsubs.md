# cleanupDocumentStoreEventSubscriptions command

Event subscriptions are created by Process Designer for
document and folder classes. The event subscriptions are stored in
the BPM document store.
When named snapshots, branches or process applications are deleted,
or an event subscription is modified or removed in Process Designer, the
corresponding subscription in the BPM document store is not
removed. Another event subscription might still exist in another process
application that remains subscribed to the same event.

This
command checks all event subscriptions in all process applications
and synchronizes the event subscriptions with the BPM document store. Subscriptions
that are no longer needed are removed. The command reduces the load
on the system as the system does not need to handle events where event
subscriptions no longer exist.

To run a process that uses the
Basic Case Management feature to manage documents and folders, you
must have installed the Basic Case Management feature from a previous
release.

The cleanupDocumentStoreEventSubscriptions command
is run by using the AdminTask object of the wsadmin scripting client.

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
profile. The cleanupDocumentStoreEventSubscriptions command does not write to a
log file, but the wsadmin scripting client always writes a
profile\_root/logs/wsadmin.traceout log file where you find
exception stack traces and other information.

## Syntax

```
cleanupDocumentStoreEventSubscriptions
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

- If event subscriptions are removed, then the number of changes
is reported.CWTDS2060I: The cleanup finished successfully. '{0}' changes were made.Otherwise,
if there are no event subscriptions to remove, the command outputs
the following message:CWTDS2059I: The cleanup finished successfully without making any changes.

## Examples

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.cleanupDocumentStoreEventSubscriptions(['-nodeName', 'myNodeName', '-serverName', 'myServerName'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.cleanupDocumentStoreEventSubscriptions(['clusterName', 'myClusterName'])
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.cleanupDocumentStoreEventSubscriptions(['-deName', 'myDeName'])
```

The
following Jython example uses the cleanupDocumentStoreEventSubscriptions command
to remove event subscriptions for a specified server target object:

```
wsadmin -user admin -password admin -lang jython
wsadmin>server = AdminConfig.getid('/Cell:myCellName/Node:myNodeName/Server:myServerName')
wsadmin>AdminTask.cleanupDocumentStoreEventSubscriptions(server)
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>cluster = AdminConfig.getid('/Cell:myCellName/ServerCluster:myClusterName')
wsadmin>AdminTask.cleanupDocumentStoreEventSubscriptions(cluster)
```