# Runtime logs in a database: Overview

The WebSphere Application Server transaction service writes information
to a transaction log for every global transaction that involves two
or more resources, or that is distributed across multiple servers.
These transactions are started or stopped either by applications or
by the container in which they are deployed. The transaction service
maintains transaction logs to ensure the integrity of transactions.
Information is written to the transaction logs in the preparation
phase of a distributed transaction. If a WebSphere Application Server
with active transactions restarts after a failure, the transaction
service is able to use the logs to replay any in-doubt transactions.
This implementation allows the overall system to be brought back to
a consistent state. For more information, see Transaction log file.

The WebSphere Application Server compensation service allows applications
on disparate systems to coordinate activities that are more loosely
coupled than atomic transactions. It stores information in its own
dedicated recovery logs. That information is necessary for compensation
after a system failure.

IBM Business Process Manager provides two ways that you can store
these runtime logs in a data recovery system. The transaction logs
can be stored as operating system files. Using that approach, high-availability
transaction support requires the use of a shared file system to host
the transaction logs, such as Network File System (NSF) or IBM General
Parallel File System (GPFS). The shared file system is typically mounted
on a storage area network (SAN). Storing runtime data in the operating
system files remains a recommended configuration, but now you have
another configuration that you can use for high availability.

With features introduced in IBM Business Process Manager Version
8.0.1.2 and 8.5.0.1, you can choose to store transaction logs and
compensation logs in a relational database. This configuration is
a useful option if you want to use database features such as DB2 HADR
or Oracle Data Guard to provide high availability for runtime logs.
It supports automatically replicating transaction logs and compensation
logs to a disaster recovery system. Installation and configuration
data can be copied directly from the primary site. All runtime data
is persistent in database. You can use database replication to synchronize
runtime data from the primary site to the disaster recovery site,
if all related runtime data can be configured into the same database.

In the topology that is shown in the accompanying diagram, in each
data center, each cluster has two members. To use high availability
features, configure all members in application, message, and support
clusters to use the database to store transaction logs. During normal
processing, all cluster members access their own transaction tables
to store transaction information. If one cluster member fails, the high availability manager notifies the other
member from that cluster to take over the work. Then, the high availability
manager starts an automatic peer recovery of the transaction log tables
of the failed cluster member.

For database replication, you can be confident of data consistency
only if you use a single database. If two or more databases are used
by a single transaction, there is no way to guarantee the data consistency
because it is impossible to coordinate the two replication processes.
So, in a Standard
deployment environment, configure
transaction logs in BPMDB. For process applications in an Advanced
deployment environment, you can use CMNDB for transaction
logs with Oracle products with Data Guard. You can use CMNDB with
DB2 if the process application uses only BPEL.

Since a single transaction might involve two or three cluster members,
make sure that the transaction logs from all cluster members are configured
in the database. Place compensation service logs in the same database.

The figure shows a typical configuration for primary and standby
data centers.

<!-- image -->