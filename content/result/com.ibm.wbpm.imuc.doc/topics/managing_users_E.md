# Business Automation Workflow security
roles

- Use the product launchpad for a typical installation. This method automatically creates the
authentication aliases for the CellAdmin, DeAdmin, DbUser, and DbUserXAR roles. You enter one user
ID and password for both the DbUser role and the DbUserXAR role.
- Use the BPMConfig command. This method requires that you specify theauthentication aliases for the CellAdmin, DeAdmin, DbUser, DbUserXAR, and ProcessCenterUser roles.
    - The ProcessCenterUser role is used for online workflow servers.
    - You specify the authentication alias for the CellAdmin role only if the
BPMConfig command is also being used to create the profile. If you use the
BPMConfig command on existing profiles, the CellAdmin role's authentication alias
is already configured.
    - When you use this method, you can specify any of the other roles as needed for your
environment.
- Use the administrative console's Deployment Environment wizard. This method requires that youspecify the authentication aliases for the DeAdmin, DbUser, DbUserXAR, and ProcessCenterUser roles.

- The ProcessCenterUser role is used for online workflow servers.
- You enter one user ID and password for both the DbUser role and the DbUserXAR role.
- When you use this method, you cannot specify any other roles as needed for your
environment.
- Use the manageprofiles command-line utility.

- You can specify the CellAdmin role's authentication alias only in the
manageprofiles
-adminAliasName parameter.
- The deployment environment is created after profile creation, so there are no deployment
environment-level authentication aliases to configure during profile creation.
- Using the Profile Management Tool.

- The Profile Management Tool automatically associates the CellAdmin role to the CellAdminAlias
authentication alias. It does not allow you to specify a different authentication alias.

- Each authentication alias only contains only one user ID and password.
- Each authentication alias can be mapped to one or more roles.
- Each scenario may require more than one role to complete the scenario.
- The following roles require additional stepswhen you update the role to an authentication alias mapping:
    - BPMAuthor - The BPMAuthor user must be a member of either
the tw\_admins or tw\_authors groups.
    - CellAdmin - Add the user to the administrator role in
WebSphere® Application
Server and to the groups defined as the admin and
author groups in Business Automation Workflow. The groups are either the
tw\_admins and tw\_authors defaults, or the groups defined by the bpmAdminGroup properties and
bpmAuthorGroup if the groups have been modified. For more information about the administrator role
in WebSphere Application
Server, see Security planning overview. If the password is changed, ensure that you
follow all of the steps listed in the topic Changing IBM Business Automation Workflow passwords.
    - DEAdmin - Add the user to
the administrator, deployer and operator roles in WebSphere Application
Server and to
the groups defined as the admin and author groups in Business Automation Workflow. The
groups are either the tw\_admins and tw\_authors defaults, or the groups
defined by the bpmAdminGroup properties and bpmAuthorGroup if the
groups have been modified.
    - SCADeploymentUser - Add the
user to the deployer and operator roles in WebSphere Application
Server.
    - EmbeddedECMTechnicalUser - The technical user musthave the WebSphere ApplicationServer administrator role. There must be an authorized user assigned to this role at every point in theruntime process. Authorization in the BPM document store refers to unique userIDs, so a user with the same name is not considered the same user. This is important if you intendto delete and recreate a user, or switch to a different user registry. A user assigned to thisrole is configured with the following permissions for an embedded environment: For an external Content Platform Engine configuration, ensure the user assigned to theEmbeddedECMTechnicalUser role is configured as For an external Content Navigator configuration, ensure the user assigned to theEmbeddedECMTechnicalUser role is configured as See Administering the technical user for the BPM document store .

A user assigned to this
role is configured with the following permissions for an embedded environment:

        - Domain administrator for the embedded document store
        - Object store administrator for the target object store
        - Administrator for the embedded Content Navigator

For an external Content Platform Engine configuration, ensure the user assigned to the
EmbeddedECMTechnicalUser role is configured as

        - Domain administrator or GCD administrator
        - Object store administrator for the target object store

For an external Content Navigator configuration, ensure the user assigned to the
EmbeddedECMTechnicalUser role is configured as

        - Administrator for Content Navigator

1. Log in to the administrative console.
2. Click Servers > Deployment
Environments > Deployment Environment
Name > Related Items > Authentication Aliases.

To make changes to the authentication alias, see Modifying authentication aliases.

