# Restoring your system

## About this task

- Restoring FileNet P8 components
- Restoring workflow components

## Restoring FileNet P8
components

Start your restore with the foundation components in the IBM
FileNet P8 domain. For each high-level step
in your restore process, work with the backup administrator and use the appropriate product
documentation to determine the specific steps that are required.

### About this task

See the following table for a list of FileNet P8 components to restore.

| FileNet P8 components                                                                      | Recovery instructions                                             |
|--------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Global configuration database                                                              | Recovering the data in your FileNet P8 domain                     |
| Object stores (design, staging, and target), workflow system, and file stores storage area | Recovering the data in your FileNet P8 domain                     |
| IBM Content Navigator                                                                      | Refer to the backup information: Backing up IBM Content Navigator |
| Optional: Case Analyzer                                                                    | Recovering the data in your FileNet P8 domain                     |
| Content Platform Engine server                                                             | Refer to the backup information: Server configuration backup      |

## Restoring workflow components

You can restore Business Automation Workflow components by using
your latest backups. Work with your backup administrator to understand the backup policy and the
best way to perform the restore.

### Procedure

To restore the workflow components:

- Restore the workflow servers.
    1. Reinstall the Business Automation Workflow software as
needed.
    2. Reconfigure the software or restore the workflow configuration files from a
backup.
- Restore the Business Automation Workflow network share that hosts runtime plug-ins, add-ons configuration, documents, and customized
widget pages (run time) from the latest backup.
- Restore the case management solutions (design time or run time) and customized widget pages
(design time) by recovering the object store. See Recovering the data in your FileNet P8 domain.
- Optional: Restore the case history store database from the database server.
- Optional: Restore the business rules repository. Restore and overwrite the network shared
directory from the latest backup.