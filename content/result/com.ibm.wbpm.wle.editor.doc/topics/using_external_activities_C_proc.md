# Creating an external implementation to implement an activity

## Before you begin

## About this task

The following steps describe how to select a custom application as the implementation for
a user task in a process.

## Procedure

1. Open a process and click the activity that you want to
implement using a custom application.
2. Click the General tab in the properties.
3. Under Implementation, select the User Task option from the
displayed list.
4. Click the Select button to choose an external service from the
library.
5. In the Task Header section, specify the following properties: 

Table 1. Properties in the Task Header section

Property
Action

Subject
Type a descriptive subject for the task that is generated in IBM Process
Portal
 when you run the
process. You can also use the embedded JavaScript syntax (for example,
<#=tw.local.mySubject#>) to express the subject.

Narrative
Type an optional description. You can also use the embedded JavaScript syntax
to express the narrative. Restriction: Do not use JavaScript variable references in task
narratives if you need the data to be available after the task completes. Once a task is complete,
the data for completed tasks is removed to conserve space. Instead, store the data items in another
location, such as a
database.

Note: For the following properties (in the Priority Settings section) you can click the JS button
for an option if you prefer to use a JavaScript expression with predefined variables to establish
the priority settings.
6. For the Priority field, select one of the default priority
codes: Very Urgent, Urgent, Normal, Low, or Very Low. You can also
use a JavaScript expression with predefined variables to establish
the priority settings.
7 Enter the Due In date in one of the following ways:
    - Enter a value in the text box and then choose Minutes, Hours, or Days. Do not set a due
in value greater than 800 Hours, Minutes, or Days as it decreases performance. Instead, use a
JavaScript expression to directly set the due date.
    - Enter JavaScript. You must return a TWDate object
    - Select an existing variable from the library. At run time,
the variable should reflect the value that you want for the time period.
Be sure to select the option that you want from the drop-down list:
Minutes, Hours, or Days.
8. For the Time Zone field, select the time zone that you
want to apply to the tasks that result from the current activity.
For example, you can select US/Pacific for
users who work in California.
9. For the Holiday Schedule field, you can leave the setting
at (use default) as described in the preceding note
or you can click the JS button if you prefer to use a JavaScript expression.
Each Holiday Schedule is made up of a list of Dates.   You can leave the Time Schedule, Timezone, and Holiday Schedule fields set to (use default). If
you do, the work schedule specified for the process used. See Setting the work schedule for a process for more information. 
If you choose JavaScript, you can enter either a String (or String-generated JavaScript) or
JavaScript that returns a TWHolidaySchedule variable. If you use a String, the holiday schedule is
looked up by name according to those rules. If you use a TWHolidaySchedule variable, then the
holiday schedule is assumed to be filled in appropriately. (Go to the System Data toolkit and open
the TWHolidaySchedule variable to view its parameters.)
10. Click the Data Mapping tab in the properties.  Because
you added the input and output parameters for the external implementation
when you created it, the Data Mapping tab for the activity in the
process should include those parameters.
Under Input Mapping,
click the auto-map icon in the upper-right corner, and then click
the auto-map icon in the upper-right corner of the Output Mapping
section. For more information about mapping variables, see Business objects and variables.
11. Click Save or Finish Editing.