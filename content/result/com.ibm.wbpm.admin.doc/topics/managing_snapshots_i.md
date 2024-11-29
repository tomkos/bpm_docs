# Deleting unneeded snapshots from a Workflow Center server manually

## Before you begin

The easy way to manage the accumulation of unnamed snapshots
on your Workflow Center server is to enable
automatic deletion of snapshots. However, you can also delete
specific unnamed snapshots or archived snapshots by following the
steps that follow.

You must be a repository administrator to
perform this task.

## About this task

You might want to delete unneeded snapshots to reduce
the size of the Workflow Center database.
If you have many projects in development in your Workflow Center, you
are likely to find that the Workflow Center database
is growing rapidly. One action that you can take is to remove unnamed
snapshots. Unnamed snapshots exist between named snapshots. Reduce
database bloat by removing the unnamed snapshots. You can also delete
archived snapshots for the same purpose.

You might also want
to delete unnamed snapshots if your Workflow Center server
performance is slowly degrading. Having hundreds or thousands of unnamed
snapshots on the server could contribute to worsening performance.
Delete snapshots that are not used or needed.

Use the wsadmin command BPMSnapshotCleanup to delete unnamed and archived snapshots for a process. The BPMSnapshotCleanup command deletes all instances of the
snapshot, including task instances and process instances, no matter
what state they are in. See the command reference topic for a complete
list of parameters for this command.

In many situations, it
is a good idea to purge unneeded snapshots on a regular schedule.
To avoid performance degradation or timeouts in  Process Designer run
the BPMSnapshotCleanup command when no operations
are running on the Workflow Center and
no connections are open between the Process Designer and
the Workflow Center.

## Procedure

1. Run the wsadmin
BPMListProcessApplication command on the Workflow Center server to show all process application
snapshots on that server.
2. Archive named snapshots if they are no longer needed and
you want to delete them. You can delete named snapshots
from the Workflow Center server only if they are archived. Run BPMShowSnapshot to see information about a specific snapshot.
3. Run the wsadmin BPMShowProcessApplication command to show details about the process application, including
the process application acronym. You need the acronym to
run the BPMSnapshotCleanup command.
4. Set the containerAcronym parameter
to identify the process application that contains the snapshots to
be deleted.
5. Set optional parameters. You must set at least
one optional parameter as a filter for determining which unnamed snapshots
are deleted. You can also use one of the optional parameters, deleteArchivedSnapshot, to delete archived snapshots in
addition to unnamed snapshots. See the BPMSnapshotCleanup command reference for a complete list of parameters for that command.
6. Run the BPMSnapshotCleanup command to
delete all unnamed snapshots that fit within the parameters that you
have defined. To
delete the first snapshot of a process application, you must use the -force option. The first snapshot is needed because it contains
the information that shows in the Revision History window in Process Designer. Tip: If you are using a SOAP connection,
the command can take longer to complete than the specified SOAP timeout
value. Although the command continues to run until it is finished,
you might see the exception java.net.SocketTimeoutException: Read
timed out. To prevent this exception, set a higher value for the com.ibm.SOAP.requestTimeout property in the profile\_root/properties/soap.client.props file.