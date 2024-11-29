# Migrating artifacts and then business data and applications to V20.0.0.1

1. Migrate Workflow Center (migrating artifacts)
2. Migrate the test Workflow Server environment (migrating artifacts)
3. Migrate the preproduction or staging Workflow Server environment (migrating business data and
applications)
4. Migrate the Workflow Server production environment (migrating business
data and applications)

- Upgrading from IBM Business Automation Workflow
Enterprise or IBM Business Automation Workflow
Express 18.0.x, 19.0.0.1, or
19.0.0.2 to 24.x is
not supported. Upgrade to 23.0.1, then upgrade to 24.x.
- You cannot upgrade from IBM Business Process Manager
Express to IBM Business Automation Workflow
Express. Use migration
instead.
- Upgrading from IBM Business Process Manager
 V8.5 or V8.6 is not
supported. Install a fix pack earlier than 22.0.2, then upgrade to 23.0.1.
- Migrating from IBM Business Process Manager
 V7.5.x to IBM Business Automation Workflow 24.x is not supported.
Migrate to IBM Business Automation Workflow
V19.0.0.3, then install the latest cumulative fix. See Migrating and upgrading in the V19.x information.
- Migrating from WebSphere® Process
Server V7.0.x to IBM Business Automation Workflow is not supported.
Migrate to IBM Business Process Manager

V8.6 cumulative fix 2018.03, then install the fix pack earlier than 23.0.1, then upgrade to latest
cumulative fix. See Migrating and upgrading in the V8.6.x information.
- Migrating from IBM Business Process Manager
 V8.0.x to IBM Business Automation Workflow 24.x is not supported.
You can use artifact migration, or you can migrate to IBM Business Automation Workflow V20.0.0.1, then
install the latest cumulative fix.
- Migrating from IBM Business Process Manager
 Advanced or IBM Business Process Manager
 Standard V8.5.x or
V8.6 to IBM Business Automation Workflow 24.x
is not supported. You can use artifact migration, or you can migrate to IBM Business Automation Workflow V22.0.1, then install
the latest cumulative fix.
- If you are migrating from IBM Business Process Manager
Express to IBM Business Automation Workflow
Express, you can use artifact
migration (see Migrating artifacts to IBM Business Automation Workflow) or you can migrate business data and
applications (see Migrating business data and applications from any version of IBM BPM Express to IBM Business Automation Workflow).

## Migrate Workflow Center

Because
Workflow Center contains playback instances only, you do not need to
migrate the instances to the new product version. You can use the
artifact migration approach to migrate Workflow Center first, rather
than extracting database information and upgrading the old databases.
With this type of migration, you create both a new database and a
new installation and configuration of Business Automation Workflow.

With
artifact migration, the Workflow Center does not keep playback instances
and contains only the change history of the snapshots that you choose
to import. Runtime data (such as instances, tasks, tracking groups)
and offline server deployment information are not migrated.

- You can set up Workflow Center and start migrating applications
before you install the new version of the product.
- You can move applications to the new product version one application
at a time.
- The previous Workflow Center remains available to handle fixes
for the production system.
- Workflow Center does not incur any downtime.

1. Install Workflow Center V20.0.0.1.
2. Use the BPMConfig command or manually configure
the new environment and create new databases.
3. Start the new deployment environment and move your applications
from the source to the target. Follow the instructions in Migrating Process Center artifacts to
export all the snapshots from the old environment that you want to
keep, and then import them into the new environment. For each application,
import the oldest to newest snapshots to preserve the change history.
4. Test the process applications to ensure that they work in the
new environment.
5. Fix issues and performance tune the new environment in parallel.

## Migrate the test Workflow Server
environment

Migrate
the test Workflow Server environment using the artifact migration approach.
You can use this environment to test all the process applications
from the previous version.

1. Install Workflow Server V20.0.0.1.
2. Use the BPMConfig command or manually configure
the new environment and create new databases.
3. Connect the new Workflow Center with this Workflow Server.
4. Follow the instructions in Installing process application snapshots to install
the process applications from the new Workflow Center.
5. Test the process applications to ensure that they work in the
new environment.
6. Fix issues and performance tune the new environment in parallel.

## Migrate the preproduction or staging Workflow Server environment

1. Follow the procedure in Migrating business data and applications to IBM Business Automation Workflow,
choosing your specific configuration.
2. Clone the databases before configuring the new environment and
point to the cloned databases to make sure that migration works correctly
before you upgrade the databases that are in use.
3. Test the migrated target environment and resolve migration-related
issues by manually updating the target configuration. Performance
tune the environment in parallel.

## Migrate the Workflow Server production
environment

1. Follow the procedure in Migrating business data and applications to IBM Business Automation Workflow,
choosing your specific configuration.
2. Test the migrated target environment and resolve migration-related
issues by manually updating the target configuration. Performance
tune the environment in parallel.