| IBM Business Automation Workflow Required roles   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CellAdmin                                         | The cell administrator is the primary administrator at the WebSphere Application Server level. A user assigned to this role during installation and configuration has the following characteristics and capabilities: Has authorization in all deployment environments Can assign other administrator roles Is responsible for the administration of the cell and topology Has access to all interfaces, enabling users to alter or delete all types of available library items and assets, including process applications and toolkits This role also enables administration of workflow servers, performance data warehouses, and internal users and groups   Note: If you change the user ID and password in the authentication alias that is mapped to the CellAdmin role, additional steps are required when updating the role to an authentication alias mapping. See CellAdmin. The following characters are supported when specifying the cell administrator user name and password: User name characters: a-zA-Z0-9!()-.\_`~@ Password characters: a-zA-Z0-9!()-.\_`~@ |
| DeAdmin                                           | The deployment environment administrator is the primary administrator at the Business Automation Workflow level. A user assigned to this role: Has authorization in their assigned deployment environments Has administrative access to Workflow Center and Process Admin Console Has access to all interfaces, enabling users to alter or delete all types of available library items and assets, including process applications and toolkits This role also enables administration of workflow servers, performance data warehouses, and internal users and groups   Note: If you change the user ID and password in the authentication alias that is mapped to the DeAdmin role, additional steps are required when updating the role to an authentication alias mapping. See DeAdmin. The following characters are supported when specifying the deployment environment administrator user name and password: User name characters: a-zA-Z0-9!()-.\_`~@ Password characters: a-zA-Z0-9!()-.\_`~@                                                                            |
| DbUser                                            | A user assigned to this role has access to the specified database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DbUserXAR                                         | A user assigned to this role has authorization to do XA recovery. This user can also be assigned to the DbUser role.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

| IBM Business Automation Workflow Optional roles   | Description                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PerformanceAdmins                                 | Required role to view the Performance Dashboard in the Process Admin Console.                                                                                                                                                                                                                                                  |
| PerformanceDWUser                                 | Required user to run the Performance Data Warehouse.                                                                                                                                                                                                                                                                           |
| ProcessServerUser                                 | The workflow server user for JMS queues that is used to authenticate with a JMS connection.                                                                                                                                                                                                                                    |
| ProcessCenterUser                                 | This role maps to an authentication alias for a Workflow Center user who is authorized to connect from the workflow server to the Workflow Center. This user does not need any special permission in Workflow Center.                                                                                                          |
| BPMAdminJobUser                                   | A user assigned to this role has the authority to perform the actions on the product activity log (PAL) Admin code.                                                                                                                                                                                                            |
| BPMAuthor                                         | This role maps to an authentication alias for a user that requires the authority to access and deploy snapshots to the runtime workflow server and access that workflow server from the Process Inspector, which is located in IBM Process Designer.                                                                           |
| BPMUser                                           | Authentication alias for BPM UserBPC\_Auth\_Alias.                                                                                                                                                                                                                                                                               |
| BPMWebserviceUser                                 | Authentication alias for Anyonymous Webservice User.                                                                                                                                                                                                                                                                           |
| EventManagerUser                                  | This role maps to an authentication alias for a user that is used as the run-as user for the Event Manager.                                                                                                                                                                                                                    |
| RALUser                                           | Authentication alias for RAL User.                                                                                                                                                                                                                                                                                             |
| SCADeploymentUser                                 | Authentication alias used to deploy SCA applicationsNote: If you change the user ID and password in the authentication alias that is mapped to the SCADeploymentUser role, additional steps are required when updating the role to an authentication alias mapping. See SCADeploymentUser.                                     |
| SCAUser                                           | Authentication alias used by SCA to login to a secured SIBus.                                                                                                                                                                                                                                                                  |
| BPCUser                                           | Business Process Choreographer JMS authentication alias.                                                                                                                                                                                                                                                                       |
| EmbeddedECMTechnicalUser                          | If user does not specify, this role is defaulted during the installation. Note: If you change the user ID and password in the authentication alias that is mapped to the EmbeddedECMTechnicalUser role, additional steps are required when updating the role to an authentication alias mapping. See EmbeddedECMTechnicalUser. |

- Business Process Choreographer roles

Business processes have predefined roles which can be modified using the administrative console.
- Service Component Architecture role

The Service Component Architecture (SCA) has a predefined role which can be modified using the administrative console.
- Remote Artifact Loader (RAL) role

The Remote Artifact Loader (RAL) has a predefined role which can be modified using the administrative console.
- Modifying authentication aliases

Existing authentication aliases are modified from the administrative console or by using the WebSphere command-line administration tool (wsadmin) AdminConfig commands.