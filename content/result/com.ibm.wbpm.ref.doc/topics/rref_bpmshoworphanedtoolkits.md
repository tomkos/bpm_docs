# BPMShowOrphanedToolkits command

Traditional: 
This command returns a list of toolkit snapshots that are not referenced by
other process applications or toolkits. You can use the list to delete the orphan snapshots on your
server.

The BPMShowOrphanedToolkits command was introduced in
IBM® Business Process Manager
 8.5.7 cumulative fix (CF)
2017.03.

When you install a process application snapshot on a workflow server, the toolkit snapshots that
the process application references are also installed with it. However, when you delete a process
application snapshot, the toolkit snapshots are not deleted. You can use the
BPMShowOrphanedToolkits in connected mode from either a Workflow Center server or Workflow Server to return a list of all orphaned toolkit
snapshots on that server. You can use output from this command in a script with other wsadmin
commands. For example, you can use the output from the BPMShowOrphanedToolkits
command as input to the BPMDeleteSnapshot command.

The BPMShowOrphanedToolkits command is run using the AdminTask object of the
wsadmin scripting client.

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- In a network deployment environment, you must run
this command on the node containing the application cluster member
that handles Workflow Server or Workflow Center applications.
Do not run this command from the deployment manager profile.
- The installation package must already be created and extracted
on the server. After this command is complete, the installed snapshot
is active.
- Note: If you are using a SOAP connection, the command can take
longer to complete than the specified SOAP timeout value. Although
the command continues to run until it is finished, you might see the
exception java.net.SocketTimeoutException: Read timed out.
To prevent this exception, set a higher value for the com.ibm.SOAP.requestTimeout
property in the profile\_root/properties/soap.client.props file.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMShowOrphanedToolkits 

[-showOrphanedToolkitSnapshot true|false]
[-orphanedToolkitAcronym toolkit\_acronym]
```

## Parameters

## Example

The following example illustrates
how to return all the orphaned snapshots of  the toolkit that has
the acronym TK6. In the example, the user establishes a SOAP connection
to the Workflow Center server.

<!-- image -->

```
wsadmin -conntype SOAP -port 8880 -host localhost -user admin -password admin -lang jython
wsadmin>AdminTask.BPMShowOrphanedToolkits('[-showOrphanedToolkitSnapshot false -orphanedToolkitAcronym TK6]')
```

```
{containerName: TK2
containerAcronym:ORTTTK2
containerSnapshotAcronym: S1}
{containerName: TK6
containerAcronym:ORTTTK6
containerSnapshotAcronym: S2}
{containerName: TK5
containerAcronym:ORTTTK5
```