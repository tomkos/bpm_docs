# Planning a migration

- You want to improve performance.
- You need fixes that are in the new version.
- You want to use new features that are provided in the new version.
- Your existing product version is going out of service.

- You must estimate in advance the amount of downtime that will
be needed for migration. An estimate of downtime cannot be created
without testing.
- You want to make sure that the new version improves performance.
- You want to make sure that the fixes you require are in the new
version and work as expected.
- You want to make sure that your existing applications work correctly
in the new version.

- Prepare test cases that are based on the existing functions and requirements.
- Prepare the test environment. The following factors must be the same in both the testenvironment and the production environment: If you are not testing for the amount of downtime, you might not care about disk space, memory,or processor.
    - Operating system type and version
    - Database type and version
    - IBM® Business Automation Workflow version
and WebSphere® Application
Server version
    - IBM Business Automation Workflow
topology
- Test the migration. Make sure that all the migration steps run successfully.
- Use your test cases to make sure that all applications work correctly after migration.
- Make sure that you note all changes to your applications, and keep track of everything that you
moved to the new environment, to help when you migrate the production environment.

<!-- image -->

When you move the database to a new server, the data sources are generally updated using the
BPMConfig command. However, BPMConfig does not update the
transaction log data sources. The data sources for transaction logs must be updated in the admin
console or using wsadmin commands. The target database requires XA and same user
privilege. See Configuring XA transactions for your database type, for example: Configuring XA transactions for Oracle in a network environment on Windows.

```
J2CXAResource W J2CA0061W: Error creating XA Connection and Resource com.ibm.ws.exception.WsException: DSRA8100E: Unable to get a XAConnection from the DataSource jdbc/DefaultEJBTimerDataSource
```

For tuning guidance on migration, see Chapter 6: Migration considerations in
IBM Business Process Manager V8.5 Performance Tuning and Best Practices.

- Premigration cleanup

Cleaning up your environment regularly is an important part of maintaining a production environment. Cleaning up Business Automation Workflow is especially important if you plan to migrate to a new version.
- Choosing a migration approach

Before you migrate your systems, you can choose to migrate artifacts only or (for Express) you can choose to migrate artifacts in your test and development environments and then migrate business data and applications in your staging and production environments. The approach you choose depends on the production downtime that the business can tolerate.
- Planning to migrate databases

Before you migrate to IBM Business Automation Workflow, consider the databases and schemas that you want to create and the ones that you want to reuse.
- Default users and authentication aliases removed from IBM Business Automation Workflow

IBM Business Automation Workflow uses role-based user assignments to access interfaces, process applications, and toolkits. Based on this change, the default users from previous products have been removed. In addition, many of the authentication aliases have been removed. Before you migrate, check the list of default users and authentication aliases that have been removed.
- Planning to migrate multiple deployment environments or extra clusters

If you are planning to migrate your business data and applications to Business Automation Workflow and you have more than one deployment environment in one cell in IBM Business Process Manager, or if you have a deployment environment and extra clusters, you must perform more steps.
- Enabling custom password encryption

If you are migrating to IBM Business Automation Workflow 24.x, and you enabled custom password encryption in your source Business Automation Workflow environment to protect passwords that are contained in your WebSphere Application Server configuration, you must complete the following steps before migration.