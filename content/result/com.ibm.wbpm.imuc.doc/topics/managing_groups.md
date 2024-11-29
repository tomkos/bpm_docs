# IBM Business Automation Workflow group
types

Many customers define their groups in the Lightweight Directory
Access Protocol (LDAP). IBM Business Automation Workflow accesses
the groups through federated repositories.

- WebSphere
Application Server administrative
roles.
- IBM Business Automation Workflow application
Java EE roles.
- IBM Business Automation Workflow security
roles
- Internal groups with specific privileges. For example, a group
that is defined using the bpmAdminGroup security
configuration property. See Security configuration properties.

IBM Business Automation Workflow group
management manages several types of IBM Business Automation Workflow private
groups. In this context, private means that the groups are
not visible outside of the IBM Business Automation Workflow environment,
not available in LDAP, and not visible to WebSphere
Application Server. Such groups
cannot be used for Java Platform, Enterprise Edition or WebSphere
Application Server administrative
role assignment.

- Security group - A group that was replicated from the user registry.
In the diagram in this topic, the user registry is referred to as
the Federated Repositories. The group might be defined in either the
file registry or LDAP and is stored in the BPMDB table.
- Team - There is an entry for each team in the BPMDB table. Teams are defined in
either process applications or toolkits. Teams can have static member lists that include users or
groups, or they can use a service to calculate their members. Teams can be used to expose process
application artifacts by, for example, controlling who can start a business process or human
service. Process application administrator teams
(referred to as Portal Admin Team in the desktop Process Designer) can be defined to administer process
instances of the process application. Teams can be used in task assignments. Team managers can
be defined as a team, which makes it possible for you to create a hierarchy. Team managers can
assign work from one team member to another team member and can view dashboards check their team's
performance.
- Ad hoc group - If a team calculates its members using a service,
the service returns a set of users and groups. This list of users
and groups is then persisted as a reusable entry in the database.
Ad hoc groups are immutable. Ad hoc groups can also be created by
using a list of users or a list of groups (deprecated).
- Internal group - Internal groups are created by using the Process Admin Console or anapplication programming interface. They are not process-application specific, but can be reusedacross multiple process applications. They are similar to LDAP groups, but are Note: Internal groups are also created implicitly during a processapplication deployment if the snapshot includes security groups that do not exist on the targetsystem. If later on such security groups are created in the connected user registry the group typecan be migrated from internal group to security group. Use the group synchronization REST API/system/groups\_sync/ (Operations REST APIs ) and set themigrate\_group\_type parameter to true .
    - Managed by IBM Business Automation Workflow
    - Writable using IBM Business Automation Workflow application program
interfaces
    - Invisible except to IBM Business Automation Workflow and its process
applications

The following diagram illustrates how IBM Business Automation Workflow group
management works with the federated repository to manage the various
types of groups.

- Grant permission to users by making them members of these groups.
For example, by adding a group from LDAP as a subgroup.
- Specify different group names in place of the default groups that
are listed below. See Security configuration properties.
- Specify groups that exist in the user registry or internal groups.

Table 1 lists the IBM Business Automation Workflow groups
that are included by default.

| Default group        | Description                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| tw\_admins            | Members of this group have full access to all interfaces, assets, servers, and security. Note: You can rename this group, but there must always be an administrator group defined. Administration of Business Automation Workflow is not possible without this group.                                                                                                                                    |
| tw\_allusers          | This group is the default lane assignment for non-system lanes when business process definitions (BPDs) are created in Process Designer. The dashboards that you create in Process Designer are available to this group by default.                                                                                                                                                                      |
| tw\_allusers\_managers | This group contains the team of managers for the tw\_allusers group. In the Team Performance dashboard in Process Portal and Heritage Process Portal, members of this group can see a dashboard for the All Users team and the sample teams that are delivered with the product. By default, the tw\_allusers\_managers group includes the tw\_admins group.                                                 |
| tw\_authors           | Members of this group have access to the Designer and other interfaces in the Process Designer, including Workflow Center. From Workflow Center, members of this group can create process applications and toolkits and control access to projects. Access to other process applications and toolkits (projects) and the assets they contain is controlled by Workflow Center repository administrators. |
| Debug                | You can use this account to restrict access to service debugging in the Inspector in the Process Designer.                                                                                                                                                                                                                                                                                               |
| tw\_eventmanager      | Members of this group have full access to historical information about Event Manager processing.                                                                                                                                                                                                                                                                                                         |
| tw\_managers          | Members of this group can see the Team Performance dashboard in Process Portal and Heritage Process Portal. To see dashboards for individual teams, the group member must also be a member of a managers team that is defined in Process Designer.By default, the tw\_managers group includes the tw\_allusers group.                                                                                      |
| tw\_portal\_admins     | Because of functionality changes in Business Automation Workflow V8, members of this group no longer have any special access rights.                                                                                                                                                                                                                                                                     |
| tw\_process\_owners    | Members of this group can see the Process Performance dashboard. By default, this group is also assigned to the ACTION\_CHANGE\_CRITICAL\_PATH Process Portal policy, which allows members to view and change the projected path of a process instance.By default, the tw\_process\_owners group includes the tw\_admins group.                                                                                |