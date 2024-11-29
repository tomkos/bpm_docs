# Identifying and removing inactive change log consumers

When working on tasks and process instances, the federated business process management
system populates the following change logs in the database: PFS\_BPD\_CHANGE\_LOG
table for BPD federated systems, and PFS\_BPEL\_CHANGE\_LOG for the BPEL federated
systems. Process Federation Server acts as a consumer of this change log to identify which tasks or process instances have been
updated on the federated system and then perform corresponding updates to the federated data
repository.  If you updated the federated system index name more than 5 times, you may face a
degraded performance. A good practice is to remove the inactive consumer columns before you start
the Process Federation Server
cluster

## Before you begin

A consumer represents the indexing service on Process Federation Server for a specific
business process management system. For each new change log entry, the consumer indexes the changed
data in the federated data repository and then marks the change log entry as consumed.

The change log table includes a row for each change which has been performed on a task or process
instance. The row also contains columns which are ranging from CONSUMER\_001 to
CONSUMER\_020. When an indexing service starts, it automatically reserves the first
unused consumer column in the change log table. Consumers are identified by the federated data
repository index identifier which is set to same value as the indexName property of
the <ibmPfs\_federatedSystem> configuration element. For more details, see Configuration properties for federated systems.

- 0: the change log row has not been consumed yet,
- 10: the consumer is currently processing the change log row. The processing of
a change log rows consists of building the corresponding document by querying the database, and then
indexing the document in the federated data repository,
- 20: the change log entry has been consumed. The corresponding change has been
reflected into the federated data repository.

Only the first 5 consumer columns have a database index created by the Process Federation Server initialization
SQL scripts. If you updated the federated system index name more than 5 times, you may face a
degraded performance. A good practice is to remove the inactive consumer columns if the environment
have been federated multiple times.

## About this task

The following procedure explains how to identify and remove the inactive consumers.

Every time that a <ibmPfs\_federatedSystem> configuration element is
defined in a Process Federation Server
server.xml file, and that a BPD indexer is started for this system, Process Federation Server records the
consumer by creating an entry in the PFS\_BPD\_CHANGE\_LOG\_CONSUMER table if the
entry has not already been created: the CONSUMER\_ID in this table is the id of the
<ibmPfs\_federatedSystem> element, while the COLUMN\_NAME
column is the name of the consumer. for example CONSUMER\_001.

At regular interval, Process Federation Server deletes entries
from the PFS\_BPD\_CHANGE\_LOG table that are related to deleted tasks and that have
been consumed by all consumers defined in the PFS\_BPD\_CHANGE\_LOG\_CONSUMER
table. Because Process Federation Server creates entries
in the PFS\_BPD\_CHANGE\_LOG\_CONSUMER table when a new consumer is started but never
deletes these entries, some entries in the PFS\_BPD\_CHANGE\_LOG table will never
be deleted (so that the inactive consumer can consume those entries later).

If you have an inactive consumer and do not intend to re-activate it (for example, a consumer
created during a test period, or a change of id of an
<ibmPfs\_federatedSystem> element that led to the creation of a new consumer),
you can delete the entry of your inactive consumer in the
PFS\_BPD\_CHANGE\_LOG\_CONSUMER table by nullifying the corresponding
CONSUMER\_ID column, as described in the procedure.

## Procedure

1. List all the registered consumers: 
SELECT * FROM PFS\_BPD\_CHANGE\_LOG\_CONSUMER;
2. For the rows where CONSUMER\_ID column is set to an index name which is
not used anymore in your configuration, clear the column name registration by using an SQL statement
similar to the following example, which shows how to clear the reservation for the 3rd column. 
UPDATE PFS\_BPD\_CHANGE\_LOG\_CONSUMER SET CONSUMER\_ID = NULL WHERE COLUMN\_NAME = 'CONSUMER\_003'
3. Reset the state of the consumer column by using an SQL statement similar to the following
example. 
The example shows how to reset the 3rd column.

UPDATE PFS\_BPD\_CHANGE\_LOG SET CONSUMER\_003 = 0