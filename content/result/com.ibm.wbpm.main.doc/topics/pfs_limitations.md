<!-- image -->

# Process Federation Server known
limitations

## BPEL indexer

- To-do tasks
- Collaboration tasks
- Subtasks
- Follow-on tasks

- Administration tasks
- Task templates
- Invocation tasks
- Parallel routing tasks

- Task escalations
- Process suspension

Only query properties are indexed as business data. Input, output, fault messages, custom
properties, and fast custom properties are not indexed.

## Deferred deletion of process instances and task documents from the Process Federation Server index

When you delete a process instance with Process Inspector, this process instance and its
corresponding tasks might not be immediately deleted from the Process Federation Server index. They will be deleted the next
time that the SYNC\_INSTANCE\_DELETE and SYNC\_TASK\_DELETE operations
are run by the Process Federation Server BPD indexer,
as specified by the synchronizeInstancesDeleteInterval and
synchronizeTasksDeleteInterval properties of the indexers.

## Saved Searches

If a saved search result is sorted on a business data field that is defined as a
Long for one process and as a Double for another, the sort is
performed as if the business data field type was String.