# Configuring security by using the Case administration client 
wizard

## About this task

You can assign permissions to different users, groups,
and roles to determine what areas and objects of a solution in a FileNet® P8 object
store that these users can access. A set of permissions is called
a security configuration. You can use the Case administration client to
create a security configuration for a solution. You can also transfer
that security configuration from a user-acceptance testing environment
or a staging environment into a production environment. The Case administration client simplifies
the process of setting up security for objects, users, groups, and
roles.

To create or make changes to a security configuration
by using the Case administration client,
you must have administrator privileges. When you first create a security
configuration, the administrators window in the security wizard is
automatically populated with an entry, which is the current user who
created the security configuration. This entry in the administrators
window cannot be removed and is required to apply the configuration.

Use
the Case administration client in
a test environment before you add those changes to a production environment.
When you have applied and tested the security configuration in the
test environment, migrate those changes to the production environment.
Using the Case administration client in
the test environment, export the security configuration. Then, in
the production environment, use the Case administration client to
import the security configuration.

The available
settings in the wizard are the results of the solution design. The
case types and roles that are displayed were created by the business
analyst in Case Builder during
the design of the solution. Based on the security plan for the solution,
you use the wizard to assign permissions for each type of case worker.
For example, you might want the case worker role to have permission
to view and update cases. You might grant another role, case auditor,
permissions to view cases only.

When you apply a security configuration for a solution, the following user permissions for the
case operations (ICM\_Operations) user are applied to the solution.

- Case type class definition: Read, Create instance, Read permissions (this object
only)
- Deployed case type folder: Write (this object only). On this object and all children:
View all properties, Modify all properties, File in folder/Annotate, Unfile from folder, Create
subfolder, Delete, Read permissions, Modify permissions, Modify owner, Change state
- Deployed solution folder: Read (this object only)

## Procedure

- To configure security for case solutions (workflow projects), see Configuring security for case solutions (workflow projects).
- To configure security for legacy case solutions, see Configuring security for legacy case solutions.

## Configuring security for case solutions (workflow projects)

### Procedure

1. Start the IBM® Workflow
Center. Enter the
following URL in the browser:  Enter the following URL in a
browser:
http://server:port/WorkflowCenter
where
server is the Workflow Center IP address or fully
qualified server name, and 
port is the
Workflow Center port
number.
2. Open the menu for the case solution (workflow project) that you want to apply the
security configuration to. Click Advanced.
3. On the Solutions page, select the solution for which to configure
security.
4. Click Actions > Manage > Security Configuration and complete the wizard
steps.

## Configuring security for legacy case solutions

### Procedure

1. Start the IBM Case
Manager administration
client. Enter the following URL in the browser:

http://server:port/navigator/?desktop=bawadmin,
where server is the IBM Content
Navigator IP address
or fully qualified server name, and 
port is
the IBM Content
Navigator
port number.
2. In the navigation tree, select a design object store and click
Solutions.
3. On the Solutions page, select the solution for which to configure
security.
4. Click Actions > Manage > Security Configuration and complete the wizard
steps.