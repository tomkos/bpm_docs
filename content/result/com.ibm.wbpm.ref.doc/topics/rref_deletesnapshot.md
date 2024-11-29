# BPMDeleteSnapshot command

Run the BPMDeleteSnapshot command to delete the process application snapshot
from the server. If you are deleting the default snapshot, you must use the
-force parameter.

The BPMDeleteSnapshot command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

Ensure that you meet the following prerequisites:

- Have administrative access to the snapshot.
- Deactivate the toolkit snapshot of the dependency by using the BPMDeactivate
command. For more information, see BPMDeactivate
command.
- Stop the toolkit snapshot by using the BPMStop command. For more information,
see BPMStop command.
- Get a list of toolkits and process applications that have dependencies on the toolkit snapshot
by using the following command on a Workflow Server:
BPMShowSnapshot -showDependents snapshot\_name. For more information, see BPMShowSnapshot command.Starting with the root of the list of
reported dependencies, remove each dependency. For each dependency that you want to remove, delete
the snapshot of the toolkit or process application.
After you resolve all of the dependencies,
delete the snapshot by using the BPMDeleteSnapshot command.
- There are no running BPEL instances.

- You can run the command for only one process application or toolkit at a time. In a network
deployment environment, you must run this command on the node containing the application cluster
member that handles Workflow Server or Workflow Center applications. Do not run this command from
the deployment manager profile.
- Only a user with Repository Admin privileges can delete a snapshot.

- The snapshot must exist.
- The snapshot must be inactive.
- The snapshot must have no running instances.
- The snapshot must not be a dependency for any other snapshot.
- The snapshot must not be deployed.
- In an Advanced
deployment environment, any
business-level applications that are related to the snapshot must
be uninstalled before you can delete the snapshot.

If one or more of the preconditions has not been met when
the command is run, the command is terminated and an error message
is written to the command-line console and the SystemOut.log file
to indicate which of the preconditions was not met. Generally, the
message contains some suggestions for achieving the preconditions.
For example:

You cannot delete an active snapshot.

To
view the status of a snapshot, use the BPMShowSnapshot
command. You can also view the status of snapshot instances
in the Inspector view of Process Designer.

1. Run the BPMShowProcessApplication command to
determine whether the snapshot exists for the process application.
2. Run the BPMShowSnapshot command to determine the status
of the snapshot, such as whether it is the default snapshot and whether it is active with running
instances.
3. For a snapshot of a toolkit, run the BPMShowSnapshot
command using the -showdependents
snapshot\_name parameter to determine if there are other dependencies. If there
are, starting with the root of the list of reported dependencies remove each dependency. For each
dependency that you want to remove, delete the snapshot of the toolkit or process application. You
must delete those dependencies first because a loop of dependencies will mean none of the snapshots
can be deleted.
4. Run the BPMDeactivate command to
deactivate the snapshot.
5. Run the BPMStop command to stop the snapshot
and its running instances.
6. Run the BPMUndeploy
command to undeploy the snapshot from the server. This command also uninstalls any
business-level applications that are related to the snapshot.

After you have completed these tasks, you can run the BPMDeleteSnapshot
command.

- When you delete a snapshot, any related process instances that have a status of Terminated,
Completed, or Failed will also be deleted.
- If you run the BPMDeleteSnapshot command on
a snapshot of a system process application or a toolkit, it removes
the process application or toolkit. To fix the problem, run the bootstrapProcessServerData utility,
which reinitializes the deleted process application or toolkit.
- When the default snapshot of a process application is deleted, the process application is
removed. Toolkits that the process application depended on remain. There might be other toolkits and
process applications depending on those remaining toolkits. The toolkits cannot be deleted while
those dependencies exist.

- When you are using the command to remove a snapshot that has many business process
instances.Note: Each instance of the snapshot must have a status of Terminated, Completed, or
Failed.
- When you are deleting many snapshots at a time by using the command. Note: Workflow Server snapshot deletion is not affected by the timeout.
To avoid the exception, increase the value of the SOAP.requestTimeout property,
which is set by default to 180 seconds. You can find this property in the
soap.client.props file in your server profile/properties
folder.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMDeleteSnapshot 
-containerAcronym process\_application\_or\_toolkit\_acronym
-containerSnapshotAcronyms snapshot\_acronym
-caseDosName input\_dos\_name
[-force]
[-outputFile file\_path]
```

## Parameters

If you do not know the acronym
for a required parameter, use the BPMShowProcessApplication command
to list the details of a process application and its snapshots, including
acronyms.

## Examples

The following example shows how
to establish a SOAP connection to Workflow Server and
delete those snapshots for the process application BILLDISP that have
snapshots acronyms of SS2.0.1 and SS2.0.2:

<!-- image -->

```
wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMDeleteSnapshot('[-containerAcronym BILLDISP -containerSnapshotAcronyms [SS2.0.1 SS2.0.2]]')
```