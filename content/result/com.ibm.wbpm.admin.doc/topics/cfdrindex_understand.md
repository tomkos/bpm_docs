# Understanding the federated data repository BPD indexing

- How the federated data repository indexing works
- Administering the federated data repository indexing
- Monitoring the federated data repository indexing

## How the federated data repository indexing works

An entry is inserted in the indexing queue each time the Business Automation Workflow BPD engine creates,
updates or deletes a process instance, or creates or updates a BPD task that is expected to be
indexed.

- An indexer thread is created. You can have more than one indexing thread per node by setting the
<fdr-index-threads> property in 100Custom.xml. All the
indexer threads that are running in your cluster work without conflicting each other. Consequently,
you can use scalability options such as adding new nodes or increasing the number of threads per
node to improve the indexing performance.
- A maintenance thread is started to handle and coordinate the processing of the various
maintenance operations.

The indexer thread starts an indexing cycle by reading up to 1000 entries from the queue. The
1000 batch size is configurable by setting the <fdr-index-batch-size>
property in 100Custom.xml.

For all the process instances and tasks referenced in the batch of entries, the indexer thread
queries the database to retrieve the data required to build the JSON documents to insert or update
in the federated data repository index. A request is sent to the federated data repository REST API
to create, update, or delete the documents, as needed.

- A row is created, updated or deleted in FED\_INDEX\_INSTANCE for each process instance and in
FED\_INDEX\_TASK for each task. These rows hold a version number of the corresponding indexed
document, which can be later compared with the INDEX\_VERSION column of  LSW\_BPD\_INSTANCE and
LSW\_TASK database tables, respectively, to verify that the indexed data is in sync with the
database, or to perform any required reconciliation to bring the index back in sync.
- Finally, the queue entries are deleted from the indexing queue.

- The failure counter for the corresponding queue entry is incremented.
- The queue entry is re-attempted on the next indexer cycle, unless the failures count reaches the
threshold defined by the <fdr-index-failure-threshold> property in
100Custom.xml. The default value of the threshold is set to
20.
- The indexing queue entries that reach the threshold are no longer reprocessed, and remain in the
queue until the ‘retry-failures’ maintenance operation is executed. To determine if
the queue contain such rows, you can execute the /ops/fdr/bpd/info REST
API.

Next, an audit entry is logged in the FED\_INDEX\_AUDIT table with details about the indexing
cycle, such as the start and end time, the number of queue entries being processed, the number of
documents indexed, deleted, and failed, and so on. Finally, the current cycle completes and a new
cycle starts.

Back to top

## Administering the federated data repository indexing

The federated data repository indexing comes with a set of maintenance operations. Some of them
are executed automatically, others are meant to be executed by an administrator by using the REST
API for federated data repository indexing.

- Start a maintenance operation: POST
/ops/fdr/bpd/maintenanceOperations/{maintenance-operation-type}
- Get the latest status of a maintenance operation: GET
/ops/fdr/bpd/maintenanceOperations/{maintenance operation type}
- Abort, suspend, or resume an on-going maintenance operation: PUT
/ops/fdr/bpd/maintenanceOperations/{maintenance operation type}
- Get details about the latest maintenance operation runs: GET
/ops/fdr/bpd/maintenanceOperations

On each running Business Automation Workflow node, there is a running maintenance daemon that is responsible for handling and coordinating the
processing of the various maintenance operations. In a clustered environment, out of all the running
nodes, only one maintenance daemon is active. The other maintenance daemons remain idle until the
active daemon is stopped. When the active daemon is stopped or becomes unresponsive, another running
maintenance daemon becomes active, while all the other daemons remain idle.

- ‘create-index’
- ‘rebuild’
- ‘house-keeping’
- ‘retry-failures’
- Failover support
- ‘reconcile’
- ‘sync-deletions’

Back to top

To rebuild the index from scratch,
delete it using the Elasticsearch or OpenSearch REST API. The index is recreated and repopulated
automatically without having to restart your Business Automation Workflow nodes.

Back to top

Back to top

- The indexing cycle audit rows that are by default less than 7 days old. The default value can be
customized by using <fdr-index-house-keeping-audit-max-age>, expressed in
number of minutes.
- The maintenance operation records that are related to the latest 50 executions of each kind.
This value can be customized by using
<fdr-index-house-keeping-maintenance-log-size>, expressed in number of
minutes.

To disable the automatic scheduling of the ‘house-keeping’ maintenance
operation, set <fed-index-house-keeping-interval> to a negative value. In
such case, ‘house-keeping’ is executed on a regular basis by calling POST
/ops/fdr/bpd/maintenanceOperations/house-keeping.

To get the status and details about
the latest run of the ‘house-keeping’ maintenance operation, call GET
/ops/fdr/bpd/maintenanceOperations/house-keeping.

Back to top

To find out if such situations might occur,
you can check your logs and/or regularly query the GET /ops/fdr/bpd/info API . If
this API returns a positive number under indexingQueue.failedCount, this indicates
that some entries in the indexing queue have reached the failure threshold. For example, this can
occur if the indexing of the corresponding document in the federated data repository index is
rejected by Elasticsearch or OpenSearch because it exceeds the configured total fields limit. If you
find evidence in the Business Automation Workflow logs that the problem is
related to the total fields limit, you can fix the issue by configuring Elasticearch or OpenSearch
with a higher federated data repository index fields limit.

