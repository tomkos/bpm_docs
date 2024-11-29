# Cleaning up the BPM document store

## Before you begin

The cleanupDocumentStoreProperties command
is used to help clean up the BPM document store. It
is run using the AdminTask object of the wsadmin scripting client.
To run the command, the following conditions must be met:

- The command must be run on the deployment manager node.
- One or more application cluster members must be running.
- The command must be run in connected mode. Do not specify the wsadmin
-conntype none option.
- You must connect to the deployment manager with a user ID that
has WebSphere Application Server operator privileges.

Start the wsadmin scripting client from the
profile\_root/bin directory of the deployment manager
profile. The cleanupDocumentStoreProperties command does not write to a log file,
but the wsadmin scripting client always writes a
profile\_root/logs/wsadmin.traceout log file where you will
find exception stack traces and other information.

## About this task

The cleanupDocumentStoreProperties command
deletes all properties that are currently specified in the case and
document classes but are no longer used. (An unused property is one
that is no longer referenced in any named snapshot or tip in any branch
of a process application or toolkit.) After the properties are removed,
the command also removes any unused property templates.

## Procedure

To remove unused properties from the BPM document store for
a specific application, and optionally delete the associated database
columns, complete the following steps:

1. Run the cleanupDocumentStoreProperties command.
For example, to remove all unused properties for the application
that has the acronym MYAPP, from the document store
that is on cluster myClusterName, enter the following
command:AdminTask.cleanupDocumentStoreProperties('[-clusterName myClusterName -containerAcronym MYAPP]')Important: Instead of specifying a cluster, you can specify
either a deployment environment or a server and node. For more information
about the command, including various Jython and Jacl examples, see cleanupDocumentStoreProperties command.

If no unused properties are found, the command outputs
the following message:CWTDS2050I: No property was deleted.Otherwise,
for each deleted property, property, the command
outputs the following message:CWTDS2049I: The property 'property' was deleted.
2 Optional: Remove the database columns for the deleted properties. Tip: You do not need to remove the database columns every timethat you remove unused properties. However, over time, the numberof columns might exceed the table row size limit. Completing the actionsin this step helps to avoid reaching that limit.
    1. Stop the Workflow Center application
to ensure that there is no user activity on the document store. 
Important: The object store database is altered
by this procedure and it is important that no users are accessing
the database.
    2 Decide which tables you want to clean up. Youcan clean up any of the following tables: Important: You do not have to check or clean up alltables. However, if you decide to drop any unused columns on a table,you must drop all unused columns.
        - DocVersion
        - Container
3. For each table that you want to clean up,
display the names of all database columns that are no longer used
by any properties. Enter the following command in the appropriate
database tool. select column\_name from ColumnDefinition
       where lower(dbg\_table\_name) = lower('TableName')
       and is\_system\_owned = 0
       and object\_id not in (select column\_id from PropertyDefinition where column\_id is not null)Where TableName is
the name of the table.Important: For each column returned,
verify that it is named prefix\_propertyName,
where propertyName is the unused property name,
for example u5c\_myString.
4 Drop all unused columns for the tables thatwere displayed and examined from the query in step 2.c . DB2 procedure SQL Server procedure For SQL Server, no actions are necessary. Oracle procedure Complete one of the following steps:
    1. If the table has many rows, this procedure can take a long time.
Make sure that there is adequate disk space for logging.
    2. Start the DB2 Control Center.Restriction: You cannot
drop the columns programmatically.
    3. On the Alter panel, select Remove.
    4. Select the columns to remove. The Control Center displays a warning
that the action involves actions such as renaming the table, re-creating
the table, and copying the data.Tip: For more information
about using the Control Center to drop columns, see your DB2 documentation.
    - If your tables are not large, drop each unused column individually
by entering the following command for each column, ColumnName,
on each table, TableName that you identified in
step 2.c:alter table TableName drop column ColumnName;Tip: If the table has many rows, this step can take a long time.
Be sure to have a large amount of undo table space disk space available.
    - If your tables are large, it is easier to drop the unused columns
in one go because each action can take a long time. Enter the following
commands for each table:ALTER TABLE TableName SET UNUSED (ColumnName1, ColumnName2, ...);
ALTER TABLE TableName DROP UNUSED COLUMNS;Where TableName is
the name of the table and ColumnName1, ColumnName2,
... denotes the list of column names that you identified in step 2.c.Tip: You can reduce
the size of the undo logs by using the CHECKPOINT option.
The CHECKPOINT option forces a checkpoint after the
specified number of rows are processed. The following example illustrates
how to drop the unused columns, with a checkpoint created after every
250 rows are processed.ALTER TABLE TableName DROP UNUSED COLUMNS CHECKPOINT 250;
5. If you use DB2 or Oracle, for each table, TableName,
from which you dropped all unused column, delete the affected rows
in the ColumnDefinition table: delete from ColumnDefinition where lower(dbg\_table\_name) = lower('TableName') 
       and is\_system\_owned = 0
       and object\_id not in (select column\_id from PropertyDefinition where column\_id is not null)
6. Restart Workflow Center.