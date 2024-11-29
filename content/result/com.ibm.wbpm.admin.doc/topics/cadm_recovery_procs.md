# Disaster recovery procedures

Disaster recovery for IBM Business Automation
Workflow is supported through
the disk replication technology. A snapshot of the original production environment is taken, and
data is restored and validated in the secondary data center. You can store transaction and
compensation logs in a relational database so you can use the high availability disaster recovery
features that the database offers.

The following topics provide some guidance in setting up and managing
a disaster recovery system.

- Configuring a disaster recovery backup system

The configuration data of your system describes the IBM Business Automation Workflow environment.
- Backing up runtime data with a SAN drive

The runtime data of your system is the information that is stored in transaction logs and compensation logs. You can use a storage area network (SAN) drive to copy files from your primary data center to a standby server.
- Storing transaction logs in a database for high availability

You can configure transaction logs to be stored in a database where you can implement automatic replication and simpler disaster recovery.
- Restoring data

If a disaster occurs in the primary data center, you can continue to provide business support if you have a valid backup. You restore the backup to the secondary data center and then verify the restored data.
- Verifying restored data

After you restore the backup of your production environment to the secondary data center, verify the data to determine whether the backup is a valid copy.