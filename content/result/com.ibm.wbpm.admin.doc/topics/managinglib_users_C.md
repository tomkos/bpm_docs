# Managing access to workflow projects

## About this task

To manage access to individual workflow projects, you must have administrative access to the
process application, toolkit, or case template, or you must have administrative access to the
Workflow Center repository. The user who created the
workflow project automatically has administrative access.

- To use Workflow Center to
test, install, or administer a process application snapshot that contains advanced content, such as
a BPEL process, the user or group to which you belong must be assigned to the WebSphere® Application
Server administrative security
roles of Configurator, Operator, and Deployer. If you are not currently assigned to all of these
roles, click Users and Groups in the WebSphere administrative console to
modify the user or group roles.
- For case solutions, you must use the Case administration client to add users or groupsto a case project area. Alternatively, If you are using an embedded CPE and wants to add users tothe default project area, you can follow the below procedure as well. When the user is added to the admingroup, he or she has full administrative control.For moreinformation about giving a user access to a case solution, see Planning for security in the development environment .
    1. Log in to the WebSphere administrative console as an administrator.
    2. In the left navigation, click Users and Groups > Manage Groups.
    3. Select admingroup and then click the Members tab.
    4. If you don't see the user you want to grant permissions to already listed, click Add
Users and complete the required fields.

For more
information about giving a user access to a case solution, see Planning for security in the development environment .

## Procedure

To manage access to process apps, case templates, or toolkits, complete the following
steps:

1. Select Process apps, Case solutions, or
Toolkits.
2 To manage user access
    - For a process app or toolkit, click the Details icon
    - For a case template, select Templates and then select
Details icon.
3. Select Permissions.
4. Click Add users or Add groups.
5. Search for the name of the user or group (typing two asterisks shows everyone), select the
check box for the ones you want to add, and then click Add users or
Add groups.
These users and groups are given Read access to the specified workflow
project.
6 To grant additional permissions to the specified workflow project, selectWrite or Admin for each user or group. The followingtable describes each permission level. Table 1. Permissions for users and groups Workflow Project Access Level Description Read With Read permission, a user can do these things: Write With Write permission, a user can do these things: Admin With Admin permission, a user can do these things:

| Workflow Project Access Level   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Read                            | With Read permission, a user can do these things:  View the process application, toolkit, or case solution in Workflow Center. View all library items included in the process application, toolkit, or case solution in Process Designer if the user also has Read access to the repository. Open the process application, toolkit, or case template in Process Designer. Install snapshots to workflow servers in development environments. Export snapshots from Workflow Center.                                                                                                          |
| Write                           | With Write permission, a user can do these things:  Perform all the tasks associated with Read permission. Create, edit, or delete library items in the process application, toolkit, or case template if you have Read access to the project and repository. Create process application, toolkit, or case template snapshots and edit snapshot properties in Workflow Center. Archive snapshots in a process application or case template. Create and archive branches for a process application or case template. Install snapshots to workflow servers in any non-production environment. |
| Admin                           | With Admin permission, a user can do these things: Perform all the tasks associated with Read and Write permission. Edit process application, toolkit, or case template settings in Workflow Center. Activate snapshots in Workflow Center. Edit track details in Workflow Center. Modify user and group access to the process application, toolkit, or case template. Archive a process application or case template in Workflow Center. By default, install snapshots to workflow servers in production environments.                                                                      |

7. To remove access for a user or group, click the Remove icon.