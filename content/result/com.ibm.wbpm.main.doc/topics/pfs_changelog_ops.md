# Change log maintenance operations

| Operation           | Description                                                                                                                                                                                                                                                                                                  |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SyncTasks           | Checks the federated environment database for tasks that are not referenced in the change log table. A new entry is created for any missing task. Runs at regular intervals and when the indexer first starts, unless the scheduled operation is disabled.                                                   |
| SyncInstances       | Checks the federated environment database for instances that are not referenced in the change log table. A new entry is created for any missing instance. Runs at regular intervals and when the indexer first starts, unless the scheduled operation is disabled.                                           |
| SyncTaskDeletes     | Checks the federated environment database to see whether the change log table references any tasks that have been deleted. If some deleted tasks are found, an entry is then created in the change log table to report that the task should be deleted from the Process Federation Server index.             |
| SyncInstanceDeletes | Checks the federated environment database to see whether the change log table references any instances that have been deleted. If some deleted instances are found, an entry is then created in the change log table to report that the instance should be deleted from the Process Federation Server index. |
| Compaction          | Purges all but the most recently consumed entry for each task and instance referenced in the change log table.                                                                                                                                                                                               |
| IndexLogTrim        | Removes entries from the consumer log table (PFS\_BPD\_CHANGE\_LOG\_CONSMR\_LOG / PFS\_BPEL\_CHANGE\_LOG\_CONSMR\_LOG) that are older than 7 days. An entry is created by the indexer in the consumer log table after each indexing cycle.                                                                             |
| Cleanup             | When a task or an instance has been deleted in the federated environment and marked for deletion in the change log, and once the deletion has been consumed by the indexer, then all entries referencing the deleted tasks and instances will be deleted. Cannot be run as an unscheduled MBean operation.   |

## Related reference

- Configuration properties for the Process Federation Server index

## Related information

- Monitoring indexers with MBeans