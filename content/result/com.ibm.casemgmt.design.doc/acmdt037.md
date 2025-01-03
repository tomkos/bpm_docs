# Preparing a database for the case history store

## Before you begin

## About this task

The system can store extended case history data in the
database instance that is used for the target object store, or in
a separate database instance. Consider the capacity of your database
server, the case size, and the case load when determining where to
store extended case history data.

When extended case history
data is stored in the database instance that is used for the target
object store, you do not need to define an additional JDBC data source,
and you can easily back up the case history store along with the target
object store. However, including the case history data increases the
load on the database server, and this can have a negative impact on
performance. Defining a separate database on the same remote database
server as the target object store can also degrade performance.

Alternatively,
the system can store extended case history data in a separate database
instance. For example, you might want to use a separate, remote database
server if I/O throughput is problematic. If the system stores extended
case history data on a different remote database server, you can get
additional disk arms, disk space, CPU, and memory to support it.

The following procedure refers
to IBM®
FileNet® P8 tools and procedures
to set up a database for your case history store.

## Procedure

To store extended case history in a separate database instance:

1. Prepare the database for the case history store.
For more information, see Database administrator installation tasks.
2. Create JDBC data sources. Run the Configure JDBC Data Sources task by using the IBM
FileNet P8 Configuration Manager.
For more information, see Editing the Configure JDBC Data Sources tasks and Configuration Manager reference.
3. Create a database connection.
For more information, see Creating a database connection. Based on performance
considerations, you might want to share data sources. For more information, see Sharing data sources. You enter the database schema name when
you configure and enable the case history store by using the IBM Business Automation
Workflow administration
client.

## What to do next