# Setting the work schedule for a process

## About this task

The default work schedule for all processes is specified
in the 99Local.xml configuration file. If you
do not specify a work schedule for a process, or if you leave the
settings as use default, due date calculations for
process instances are based on the <default-work-schedule> in
this configuration file. However, the default
settings are used only if the timer-use-activity-schedule property
in the 100Custom.xml file is set to true.
If the timer-use-activity-schedule property is not
set, or if it is set to false, the default-work-schedule property
is ignored, and the 24x7 calendar is used to calculate
the timer's fire date.

If you want to customize the default work schedule, add the corresponding elements to your
100Local.xml configuration file. For an example of configuring the time zone,
see Specifying a default system time zone. If you select use default as the
time zone setting and you do not have a customized work schedule, Central Standard Time (CST) is
used as time zone for due date calculations and the value of the JavaScript
tw.system.defaultTimeZone constant. If you use the default time zone, and it differs from your
system time zone, you might get unexpected results when due dates are calculated or when you use the
JavaScript tw.system.calculateBusinessDate() method to calculate business
dates.

## Procedure

- The Time Schedule specifies the normal business hours in which work can
be completed.
- Timezone specifies the timezone that you want to apply to running
instances of the current process.
- The Holiday Schedule is a list of exceptions to the normal time
schedule.

You can also write a service to dynamically set
schedules. For more information, see Creating and managing time and holiday schedules.