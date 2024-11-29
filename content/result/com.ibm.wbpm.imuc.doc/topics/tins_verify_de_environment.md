# Verifying the status of your environment using the Health Center

## Before you begin

## About this task

- The associated resources for every component are checked to determine whether they are usable.
For example, each component's database is checked to determine whether it has been created and a
connection can be established.
- The security configuration is checked to determine whether the essential requirements have been
met.
- Workflow Server, Workflow Center, and Performance Data
Warehouse are checked to determine whether they are usable. Several runtime checks are performed,
such as whether the associated applications and message engines have started.

## Procedure

1. Log into the administrative console.
2. If your environment has not yet been started, start the environment by following the
instructions in the Starting and stopping your environment topic.
3. In the tree view, select Servers > Deployment Environments > Deployment
environment name > Additional Properties > Health Center. The Component
Health Center opens.
4. In the Status column, examine the
status of the components. Icons are used to indicate the status of
components or resources in the Component Health Center, as shown in
the following table: 

Icons
Description

Indicates that there are no detected problems
for a component or resource.

Indicates that there are possible problems for
a component or resource.

Indicates that the status of a resource cannot
be determined.
5. In the Component column, click the
hyperlinked name of a configured component. The Details page opens.
The Details page displays the configuration status of the component. If the component has any
associated resources, such as applications and databases, the resources are displayed in tables.
6. In the Configuration status field,
examine the configuration status of the component. For
the Cell Database, Cell Security, and Deployment Environment Security
components, there is never a configuration status. For the Deployment
Environment Bootstrap component, the configuration status can be Finished, Unfinished,
or Unknown. For all other components,
the configuration status is always Configured.
7. In the associated resource tables, examine the status of the resources that are associated with
the component. Depending on the component, there are five main types of associated resources, as
shown in the following table:

Option
Description

Applications
Applications are associated with many different components, such as the ProcessServer,
ProcessCenter, and PDW components. In the Application table, examine the icons in the
Installed and Started columns to determine whether
each application is installed and started. Also examine the Exception
Messages column to determine if there are any messages for the applications.

Authentication aliases
Authentication aliases are associated with the Cell Security and Deployment Environment
Security components. In the Authentication Aliases table, examine the icons in the
Created column to determine whether each authentication alias has been
created.

Messaging
Messaging engines are associated with the Messaging component. In the Messaging table,
examine the icons in the Started column to determine whether each messaging
engine has been started. Also examine the Exception Messages column to
determine if there are any messages for the messaging engines.

Bootstrap
Bootstraps are associated with the Deployment Environment Bootstrap component. In the
Bootstrap table, examine the icons in the Imported column to determine
whether the bootstraps have been imported.

Databases
Databases are associated with many different components, such as the ProcessServer, PDW,
BusinessSpace, and BPC components. In the Databases table, examine the icons in the
Created and Connected columns to determine whether
each database is installed and connected. Also examine the Exception Messages
column to determine if there are any messages for the databases. Note: Health Center is unable to
check PostgreSQL.

## Results

## Related reference

- Problems testing a connection to a data source in a network deployment

## Related information

- Starting and stopping your environment
- Verifying the status of your environment using the BPMConfig command