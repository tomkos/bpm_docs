# Snapshot and process instance migration

- Snapshot and process instance migration overview

To help better understand the snapshot and process instance migration, this overview shows the involved actions and behaviors.
- Migration tuning options

You can improve the performance of migrating snapshots and instances by adjusting the configuration options.
- Administrative strategies for migrating snapshots and instances

As an administrator, you can ensure that snapshots and instances migrate successfully.
- Development strategies for migrating instances

Migrating process instances is not a fully automated process. Understanding the way program elements are handled during migration helps you avoid migration failure.
- Managing tokens

A token is a pointer that is associated with an activity. The token becomes orphaned when it is associated with an activity which has been deleted from the process. You can manage tokens by using REST APIs. When tokens are orphaned, you can also manage them by using a migration policy file or the Process Inspector.
- Migrating process instances and snapshot data

After a snapshot has been deployed, you can migrate instances and snapshot data from one snapshot to another by using the Process Admin Console or the BPMMigrateInstances command. Snapshot data is also migrated when instances are migrated.
- Migrating snapshots by using Workflow Center

If you are creating a custom deployment package or deploying a snapshot by using IBM Workflow Center, you can specify various migration options to trigger automatic migration or deletion of instances with deployment. These migration options don't apply to other methods of deployment or instance migration. This method doesn't support the orphan token migration policy file.
- Migrating case snapshots and related process instances

You can migrate process instances and snapshot data for case projects in line with the traditional Business Automation Workflow process applications.