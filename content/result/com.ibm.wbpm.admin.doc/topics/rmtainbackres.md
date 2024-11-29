# Backup and restore considerations with an external Content Platform Engine environment

Although each product has backup and restore information, the information is only for a backup
and restore within the context of each product. In other words, the backup and restore information
does not include other environments and components that interact with the product. When Business Automation Workflow has an external Content Platform Engine (or ECM) configuration, you must include the
other environment in your process.

- The object store database is integrated with both Business Automation Workflow and Content Platform Engine. Therefore, backing up or restoring the object
store database must consider the data needs of both environments.
The database location was
determined when the external object store was created and this database must be included in a backup
of the Business Automation Workflow environment. See setBPMExternalECM command.
- Depending on which option you used when you initially integrated Business Automation Workflow with the Content Platform Engine environment, database backup considerationsvary. Check which parameter was used for the setBPMExternalECM administrativecommand. See setBPMExternalECM command .
    - If you used the NEW\_EXTERNAL\_OBJECT\_STORE parameter, then the database location was determined
when the external object store was created. This database must be included in a backup of the
Business Automation Workflow environment.
    - If you used the REASSIGN\_OBJECT\_STORE or
REASSIGN\_DOMAIN parameters, then the database location did not change. In this case, back up the
Business Automation Workflow environment databases, which include
the database for the original BPM content store.
This is the database that was defined at deployment environment creation as the database that
contains the data of the BPM content store.
- If an offline backup is required for a Business Automation Workflow environment that is connected to a Content Platform Engine environment, the servers in both environments
must be shut down. To minimize impact on both environments, there is a recommended sequence to shut
down both environments. See Maintaining an external Content Platform Engine configuration.