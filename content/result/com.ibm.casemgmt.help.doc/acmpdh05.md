# Disassociating a role’s primary queue

## About this task

In IBM
FileNet Process Designer, for example, if the supervisor role in
your solution views work assignments but does not complete work items you can disassociate the
primary queue for the supervisor role.

## Procedure

To disassociate a primary queue for a role:

1. In a stand-alone IBM
FileNet Process Designer, open the solution for
editing the FileNet P8 activity workflow.
2. Click
View > Roles.
3. Select the role and click the Custom Attributes tab.
4. Select the CB\_PrimaryQueue attribute and click the Delete
icon.
5. Optional: 
Assign other in-baskets to view work on the Select In-baskets and Members
page by clicking the Modify icon. If a role does not have
CB\_PrimaryQueue attribute, and when the solution is promoted or when the security manifest
configuration is applied or manage roles in Case Client is performed, the IBM Business Automation
Workflow process team synchronization is skipped for the
role.