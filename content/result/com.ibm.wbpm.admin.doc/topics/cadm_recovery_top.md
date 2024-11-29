# Disaster recovery concepts

## Production environment

The data center of
an IT environment typically consists of various systems and environments,
such as Enterprise Resource Planning (ERP), Customer Relationship
Management (CRM), and Human Resource Management (HRM). The disaster
recovery strategy must define the general rules from a high-level
point of view, with detailed plans for each system.

Each system
might be a complicated combination of software and hardware deployments.
The disaster recovery for the system must take all components into
consideration to provide a complete solution.

The underlying database to support IBM® Business Automation
Workflow and the messaging
engine, which is Business Space that is powered by WebSphere, are also regarded as part of the
production environment. They are included in the same recovery scope because the whole production
environment must be in a consistent state during the restoration phase.

## Data classification

<!-- image -->

Some kinds of data, such as operating system installation and configuration data, IBM Business Automation
Workflow installation data,
and database installation data, can be rebuilt or reinstalled. Other kinds of data, such as
transaction logs, application data, and configuration data for IBM Business Automation
Workflow, must be recovered.

Define your recovery scope, recovery point objective,
and recovery time objective goals according to your business needs.

## Recovery scope

## Recovery point objective

The recovery
point objective defines how much data you can afford to lose
between the original environment and the restored environment. From
a business perspective, a smaller recovery point objective means that
fewer business transactions are lost, which is critical for normal
business operations.

To achieve a smaller recovery point objective,
you must increase the frequency with which you back up the production
environment. However, you must also consider the cost and effect of
frequent backups on your production environment. The more times you
back up, the more copies you must maintain.

## Recovery time objective

The recovery
time objective defines how long you can wait until the restored
environment can continue with normal processing. From a business perspective,
you might want to achieve different recovery time objectives that
are based on your own business needs.

To define the appropriate recovery time objective, consider the work that must be done during
disaster recovery. Increasing the frequency of your backups does not always lead to a smaller
recovery time objective. For example, if the server startup takes 20 minutes, you cannot reduce
recovery time to less than 20 minutes, no matter how often you back up. You must rearchitect your
server to start faster or get a faster server.

Figure 1. Recovery
point objective and recovery time objective

<!-- image -->

## Consistency

After a disaster and a successful recovery of the production system from backup, you must ensure
that you have consistent data. For IBM Business Automation
Workflow, this consistency
must apply to all cell members. If one node in a cell is inconsistent, the backup image and restore
attempt are invalid.

| Type of consistency     | Description                                                                                                                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Crash consistency       | The bytes in the restoration match the ones in the primary system at the time of the backup. In a shared, multinode environment, the data for the cluster is assured to be in the same time sequence as the write operations. |
| Application consistency | When the operating system starts, there are no file system recovery errors. Applications can access data from the time of the backup without failure. The applications recover inflight transactions when they are restarted. |