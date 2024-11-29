# Securing process applications

IBM Business Automation Workflow defines
a fine-grained authorization model that uses groups, roles, and teams.

## Groups

In the JavaScript API for processes and service flows (which is described in the topic JavaScript API in
processes and service flows), the word role and the object TWRole are synonyms for the
word group. They have nothing in common with the roles authorization model described in the
following Roles section.

## Roles

- Administrators
- Catalog managers
- Customers
- Anonymous

Different roles can be assigned different levels of security, and the security access of
individuals, or groups of individuals, can be controlled by assigning them to specific
roles.

- WebSphere®
Application Server administrative
roles. See Administrative roles.
- Business Automation Workflow application
Java EE roles. See IBM Business Automation Workflow application Java EE roles.
- Business Automation Workflow security
roles that allow configuring system accounts. See Business Automation Workflow security roles.

## Teams

| Task                                                                                         | Interface                    | To learn more                                          |
|----------------------------------------------------------------------------------------------|------------------------------|--------------------------------------------------------|
| Granting access to the repository                                                            | Workflow Center              | See Managing access to the Workflow Center repository. |
| Binding users to teams during process development                                            | Designer in Process Designer | See Creating a team.                                   |
| Defining who has managerial authority over a team                                            | Designer in Process Designer | See Defining team managers.                            |
| Using services to define dynamic teams                                                       | Designer in Process Designer | See Using services to define dynamic teams.            |
| Assigning an activity to a team                                                              | Designer in Process Designer | See Assigning teams to BPD activities.                 |
| Adding users and groups from a user registry to Business Automation Workflow security groups | Process Admin Console        | See Creating and managing groups.                      |
| Modifying existing teams at run time                                                         | Process Admin Console        | See Configuring runtime teams.                         |

## Users

| Task                                                                | Interface    | To learn more                                |
|---------------------------------------------------------------------|--------------|----------------------------------------------|
| Restricting inactive users from participating in runtime operations | Command line | See Runtime user availability and lifecycle. |

## User registry

IBM Business Automation Workflow
authorization relies on users and groups that are defined in the user registry. A user registry is an architectural layer that manages users and groups in WebSphere
Application Server. LDAP servers are
the most commonly used source of user and group data storage. Although IBM Business Automation Workflow can utilize a
stand-alone LDAP registry, you should use a federated repository configuration that can comprise
multiple LDAP repositories. For more information, see Authentication of users.

IBM Business Automation Workflow does
not lock user accounts after a configurable number of failed authentication
attempts. End user accounts are managed in a user repository (typically
LDAP connected to Federated Repositories). IBM Business Automation Workflow is
just one of many client systems to the user repository. The user repository
is the system of records for the user accounts and therefore defines
rules such as password lock policy. For IBM Security Directory
Suite,
you can read more about password policies at Additional information on password policy.

The following diagram illustrates how WebSphere
Application Server and applications access
user and group data in the user registry.

The following diagram illustrates how the user registry works for member
management APIs.

## Encrypted communication

## Authorization

Authorization roles are used to determine the actions that a user can take on objects, such as
processes, tasks, and user data. For information about how to protect the REST services, coach
views, or external implementations that call a service flow, see step 6 in Creating a service flow. For information about how to protect REST APIs, see Authorization for Workflow REST APIs.