<!-- image -->

<!-- image -->

<!-- image -->

# Planning for security in the development environment

When you identify the Content Platform Engine object stores that are
used for case management, you must identify the users that have access to these object stores. Your
users must have the appropriate access permissions on the object stores. The permissions that are
required vary depending on the user roles.

In the development environment, you assign permissions to users and groups for designing,
testing, and administering case solutions. Business analysts design and test solutions. Solution
administrators manage the solution environment, including copying solutions and resetting test
environments.

The groups or roles that are described in this task cover the main case management functions. If
you are extending your system, you might need to create or designate more groups or roles.

- Assign permissions to LDAP groups rather than individual users. How you assign users and groups
can vary based on the directory service provider in your environment. Use the documentation that is
provided for your directory server to identify case management groups.
- Create a case management master group to use for assigning access to object stores when you
create the object store. Give this group Use object store permission. With
this method, you can grant new users access to the object store by adding them to the master group.
This approach can prevent issues with changing security on an established object store. For
development environments, the master group can be #AUTHENTICATED-USERS. For a
production environment, more controlled security is needed.
- Add the user associated with the ECM Technical User
(EmbeddedECMTechnicalUser) role, as a member of the Solution
administrators user group. The project and solution migration process configures this
user as the owner of solution artifacts. For more information about the ECM Technical User
(EmbeddedECMTechnicalUser) role, see Business Automation Workflow security roles.

For more information about EmbeddedECMTechnicalUser user, see Business Automation Workflow security roles .

1. In your directory server, find the configured realm for the Content Platform Engine instance that you are
using with IBM® Business Automation
Workflow.
2. Identify the groups.The following table shows sample groups for users who are designing and
administering solutions.
Table 1. Sample groups
for business analysts and solution administrators

Group
Description

Business analysts
Responsible for designing solutions in Case Builder and user interface
applications in Case Client.
Business analysts work in a development environment to develop and test solutions. The require
access to objects in the case management design object store to create and edit solutions, and
create client application pages. They must also have access to the Workflow Center repository, a case
process configuration, and workflow definitions of a
solution.Business
analysts require permission to log in to the default IBM Content
Navigator desktop.
When IBM Content
Navigator is installed, the IBM Content
Navigator
administration desktop with the ID admin is set as the default. When IBM Business Automation
Workflow is configured, the
default desktop is changed to the default IBM Business Automation
Workflow desktop with the ID
baw. If you do not change this configuration, business analysts have the appropriate
access to use the Page Designer application. If you add security restrictions to the desktop, you
must ensure that business analysts can log in to the baw desktop under
those security restrictions. If you change the default desktop, ensure that the business analysts
can log in to the updated default desktop. For example, if you change the default desktop back to
the IBM Content
Navigator
admin desktop, then the business analysts must be granted IBM Content
Navigator
administrator access.
In addition to ensuring that security is correctly assigned to the
default desktop baw, the Page Designer application requires the default desktop in
IBM Content
Navigator
with the case management plug-ins enabled. If these plug-ins are not enabled, the menu and toolbar
button actions do not load correctly in the Page Designer of Case Builder.
Business analysts
must be a member of the tw\_authors group.

Solution administrators
Responsible for managing project areas, copying and deploying solutions, and
creating solutions from templates. The user that you specify in the Case configuration tool as the Content Platform Engine domain user must have the
permissions that are specified for this group.Solution administrators control any management or
destructive aspects of solutions. For example, solution administrators can delete a solution along
with all its artifacts. You can also grant this role permission to reinitialize the case management
development environment, which results in the removal of all solutions that are deployed within the
development environment. To delete cases and reset the development environment, solution
administrators must have GCD domain administrator rights, administrator rights on the target object
store, and workflow system Configuration group rights.
Solution administrators must be a
member of the tw\_admins group and have access to the Workflow Center
repository.
3. Ensure that both groups also have the following permissions:

