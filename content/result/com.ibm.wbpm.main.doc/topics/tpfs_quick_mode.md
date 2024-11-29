# Enabling the quick start mode

IBM® Process Federation
Server provides a quick
start mode that allows you to partially index tasks in the federated data repository based on a past
date criteria.  This procedure only applies to BPD and BPEL systems when indexing is done by
Process Federation Server.

## About this task

When you enable the quick start mode, only the change log entries that are newer than the
specified point in time are processed by the indexers. This mode can be used to reduce the number of
tasks to index or re-index so they can be available faster. The quick start mode is available for
both the BPD and the BPEL indexers and can be enabled by setting the date criteria in the format
yyyy-MM-dd HH:mm:ss with the attribute
skipChangeLogEntriesOlderThan for the related indexer element. The date must be
specified in UTC time, regardless of the federated system timezone that the indexer element refers
to.

- For the BPD indexer : the purge of the audit log table
PFS\_BPD\_CHANGE\_LOG\_CONSMR\_LOG and the compaction of change log
PFS\_BPD\_CHANGE\_LOG.
- For the BPEL indexer : the purge of the audit log table
PFS\_BPEL\_CHANGE\_LOG\_CONSMR\_LOG.

## Procedure

1. Stop Process Federation Server.
2. Edit the server.xml file.
3. Locate the ibmPfs\_bpdIndexer element for the BPD indexer, or the
ibmPfs\_bpelIndexer element for the BPEL indexer, add the attribute
skipChangeLogEntriesOlderThan, and specify a date as a starting point for
indexing tasks.

For example, for the BPD indexer, if the current date is 2017-01-30 13:10:00, the following
settings will index or re-index tasks for the last three
days:<ibmPfs\_bpdIndexer ... skipChangeLogEntriesOlderThan="2017-01-27 13:10:00"/>For
the BPEL indexer, if the current date is 2017-01-30 13:10:00, the following settings will index or
re-index tasks for the last three
days:<ibmPfs\_bpelIndexer ... skipChangeLogEntriesOlderThan="2017-01-27 13:10:00"/>
4. Start Process Federation Server.