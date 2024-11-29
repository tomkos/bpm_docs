<!-- image -->

# Setting duration values for your human task

## About this task

## Procedure

1. In the Properties view of the task settings, click the Duration tab.
2. From the Calendar type field, you
will have the following three options that will dictate the format
your calendar entries will take:

Option
Description

Simple
This is, as the name suggests, a simple arithmetic calendar.
Use the Timeout Duration fields to select the
amount of time that this activity should wait for an action to occur
before it expires. 

WebSphere® CRON
calendar
This is a built-in calendar that uses a list of term expressions
representing elements of time to calculate the interval. Examples
of this type of calendar can be found in the Related Information section
below.

User-Defined calendar
Use this option to select a calendar other than those provided.
You can use the fields to name the calendar, and point to a valid Java™ Naming and Directory Interface
(JNDI) location.

Business calendar
There will be more than three options in the Calendar
Type field if a business calendar is available.
A business calendar can be used to model duration values for time-sensitive
aspects of your human task in order to account for such variables
as regular working hours, weekends, and holidays.
3 The remaining fields on this page can be configured inany combination that you see fit, and according to these choices: Option Description Duration until task is overdue Use this field to set the amount of time that will elapse between the time this task is started and the time that it is expected to be completed. Enter a value that makes sense to the calendar you selected in the Calendar type field, or choose one of the following options: Duration until task expires Use this field to specify the amount of time that will elapse before this task is moved to the Expired state. A user cannot work on an expired task.Enter a value that makes sense to the calendar you selected in the Calendar type field or choose one of the following options: Duration until task is deleted Use this field to specify the amount of time that will elapse before this task is removed from the system once it has reached a completed state. Completed states include: Finished , Failed , Terminated , or Expired . Deletion is also dependent on the choice you make in the Auto deletion mode field.Enter a value that makes sense to the calendar you selected in the Calendar type field or choose one of the following options: Auto deletion mode This selection is not available when Duration until task is deleted is set to Never . Use this setting to configure the circumstances of the deletion of a task.You have the following options: Calendar name This field appears when you choose the User-defined option in the Calendar type field.Use this field to enter a name for your custom calendar. User calendar JNDI This field appears when you choose the User-defined option in the Calendar type field.Use this field to specify the Java Naming and Directory Interface (JNDI) location for your custom calendar.

| Option                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Duration until task is overdue | Use this field to set the amount of time that will elapse between the time this task is started and the time that it is expected to be completed.   Enter a value that makes sense to the calendar you selected in the Calendar type field, or choose one of the following options:  Immediate In this context, this setting means that the task will be considered due the moment it is started.   Never In this context, this setting means that the task will not be given a due date.                                                                                                       |
| Duration until task expires    | Use this field to specify the amount of time that will elapse before this task is moved to the Expired state. A user cannot work on an expired task.  Enter a value that makes sense to the calendar you selected in the Calendar type field or choose one of the following options:  Immediate In this context, the task will be expired the moment it is started.   Never In this context, the task will not move to the expired state.                                                                                                                                                       |
| Duration until task is deleted | Use this field to specify the amount of time that will elapse before this task is removed from the system once it has reached a completed state. Completed states include: Finished, Failed, Terminated, or Expired. Deletion is also dependent on the choice you make in the Auto deletion mode field.  Enter a value that makes sense to the calendar you selected in the Calendar type field or choose one of the following options:  Immediate In this context, the task will be deleted the moment it is completed.   Never In this context, the task will not be removed from the system. |
| Auto deletion mode             | This selection is not available when Duration until task is deleted is set to Never. Use this setting to configure the circumstances of the deletion of a task.  You have the following options:  On completion Choose this option to delete the task from the system once it is finished, whether or not it was successfully completed.   On successful completion Choose this option to only delete the task when it has been successfully finished.                                                                                                                                          |
| Calendar name                  | This field appears when you choose the User-defined option in the Calendar type field.  Use this field to enter a name for your custom calendar.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| User calendar JNDI             | This field appears when you choose the User-defined option in the Calendar type field.  Use this field to specify the Java Naming and Directory Interface (JNDI) location for your custom calendar.                                                                                                                                                                                                                                                                                                                                                                                             |

- Using business calendars within human tasks

When it comes to modeling duration values for time-sensitive aspects of your human task, you can use a business calendar to account for such variables as regular working hours, weekends, and holidays.

## Related tasks

- Configuring the wait activity
- Defining timer-driven behavior in a BPEL process
- Using business calendars within a BPEL process
- Creating an escalation for your human task
- Selecting a calendar type for your escalation
- Using business calendars within human tasks
- Notifying an event handler of an escalation

## Related reference

- Expiration tab: BPEL process editor
- Details tab: business state machine editor
- Duration tab: Human Task editor