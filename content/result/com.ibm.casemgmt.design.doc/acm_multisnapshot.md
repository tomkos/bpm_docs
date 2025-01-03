# Creating flexible case activities

As of 23.0.2, you can enable users to initiate more flexible activities that start from the same
snapshot as their parent case
instance. The Starts from the parent case
snapshot
option in the configuration properties of the activity enables you to initiate activities from a snapshot that reflects the business
process logic in place when the case instance was created, rather than the logic of the default case
snapshot.

## Expected activity behaviors

- The type of environment that is being used, Process Center (development
environment) vs Process Server (production environment).
- Where the case started from and the activities within the case are initiated, by clicking the
Play button from the snapshot or from the solution process
application.
- Whether the Starts from the parent case
snapshot
checkbox in the configuration properties of the activity is selected or clear.

| Scenario                                                                                  | Checkbox is selected                                                                         | Checkbox is clear                                                                                                                                                       |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Process Center                                                                            | Process Center                                                                               | Process Center                                                                                                                                                          |
| The case is created from the solution process application when an active snapshot exists. | The activity starts from the tip from when the activity was started.                         | The activity starts from the most recently activated snapshot at the time of case creation. If the snapshot is no longer active, then the activity starts from the tip. |
| The case is created from a specific snapshot in the snapshot list                         | The activity starts from the specific snapshot that was used when case instance was created. | The activity starts from the specific snapshot that was used when case instance was created.                                                                            |
| The case is created from the solution process application                                 | The activity starts from the tip from when the activity was started.                         | The activity starts from the tip from when the activity was started.                                                                                                    |
| Process Server                                                                            | The activity starts by using the default, active snapshot at the time of activity creation.  | The activity starts by using the specific snapshot that was default and active at time of case creation.                                                                |

Client-side human services pages

## Limitations

| Scenario                                                                                                                                                                                                                                                                                                                                                                             | Result                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A solution with snapshot1 has a case type case1 that is defined with an activity that is configured to a process, say, activity1 with process1. Snapshot2 has a new activity that is configured to a process, say activity2 with process2. Both snapshots are activated.                                                                                                             | If a case instance is created out of snapshot1, activity2 appears as 'failed' because the process is not available in snapshot1 of the solution process application. |
| A solution with snapshot1 has a case type case1 with a property named property1. Snapshot2 A new property property2 is added to the case type case1 and is set as required.                                                                                                                                                                                                          | If you try to add cases with snapshot1, the action fails with a message “Required property is missing".                                                              |
| A solution with snapshot1 has a case type case1 defined with an activity that is configured to a process, say activity1with process1. Snapshot2 has a new external toolkit that is added with a process say process2. An activity with an existing process activity2 is created under case type case1 and uses “This project” as the workflow project. Both snapshots are activated. | If a case instance is created out of snapshot1, activity2 appears as 'failed' because the toolkit for process2 is not available in snapshot1 of “This project”.      |

## Using flexible case activities for case instances existing from previous releases

Before you use the flexible case activities feature, you need to update the case instances that
exist from previous releases by using scripts.

The following sample query fetches case instances of a specific case type and created before a
specific date that is still in Working state:

```
SELECT [This], [CmAcmCaseIdentifier], [CmAcmCaseState], [Name] FROM [CmAcmCaseFolder] WHERE [DateCreated] < 
20230809T183000Z AND [CmAcmCaseIdentifier] like 'TE\_loancasetype%' AND [CmAcmCaseState] = 2 OPTIONS(TIMELIMIT 180,COUNT\_LIMIT 1000)
```

```
importClass(Packages.com.filenet.api.property.Properties);
importClass(Packages.com.filenet.api.constants.RefreshMode);
function OnCustomProcess (CEObject)
{ 
     CEObject.refresh(); 
     CEObject.getProperties().putValue("CmAcmSnapshotId", "2064.828db841-dd71-4323-a99a-43a6102bc00d");
     CEObject.getProperties().putValue("CmAcmSnapshotName", "Test1"); CEObject.save(RefreshMode.REFRESH);
 }
```