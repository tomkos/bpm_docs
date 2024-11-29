# Implementing activities in a BPD (deprecated)

## About this task

| Implementation option   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | See...                                                                |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| User Task               | Select this option if an activity is to be started or completed by a user (human performer). For example, if an activity requires that managers enter employee data, choose  User Task and select or create a client-side human service or a heritage human service to implement the task.                                                                                                                                                                                                              | Building a client-side human serviceBuilding a heritage human service |
| System Task             | Select this option if an activity is to be completed by an automated system or service. For example, if an activity requires integration with an external system, such as a database, choose System Task and select or create an Integration service to implement the task.                                                                                                                                                                                                                             | Service types                                                         |
| Decision Task           | Select this option when you want a decision or condition in a business rule to determine which process implementation is started. For example, if you want Process Designer to implement an activity when a condition evaluates to true, choose Decision Task and select or create a decision service to implement the task.                                                                                                                                                                            | Service types                                                         |
| Script                  | Choose this option if you plan to create a script to implement an activity. A Script activity runs a Java™ script.                                                                                                                                                                                                                                                                                                                                                                                      | Using complex variables and lists in JavaScript                       |
| Subprocess              | Use this option to encapsulate logically related steps within a parent process. Steps in a subprocess can directly access business objects (variables) from the parent process. No data mapping is required. However, unlike a linked process, a subprocess can be accessed and instantiated only from the parent BPD, and it is not reusable by any other process or subprocess. Therefore, use a subprocess for those implementations that are limited to a single business process definition (BPD). | Modeling subprocesses                                                 |
| Linked Process          | You can implement an activity by using a linked process. Linked processes encapsulate logically related steps within a process while retaining the high-level view of the parent process. Linked processes differ from subprocesses because they can be accessed and instantiated from processes other than a single parent process.                                                                                                                                                                    | Working with linked processes                                         |
| Event Subprocess        | Use this specialized subprocess to model event-handling logic for a process or subprocess. It is triggered upon occurrence of a configured start event, and it is not connected to other steps through a sequence flow. It has access to the business objects (variables) of its parent process, and can encapsulate steps that use those variables. When triggered, an event subprocess can either interrupt the execution of its parent or can run in parallel.                                       | Modeling event subprocesses                                           |
| None                    | Select this option if you are not ready to associate an implementation. Use this option to create a temporary placeholder activity in your process diagram until an implementation is available. If you run a process that includes an activity with this option selected, the task completes immediately after it starts.                                                                                                                                                                              |                                                                       |

## Procedure

To select an implementation type and set its properties,
complete the following steps:

1. Open the desktop Process Designer (deprecated).
2. Open a process application that contains a BPD.
3. Select the activity that you want to use in the BPD diagram,
and then go to the Implementation properties.
4. Under Implementation, select an option
from the displayed list. For example, choose  User
Task if the implementation for the current activity is
a human service with a coach. (The preceding table describes each
available option.) Tip: 
To implement the task as either a client-side human service or a heritage
human service, see Implementing a BPD activity as a human service.
5. Click Select to choose the implementation
from the library. If the implementation does not yet exist,
click New to create it. (The previous table
provides instructions for creating implementations.)If
you choose User Task, System Task, or Decision Task for
your implementation option, you can specify extra properties, as outlined
in the following steps.
6. (System Tasks and Decision Tasks only) Select Delete
task on completion if you want to run an automated service
that does not require routing. When you select this check box, audit
data for the task is not retained by Workflow Server. By
default, this option is disabled.
7. (User Tasks, System Tasks, and Decision Tasks only) In
the Task Header section, specify the following
properties: 
Table 2. Properties in the Task Header
section

Property
Action

Clean State 
Select to clear the runtime execution state
of an activity after it is complete. By default, this option is disabled.
Enable this option only when you do not want to store execution
data (such as variable values) for viewing after the process finished
execution.

Subject
Type a descriptive subject for the task that
is generated in IBM® Process
Portal when
you run the BPD. You can also use the Business Automation Workflow embedded JavaScript syntax (for example, <#=tw.local.mySubject#>)
to express the subject.

Narrative
Type an optional description. You can also use
the Business Automation Workflow embedded JavaScript syntax to express
the narrative. Restriction: Do not use JavaScript variable references in task
narratives if you need the data to be available after the task completes.
When a task is complete, IBM BPM
removes the data for completed tasks to conserve space. Instead, store
the data items in another location, such as a database.
8 (User Tasks, Decision Tasks and System Tasks only) In the PrioritySettings section, specify values as needed. Tip: If you prefer to use a JavaScript expressionwith predefined variables to establish the priority settings, click JS foroptions.
    1. Under Priority, select one of
the default priority codes from the list: Highest, High, Normal (the
default), Low, or Lowest.
    2. Under Due In, enter a value in
the text box and then choose Minutes, Hours,
or Days from the list. When you choose Days,
you can use the text box after the list to specify hours and minutes.
You can also use the variable selector next to the text box
to choose an existing variable from the library. At run time, the
variable reflects the specified value for the time period. Select
the required option from the list: Minutes, Hours,
or Days.Do not set a due in value greater
than 800 Hours, Minutes, or Days as it decreases performance, and
the calculation for the due date takes a long time. Instead, use a
JavaScript expression to directly set the due date and avoid the costly
calculation that includes multiple checks for the time or holiday
schedule. To set the due date, click JS, and
use the variable selector next to the text box to pass either an existing Date variable,
or create a new one, for example new TWDate('2020-12-01 09:08:06.02').Note: When
you pass a fixed due date, Business Automation Workflow ignores
any time or holiday schedule.
    3. Under Schedule, select an option
from the list. For example, select 24x7 if
you want 24 hours a day, seven days a week to be the time period in
which the resulting tasks from the current activity can be due.
You can leave the Schedule, Timezone,
and Holiday Schedule fields set to (use
default). If you do, the work schedule that is specified
for the BPD is used. For more information, see Setting the due
date and work schedule for a BPD.
    4. Under Timezone, select the time
zone that you want to apply to the tasks that result from the current
activity. For example, you can select US/Pacific for
users who work in California.
    5. Under Holiday Schedule, leave
the setting at (use default) as described in the
preceding note, or click JS if you prefer to
use a JavaScript expression.
Each holiday schedule is made up of a list of dates. If
you choose JavaScript,
you can enter either a String (or String-generated JavaScript) or a JavaScript that returns a TWHolidaySchedule variable.
If you use a String, Business Automation Workflow looks
up the Holiday Schedule by name according to those rules. If you use
a TWHolidaySchedule variable, Business Automation Workflow assumes
that the holiday schedule is appropriately specified. (Go to the System
Data toolkit and open the TWHolidaySchedule variable
to view its parameters.)
9. (User Tasks only) In the Processing Behavior section,
select Automatically flow to next task to run
the next task in the sequence automatically  if the task is assigned
to the same user.  The coach of the next activity is displayed to
the user. Do not use this option to model all user screen flow interactions
at the process level or the token might time out, causing the user
to go to the task list  instead of the coach. See Automatically starting the user's next task.