<!-- image -->

<!-- image -->

<!-- image -->

# Identifying case management users

## About this task

The groups or roles that are described in this task cover the main case management functions. If
you are extending your system, you might need to create or designate more groups or roles.

- Assign permissions to LDAP groups rather than individual users.
How you assign users and groups can vary based on the directory service
provider in your environment. Use the documentation that is provided
for your directory server to identify case management groups.
- Create a case management master group to use for assigning access
to object stores when you create the object store. Give this group Use
object store permission. With this method, you can grant
new users access to the object store by adding them to the master
group. This approach can prevent issues with changing security on
an established object store. For development environments, the master
group can be #AUTHENTICATED-USERS. For a production
environment, more controlled security is needed.
- Add the user associated with the ECM Technical User
(EmbeddedECMTechnicalUser) role, as a member of the Solution
administrators user group. The project and solution migration process configures this
user as the owner of solution artifacts. For more information about the ECM Technical User
(EmbeddedECMTechnicalUser) role, see Business Automation Workflow security roles. For
more information about the Solution administrators group, see Planning for security in the development environment .

## Procedure

To assign groups:

1. In your directory server, find the configured realm for
the Content Platform Engine instance
that you are using with IBM® Business Automation
Workflow.
2. Identify the following groups: 
Table 1. Groups for business analysts and solution administrators

Group
Description

Business analysts
Responsible for designing the solution in Case Builder and the user interface
application in Case Client.
Business analysts work in a development environment to develop and test the solution. To create and
edit solutions, and design the application, business analysts need access to objects in the design
object store. In addition, the business analysts need access to the target object stores and the
isolated region to deploy, test, and customize the solutions.

Solution administrators
Responsible for managing project areas. Responsible
for copying and deploying solutions, and for creating templates from
solutions. Responsible for managing roles.
3. Ensure that both groups also have the following permissions:

Table 2. Group permissions

Component area
Permissions to assign

IBM
FileNet® P8 Domain
GCD
Both the business analyst and the solution administrator
groups require Global Configuration Domain (GCD) administrator rights.
This role is referred to as the FileNet P8
Platform Administrator
in FileNet P8
Platform documentation.

Content Platform Engine
Add to Configuration groups rights to enable deployment, which requires
creation of rosters, queues, applications spaces, and roles. Case workers can view the list of
roles for a solution for reassigning work only if the user or group has access to the application
space. You can add the users to the SysAdminG group or manually add the users to the access list of
the application space.
If a business analyst must run Process Administrator to update work
items, then also add the business analyst to the Process Administrator group. Tip: If a
roster does not have users or groups that are assigned to it, then all users can access the roster.
That is, all users have query and create rights. Users must have create rights to start a workflow.
If a queue does not have users or groups that are assigned to it, then all users can access the
queue. That is, all users have query and process rights.

Object store permissions
For the business analysts group, assign Use
Object Store level permission for the design object store and target
object stores.

IBM
FileNet Process Designer
Business analysts must belong to the Workflow
System Configuration group to edit workflows in the IBM
FileNet Process Designer application
from Case Builder.
You can configure this group in IBM Administration Console for
Content Platform Engine when
you configure the target object store workflow system.