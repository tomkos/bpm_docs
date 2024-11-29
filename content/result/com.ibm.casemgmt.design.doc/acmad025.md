# Indexing event logs for older case types to enable case health analysis of work items

## Procedure

To index the event log for a case type to support case health analysis:

1. Log in to the Administration Console for Content Platform
Engine.
2. Expand Object Stores, open your target object store, and expand Administrative > Workflow System > Isolated Regions > Event Logs.
3 For each case type, add an index to the event log.
    1. On the Indexes tab, click New.
    2. Enter a name for the index name.
    3. Select F\_CaseFolder as the first key.
    4. Select F\_EventType as the second key.
    5. Click OK and then save the index.