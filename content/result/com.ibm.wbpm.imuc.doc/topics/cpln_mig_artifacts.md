# Choosing a migration approach

- Starting in IBM Business Process Manager
 V8.5.0, stand-alone
tasks are no longer supported. If you migrated from Teamworks and still have stand-alone tasks in
your source environment, you will not be able to use them in 22.x. You must use an alternative
approach to achieve the functionality that was provided by the stand-alone task.
- The WebSphere InterChange Migration wizard and the WebSphere Business Integration Server
Foundation Migration wizard were removed from IBM Integration
Designer V8.5.7. If you have
applications that run on WebSphere InterChange Server or WebSphere Business Integration Server
Foundation, or applications that you created that use IBM WebSphere Adapters, you cannot migrate the
applications directly to 22.x. You must migrate them using another version of Integration Designer V8.5.x and then upgrade to
V8.5.7.

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

## Migrating artifacts

You can migrate artifacts from IBM Business Process Manager
 7.5.x or later to
IBM Business Automation Workflow 22.x.

- You can keep two systems running in parallel until all existing
processes have completed.
- You are changing database vendors.
- You are upgrading from IBM BPM Express.
- You are upgrading to
Business Automation Workflow Enterprise Service Bus
24.x from Business
Process Manager Enterprise Service Bus 8.6.
- You do not have long-running process instances and human tasks, or you can run
parallel production environments while you drain the process instances and human tasks in the source
environment as new instances are started in the target production environment.
- Your business cannot tolerate a production environment downtime
window to perform the migration.

To migrate artifacts, you create a parallel target production
environment that is configured from scratch differently from the source
production environment. After you have migrated the artifacts, you
can modify your applications to use the new capabilities that the
new version of IBM Business Automation Workflow contains.
You can then test and deploy the applications to the parallel target
production environment. When the applications are deployed to the
target production environment, a new set of database tables are created,
so the applications do not have access to the application data that
is stored in the databases that are configured for the source production
environment.

- With the drain approach, you migrate artifacts to the new system
and let the existing process instances in the old system run to completion.
This process is called the drain approach because the
existing process instances are drained from the old system. Then you
start all new instances in the new system.
- With the milestone-transfer approach, you transfer the process
instance state midstream. You let the existing process instances in
the old system run to a designated set of business milestones and
then start new instances in the new system from those milestones.
This approach is not supported by the system and requires custom coding
to perform the transfer.

## Migrating artifacts and then migrating business data
and applications

You can migrate from a previous version of IBM BPM Express to IBM Business Automation Workflow 22.x.

- You have long-running process or human task instances that started
in the source environment and must complete in the target environment.
- You have product data in queues that were created in the source
environment and this data must survive the migration and be managed
in the target production environment.
- You want to move your applications to the target version without
a dependency on the development tools and the development environment.
- Your business can tolerate a production environment downtime window
to perform the migration.

When you migrate artifacts and then migrate business data and applications, you migrate the
artifacts in your development and test environments and then you migrate the business data and
applications in your staging and production environments. To migrate business data and applications,
you export the configuration information from your current environment (the source), modify it for
your new environment, and transfer the modified configuration information into your new environment
(the target). Then you point to your databases from your new environment and update the databases.
Alternatively, you can clone your databases and use the cloned databases to test the migration
before you migrate your production environment. When all applications are working in the new system,
you convert the databases to make them compatible with the new system.

This approach works on one deployment
environment at a time. If your environment contains multiple deployment
environments, consider the relationships within your topology so that
you can map them properly in the target environment.

## Summary of the benefits and drawbacks

The
following table compares the approaches.

| Approach                                                              | Benefits                                                                                                                                                                                                                                                           | Drawbacks                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Migrating artifacts (drain approach)                                  | You can migrate one application at a time to the new system No system downtime is required You can change database vendors                                                                                                                                         | Historical information is not moved to the new system You must keep two systems running in parallel until all existing processes have completed You must have a separate Heritage Process Portal for the users of the two systems, or use a custom federated portal                                                                                                                                                                                                                              |
| Migrating artifacts (milestone transfer approach)                     | You can migrate one application at a time to the new system No system downtime is required You can change database vendors Depending on how you set up the milestones, the time it takes to migrate all instances can be much shorter than with the drain approach | Historical information is not moved to the new system You must keep two systems running in parallel until all existing processes have transferred You must have a separate Heritage Process Portal for the users of the two systems until all process instances have reached their designated milestones, or use a custom federated portal Custom development of the transfer process is required and might be complicated depending on the existing process design and where records are stored |
| Migrating artifacts and then migrating business data and applications | All historical information is preserved                                                                                                                                                                                                                            | This approach has more steps to perform System downtime is required (24-48 hours or more depending on the size of the database) All applications must be migrated at the same time                                                                                                                                                                                                                                                                                                               |

- Migrating artifacts and then business data and applications to V20.0.0.1

To migrate to IBM Business Automation Workflow V20.0.0.1 and test the migration as you go, you might choose to migrate the Workflow Center artifacts first, followed by the test Workflow Server artifacts, before you migrate all business data and applications.