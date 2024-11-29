# Backing up databases

## Before you begin

- Restoring the databases to a prior state should be done with care,
because you will lose all business process-related data.
- You must back up and restore all the databases related to the
deployment environment. You cannot restore only one database and not
the others.
- For IBM Business Automation Workflow Advanced
environments where you have BPEL applications installed, restoring
the database can cause inconsistencies between the WebSphere configuration
(where the BPEL applications are installed) and the Business Process
Choreographer database. Therefore, you must manually uninstall all
BPEL applications that have been installed after the last backup before
you restore the databases. See the related information.
- If you installed interim fixes after you created the backup, review
the readme files for the interim fixes and rerun any database upgrade
steps after you restore the database from the backup.
- You can use backups to revert to the post-installation state of
the databases, if necessary.

## Procedure

1. Verify that sufficient space exists to back up your databases.
The size that is required for the backups depends on the size of your
production databases and the specifics of your database backup strategy.
2. Back up your existing IBM Business Automation Workflow databases,
using the backup utilities for your database software.

## Related information

- Undeploying BPEL process and human task applications, using the administrative console
- Undeploying BPEL process and human task applications, using an administrative command
- Cleanup procedures for Business Process Choreographer