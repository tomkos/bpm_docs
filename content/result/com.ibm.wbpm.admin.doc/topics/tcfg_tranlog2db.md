# Storing transaction logs in a database for high availability

## Before you begin

## About this task

This solution uses two data centers. One is the primary
data center and the other is a standby data center. The installation
and configuration data from the primary data center is copied to the
standby data center. Database replication is used to synchronize replication
of runtime data from the primary database to the standby database.

## Procedure

1. At the primary site, install IBM BPM on all nodes and create a deployment environment as
you would normally.
2 Set up and configure the database.
    1. Install the database for the primary data center.
    2. Use generated database scripts to create database objects.
    3. Install the database in corresponding standby data center.
    4. Configure the databases to implement data replication
between the primary database and the standby database.
3 Configure the transaction service.

1. Start the deployment environment at the primary data
center.
2. For each cluster member in the application cluster and
in the support cluster, create a data source on the cluster level.
Configure the logs for the transaction service and the compensation
service for each cluster member into the database. Use a unique prefix
for each member. See detailed instructions in Storing transaction and compensation logs in a relational
database for high availability in the WebSphere Application
Server documentation.
4. When all cluster members in application and support clusters
are configured, enable transaction high availability for each application
and support cluster. On the Configuration page
under General Properties, select Enable
failover of transaction log recovery.
5 Restart the whole environment and make sure that thereare no exceptions in the system log files. When you starta process server that is configured to store transaction and compensationlogs in a database, the transaction service can time out while theservice waits for the data source to become available. If that happens,you see this error message: WSVR0009E: Error occurred during startupcom.ibm.ws.exception.RuntimeError: com.ibm.ws.recoverylog.spi.InternalLogException: Failed to locate data source, com.ibm.ws.recoverylog.spi.InternalLogException: Failed to locate data source at com.ibm.ws.tx.util.WASTMHelper.asynchRecoveryProcessingComplete(WASTMHelper.java:176) at com.ibm.tx.util.TMHelper.asynchRecoveryProcessingComplete(TMHelper.java:57) If you encounter an error of this sort, increasethe timeout value.

```
WSVR0009E: Error occurred during startup
com.ibm.ws.exception.RuntimeError: com.ibm.ws.recoverylog.spi.InternalLogException: Failed to locate data source, 
com.ibm.ws.recoverylog.spi.InternalLogException: Failed to locate data source
        at com.ibm.ws.tx.util.WASTMHelper.asynchRecoveryProcessingComplete(WASTMHelper.java:176)
        at com.ibm.tx.util.TMHelper.asynchRecoveryProcessingComplete(TMHelper.java:57)
```

1. Open the administrative console.
2. Select Servers > Application servers > server
name.
3. Under Server infrastructure,
select Java and Process Management > Process Definition.
4. Under Additional properties,
select Java virtual machine > Custom properties > > New.
5. In the Name entry field, type com.ibm.ws.recoverylog.custom.jdbc.impl.ConfigOfDataSourceTimeout.
6. In the Value entry field, set
an integer timeout variable such as 30000 to
represent a 30-second timeout. The timeout period is measured in milliseconds.
7. Select OK.

## What to do next

Devise a high availability and disaster recovery test
plan that is appropriate for the business needs of your organization.
The plan might include simulating a WebSphere Application Server ND
failover and a cross-database failover to ensure that your system
provides adequate business continuity.