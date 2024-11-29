# Modeling delays, escalations, and timeouts by using timer events

## About this task

- Create a delay to prevent an event or activity from immediately triggering.
- Create an escalation to handle when an activity fails to complete in a timely fashion.
- Create a timeout to prevent a flow from waiting indefinitely.

<!-- image -->

<!-- image -->

<!-- image -->

## Procedure

To model a delay, escalation, or timeout:

1. Open a process.
2 Drag a timer intermediate event from the palette.
    - To create a delay, drop the timer event into a blank area of the canvas.
    - To create an escalation, drop the timer event onto an activity. This action attaches the timer
event as a boundary event. To verify that you have created a boundary event, select the activity and
check that the outline of the activity includes the event icon.To have multiple escalations,
attach more than one intermediate events to the activity. Each boundary event triggers a different
escalation path.
    - To create a timeout, drop the intermediate event into an event gateway group.
3. If you are creating an escalation and you want the activity to remain open after the
timer is triggered, in the Boundary Event Details section clear the
Interrupt Activity check box. For example, imagine that you
create a timer boundary event for a user task. The human service that is associated with the user
task has coaches. If you want the users to complete the coaches even after the timer elapses, clear
the Interrupt Activity check box.If you clear the
Interrupt Activity check box, you can choose to have the escalation occur
only once by clearing the Repeatable check box.
4 Specify when to start the timer for the timer event by setting the Timerproperties:

1. In the Trigger on drop-down list, select one of the options in the
following table to start the timer:

Option
Timer event types
Description

After start of step
Escalations
Starts the timer when a step starts.

Before due date
Escalations
Starts the timer before the due date for an activity. The due date is calculated according to
the work schedule for the process and the priority settings for the activity. For more information, see Setting the work schedule for a process.

After due date
Escalations
Starts the timer when the due date for an activity elapses. The due date is calculated
according to the work schedule for the process and the priority settings for the activity. For more information, see Setting the work schedule for a process.

After start of process or subprocess
Delays and timeouts
Starts the timer when the process and subprocess start.

Before custom date
Delays, escalations, and timeouts
Starts the timer before the custom date specified in the Custom date
field.

After custom date
Delays, escalations, and timeouts
Starts the time after the custom date specified in the Custom date
field.
2. If you selected either Before custom date or After custom
date in the Trigger on drop-down list, specify the JavaScript in the Custom date field
that is required to determine the custom date. Your JavaScript must return a Date object, which specifies when to start the timer. You should use
the following value (or a variable of that type):

new tw.object.Date();
3. To modify the trigger, use the Before or after difference field.
For example, if you want start the timer a day after the due date of the activity, type
1 into the field and select Days from the associated
list.

Note: When you select to run the timer event repeatedly, make sure that you set the
Before or after difference to at least 1 minute. When the timer is set to
Repeatable, an escalation notice is sent each time that the specified
interval elapses until the activity is completed. However, if this interval is 0, it causes high CPU
load because the escalation notices are continuously sent, without an interval, until the activity
completes.
4. Optional: To further modify the trigger, use the Tolerance
Interval field. 
The Tolerance Interval is an additional time interval that is associated
with the algorithm. If a task has not been claimed when the primary interval is reached, the timer
fires as expected. However, if the task is already claimed, then the additional Tolerance
Interval value is used to extend the deadline to complete the task before the timer
fires.

For example, specify the delay as a static value of 10 minutes. At run time, the Teamworks engine
checks for task activity at the time the timer event is set to be triggered. If there is no
activity, the timer event is executed. If there is some task activity within the last 10 minutes,
the timer event is delayed for 10 more minutes.
5. If you are creating an escalation or timeout, create the flow that the process uses after
the timer elapses. The escalation path is the logic that the process performs if the
timer elapses before the activity it is attached to finishes. Similarly, the timeout path is the
logic that the process performs if the timer elapses before another event in the event gateway group
triggers.
6 Connect the timer event:

- For a delay, connect the timer event to the rest of the process.
- For an escalation or timeout, connect the timer event to the escalation or timeout path.
7. Click Save or Finish Editing.