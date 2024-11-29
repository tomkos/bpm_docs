# Migrating snapshots by using Workflow Center

If you are creating a custom deployment package or deploying a snapshot by using IBM® Workflow
Center, you can specify
various migration options to trigger automatic migration or deletion of instances with deployment.
These migration options don't apply to other methods of deployment or instance migration. This
method doesn't support the orphan token migration policy file.

## About this task

Consult the following table to understand the migration options.

| Migration option   | Description                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Leave              | The instances that are currently running continue to completion using the previously installed snapshot.                                                                                                                                                                                                                                                                                        |
| Migrate            | You can select multiple source snapshots to migrate instances. The running instances will be migrated to the deployed snapshot. Note: You can select only source snapshots that meet certain conditions. You cannot use a migration policy file.                                                                                                                                                |
| Delete             | The instances that are currently running are immediately stopped and do not continue to completion. All records of the running instances are removed from the workflow server. The delete option does not delete BPEL process instances, human task instances, or business state machine instances. Note: This option is not available for workflow servers with a Production environment type. |

## Procedure

1. In Workflow Center, go to the
snapshot and click Install to install it to a selected online server or
create a deployment package for a selected offline server.
2 If any snapshots of the process app for the server meet certain conditions, the manageinstances screen opens.
    - For an online server, Workflow Center must show
running BPD instances for a snapshot.
    - For an offline server, Workflow Center must
contain a deployment package for a snapshot.
3. For each listed snapshot, select to leave, migrate, or delete instances as mentioned in the
previous table. When the snapshot has installed successfully, the selected action is performed.