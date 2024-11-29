# Performing premigration tasks

Before you begin the migration
procedure, verify that your target migration environment is supported
and that your source migration environment is ready to be migrated.

Figure 1. Sample environment before migration begins.
The source environment is running and transferring data to and from
its databases. The deployment environment has three clusters and is
configured across two nodes.

<!-- image -->

<!-- image -->

## Before you begin

- Make sure that your test environment is isolated from the production environment. Make sure that
the two environments do not use the same Workflow Center.
- While you are using the cloned database, do not deploy new applications or update existing
applications on your test or production environments.

After you finish testing migration, configure a new deployment environment that you intend to use
as the target production environment. You can clone the latest version of the production database to
keep the database data up-to-date, or you can switch your new target deployment environment to point
to the source production database when you run the migration.

To prevent performance problems, you must perform regular maintenance on
artifacts that accumulate over time, such as process instances, named snapshots, unnamed snapshots,
task instances, and durable messages. To customize the settings for system maintenance, see Configuring notifications and actions for system maintenance.

## About this task

This migration procedure is for a single deployment
environment. A deployment environment is a logical grouping of clusters
that work together as a unit, so a deployment environment might consist
of an application cluster and a messaging cluster, or might consist
of an application cluster, a messaging cluster, and a support cluster.
If you have more than one application cluster, you have multiple deployment
environments.

If
you have multiple deployment environments in your source version,
you must repeat the migration procedure for each deployment environment
that you want to migrate. Create different source and target migration
properties files for each deployment environment.

## Procedure

1. Verify that your target migration environment - including hardware,
operating systems, and database prerequisites - is a supported operating environment for IBM Business Automation Workflow 24.x 
Visit IBM Business Process Manager Express detailed system
requirements.

Important: If required, move to a new database version and make sure that IBM Business Automation Workflow is working correctly
before you proceed with the migration.
2 Prepare your applications for migration.
    1. Identify all applications that might be affected. Potentially
affected applications are all applications that are installed on the source environment and all
back-end applications that communicate with the source environment. Identify the contact person for
each of these applications.
    2 Some authentication aliases and users have been removed from IBM Business Automation Workflow 24.x . Before youmigrate, check Default users and authentication aliases removed from Business Automation Workflow .
        - If your applications are using aliases that have been removed, you must re-create them manually
in the target environment after migration.
        - If your applications are using users that have been removed, you must assign the required
security roles to them again after migration.
3 If your applications rely on specific WebSphere® ApplicationServer configuration, theapplications might fail to start, or fail to work correctly in 24.x unless you re-create anyrequired resources. Check for dependencies in the following areas: You might need to re-create these resources manually in the target environment aftermigration.
    - JMS configurations
    - Schedulers
    - Environment variables
    - Shared library configurations
    - Work Manager
3. If you created saved searches in Process Portal in an earlier version of the product, make sure that none of them have conditions with an empty
value. Otherwise, you will see only a blank page in Process Portal and will have to re-create those saved
searches.
4. Ensure that the source environment is running correctly. Before starting the migration, ensure
that all the Java virtual machines (JVMs) in the source system start without errors by checking the
SystemOut.log files of the deployment manager, node agents, application server
clusters, and non-clustered servers, even if they are not going to be migrated. You must especially
solve any configuration-specific problems before migrating. Also check that the proxy server or HTTP
server is running correctly.