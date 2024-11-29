# Recovery scenarios

Learn about a disaster recovery scenario to back up, restore, and verify IBM® Business Automation
Workflow, including the
installation, configuration, and underlying database. The recovery scope covers only the production
environment and no other systems and components that interact with it.

- Configuration backup and restoration

After a configuration change, such as when you create a profile, configure a deployment environment, or install an application, back up the configuration data of the primary environment. Then verify whether the configuration change can be restored successfully in the secondary environment.
- Runtime backup and restoration

After you back up and restore the configuration and runtime data, verify whether the current instances, such as long-running process instances, short-running process instances, and SCA invocation instances can be restored to the secondary environment.
- Verification of the backup and restoration

For production environment and application scenarios, test your backup and restoration procedure so that you can identify any problems that might exist in your procedure.