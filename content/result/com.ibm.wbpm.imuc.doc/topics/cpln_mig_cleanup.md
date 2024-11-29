# Premigration cleanup

The quantity and size of artifacts to be migrated affect the complexity
and overall duration of the migration.

- Completed process instances. To remove all runtime data in the
Process database that is associated with a completed business process
definition (BPD) instance, see Removing process instances from the Process database.
- Completed tasks. To delete unneeded tasks from the Process database,
see Deleting tasks from the Process database.
- Snapshots that are no longer required. To delete inactive process
application snapshots, see Deleting snapshots on workflow servers.
- Performance Data Warehouse data that is no longer required. To
remove data that you no longer need from the Performance Data Warehouse
database, see Running the prune command.
The prune command removes data that is older than the number of days
old specified by the -daysOld parameter.
- Durable subscription messages that have already been used. To
delete used durable subscription messages from the LSW\_DUR\_MSG\_RECEIVED
database table,  see the BPMDeleteDurableMessages command.