# Deleting snapshots

## Before you begin

- For information about the prerequisites for deleting snapshots from Workflow Server see BPMDeleteSnapshot command.
- For information about the prerequisites for deleting snapshots from Workflow Center see BPMSnapshotCleanup command.
- BPMCSRFToken is required for this REST API. For more information, see Preventing cross site request forgery.

## Using the Process Admin Console

1. Click Server Admin > Workflow Admin > Health Management.
2. Select the command Delete Snapshots.
3. Specify values for the command's parameters.
4. Click Submit.
5. If there is an error, you will see the error message. Otherwise, you can check the progress of
the deletion in the system log.

## Using a REST API call

Call the operations REST API DELETE
https://host:port/ops/std/bpm/containers/acronym/versions.
Where acronym is the acronym of the process application or toolkit that contains
the snapshots to delete.

- Delete named snapshots V01 and V02 of toolkit
TK1:DELETE http://host:port/ops/std/bpm/containers/TK1/versions?versions=V01,V02
- Delete the last and default snapshot VLAST of process application
APP1:DELETE http://host:port/ops/std/bpm/containers/APP1/versions?versions=VLAST&force=true

- Delete archived named snapshots V01 and V02 of the default
branch of toolkit
TK1:DELETE http://host:port/ops/std/bpm/containers/TK1/versions?versions=V01,V02
- Delete all unnamed snapshots except the tip snapshot of branch Test of toolkit
TK1:DELETE http://host:port/ops/std/bpm/containers/TK1/versions?branch\_name=Test&kept\_number=0
- Delete all unnamed snapshots of branch Test of process application
APP1 created before snapshot
V20:DELETE http://host:port/ops/std/bpm/containers/APP1/versions?branch\_name=Test&created\_before\_snapshot=V20
- Delete all unnamed snapshots of branch Test of process application
APP1 created before a point in
time:DELETE http://host:port/ops/std/bpm/containers/APP1/versions?branch\_name=Test&created\_before=2016-10-01T00:00:00-06:00Remember: If you need to specify a time zone that is ahead of UTC, you must encode the
+ symbol as %2B. For example, for the Central European Time zone
+01:00, you must use %2B01:00 in your URL. Alternatively, you can
specify a UTC date, for example created\_before=2016-01-01T01:00:00Z.
Remember: The operations REST APIs have the following URL,
https://hostname.bpm.ibmcloud.com/bpm/environment/ops/std/bpm/containers/acronym/versions,
where environment has the value dev for the development system,
test for the test system, or run for the production (runtime)
system.