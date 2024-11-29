<!-- image -->

# Business calendars and human tasks

The human task uses a single calendar, therefore if multiple calendars
are applicable, they must be wrapped in a single composite calendar.
After selecting the business calendar to use in the human task, you
can also enter durations for when a task is considered overdue and
for when it is to be deleted or when it expires.

Durations only work for simple and business calendars. In other
calendars like the WebSphere CRON or custom calendar, you must enter
the duration as a text string. If you select a non-Gregorian calendar
such as the Hijri calendar from the Preferences page, it will not
change the text field.

How the value of the duration is consumed depends on the calendar
runtime that you use, which also applies for directly entered values
for the simple and business calendars. Usually values such as months
or larger are calculated differently for non-Gregorian calendars like
the Hijri calendar.

The Business Process Choreographer runtime schedules these tasks
with the WebSphere Application Server scheduler which uses the selected
business calendar to determine when the duration has elapsed and performs
as required when a task is overdue or expired.