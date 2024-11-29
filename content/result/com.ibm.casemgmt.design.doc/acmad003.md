# Backing up your system

## About this task

When you create a backup policy for your IBM Business Automation
Workflow system, you must be familiar
with the requirements of all the components. For example, the IBM
FileNet® P8 contains both content and
workflow elements for the system.

- Backing up FileNet P8 components
- Backing up IBM Business Automation Workflow components

- C:\IBM\FormsServer\installation path\ICM
- C:\IBM\FormsServer\installation path\API

## Backing up FileNet P8
components

Work with your backup administrator to prepare a plan for backing up the FileNet P8 data and assets that are
associated with your IBM Business Automation
Workflow
system. Use the information from the FileNet P8 documentation to understand and
plan for your backups of the FileNet P8 system.

### About this task

Determine the location of IBM
FileNet P8 data in the FileNet P8 domain that is used by IBM Business Automation
Workflow. This data set includes the
global configuration database, object stores, workflow systems, and solutions. Also determine the
location for all IBM Content
Navigator data that is
related to IBM Business Automation
Workflow,
including desktops and plug-ins.

See the following table for a list of FileNet P8 components to back up.

| FileNet P8 components                                                                      | Backup instructions                  |
|--------------------------------------------------------------------------------------------|--------------------------------------|
| Global configuration database                                                              | Global configuration database backup |
| Object stores (design, staging, and target), workflow system, and file stores storage area | Object store backup                  |
| IBM Content Navigator                                                                      | Backing up IBM Content Navigator     |
| Optional: Case Analyzer                                                                    | Case Analyzer store backup           |
| Content Platform Engine server                                                             | Server configuration backup          |

## Backing up IBM Business Automation
Workflow
components

Work with your backup administrator to prepare a plan for backing up workflow components.
For the IBM Business Automation
Workflow files and
data, your backup plans can depend on how often files are used or changed.

### Procedure

To back up the workflow components:

- Back up the IBM Business AutomationWorkflow network share that hosts runtime plug-ins, add-ons configuration, documents, and customized widgetpages (run time). To determine the location of the directory to back up:
    1. In the workflow configuration tool, open your configuration profile.
    2. Right-click profile name and click Edit Profile
Properties.
    3. Click Next twice, navigate to the Content Platform Engine
definition page and locate the Network shared directory
field.
- Back up the workflow server.

1. Back up all files and sub directories in
icm\_installation\_path\configure.
2. Back up your application server profiles.
- Optional: Back up the IBM Business AutomationWorkflow rules repository directory.This backup step should be part of the Content Platform Engine file store backup policy. Todetermine the location of the directory to back up:

1. In the workflow configuration tool, open your configuration profile.
2. Right-click Configure Business Rules in the profile pane and click
Edit Selected Task. Locate the Rules repository
directory.
- Back up case management solutions (design time or run time) and customized widget pages (design
time) by backing up the object store. See  Object store backup.
- Optional: If you are using a case history store to record extended case history, determine thelocation of the case history store database. Include your plans for backing up the case historystore as part of the backup of the IBMFileNet P8 domain.

1 Determine the data source that was used for the case history database connection.
    - In the workflow administration client, expand Object Stores in the Domain
pane, then click the target object store.
    - Click Case History Store and note the value for the data source in the
Case history database connection field.
2. In your application server console, view the information for the data source. For example, in
WebSphere® Application
Server, the information is
listed in the JDBC data sources. The database information is indicated in the Comment and required
data source properties.