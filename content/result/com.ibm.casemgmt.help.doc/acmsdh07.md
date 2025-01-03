# Adding activities

A case activity is a automated set of actions that are performed on a case instance to
help drive it to a successful outcome. These activities are orchestrated by the case or case worker
in the Case Client and can
perform various functions depending on its type, including launching a process, adding a to-do list
to a case at the appropriate time, and acting as a container for other activities to control when
they are available.

Your case projects can include activities that start processes. These processes can use all the
capabilities described in Business process management as well as additional integration features that are available
when these processes run in a case activity.

## About this task

Instead of adding a new activity, you can create an activity from a business process workflow if
your administrator configured access to a business process management system.

Activities are shown in two views on the Activities page: priority and sets.
In the priority view, the activities are displayed with required activities first, optional
activities are next, and discretionary activities are last. In the sets view, the activities are
displayed by whether the activities are mutually exclusive, all-inclusive, or neither.

## Procedure

To add an activity:

1. After you create a case type, open the Activities page and click
Add Activity to choose the type of activity to add.

Activity type
Description

Activity with New Process
Adds an activity with a new workflow process. For more information, see Adding an activity with a new process.

To-do Task
Adds a task that provides a checklist of items that must be completed or information that
must be collected for a case type. A to-do task does not have an associated workflow.

Container Activity
Adds a container in which you then add subactivities. The subactivities can be activities,
to-do tasks, or even other container activities.

Activity with Existing FileNet® P8
process
Adds an activity based on an existing FileNet P8 process. For information about
creating these processes and making them available for reuse in Case Builder, see Adding an existing FileNet P8 process as an activity.

Activity with Existing Process
Adds an activity that is based on an existing workflow process. For more information, see
Adding an activity with an existing process.

Activity with New FileNet P8 Process
Adds an activity for which you define the process in FileNet P8
IBM®
FileNet Process Designer. For information
about defining the process, see Building new FileNet P8 processes to complete activities.

Activity with Existing FileNet P8 process
Adds an activity based on an existing FileNet P8 process. For information about
creating these processes and making them available for reuse in Case Builder, see Adding an existing FileNet P8 process as an activity.
2 On the General page, specify a name and unique identifier for theactivity. The unique identifier is added to the name that you entered for the activity. The name ofan activity must conform to the following rules:
    - Begin with an alphabetic character
    - Can contain letters, digits, underscores, or spaces
    - Can have up to 64 characters although character limits might vary depending on your
language
    - Not use F\_ or two tilde (~) characters as the first two characters
    - Be unique among workflow definitions in the production environment
    - Not use the same name as a role in the same solution
3 On the General page, define the behavior of the activity:

1. Define how the activity will start by specifying Automatically,
Manually, or Discretionally.
If you select Discretionally, the activity must be added to a case
programmatically or by the case worker in Case Client.
2. Optional: 
Add the activity to a set.
In the Add Activity window, you can add the activity only to an existing
set. You can create new sets in the Manage Sets window or drag activities
around to different sets in the Activities page. Activities can belong to a
mutually exclusive set, an all-inclusive set, or no set. 
Mutually exclusive set
If the activity is part of a mutually exclusive set, the user can complete only one of the
activities in that set. 
All-inclusive set
If the activity is part of an all-inclusive set, the user must complete all the activities in
that set.

Activities that belong to a set must have preconditions.
3. In the Process Task Details Adapter drop-down list, choose an
item. By default, the Process Task Details Adapter page is already selected when a BPM process task
is opened for a parent case activity. You can create your own Task Detail pages from the default
Process Task Details Adapter page and add additional case widgets to the page (such as the Case
Information widget). 
acmsdh18

Note: When a page is created for a BPM process activity, it must contain both the Task Toolbar
widget and the Website Viewer widget.
4 On the Preconditions page, define any preconditions that are requiredbefore the activity can start. You can have no preconditions, or you can have the activity start only if one of the followingpreconditions are met: You can also define a property expression for any of the precondition types. If you want theactivity to start when one or more documents is added, select A document is filed in thecase in the case precondition and specify an additional property expression. For example, you might require that a loan application document is added to the case beforethe loan application activity can start.

- When one or more documents are added to the case
- When a condition is met on a property
- When a property is modified

If you want the
activity to start when one or more documents is added, select A document is filed in the
case in the case precondition and specify an additional property expression.

5. On the Activities Properties page, add and configure the properties that
are associated with this activity.

Activity properties provide a mechanism for tracking activity-specific information beyond the
scope of the activity. For example, you might have a repeating activity to process witness
statements. Each instance of a witness statement activity has properties to record information, such
as who processed the witness statement and the date that the statement was taken. This information
can be maintained through the activity properties rather than through case properties. 
For to-do tasks, which are displayed as checklists, all associated properties are shown as to-do
items in the default view.
You can create properties for an activity or reuse existing properties from the solution or
object store. When you create an activity property, that property becomes one of the solution
properties and can be used as a property for a case type or other activities. You can also use an
activity property in an in-basket.
6. Optional: 
On the Design Comment page, add a design comment that explains, for
example, the reasons that this activity was created, or what the imported process does, or how it
works with the solution.
7. Click OK.

## What to do next

To create steps for an activity, click the Edit steps icon. To
customize the view for a to-do task, click the Open To-do View Designer
icon.

- Activities in solutions

An activity represents a specific operation that is performed as part of a case. An activity can consist of one or more steps that must be completed to complete the activity. Alternatively, an activity can be a simple checklist item that is not associated with a workflow.
- Activity preconditions

For manual and automatic activities, you can specify preconditions that must be met before the activity is ready to start. Activities can start automatically after all preconditions are met or manually by a user after all preconditions are met.
- Activity initiation

A case type can contain many activities, and each activity can be started by using one of three methods. The decisions that you make when you design an activity affect what a case worker can view and edit in Case Client when the activity starts.
- Activity states

Activities have different states that are displayed to the case worker in the Case Client. For example, a manual activity that has met all of its preconditions is in the Ready state. An automatic activity that has met all of its preconditions is in the Started state. Depending on how the activity is defined it might require to be started manually by the case worker.
- Adding activities with workflow processes

IBM Business Automation Workflow provides an integrated workflow environment for authoring, deploying, monitoring and maintaining solutions that contain both cases and business processes. In this environment, process instances interact with case and activity properties in a first-class manner.