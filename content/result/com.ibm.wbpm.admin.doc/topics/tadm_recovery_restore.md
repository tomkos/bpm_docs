# Restoring data

## About this task

Figure 1. Restoration process

<!-- image -->

## Procedure

To restore the production environment to the secondary
environment, complete the following steps:

1. Reinstall the installation data, including the IBM® Business Automation
Workflow installation
data.
2. Reinstall Db2 and create the Db2 instance.
3. Restore the configuration data to all servers from the
backup configuration data.
4. Restore the runtime data to all servers by replicating
the backup runtime data.
5. Perform changes that are specific to the environment.
 For example, update the host name to reflect the secondary
environment, or change the data source configuration to point to the
secondary database.
6. Validate the connectivity to the resources outside the
recovery scope.
7 To restart the environment, follow these steps:
    1. Start the database server.
    2. Start the deployment manager and node agents.
    3. Start the message servers of IBM Business Automation
Workflow.
    4. Start the support servers of IBM Business Automation
Workflow.
    5. Start the application servers of IBM Business Automation
Workflow.
8. Verify the restored environment and determine whether it
is valid.
9. Recover inflight transactions.
10. Redirect load to the new environment.  Tip: You can typically set the same host name and IP address
for the secondary environment as for the primary environment. This
step depends on your backup policy.