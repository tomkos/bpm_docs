<!-- image -->

# Using scripts to administer Business Process Choreographer

## About this task

There is no cross-cell support for the
Business Process Choreographer administrative scripts. This means
that you can connect the scripting client only to the
deployment manager of the cell to which the node of the profile where
the script runs belongs.

- Archiving completed BPEL process and task instances

The archive.py administrative script moves completed parent BPEL process instances and human task instances, including their associated data, from a Business Process Choreographer database to an archive database.
- Querying and replaying failed messages, using administrative scripts

Use the queryNumberOfFailedMessages.py administrative script to determine whether there are any failed messages for BPEL processes or human tasks. If there are any failed messages, use the replayFailedMessages.py administrative script, to retry processing them.
- Refreshing people query results, using administrative scripts

Use the refreshStaffQuery.py administrative script to refresh people queries because the results of a people query are static.
- Deleting Business Process Choreographer objects

Various database objects accumulate in a running system, for example, audit log entries, task and process instances, task and process templates, and people queries. Regularly running administrative scripts to delete objects that are no longer needed from the Business Process Choreographer databases can help prevent wasting storage space.
- Administering query tables

Use the administrative script, manageQueryTable.py script to administer query tables in Business Process Choreographer, which were developed using the Query Table Builder. Unlike predefined query tables, which are available by default, you must deploy composite and supplemental query tables on Workflow Server before you can use them with the query table API.

<!-- image -->