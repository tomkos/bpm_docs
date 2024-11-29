# Backing up runtime data with a SAN drive

## About this task

Your runtime data changes continuously, and you can back up this data synchronously or
asynchronously. Synchronous backups ensure that the backup data center matches the primary data
center, but in many cases synchronous backups are not feasible because they have a high impact on
the system's performance. Asynchronous backups do not have the same performance issues, but the
trade-off is that the backup and primary data centers do not always match.

The runtime data consists of the WebSphere®
transaction logs and the compensation logs. Some of the files are associated with the IBM® Business Automation
Workflow databases and some of the files are associated
with any other resource managers. The files of interest are files that reflect the current state of
the database tables, the current state of the transactions. Any other data that is managed by the
resource that reflects the current state of the resource. These files vary from one implementation
to another, depending on the database product or resource manager and vendor that is being used. The
set of database tables in this runtime data includes at least all of the tables that are associated
with your Business Automation Workflow configuration, such as persistent
stores for messaging engines, business process applications, human tasks, and failed events.

Include the data
that you require on a disk replication system with the following configuration:

## Procedure

1 Configure the original data center.
    1. Create directories that are needed for mounting the
SAN, like /opt/ibm/WebSphere/tranlogs on the WebSphere servers and /opt/ibm/WebSphere/database on
the database server.
    2. Mount the storage area network (SAN) drive.
    3. Configure the transaction service to use a distributed
file system.  The SAN creates two volumes, one for the
database and one for the distributed file system, which is mounted
on the SAN for its transaction logs. The distributed file system serves
high availability by managing file locks for the distributed servers.
The SAN serves disaster recovery by providing replication.
    4. Configure the database server to use this mount for
its data and log files.
2 Configure the disaster recovery data center. The entire set of files for the runtime data must be includedin the same snapshot and that snapshot must be taken at an instantof time. Your performance needs might require you to place the databaselog files on different disk arms than the database data or indicatesome other placement needs. Work with your database vendor, your SANvendor, and your operating system to configure the optimum configurationfor your requirements. As you work with your SAN vendor, you mustmake sure that the write order is preserved in the snapshot and itsreplica.

1. Create a directory in the disaster recovery data center
similar to the one in the original data center.
2. Load the disaster site recovery scripts or procedures
for the run data replicated volume.
3. Install and configure the data database catalog to find
the appropriate files.

## What to do next

Set a schedule for the snapshot that is taken of the volume. The schedule determines whether you
can meet your recovery point objective. For example, if you have a recovery point objective of 30
minutes, capture a snapshot at an interval of less than 30 minutes. You must consider the time that
it takes to take a snapshot and transfer it to the disaster data center. Your SAN provider can help
you sort out those details.