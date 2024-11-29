# Migrating from any version of IBM BPM Express on Windows

Migrate from a previous version of IBM Business Process Manager
Express to IBM Business Automation Workflow
Express on Linux or UNIX.

To migrate your business data and applications, complete the following tasks.
Until you are ready to upgrade the databases, your source environment can still be running.

1. Performing premigration tasks

Before you begin the migration procedure, verify that your target migration environment is supported and that your source migration environment is ready to be migrated.
2. Installing IBM Business Automation Workflow 24.x

Before you begin migration, use custom installation to install IBM Business Automation Workflow 24.x on a different computer, or in a different directory on the same computer as your previous version.
3. Copying the migration utilities to the source computer

If you installed IBM Business Automation Workflow 24.x on a different computer from your source environment, package the remote migration utilities into an image and copy the image back to the source computer. You will use the migration utilities to take a snapshot of the previous version.
4. Migrating the configuration from the source environment

Migrate the configuration information from your source environment so that you can start with the same configuration when you create your target environment. Later, you will use the IBM BPM Configuration editor to configure the environment that you want.
5. Configuring your environment graphically with the IBM Business Automation Workflow Configuration editor

The IBM Business Automation Workflow Configuration editor is a browser-based interface for configuring your new deployment environment. You can graphically edit the configuration properties file that was exported from your source environment by the BPMConfig -migrate command. After you modify the properties file in the editor, you can use the BPMConfig -create command to create a new deployment environment that is based on the modified file.
6. Creating new databases and validating database connections

If you need new databases, you must create them before creating your deployment environment. Even if you have no new databases, validate that all database connections are correctly configured before you continue with the migration.
7. Configuring IBM Business Automation Workflow 24.x

After you install IBM Business Automation Workflow 24.x and use the IBM Business Automation Workflow Configuration editor to modify the properties file that is used to configure the new topology, run the BPMConfig -create command to create the profiles and network deployment environment. The BPMConfig command is required for migration.
8. Backing up databases

Before you upgrade your existing databases, if you are not using cloned databases to test migration, create backup copies. You can use backups to revert to the premigration state of the databases at any time, if necessary.
9. Upgrading existing databases

After you install the new version of IBM Business Automation Workflow, initialize new databases and upgrade your existing databases so that your data works with the new version.
10. Starting the target environment

Start the new environment, including the deployment manager, managed node or nodes, and servers.
11. Moving your custom configuration to the target environment

During the migration, many of the customizations that you made in the source environment are automatically applied to the target environment.
12. Restarting and verifying the migration

After you migrate to IBM Business Automation Workflow, restart the deployment environment and verify that the migration was successful.
13. Migrating document attachments to the BPM document store

After migration, you must migrate your document attachments from the Process Server
database to the BPM document store. The migration of document attachments is a required
post-migration task.
14. Completing configuration for migrating to a different computer

After you migrate to a different computer, you might need to change some configuration settings that were not updated automatically.