# Migrating process instances and snapshot data

After a snapshot has been deployed, you can migrate instances and snapshot data from one
snapshot to another by using the Process Admin Console or the BPMMigrateInstances
command. Snapshot data is also migrated when instances are migrated.

## Before you begin

## About this task

- Use the BPMMigrateInstances wsadmin command - For each source snapshot you
want to migrate instances from, run the BPMMigrateInstances wsadmin command. For
more information, see BPMMigrateInstances command.
- Use the Migrate Inflight Data option in the Process Admin Console by
completing the following procedure.

## Procedure

1. From the Process Admin Console, select Installed Apps.
2. From the list of snapshots, select the one you are migrating data to.
3. Click Migrate Inflight Data.
A source snapshot selection menu opens listing valid snapshots. A snapshot must have active,
failed, or suspended instances for it to be listed.
4. Select the snapshot you want to migrate data from.
5. Optional: Upload a migration policy file.
6. Click Migrate.
When instance migration completes, you see a summary. If instance migration takes a long time,
you might see a timeout error instead of the summary. A network timeout won't prevent the instance
migration from completing on the server.

## Results