<!-- image -->

# Adding support for shared work items

## About this task

## Procedure

1 Optional: Reduce the number of work items inyour system by completing one or more of the following steps:
    - Deleting
BPEL process instances
    - Deleting
completed task instances
    - If you configured a Business Process Archive Manager to archive
instances from this Business Process Choreographer configuration,
complete the actions that are described in Archiving
completed BPEL process and task instances.
2 At a time when there is a low load on thedatabase, run the migrateWI.py script to create sharedwork items for existing work items.

1. Decide on the maximum duration in minutes, duration,
that you want the script to run for.
2 Change to the directory where the migrateWI.py scriptis located:
    - install\_root/ProcessChoreographer/admin
    - install\_root\ProcessChoreographer\admin
3. Run the script by starting wsadmin with the following
parameters:   -conntype NONE
 [-profileName profile] 
 [-tracefile trace\_file] 
  -f migrateWI.py 
  -migrateToWISharing
 [-duration duration]
 [-slice slice\_size]
 -cluster clusterName
[[-dbUser userID] -dbPassword password]
 [-dbSchema schema]Note: You must run
the script on the node of a cluster member, and not on the deployment
manager. Because wsadmin overwrites its trace file, use the -tracefile option
to specify a file name and location for the trace file for the work
item data migration. You do not need to stop the cluster. For more
information about using this script and its parameters, see Business Process Choreographer data
migration script for shared work items.
4 When the script finishes, it reports a summary of themigration status of the work items that belong to each type of entity: For example: Entities Migrated Not migrated CompletedEventInstance 7602 7602 0 100%WorkBasket 0 0 0 100%TaskInstance 29883 29883 0 100%EscalationInstance 4227 4227 0 100%BusinessCategory 0 0 0 100%ActivityInstance 52572 52572 0 100%ProcessInstance 7602 3036 4566 39%--------------------------------------------------------------Total 101886 97320 4566 95%

- The total number in the system.
- The number that were migrated.
- The number that still must be migrated.
- The percentage that are completed.

```
Entities  Migrated  Not migrated  Completed
EventInstance          7602      7602             0       100%
WorkBasket                0         0             0       100%
TaskInstance          29883     29883             0       100%
EscalationInstance     4227      4227             0       100%
BusinessCategory          0         0             0       100%
ActivityInstance      52572     52572             0       100%
ProcessInstance        7602      3036          4566        39%
--------------------------------------------------------------
Total                101886     97320          4566        95%
```

3. If the script finished with less than 99% completed (that is, more than 1% of the total number
of entities and their corresponding work items in the system still need to be processed), repeat
step 2.
4 If the script finished with 99% or more completed, activate the shared work item support.

1. Stop the cluster where Business Process Choreographer is configured.
2. Now run the script a final time to process any remaining work items and switch into shared work
item mode, by starting wsadmin with the following parameters:

  -conntype NONE
 [-profileName profile] 
 [-tracefile trace\_file] 
  -f migrateWI.py 
  -setMode WS\_SHARING\_ACTIVE\_MODE
  -cluster clusterName
[[-dbUser userID] -dbPassword password]
 [-dbSchema schema]
3. Success is indicated by the following message: 
migrateWI.py finished with warnings.In case of problems,
you might get a message similar to the following
one:Exception received:
java.lang.IllegalStateException: Mode: WS\_SHARING\_ACTIVE\_MODE
migrateWI.py finished, result = WARNING.
4. Restart the cluster.

## Results

## What to do next

- Use the administrative console to change the default cleanup times
and retention periods for unused shared work items. You can change
these settings on the Runtime or Configuration tab
for the Human Task Manager.
- Delete unused staff query interfaces and unused work item patterns,
by running the cleanupUnusedStaffQueryInstances.py script.
- If you do not use anyqueries that must run against the non-shared work items, you can freeup space in the database by customizing and running a copy of the dropClassicWIIndexes.sql script to drop the indexes on the WORK\_ITEM\_T table.
    1 The script is in the following location.
        - install\_root/BPM/dbscripts/database\_type/Tuning
        - install\_root/BPM/dbscripts/database\_type/Tuning
2. Make a copy of the script file dropClassicWIIndexes.sql.
3 Edit your copy.
    1. Replace all occurrences of the string @SCHEMA@ with
the name of your schema. If you use an implicit schema, you must delete
the string @SCHEMA@., including the trailing dot.
    2. If you are using a DB2 for z/OS database, replace all occurrences
of the string @STOGRP@ with the name of your storage
group.
    3. If you are using an Oracle database,  replace all occurrences
of the string @INDEXTS@ with the name of the index
table space.
    4. Save your changes.
4 Run your edited copy of the script. In your database client commandline processor, enter one of the following commands: For more information about how to run scripts on your database,see the product documentation for your database. If there are anyerrors, or failure is indicated in your database client output, fixthe reported errors and repeat this step.

- For DB2®: db2 -tf
dropClassicWIIndexes.sql
- For Oracle: sqlplus dbUserID/dbPassword@database\_name
@dropClassicWIIndexes.sql
- For Microsoft SQL Server: sqlcmd
-U dbUserID -P dbPassword -e -i dropClassicWIIndexes.sql

- Business Process Choreographer data migration script for shared work items

If you migrated from version 7.0.0.2 or earlier, you can optionally activate support for shared work items, which should improve performance. You must use the migrateWI.py script to migrate data and activate the support.

<!-- image -->