If case the root cause of the
indexing failure is not clearly identified, contact the IBM support. After the root cause is fixed
(for example, by increasing the total fields limit), you must reset the failure count of the queue
entries so that they are processed again by the indexer. To do this, call POST
/ops/fdr/bpd/maintenanceOperations/retry-failures.

To get the status and details
about the latest run of the ‘retry-failures’ maintenance operation, call
GET /ops/fdr/bpd/maintenanceOperations/retry-failures.

Back to top

- An active topology, where the federated data repository indexing is enabled.
- A passive topology, where the federated data repository indexing is disabled.

Automatic database replication must also be in place so that changes to the active site
database are instantly replicated on the passive site database. To enable the database replication
between the two topologies, refer to your database documentation.

- On the active site, regularly:
    - Update the backup state doc by calling PUT /ops/fdr/bpd/backupState, then
    - Take snapshots of the federated data repository index on the active site to restore it on the
federated data repository of the passive site.
- When the active site fails or crashes, you must then:

- Ensure that federated data repository indexing is disabled or not running anymore on the failing
topology, which becomes the new “passive” topology, then
- Enable the federated data repository indexing on the passive topology, which becomes the new
“active” topology, and
- Once the federated data repository indexing is enabled and the system is running, call the
POST /ops/fdr/bpd/maintenanceOperations/restore API on the new “active” site.

Back to top

Back to top

- Identifies all the documents indexed into the federated data repository index that are related
to tasks from this process instance, and creates corresponding entries in the indexing queue so that
the indexer deletes these documents.
- Deletes the process instance document.

- Searches in FED\_INDEX\_INSTANCE for rows related to process instances that do not exist in
LSW\_BPD\_INSTANCE, and creates the corresponding entries in the indexing queue.
- Searches in FED\_INDEX\_TASK for rows related to tasks that do not exist in LSW\_TASK, and create
the corresponding entries in the indexing queue.

Back to top

Back to top

## Monitoring the federated data repository indexing

You can gather KPIs about the federated data repository indexer by calling the GET
/ops/fdr/bpd/info API, which returns the following data:

| Field                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| date                                                                                                                    | The time at which the information about the federated data repository indexer was retrieved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| indexedContent.instanceCount indexedContent.taskCount                                                                   | Number of indexed process instance and task documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| indexedContent.latestInstanceIndexedTime indexedContent.latestTaskIndexedTime                                           | The date of the latest process instance and task documents indexation times.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| fdrBpdIndexingQueue.oldestPendingEntry fdrBpdIndexingQueue.youngestPendingEntry                                         | Time range between the oldest entry in the queue and the newest one.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| fdrBpdIndexingQueue.pendingUpdateCount fdrBpdIndexingQueue.pendingRebuildCount fdrBpdIndexingQueue.pendingDeletionCount | Number of entries in the indexing queue by kind: pendingUpdateCount refers to the regular indexing of process instances and tasks being actively worked on. pendingRebuildCount refers to the entries in the indexing queue which are related to the rebuild. pendingDeletionCount refers to the entries in the indexing queue which are related to deletions.  When the federated data repository indexer retrieves a batch of entries to process from the indexing queue, the priority will always be given to the regular indexing. If there is some space left in the indexing batch, the federated data repository indexer will then process the entries related to the index rebuild, and finally the entries related to the deletions. pendingUpdateCount should not be greater than the indexing batch size, which is by default set to 1000. If pendingUpdateCount is larger than the indexing batch size, then it indicates that the indexing throughput cannot cope with the volume of updates performed by the BPD engine. There may be a bottleneck somewhere. You should first ask your database administrator to check the database overall performance. Also, a possible option would be to scale up the indexing by adding new indexing threads. You can do this by either adding new nodes to your cluster, or by incrementing the <fdr-index-threads> property in 100Custom.xml. |
| indexedContent.deletedInstanceCount indexedContent.deletedTaskCount                                                     | Number of deleted process instances and task documents that are still tracked in the FED\_INDEX\_INSTANCE table.The deletions are tracked when you enable the failover support. See ‘post-backup’ maintenance operation  for details. If you no longer maintain your topology for failover support and that the indexedContent.deletedInstanceCount and indexedContent.deletedTaskCount properties are returning positive numbers, then you should call DELETE /ops/fdr/bpd/backupState to free up some space by stopping tracking the deletions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| fdrBpdIndexingQueue.failedCount                                                                                         | Number of failed queue entries which will not be re-processed until a ‘retry-failures’ maintenance operation is triggered.This indicates that some documents could not be indexed. The most probable root cause is that the indexing of such document would exceed the total fields limit defined on your federated data repository index. See for 'retry-failures' maintenance operation more details.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| fdrBpdIndexingQueue.oldestFailedEntry fdrBpdIndexingQueue.youngestFailedEntry                                           | The time range between the oldest and the youngest failed queue entries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

Back to top