# Managing workflow server caches and databases

- Reviewing workflow server caches

For performance reasons, some information about the workflow server is cached. The caches refresh automatically and so resetting these caches should only be required when an issue exists that a reset might rectify.
- Deleting tasks from the Process database

To reduce the amount of space used, administrators can use the Task Cleanup utility in the Process Admin Console to delete tasks from the Process database.
- Removing process instances from the Process database

 Traditional: 
 To prevent disk-space issues and long waits in Process Portal, use the BPMProcessInstancesPurge command.
- Business data alias cache configuration

 Traditional: 
 Process variables that are configured to be available for search are given alias names and are cached in the business data alias cache. To improve performance, you can configure the cache to receive the business data aliases for only the snapshots that have associated instances instead of keeping the default setting that returns all the aliases for all the snapshot definitions.