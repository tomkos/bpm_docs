# Modifying tasks

## Before you begin

You can enable customization of task properties in a heritage human service or in a service flow
invoked by a heritage human service. To work in a service flow, you must be in the IBM® Process
Designer editor.

## About this task

You can modify task properties at levels other than the human service level, for example, at the
activity or process level. Task owners can also modify a subset of the task properties in Process Portal before or after claiming the task. Depending
on the claim status of the task at run time, the values of the task properties that you specified at
the service level can override the property values that are specified at other levels.

To model your heritage human service for task modification or service flow invoked by a human
service, use the Modify Task
 tool to add a Modify Task node to the diagram. In the implementation properties of the
node, specify the appropriate property settings for the task. The Modify Task node is not available
in a client-side human service. However, you can use the node in a service flow and call the service
flow from the client-side human service. Note that a Modify Task node should only be used in a
service flow that is called by a human service.

## Procedure

To model a service that contains a Modify Task activity, complete the following
steps:

1. Open the appropriate process application in the Designer view.
2. From the IBM Process
Designer library, select
the service flow or heritage human service that you want to work
with, and click its Diagram tab.
 To create the service, see Creating a service flow or Building a heritage human service.
3. From the palette, under Activity, use the Modify
Task
 tool to add a Modify Task node to the service diagram. Wire the node in the diagram, and
then select the node.
4. In the Implementation tab, ensure
that its activity type is set to Modify Task.
5 In the Modification tab, click atask property in the Task Modifications list,enable the property to make it editable, and specify appropriate valuesfor its settings. Due date From the Option list , select a due dateoption and specify the settings for your selection. Narrative An optional task description. Enable the narrative settings, andselect Prefix or Replace forthe narrative option. You can also use embedded JavaScript syntaxto express the narrative.Restriction: Do not use JavaScriptvariable references in task narratives if you need the data to beavailable after the task completes. Once a task is complete, Business Automation Workflow removesthe data for completed tasks to conserve space. Instead, store thedata items in another location, such as a database. Priority Enable the priority settings, and select a priority value fromthe drop-down list: Lowest , Low , Normal , High ,or Highest . Reassignment Enable the reassignment settings, and type in the name of theuser or user group to which you want to reassign the task. Status Enable the status settings and select one of the values for thetask status from the drop-down list: New , Received , Actioned , Closed , Special ,or Deleted . Subject A descriptive subject for the task at run time. Enable thesubject settings, select a type, Prefix , Suffix ,or Replace , and type in the description. Youcan also use embedded JavaScript syntax to express the subject. Forexample, <#=tw.local.mySubject#> . Use other task Enable this option, and specify the name of the task to be invokedby this task. You can also use the variable selector to choose anexisting variable from the library or use JavaScript expressions tospecify the other task.
    - Due in: Use the Increment type to
specify the expected task duration in minutes, hours, days, or months.
You can also use the variable selector next to Increment
amount to choose an existing variable from the library.
At run time, the variable reflects the appropriate value for the time
period. To avoid decreasing performance, do not set a due in value
greater than 800 hours, minutes, or days. Instead, use a JavaScript
expression to provide a Specific date. For
more information, see Specifying activity due dates.
    - Time schedule: Click the drop-down list
to select one of the options or set the time schedule to (use
default). For example, select 24x7 if
you want 24 hours a day, seven days a week to be the time period in
which the resulting tasks from the current activity are due. If you
use the default option, the work schedule specified for the activity
or process is used. For more information, see Setting the work schedule for a process.
    - Timezone: Click the drop-down list to select
the time zone that you want to apply to the task or set the time zone
to (use default). For example, you can select Eastern
Standard Time (US/Eastern) for users who work in New York.
    - Holiday schedule: Use the default setting
or click the JS button to use a JavaScript
expression. If you choose JavaScript, you can enter either a string
(or string-generated JavaScript) or JavaScript that returns a TWHolidaySchedule variable.
If you use a string, Business Automation Workflow looks
up the holiday schedule by name according to those rules. If you use
a TWHolidaySchedule variable, Business Automation Workflow assumes
that the holiday schedule is filled in appropriately.

A descriptive subject for the task at run time. Enable the
subject settings, select a type, Prefix, Suffix,
or Replace, and type in the description. You
can also use embedded JavaScript syntax to express the subject. For
example, <#=tw.local.mySubject#>.

6. Click Save or Finish Editing.