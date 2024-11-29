<!-- image -->

# Duration tab: Human Task editor

## Task level

- Simple
- This is, as the name suggests, a simple arithmetic calendar.
Configure the time using the spinners that are enabled when you choose
this option.

- WebSphere® CRON
- This is a built-in calendar that uses a list of term expressions
representing elements of time to calculate the interval. Examples
of this type of calendar can be found in the Related Information section
below.

- User-defined
- Use this option to select a calendar other than those provided.
When you select it, two new fields will appear that you can use to
name the calendar, and point to a valid Java™ Naming
and Directory Interface (JNDI) location.

- Business calendar
- There will be more than three options in the Calendar
type field if a business calendar is available.
A business calendar can be used to model duration values for time-sensitive
aspects of your human task in order to account for such variables
as regular working hours, weekends, and holidays. See Related
Tasks for more information.

- Immediate
- In this context, this setting means that the task will be considered
due the moment it is assigned.

- Never
- In this context, this setting means that the task will not be
given a due date.

- Set a duration in days, hours, minutes and seconds.
- In the Days, Hours, Minutes and Seconds fields
use the arrows or type values for the length of time you want to elapse
between the time the task is started and when it is expected to be
completed.

- Immediate
- In this context, the task will be deleted the moment it expires.

- Never
- In this context, the task will not be removed from the system
ever.

- Set a duration in days, hours, minutes and seconds.
- In the Days, Hours, Minutes and Seconds fields
use the arrows or type values for the length of time you want to elapse
before this task is moved to an end state of Expired.

- Immediate
- In this context, the task will be deleted immediately after it
is completed.

- Never
- In this context, the task will not be removed from the system
ever, and will never expire.

- Set a duration in days, hours, minutes and seconds.
- In the Days, Hours, Minutes and Seconds fields
use the arrows or type values for the length of time you want to elapse
between the time the task is completed and when it is removed from
the system.

- On completion
- Choose this option to delete the task from the system once it
is finished, whether or not it was successfully completed.

- On successful completion
- Choose this option to only delete the task when it has been successfully
completed.

## Related tasks

- Creating an escalation for your human task
- Selecting a calendar type for your escalation
- Setting duration values for your human task
- Defining timer-driven behavior in a BPEL process
- Using business calendars within human tasks
- Notifying an event handler of an escalation

## Related reference

- Details tab: business state machine editor