# Planning to migrate databases

- Make sure that your test environment is isolated from the production environment. Make sure that
the two environments do not use the same Workflow Center.
- While you are using the cloned database, do not deploy new applications or update existing
applications on your test or production environments.

After you finish testing migration, configure a new deployment environment that you intend to use
as the target production environment. You can clone the latest version of the production database to
keep the database data up-to-date, or you can switch your new target deployment environment to point
to the source production database when you run the migration.

- Normalized in Coordinated Universal Time (UTC)
- Based on the local time zone

For information about the minimum number of databases required,
see Planning the number of databases. If you are planning a single
deployment environment, you can reuse the previous common database
for both cell-scoped and deployment-environment-scoped data. If you
plan to have multiple deployment environments after migration, one
of the new deployments environments can reuse the common database
but you must create a new deployment-environment-scoped database for
each extra deployment environment.

When you migrate to 24.x, you can reuse
existing schemas or choose to create new ones. You might want to create a new schema for the
messaging engine database because there is only one messaging engine bus. Also, remember that the
Workflow Server and
Performance Data Warehouse tables must use different schemas.

| Database capability   | V7.5.1 schema   | V8.5 schema   |
|-----------------------|-----------------|---------------|
| CellScopedDB          |                 | T3CELL        |
| CommonDB              | T3CELL          | T3CELL        |
| ProcessServer         | T3S1PS          | T3S1PS        |
| PDW                   | T3S1PDW         | T3S1PDW       |
| BSpace                | T3SR01          | T3SR01        |
| BPC                   | T3SR01          | T3SR01        |
| Messaging             | T3S1C           | T3S1ME        |

More information about migrating databases is shown in the sample
migration topologies topics.