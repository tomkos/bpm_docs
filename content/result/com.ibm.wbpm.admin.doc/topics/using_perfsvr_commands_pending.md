# Archiving and restoring data in the Performance Data Warehouse database

When you use one of the commands, a SQL script is generated, which
you can use to make the appropriate database changes. You can run
the resulting SQL scripts by using the database application appropriate
for your environment, or you can use the execute argument
included with the command-line tool.

The commands are described in the following table:

| Command   | Action                                                                                                                                                                                                                                                                                                                                                     |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| archive   | Archives the snapshots that you specify and marks all the metadata in those snapshots with an ARCHIVED time stamp. IBM® Business Automation Workflow does not use archived metadata when it generates Performance Data Warehouse schema and views. To specify snapshots, use the ID for each snapshot from the SNAPSHOTS view in the performance database. |
| restore   | Restores the snapshots that you specify by nulling out the ARCHIVED time stamp and allowing the metadata of the snapshots to contribute to the Performance Data Warehouse physical schema and views. To specify snapshots, use the ID for each snapshot from the SNAPSHOTS view in the performance database.                                               |
| pending   | Identifies failed definition records and resolves their pending state. You can review and then commit pending schema changes from the archive and restore commands.                                                                                                                                                                                        |

## Before you begin

Before you run a
command, complete the following tasks:

- Ensure that you have installed or upgraded your Performance Data
Warehouses to the latest version of Business Automation Workflow.
- Start the Performance Data Warehouse. If you are running in a
clustered environment, ensure that all servers in the cluster are
running.
- Create a backup of the performance database.
- Go to the following directory: install\_root\profiles\profile\_name\binRemember: perfDWTool must be run from an active node in the
support cluster.

## Pending arguments

The following arguments
are available for use with the pending command:

| Argument   | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -preview   | Generates a preview of the SQL script that was generated as a result of the invoked command. No changes are made to the database.                                                                                                                                                                                                                                                                                                                                   |
| -prepare   | Generates a preview of the SQL script and prepares the database for the pending actions.                                                                                                                                                                                                                                                                                                                                                                            |
| -execute   | Invokes the command without providing a preview SQL script. Note: Use the -execute argument with extreme caution. It is run when the Performance Data Warehouse is running (online), and you cannot review the SQL script before its start. If the scope of changes is complex, there is a chance of data loss because, during the running of the command, data might become out of sync, which might cause a failure from which the system is not able to recover. |

## Running the archive command

You can
invoke the archive command as shown in the following
example:

perfDWTool.bat -u user\_name -p password -nodeName node\_name archive snapshot-id-1
snapshot-id-2 ...

Where snapshot-id is
the SNAPSHOT\_ID  from the SNAPSHOTS view in
the Performance Data Warehouse database.

Use the pending command
to complete the archive. You can use the pending command
with the -preview argument to review the changes
before they are completed. Or, you can simply start the archive by
using the pending command with the -execute argument.

## Running the restore command

You can
invoke the restore command as shown in the following
example:

perfDWTool.bat -u user\_name -p password -nodeName node\_name restore snapshot-id-1
snapshot-id-2 ...

Where snapshot-id is
the SNAPSHOT\_ID  from the SNAPSHOTS view in
the Performance Data Warehouse database.

Use the pending command
to complete the restore. You can use the pending command
with the -preview argument to review the changes
before they are completed. Or, you can simply run the restore by using
the pending command with the -execute argument.

## Running the pending command

To invoke
the pending command with the -preview argument,
complete the following steps:

1. Run the pending -preview command against the
performance database as shown in the following example:
perfDWTool.bat -u user\_name -p password -nodeName node\_name pending
-preview c:\temp\PS\_pending\_script.sql
2. Review the SQL script that was saved to the specified output file
(c:\temp\PS\_pending\_script.sql, in this example). If there is no pending action
on the tables and views in the performance database, then this output file is empty.

To invoke the pending command with the -prepare argument,
complete the following steps:

1. Run the pending -prepare command against the
performance database as shown in the following example:
perfDWTool.bat -u user\_name -p password -nodeName node\_name pending
-prepare c:\temp\PS\_pending\_script.sql 
The command-line
tool creates the SQL script and prepares to move the pending records
to the database. During this time, data loading is disabled until
the pending actions are complete.
2. Stop all Performance Data Warehouses.
3. Review the SQL script that was saved to the specified output file
(c:\temp\PS\_pending\_script.sql, in this example).
4. Run the SQL script against the performance database by using the
database maintenance tool of your choice. The pending records are
added to the database.
5. Restart all Performance Data Warehouses.

To invoke the pending command
with the -execute argument, complete the following
steps:

- Run the pending -execute command against the
performance database as shown in the following example:
 perfDWTool.bat -u user\_name -p password -nodeName node\_name pending
-execute 
The command-line tool runs the
SQL script against the performance database so that tracked data records
that were in a pending state are successfully transferred to the database.