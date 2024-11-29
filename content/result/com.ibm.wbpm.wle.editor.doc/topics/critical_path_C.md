# Specifying activity due dates

## About this task

In IBM® Process
Portal,
tasks are listed according to their due date status. Activity due
dates and the projected path are also used to calculate the expected
completion time for a process instance.

By default,
the due date of a human task is 1 hour from the time of task creation.
You can modify this duration for each activity in your process. Administrators
can also change the default duration after deployment. If projected
path management is enabled for the process, authorized business users
can change the due date for individual tasks and the overall process
instance in Process Portal.

The
calculation of the activity due date is also affected by the working
hours that users are available to complete work. The working hours
depend on the values that you specify for the time schedule, time
zone, and holiday schedule.

## Procedure

1. Select an activity in the diagram and go to the Implementation tab
of the Properties view.
2. In the Priority Settings section,
specify the expected duration of the activity in the Due
In field.  If you select Days for
the duration, you can also add hours and minutes to the elapsed time,
for example 2 days, 4 hours, and 30 minutes.
3 In the other fields in the Priority Settings section,specify values for the properties that affect the working hours thatare available to complete work. You can leave the TimeSchedule , Timezone , and HolidaySchedule fields set to the default value: (usedefault) . If you use the default values, the time schedule,time zone, and holiday schedule that are specified for the processare used for the activity. For more information, see Setting the work schedule for a process .

You can leave the Time
Schedule, Timezone, and Holiday
Schedule fields set to the default value: (use
default). If you use the default values, the time schedule,
time zone, and holiday schedule that are specified for the process
are used for the activity. For more information, see Setting the work schedule for a process.

    - The Time Schedule field specifies the
normal business hours. For example, if you expect the users who work
on the task to be available Monday through Friday, 9 AM to 5 PM, you
can select this schedule from the list.
    - In the Timezone field, select the time
zone that you want to apply to the tasks that result from the current
activity. For example, if you expect the users who work on the task
to be in California, you can select the US/Pacific time zone from
the list.
    - The Holiday Schedule field contains
a list of dates that are exceptions to the normal time schedule. If
you use a JavaScript expression to define a holiday schedule that
is specific to users who work on this task, enter either a String
(or String-generated JavaScript) or JavaScript that returns a TWHolidaySchedule variable.
If you use a String, then Business Automation Workflow looks
up the holiday schedule by name according to those rules. If you use
a TWHolidaySchedule variable, then it is assumed
that the holiday schedule is inserted appropriately. To view the parameters
for  the TWHolidaySchedule variable, go to the
System Data toolkit and open the variable.

## What to do next

If you plan to enable projected path management for the process, keep in mind that variable-based
due dates used in the implementation of activities are not detected in the projected path.