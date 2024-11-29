# Creating and managing time and holiday schedules

## About this task

The following table provides some
predefined example schedules to serve as a guide for specifying time values:

| Time Schedule Name   | startTime   | endTime   | Effective Days                                           |
|----------------------|-------------|-----------|----------------------------------------------------------|
| 24x7                 | 00:00       | 23:59     | monday,tuesday,wednesday,thursday,friday,saturday,sunday |
| 7AM-7PM M-F          | 07:00       | 19:00     | monday,tuesday,wednesday,thursday,friday                 |
| 7AM-7PM Every Day    | 07:00       | 19:00     | monday,tuesday,wednesday,thursday,friday,saturday,sunday |
| 9AM-5PM M-F          | 09:00       | 17:00     | monday,tuesday,wednesday,thursday,friday                 |

## Procedure

1. Create an integration service by using a server script. 
The following example script creates a service that dynamically
sets the holiday and time schedule for a process and stores the schedules
in the TWHolidaySchedule and TWTimeSchedule variables.
To view the variable parameters that you can use, open the variables
from the System Data toolkit. var holidaySchedule = new tw.object.TWHolidaySchedule();
      holidaySchedule.name = "myHolidaySchedule";
      holidaySchedule.dates = new tw.object.listOf.Date();
      holidaySchedule.dates[0] = new tw.object.Date();
      holidaySchedule.dates[0].parse("20170101", "yyyyMMdd");
      holidaySchedule.dates[1] = new tw.object.Date();
      holidaySchedule.dates[1].parse("20170116", "yyyyMMdd");
      holidaySchedule.dates[2] = new tw.object.Date();
      holidaySchedule.dates[2].parse("20170529", "yyyyMMdd");
      holidaySchedule.dates[3] = new tw.object.Date();
      holidaySchedule.dates[3].parse("20170704", "yyyyMMdd");
      holidaySchedule.dates[4] = new tw.object.Date();
      holidaySchedule.dates[4].parse("20170904", "yyyyMMdd");
      holidaySchedule.dates[5] = new tw.object.Date();
      holidaySchedule.dates[5].parse("20171231", "yyyyMMdd");
tw.system.addHolidaySchedule(holidaySchedule);

var timeSchedule = new tw.object.TWTimeSchedule();
      timeSchedule.name = "myTimeSchedule";
      timeSchedule.excludeHolidays = false;
      timeSchedule.periods = new tw.object.listOf.TWTimePeriod();
var timePeriod = new tw.object.TWTimePeriod();
      timePeriod.startTime = new tw.object.Time();
      timePeriod.startTime.parse("09:00", "HH:mm");
      timePeriod.endTime = new tw.object.Time();
      timePeriod.endTime.parse("17:00", "HH:mm");
      timePeriod.monday = true;
      timePeriod.tuesday = true;
      timePeriod.wednesday = true;
      timePeriod.thursday = true;
      timePeriod.friday = true;
      timePeriod.saturday = false;
      timePeriod.sunday = false;
      timeSchedule.periods[0] = timePeriod;
tw.system.addTimeSchedule(timeSchedule);
2. Save and run the integration service. Note: It
might take some time for the new schedules to be available in Process Designer after
running the integration service. To make use of your new schedules
right away, restart Process Designer before
you begin modeling.
3. Create a process, and add an activity with a default service.
4. Link the activity in a start-end flow.
5. On the Implementation tab of the
activity or the Overview tab of the process,
select the holiday schedule and the time schedule that you created.
6. Save the process.
7. Run the process and then verify the due date calculation in the Inspector
view.