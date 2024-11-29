# Migrating business data and applications to V20.0.0.1

You can migrate your business data and applications from IBM® Business Process Manager
 V8.0 to Business Automation Workflow V20.0.0.1. This migration method requires
downtime and involves a database upgrade.

Use this migration method for your staging (to test the
migration) and your production environments. Use artifact migration
for your development and test environments.

1. Install the new product version.
2. Export configuration information from the source environment.
3. Configure the target environment with the Business Automation Workflow Configuration editor using the properties file
that was exported.
4. Create the target environment.
5. Upgrade the existing databases.

This migration method requires downtime. There is no fixed
formula to estimate the time in advance because the amount of downtime
depends on a number of factors, such as the number of process instances,
tasks, users, groups, durable subscriptions, and tracking groups,
the size of your data, and the execution context. Before you run migration,
consider removing data that you no longer need to keep, such as completed
process instances that are more than thirty days old and performance
data that is more than thirty days old.

## Related information

- Deprecated and removed features of IBM Business Automation Workflow