| Component area               | Permissions to assign                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IBM FileNet® P8 Domain GCD   | Both the business analyst and the solution administrator groups require Global Configuration Domain (GCD) administrator rights. This role is referred to as the FileNet P8 Platform Administrator in FileNet P8 Platform documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Content Platform Engine      | Add to Configuration groups rights to enable deployment, which requires creation of rosters, queues, applications spaces, and roles. Case workers can view the list of roles for a solution for reassigning work only if the user or group has access to the application space. You can add the users to the SysAdminG group or manually add the users to the access list of the application space. If a business analyst must run Process Administrator to update work items, then also add the business analyst to the Process Administrator group. Tip: If a roster does not have users or groups that are assigned to it, then all users can access the roster. That is, all users have query and create rights. Users must have create rights to start a workflow. If a queue does not have users or groups that are assigned to it, then all users can access the queue. That is, all users have query and process rights. |
| Object store permissions     | For the business analysts permissions, see Table 3 and for solution administer group permissions, see Table 4.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| IBM FileNet Process Designer | Business analysts must belong to the Workflow System Configuration group to edit workflows in the IBM FileNet Process Designer application from Case Builder. You can configure this group in IBM Administration Console for Content Platform Engine when you configure the target object store workflow system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

| For this component                       | Configure these permissions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Design object store                      | In the New Object Store wizard, configure users and groups who have basic nonadministrative access. The Case administration client automatically grants the following rights when a user or group is added to a project area: AccessLevel.MAJOR\_VERSION\_DOCUMENT\_AS\_INT  AccessLevel.WRITE\_FOLDER\_AS\_INT  AccessRight.WRITE\_ACL\_AS\_IN  Major Versioning level plus Publish, Modify Permissions, and Create subfolder (Inherit Only) rights for this object and all children Delete for all children, but not this object. For the Solutions folder, View Properties plus the right Create subfolder for all authenticated users |
| Target object store                      | For the target object store that is referenced by the Project Area where this business analyst is assigned, give the business analyst’s security group Administrators rights in the New Object Store wizard or in the Security Script wizard.                                                                                                                                                                                                                                                                                                                                                                                   |
| Content Platform Engine                  | Add the business analyst’s security group to the workflow system Configuration group to enable deployment, which requires creation of rosters, queues, applications spaces, and roles. If a business analyst must run Process Administrator to update work items, then also add the business analyst group to the workflow system Administrator group.Tip: If you do not assign users or groups to your queues and rosters, then all users automatically have all rights to the rosters and queues. This level might be appropriate in your development environment.                                                            |
| IBM Business Automation Workflow server. | Add the business analyst’s security group to the tw\_authors group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

| For this component                       | Configure these permissions                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Design object store                      | In the New Object Store wizard or in the Security Script Wizard, configure the solution administrator’s security group as an Administrator.                                                                                                                                                                                                                              |
| Target object store                      | For the target object stores, give the solution administrator’s security group Administrator rights in the New Object Store wizard or in the Security Script wizard.                                                                                                                                                                                                     |
| IBM FileNet P8 Domain GCD                | The solution administrator’s security group also requires Global Configuration Domain (GCD) administrator rights. This role is referred to as the IBM FileNet P8 Administrator in IBM FileNet P8 documentation.                                                                                                                                                          |
| Content Platform Engine                  | Add the group to the workflow system Configuration groups rights to enable deployment, which requires creation of rosters, queues, applications spaces, and roles.Tip: If you do not assign users or groups to your queues and rosters, then all users automatically have Process Administrator rights. This level might be appropriate in your development environment. |
| IBM Business Automation Workflow server. | Add the solution administrator’s security group to the tw\_admins group.                                                                                                                                                                                                                                                                                                  |

| Group               | Description                                                                                                                                                                                                                                                                                                                                 |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Case viewers        | Have only read-only access to cases.                                                                                                                                                                                                                                                                                                        |
| Case initiators     | Create new cases. They might also be able to view case properties. For some applications, this group might be a superset of caseworker, or might be combined with caseworker .                                                                                                                                                              |
| Case workers        | View and update cases and case-related objects. They cannot create cases, delete cases, or change the permission or the owner of case-related objects.                                                                                                                                                                                      |
| Case administrators | Control all case-related objects, including case folders, subfolders, comments, and tasks. Can view the list of roles for a solution for reassigning work only if the group has access to the application space in Content Platform Engine. This group does not necessarily have full control of documents that are associated with a case. |