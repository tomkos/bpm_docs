# BPMSnapshotCleanup command

From a Workflow Center server,
use the BPMSnapshotCleanup command to delete unused
snapshots of a process application when they are obsolete or older
than a specified snapshot.

The BPMSnapshotCleanup command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- Use the BPMSnapshotCleanup command in connected
mode from a Workflow Center server. In a network deployment environment, you must run this
command on the node containing the application cluster member that
handles Workflow Center applications.
Do not run this command from the deployment manager profile.
- You must be a repository administrator.
- You cannot delete the first snapshot of a branch even though it might be unnamed or archived.
The first snapshot contains original information about the snapshot that is displayed in the history
panel in  Process Designer.
- You cannot delete the tip snapshot, which is
the most recent snapshot.
- You must archive named snapshots before you delete them.
- Run the command when the load on the system
is low, for example, during off-peak hours, as the operation locks
snapshots and deletes process instances, preventing you from updating
those resources. In addition, being a resource-intensive activity,
it might affect performance when the activity runs in parallel with
other operations.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMSnapshotCleanup 
-containerAcronym process\_application\_acronym
[-containerSnapshotAcronyms process\_application\_snapshot\_acronym]
[-containerTrackAcronym track\_acronym]
[-keptNumber number\_of\_unnamed\_snapshots\_to\_keep]
[-createdBeforeLocal local\_time\_on\_the\_server]
[-createdAfterLocal local\_time\_on\_the\_server]
[-createdBeforeSnapshotAcronym snapshot\_acronym]
[-deleteArchivedSnapshot true|false]
[-ignoreDependency false]
[-outputFile output\_file\_name]
```

## Parameters

- If keptNumber is greater than or equal to
the total number of unnamed snapshots, no snapshots are deleted.
- If keptNumber equals 0, all the unnamed snapshots
are deleted except the tip snapshot.

## Examples

The following examples illustrate
how to delete snapshots that use the BPMSnapshotCleanup command.

```
wsadmin -conntype SOAP -port 8080 -host PC1.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMSnapshotCleanup ('[-containerAcronym BILLDISP -containerTrackAcronym Main -keptNumber 100]')
```

```
wsadmin -conntype SOAP -port 8080 -host PC1.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMSnapshotCleanup ('[-containerAcronym BILLDISP -createdAfterLocal 2012-01-01T00:00:00 
-createdBeforeLocal 2012-02-31T21:37:06]')
```

```
wsadmin -conntype SOAP -port 8080 -host PC1.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMSnapshotCleanup ('[-containerAcronym BILLDISP -createdBeforeLocal 2012-01-02T21:37:06]') 
OR:
wsadmin>AdminTask.BPMSnapshotCleanup ('[-containerAcronym BILLDISP -createdBeforeLocal 2012-05-02 
-deleteArchivedSnapshot true]')
```

```
wsadmin -conntype SOAP -port 8080 -host PC1.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMSnapshotCleanup ('[-containerAcronym BILLDISP -createdAfterLocal 2012-05-31T21:38:00]') 
OR: 
wsadmin>AdminTask.BPMSnapshotCleanup ('[-containerAcronym BILLDISP -createdAfterLocal 2012-07-31 
-deleteArchivedSnapshot true]')
```

```
wsadmin -conntype SOAP -port 8080 -host PC1.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMSnapshotCleanup ('[-containerAcronym BILLDISP -createdBeforeSnapshotAcronym SS2.0.1]')
```

```
wsadmin -conntype SOAP -port 8080 -host PC1.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.BPMSnapshotCleanup ('[-containerAcronym BILLDISP -containerTrackAcronym Main 
-containerSnapshotAcronyms SS2.0.1]')
```