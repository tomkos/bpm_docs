# Due dates for processes and activities

In Process Portal,
process instances are listed by due date and marked as at risk or overdue when the due date expires.
To list only those process instances that are due on a certain date, in a specific time frame, or
that are overdue, you can use process instance due dates as search filters in saved searches.
Administrators and members of the instance owners team can change a process instance due date after
the process instance is created if, for example, they want to bring the instance back on track.

Tasks are listed by due date. Task due dates and the projected path
are also used to calculate the expected completion time for a process instance. Administrators can
change task due dates in Process Portal. If projected path management is enabled for the process, authorized business
users can change the due date for individual tasks and the overall process instance.

## How due dates are calculated

If the due-in time is specified in days, the default value to the right of the
Days selection is 00:00. This is 0 hours and 0
minutes, which is 12:00 AM. For example, assume that today's date is November 2. If you specify
3 as the number of days and you accept the default value of
00:00, the due-in time is 12:00 AM on November 5, which is the third day
after the process instance or task starts. (Based on the 24-hour clock, if you changed the value
00:00 to 14:15, you would be specifying 14 hours
and 15 minutes, which is 2:15 PM.)

## Examples

## Example: Definition of a business day

| Start date                  |   Due-in value | Due-in unit   | Hours and minutes   | Time schedule   | Holidays   | Due date                   |
|-----------------------------|----------------|---------------|---------------------|-----------------|------------|----------------------------|
| Wednesday, 2017-03-01 10:00 |           1440 | Minutes       | Not applicable      | 9AM-5PM M-F     | None       | Monday, 2017-03-06 10:00   |
| Wednesday, 2017-03-01 10:00 |             24 | Hours         | Not applicable      | 9AM-5PM M-F     | None       | Monday, 2017-03-06 10:00   |
| Wednesday, 2017-03-01 10:00 |              1 | Days          | 10:00               | 9AM-5PM M-F     | None       | Thursday, 2017-03-02 10:00 |
| Wednesday, 2017-03-01 10:00 |           1440 | Minutes       | Not applicable      | 24x7            | None       | Thursday, 2017-03-02 10:00 |
| Wednesday, 2017-03-01 10:00 |             24 | Hours         | Not applicable      | 24x7            | None       | Thursday, 2017-03-02 10:00 |
| Wednesday, 2017-03-01 10:00 |              1 | Days          | 10:00               | 24x7            | None       | Thursday, 2017-03-02 10:00 |

## Example: Due-in time is outside normal business hours

| Start date                  |   Due-in value | Due-in unit   | Hours and minutes   | Time schedule   | Holidays   | Due date                 |
|-----------------------------|----------------|---------------|---------------------|-----------------|------------|--------------------------|
| Friday, 2017-03-03 16:15    |             60 | Minutes       | Not applicable      | 9AM-5PM M-F     | None       | Monday, 2017-03-06 9:15  |
| Friday, 2017-03-03 16:15    |              1 | Hours         | Not applicable      | 9AM-5PM M-F     | None       | Monday, 2017-03-06 9:15  |
| Friday, 2017-03-03 16:15    |              1 | Days          | 16:15               | 9AM-5PM M-F     | None       | Monday, 2017-03-06 16:15 |
| Wednesday, 2017-03-01 10:00 |              1 | Days          | 10:00               | 9AM-5PM M-F     | 2017-03-02 | Friday, 2017-03-03 10:00 |

## Example: Start date is outside normal business hours

| Start date                  |   Due-in value | Due-in unit   | Hours and minutes   | Time schedule   | Holidays   | Due date                  |
|-----------------------------|----------------|---------------|---------------------|-----------------|------------|---------------------------|
| Saturday, 2017-03-04 10:00  |             60 | Minutes       | Not applicable      | 9AM-5PM M-F     | None       | Monday, 2017-03-06 10:00  |
| Saturday, 2017-03-04 10:00  |              1 | Hours         | Not applicable      | 9AM-5PM M-F     | None       | Monday, 2017-03-06 10:00  |
| Saturday, 2017-03-04 10:00  |              1 | Days          | 10:00               | 9AM-5PM M-F     | None       | Tuesday, 2017-03-07 09:00 |
| Wednesday, 2017-03-01 10:00 |              1 | Days          | 10:00               | 9AM-5PM M-F     | 2017-03-01 | Friday, 2017-03-03 09:00  |

## Example: Due-in time includes days, hours, and minutes

| Start date               |   Due-in value | Due-in unit   | Hours and minutes   | Time schedule   | Holidays   | Due date                    | Type             |
|--------------------------|----------------|---------------|---------------------|-----------------|------------|-----------------------------|------------------|
| Monday, 2017-03-06 10:00 |              1 | Days          | 10:30               | 9AM-5PM M-F     | None       | Wednesday, 2017-03-08 12:30 | Process instance |
| Sunday, 2017-03-05 10:30 |              1 | Days          | 10:30               | 9AM-5PM M-F     | None       | Tuesday, 2017-03-07 09:00   | Activity         |

- For processes, the value of the hours and minutes is added to the elapsed time to give an
expected duration of 1 day, 10 hours, and 30 minutes.
- For activities, the start day is the day the runtime task was created and the hours and minutes
value denotes the start time for the due date calculation. Because the start time is on a Sunday,
the calculation starts at the beginning of the next business day.

## Example: Time zone differs from system time zone

| Start date               |   Due-in value | Due-in unit   | Hours and minutes   | Time schedule   | Holidays   | Due date                  |
|--------------------------|----------------|---------------|---------------------|-----------------|------------|---------------------------|
| Monday, 2017-03-06 12:00 |              1 | Days          | 12:00               | 9AM-5PM M-F     | None       | Tuesday, 2017-03-07 16:00 |

1. The start date is converted to CST: Monday, 2017-03-06 05:00.
2. Because the start date is outside normal business hours, the due date calculation starts at the
beginning of the next business day: Monday, 2017-03-06 09:00.
3. One business day is added to the due date calculation for the due-in time: Tuesday, 2017-03-07
09:00.
4. The due date result is converted back to CET: Tuesday, 2017-03-07 16:00.

- Setting the work schedule for a process

The work schedule determines the number of working hours that business users are available to complete work and therefore directly affects the due date work schedule of process instances and activities.
- Creating and managing time and holiday schedules

You can create and manage time and holiday schedules by using the JavaScript API. You can set time and holiday schedules for both processes and activities. After you add a new time or holiday schedule, it immediately becomes available in the time or holiday schedule list in the authoring environment.
- Specifying activity due dates

Activity due dates are used to calculate the expected completion time for an activity. This completion time is used during process execution to establish which tasks are overdue or at risk of being overdue.