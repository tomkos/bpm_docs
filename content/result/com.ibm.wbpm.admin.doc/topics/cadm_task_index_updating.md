# Updating the Process Portal index

If a problem occurs with the Process Portal index, you might need to run a command to
rebuild it. You can also update the index for an instance or task, remove an instance or task from
the index, or clean up the index
tables.

In IBM® BPM V8.5 or later and IBM Business Automation
Workflow, changes made in IBM Process
Designer to a team name in a process application
might not get updated in the Process Portal index.
Therefore, if you upgraded from IBM BPM V8.5 or
later, it is recommended that you rebuild the index by using the
processIndexFullReindex command described in the following section.

Additionally, on IBM Workflow
Center, if you
rename a team in the tip for a process application and process instances that were created with the
old team name, you must rebuild the index to update the team name for the tasks for those instances.
Rebuilding the index, in this case, is required for both upgrades and new installations of the
product.

## Index administration

- Rebuilding the index
- Freeing up space in the index by removing deleted tasks and instances
- Updating the index for a specific instance or task
- Deleting a specific instance or task
- Cleaning up index tables

In a network deployment environment, all cluster members on the same node share the index by
default. Run the commands for updating the index on the deployment manager. To specify where the
command runs, include the -host host\_name parameter of the node
and the -port SOAP\_port parameter of an application cluster
member. Repeat the command for each node in the cluster. The default values for these parameters are
-host localhost -port 8880.

## Rebuilding the index

After a migration or upgrade from an earlier release of IBM BPM or Business Automation Workflow, the index is
automatically rebuilt on server restart. In addition, if problems occur with the index or searches
in Process Portal, you can
rebuild the index manually.

<!-- image -->

```
processIndexFullReindex.bat -user DeAdmin\_user -password DeAdmin\_password -host host\_name -port SOAP\_port
```

<!-- image -->

<!-- image -->

```
processIndexFullReindex.sh -user DeAdmin\_user -password DeAdmin\_password -host host\_name -port SOAP\_port
```

## Freeing up space in the index by removing deleted tasks and instances

<!-- image -->

```
processIndexRemoveDeleted.bat -user DeAdmin\_user -password DeAdmin\_password -host host\_name -port SOAP\_port
```

<!-- image -->

<!-- image -->

```
processIndexRemoveDeleted.sh -user DeAdmin\_user -password DeAdmin\_password -host host\_name -port SOAP\_port
```

## Updating the index for a specific instance or task

If you do not change the default configuration settings in the 100Custom.xml
file, the index is updated every 5 seconds. However, you can also trigger
updates to the index when a specific instance or task is updated, for example, if you doubt the
correctness of the search index record for a specific instance or task.

<!-- image -->

```
processIndexUpdateInstance.bat -user DeAdmin\_user -password DeAdmin\_password  -host host\_name -port SOAP\_port instanceID
```

<!-- image -->

<!-- image -->

```
processIndexUpdateInstance.sh -user DeAdmin\_user -password DeAdmin\_password  -host host\_name -port SOAP\_port instanceID
```

<!-- image -->

```
taskIndexUpdate.bat -user DeAdmin\_user -password DeAdmin\_password -host host\_name -port SOAP\_port taskID
```

<!-- image -->

<!-- image -->

```
taskIndexUpdate.sh -user DeAdmin\_user -password DeAdmin\_password -host host\_name -port SOAP\_port taskID
```

## Deleting a specific instance or task

<!-- image -->

```
processIndexDeleteInstance.bat -user DeAdmin\_user -password DeAdmin\_password -host host\_name -port SOAP\_port instanceID
```

<!-- image -->

<!-- image -->

```
processIndexDeleteInstance.sh -user DeAdmin\_user -password DeAdmin\_password -host host\_name -port SOAP\_port instanceID
```

<!-- image -->

```
taskIndexDeleteTask.bat -user DeAdmin\_user -password DeAdmin\_password -host host\_name -port SOAP\_port taskID
```

<!-- image -->

<!-- image -->

```
taskIndexDeleteTask.sh -user DeAdmin\_user -password DeAdmin\_password -host host\_name -port SOAP\_port taskID
```

## Cleaning up index tables

The BPM\_TASK\_INDEX and BPM\_INSTANCE\_INDEX database tables, which track indexes, contain rows that
reflect the data in LSW\_TASK and LSW\_BPD\_INSTANCE database tables. When you clean up operational
data from these tables, the deleted rows are updated in the index tracking tables but not deleted.
In some cases, your database tables can grow very large because they mostly store data that has
already been deleted from the operational data tables and thus is no longer needed. In these cases,
the large number of rows causes high CPU usage when the database locks the tables to complete the
indexing process. Such high CPU usage causes overall slowness of Process Portal and out-of-sync issues of the search
index.

To avoid such issues, you can clean up the BPM\_TASK\_INDEX and BPM\_INSTANCE\_INDEX tables by
running one of the following commands on the command line.
The command first verifies the total
number of distinct indexes in your Business Automation Workflow
cluster, then purges all the rows from BPM\_TASK\_INDEX\_JOB that are older than 7 days. For more
information about determining the number of distinct indexes, see Configuring the Process Portal index.

<!-- image -->

```
indexTablesCleanup.bat -user DeAdmin\_user -password DeAdmin\_password -host host\_name -port SOAP\_port -numIndexes num\_indexes -maxDurationMinutes max\_duration\_in\_minutes -taskIndexTableDeleteBatchSize task\_index\_table\_delete\_batch\_size -instanceIndexTableDeleteBatchSize instance\_index\_table\_delete\_batch\_size
```

<!-- image -->

<!-- image -->

```
indexTablesCleanup.sh -user DeAdmin\_user -password DeAdmin\_password -host host\_name -port SOAP\_port -numIndexes num\_indexes -maxDurationMinutes max\_duration\_in\_minutes -taskIndexTableDeleteBatchSize task\_index\_table\_delete\_batch\_size -instanceIndexTableDeleteBatchSize instance\_index\_table\_delete\_batch\_size
```

## Related concepts

- Configuring the Process Portal index

## Related reference

- Process Portal index: Default indexed fields