# Deleting a deployed solution

## About this task

- Solution folder and all child folders and objects in the object store.
- Case type folder, Case folders, activity objects, process instances, document references, and so
on.
- Class definitions associated with the solution.
- Case type class definitions, activity definitions.
- The subscriptions associated with the solution.

- Content Platform Engine workflow system artifacts
    - Application space, event logs, queues, rosters, and so on
- Documents filed in Cases

- References are removed from the case folders. You can still find the documents if they are filed
in folders outside of the solution or in the unfiled folder.
- Events that are associated with cases and activity tasks

- Content Platform Engine events and
workflow system events are not removed.
- Events that are published for analytics

- Events in reporting tools such as Case Analyzer, Case History, or Business
Automation Insights through Case Emitter are not removed.
- Inaccurate reporting due to missing events for certain cases and/or activity processes.

## Procedure

To delete a deployed solution:

1. Using the BAWAdmin select Target Object
Store > Deployed Solutions.
2. From the Solutions page on the right side, select the solution that you
want to remove.
3. Click Actions > Remove deployed
solution.