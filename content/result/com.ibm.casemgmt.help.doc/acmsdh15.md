# Configuring in-baskets for roles

## About this task

- A case worker moves a work item from the common role in-basket to a personal in-basket.
- A case worker reassigns a work item to a different case worker.
- An automated processing step assigns the item to a specific workgroup.

In Case Client, this
in-basket appears on the My Work tab and contains the steps that are assigned
to that case worker.

By default, the following system properties are included in any new
personal in-basket: Subject, Time Created, Step Name.

You can assign this in-basket to a manager or
supervisor role in addition to a personal in-basket. To view and reassign work from the in-basket, a
user must have write access to the application space for the solution. You configure this access
after you deploy the solution by using the Process Configuration Console.

- assign a manager team/role to the case role
- add the non-admin user to the manager team/role that is assigned to monitor the work items

- In all in-baskets where the Assigned To property is used, the value of the
property displays only the user name and not the user ID.

## Procedure

To configure in-baskets for a role:

1. Click the Roles tab and then click the role for which you want to assign
an in-basket.
2. Select the type of personal in-basket you want displayed for the role: 

In-basket type
Description

Personal (Common): Show the common view
Displays the step properties that are common to all roles in the solution.

Personal (Role): Show a custom view for this role
Displays the step properties that are defined for the specific role to which the case worker
belongs.

If you do not want to display a personal in-basket, select Do not show common or
role personal in-baskets.
3. Optional: 
Select the work assignment check boxes to enable role members to move work items into the
personal in-basket or to reassign work items to other case workers.
4. Optional: 
To display the All Assigned Work in-basket for this role, select the Show the
in-basket that displays all assigned work checkbox.
5 Configure the properties and filters to be displayed in the in-baskets:
    1. Click the In-baskets tab and then click the in-basket that you want to
configure.
    2. Click the In-basket General tab and select the properties to be
displayed.
You can specify the order that the properties are listed, whether each property is sortable.
You can also limit the properties that are displayed so that only the most important information for
the role is displayed in the in-basket. The case worker must open the work item to view the
additional properties. 
For example, an automobile accident claim case has 25 properties. For quick access, you
select these five properties to display in the in-basket: claim number, client surname, client given
name, loss date, and estimated loss value.
Note: The sortable property that you selected and the specified order (ascending or
descending) are used by default to sort the items in the runtime in-basket. If you do not select a
property, the first column property is used as the default sort criterion. If the total number of
available work items is less than the default page size, and the in-basket contains a mix of FileNet
P8 work items and processes, the default sort works as described. If the total number of available
work items is larger than the default page size, the sorted FileNet P8 work items are listed first,
followed by the retrieved processes.
    3. Click the In-basket Filters tab. Define the filters that your users can
use to filter steps (work items in Case Client). Filtering reduces what users
see in their in-basket for this role.
For example, you might want to create a filter that is named High Priority for users to
quickly see high priority work items. If you define a filter with the operator is
like, the filter returns all items that include the filter string anywhere in the
value.
    4. Click OK.