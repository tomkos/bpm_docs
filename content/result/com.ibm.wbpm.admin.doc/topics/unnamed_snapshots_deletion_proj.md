# Deleting unnamed snapshots dynamically from a Workflow Center server

## Before you begin

You must be a development environment administrator with access to the local configuration files
on the server to do this task.

## About this task

If you have some projects under development in Workflow Center that generate a high number of unnamed
snapshots, you might want to delete the snapshots as they are created to avoid database bloat or
poor performance of your Workflow Center server.
When dynamic deletion is enabled, each time a named snapshot is created, the unnamed snapshots
between the new and the preceding named snapshot are deleted. Because the snapshots are dynamically
deleted, the deletion does not have to be scheduled, and there is no down time for the server.
Automatic deletion never removes named snapshots.

```
<server>
     <delete-unnamed-snapshots-between-named-snapshots merge="replace">true</delete-unnamed-snapshots-between-named-snapshots>
</server>
```

For more information about changing configuration properties, see the topic Creating a 100Custom.xml configuration file.

## What to do next

The easy way to manage the accumulation of unnamed snapshots
on your Workflow Center server is to enable automated deletion. However, you can
also delete specific unnamed snapshots or archived snapshots. See Deleting unnamed and archived snapshots, manual for details.