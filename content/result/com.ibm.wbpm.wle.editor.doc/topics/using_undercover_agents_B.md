# Creating and configuring an undercover agent for a scheduled
message event

## About this task

Scheduled undercover agents do not run on the playback server unless you click
Run Now. If you are testing a process that includes scheduled undercover
agents, and you want to ensure that the undercover agents run on time, run the process on a workflow
server in one of your runtime environments, such as your development, test or staging
environment.

## Procedure

1. Open the designer.
2. To launch the New Undercover Agent, click the plus
(+) icon beside Events and then select
Undercover Agent. The New Undercover Agent wizard
opens.
3 In the New Undercover Agent window, enter the followinginformation:
    - Name: Type a name for the new undercover
agent.
    - Schedule Type: Select Time Elapsed from
the drop-down list.
    - Click Finish.
4. In the Common section, you can type a description of the
undercover agent in the Documentation text
box.
5. In the Scheduler section, you can see the type of schedule for the current undercover
agent. After you have configured and saved the undercover agent, you can click Run
Now if you want to test and monitor the undercover agent and monitor as described in Maintaining and monitoring IBM Business Automation Workflow Event Manager.
6. Under Details, click the drop-down list next to Queue Name to
select the queue that you want from the following options:  
Table 1. Available
queue options

Option
Description

Async Queue
Allows Event Manager jobs to run at the same
time.

SYNC\_QUEUE\_1
Forces one job to finish and starts the next job even if the previous task
fails. By default, three synchronous queues are available.

SYNC\_QUEUE\_2
Forces one job to finish and starts the next job even if the previous task
fails. By default, three synchronous queues are available.

SYNC\_QUEUE\_3
Forces one job to finish and starts the next job even if the previous task
fails. By default, three synchronous queues are available.

Note: For more information about Event Manager jobs, monitoring those
jobs, and creating and maintaining Event Manager execution queues, see Maintaining and monitoring IBM Business Automation Workflow Event Manager. When you install and run the process on a workflow server
in a test or production environment, the queue that you select must exist in that environment in
order for the undercover agent to run.
7. Ensure the service shown as the Attached Service is
the one that you want to invoke according to the specified schedule.
If not, click Select to choose a different
service.
8. Ensure that the Enabled check box
is selected. Note: If this check box is not selected, the
undercover agent will not run.
9. In the Parameter Mapping section, select the Use
Default check box if you want to use the default value
of the input variable in the attached service. If the input variable
of the attached service does not have a default value, this check
box is disabled. Type a value in the text box if you
want to manually map a constant value to the input variable of the
attached service. For example, you might use a constant for testing
purposes.
10. Scroll down to the Time Schedule section and use the available
options to establish a schedule. For example, if you
want to start the attached service every weekday at midnight, use
the Ctrl key to select the options that are
selected in the following image:
 
You can select multiple contiguous
items by pressing the Shift key, clicking the
first in the series, and then clicking the last in the series. To
select multiple non-contiguous items, press the Ctrl key
each time you click an item.
Note: The On the hour value
is selected by default in the last column of the Time Schedule section.
If you clear this selection and you do not make any other selection
in the column, the On the hour value will be
used even though it is not selected.
Note: If you select the First value
and also select multiple weekdays, the undercover agent will run on
the first occurrence of each selected day for the selected months.
For example, if you select First and also select Monday, Tuesday,
and Thursday, the undercover agent will run
on the first Monday, Tuesday, and Thursday that occur in the selected
months. Similarly, if you select the Last value
and also select multiple weekdays, the undercover agent will run on
the last occurrence of each selected day for the selected months.
For example, if you select Last and also select Monday, Tuesday,
and Thursday, the undercover agent will run
on the last Monday, Tuesday, and Thursday that occur in the selected
months.
11. Open the process that includes the message event to which you want to attach the
undercover agent. For example, if you want a particular process to start at the same time each day,
you can associate the start message event in the process with an undercover agent that establishes
the required schedule.
12. Click the message event in the process to select it.
13. Click the General tab in the
properties pane.
14. In the Event Properties section, click Select next to
Attached message UCA and select the undercover agent created in the previous
steps.
15. Click Save or Finish Editing.