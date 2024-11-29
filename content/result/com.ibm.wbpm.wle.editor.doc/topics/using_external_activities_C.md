# Creating an external implementation to implement an activity (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

The following steps describe how to select a custom
application as the implementation for an activity in a BPD:

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a BPD and click the activity that you want to implement
using a custom application.
3. Click the Implementation tab in the properties.
4. Under Implementation, select the User Task or System
Task option from the displayed list.
5. Click the Select button to choose
an external implementation from the library. If the
external implementation has not been created, click the New button
and follow the steps in Creating an external implementation to
create a new external implementation.
6. In the Task Header section, specify the following properties: 

Table 1. Properties in the Task Header section

Property
Action

Subject
Type a descriptive subject for the task that
is generated in IBM Process
Portal when
you run the BPD. You can also use the IBM Business Automation Workflow embedded
JavaScript syntax (for example, <#=tw.local.mySubject#>)
to express the subject.

Narrative
Type an optional description. You can also use
the Business Automation Workflow embedded
JavaScript syntax to express the narrative. Restriction: Do
not use JavaScript variable references in task narratives if you need
the data to be available after the task completes. Once a task is
complete, Business Automation Workflow removes
the data for completed tasks to conserve space. Instead, store the
data items in another location, such as a database.

Note: For the following properties (in the Priority Settings
section) you can click the JS button for an option if you prefer to
use a JavaScript expression with predefined variables to establish
the priority settings.
7. For the Priority field, click the drop-down list to select
one of the default priority codes: Very Urgent, Urgent, Normal, Low,
or Very Low.
8. For the Due In field, you can enter a value in the text
box and then choose Minutes, Hours, or Days from the drop-down list.
When you choose Days, you can use the text box after the drop-down
list to include hours and minutes in your specification.  You
also have the option of using the variable selector next to the text
box to choose an existing variable from the library. At run time,
the variable should reflect the value that you want for the time period.
Be sure to select the option that you want from the drop-down list:
Minutes, Hours, or Days.
Do not set a due in value greater
than 800 Hours, Minutes, or Days as it decreases performance. Instead,
use a JavaScript expression to directly set the due date.
9. For the Time Period field, click the drop-down list to
select one of the options. For example, select 24x7 if
you want 24 hours a day, seven days a week to be the time period in
which the resulting tasks from the current activity can be due.
Note: You can leave the Schedule, Timezone, and Holiday Schedule
fields set to (use default). If you do, the work schedule specified
for the BPD is used. See Setting the work schedule for a process for
more information.
10. For the Time Zone field, click the drop-down list to select
the time zone that you want to apply to the tasks that result from
the current activity. For example, you can select US/Pacific for
users who work in California.
11. For the Holiday Schedule field, you can leave the setting
at (use default) as described in the preceding note
or you can click the JS button if you prefer to use a JavaScript expression.
Each Holiday Schedule is made up of a list of Dates.  If
you choose JavaScript, you can enter either a String (or String-generated
JavaScript) or JavaScript that returns a TWHolidaySchedule variable.
If you use a String, then Business Automation Workflow looks
up the holiday schedule by name according to those rules. If you use
a TWHolidaySchedule variable, then Business Automation Workflow assumes
that the holiday schedule is filled in appropriately. (Go to the System
Data toolkit and open the TWHolidaySchedule variable to view its parameters.)
12. Click the Data Mapping tab in the properties. Because
you added the input and output parameters for the external implementation
when you created it, the Data Mapping tab for the activity in the
BPD should include those parameters.
Under Input
Mapping, click the auto-map icon in the upper-right corner, and then
click the auto-map icon in the upper-right corner of the Output Mapping
section. For more information about mapping variables, see Business objects and variables.
13. Click Save or Finish Editing.