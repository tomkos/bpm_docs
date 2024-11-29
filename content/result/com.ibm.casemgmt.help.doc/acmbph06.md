# Adding an activity with an existing process

## Before you begin

Case content objects are passed by reference from a case to a process. No input mapping is
required. The reference is automatically assigned to the matching case object declaration in the
process variables. The content objects for the parent case and activity are automatically added to
the process and cannot be changed.

You must ensure that the 'Configure Case Integration with IBM® Business Automation
Workflow' task was run in the workflow
Case Configuration tool. For more information about the task, see Configuring your system for case management.

When you select the process that you want to use to implement the activity, you can choose a
specific snapshot of the workflow
project or choose the default version. If you select the default version, the process is run from
the deployed snapshot that is
designated as the default snapshot
for the application. For more information, see the topic Designating default snapshots.

By default, the Case Client
In-basket widget no longer displays work items that are created from the workflow processes that are
defined outside of a case solution project. See In-baskets for more information.

## Procedure

To add an activity with an existing workflow process:

1. In Case Builder, open the
solution that contains the case type to which you want to add the activity.
2. Click the Case Types tab.
3. Open the case type and then click Activities to open the
Activities page.
4 On the Activities page, click Add Activity > Activity with Existing Process . Note:
    - If you want to add the workflow process as a subactivity inside a container activity, open the
container activity first. Then, click Add Subactivity > Subactivity with Existing Process
5 On the General page, specify the name, unique identifier, and description,define how the activity starts, assign the activity to a set, and select a Process TaskDetails Adapter . To define how the activity starts, choose one of the following options: If you select the Discretionally option, the activity must be added to acase programmatically or by the case worker in Case Client . To select a Process Task Details Adapter, expand Process Task DetailsAdapter and choose an item from the drop-down list. By default, the ProcessTask Details Adapter page is already selected when a process activity is opened for aparent case activity. You can create your own Task Details pages from thedefault Process Task Details Adapter page and add more case widgets to the page(such as the Case Information widget).Note: When a new Task Details Adapter page is created for a workflow process activity, it must contain both the Task Toolbar widget andthe Website Viewer widget.

To define how the activity starts, choose one of the following options:

- Automatically
- Manually
- Discretionally

If you select the Discretionally option, the activity must be added to a
case programmatically or by the case worker in Case Client.

6. On the Preconditions page, define any preconditions that are required
before the activity can start.
An example of a precondition is when a document is filed in the case and the document is then
passed to the process as an initiating attachment.
7 On the Select Process page, select the process to reuse by completing thefollowing steps:

1. In the Workflow Project name field, select the name of a workflow
project in the Workflow Center.

Note: If you select the current workflow project (which has "This project" appended to the name),
the processes that are listed in the process table are those that were created by using the Designer
rather than by using Case Builder.
The local processes, which are those processes that were created by adding an activity with a new
process from Case Builder, are not
displayed in the process table.
2. Select the name of a snapshot.
Default Version is preselected as the snapshot, but you can select any other snapshot in the workflow project. Then,
the process table is populated with the processes that are associated with the snapshot. If a process is
associated with a toolkit, the toolkit name is displayed in the process table. You can view the
entire description for a process by hovering your mouse over the description.
3. To filter the list of processes in the table, type some text in the Filter
processes text area.
4 To add or edit a process, complete one of the following steps:
    - To add a process, click Open Web Process Designer to open the designer.
Add the process and create a snapshot. To view any processes that were added after you opened the Add
Activity dialog, click Refresh.
    - To edit a process, click Open Web Process Designer and edit the
process.
5. Select a process in the process table.
8 On the Map Properties page, map process data fields to caseproperties:

1. Select a process data field name from the reused process.
2. Select a case property name to map to the selected process data field name.
Properties must match the data type and number of values (single value or multivalue) of the
selected data fields. For example, string properties only match string data fields, and single value
properties only match single value data fields.
 After you select a data field name, only valid matching properties are displayed in the
Property name menu.
3. To add the selected mapping to the property map, click the plus (+) icon.

Note: Only base data types defined in the existing process are available for
mapping into a case activity property. The following data types are supported on the process side -
String, Integer, Decimal, Date and Boolean. Time, Selection and Structure data types are not
supported for mapping. For more info, see Variable types.
9. Optional: 
In the Design Comments page, add a design comment. For example, the
comment might explain the reasons that this activity was created, what the imported process does, or
how it works with the solution.
10. Click Finish to finish creating the new activity.

## Results

The process is run when the activity starts, which is based on the specified
precondition for the activity. If you edit the activity later, you can change the selected process.
However, if you select a different process, you must map properties again.

## What to do next

1. In Case Builder, hover the
cursor over the activity with the process, and then click Open the
Designer.
2. Define the process in the designer. See the topic Creating a process.

When you finish defining your process, you can commit, deploy, and test the solution.

You can also test the enhanced capability of the Case Client, which uses role-to-team
mapping to detect and display both case activities and process tasks.