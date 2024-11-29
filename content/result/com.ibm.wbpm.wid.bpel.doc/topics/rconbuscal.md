<!-- image -->

# Considerations when working with business calendars

- Business calendars can be tested in IBM Workflow
Server in
the context of a BPEL process, human task, or POJO invoking the calendar
service. Business calendars cannot be tested by the test client.
- Timetables imported from IBM
WebSphere® Business Modeler should not be edited after being imported.
- Business calendars can be refactored. As calendars only hold references
to other calendars, refactoring will be invoked when a referenced
business calendar is renamed.
- In IBM Integration
Designer, you can create both flat and hierarchical calendars.
Generally you start by creating a flat calendar to which you can add
and remove references. When you add references, it becomes a hierarchical
calendar.  Calendars exported from IBM
WebSphere Business Modeler are
generally hierarchical.
- Business calendars can be in a library and the library is referenced
by a module.
- Business calendars have dates that have offsets based on GMT (Greenwich
Mean Time). 2008-05-02T09:00:00-07:00 is 9:00 a.m.
PST which is the same as 2008-05-02T017:00:00-00:00.
- If a calendar is viewed on a computer in a time zone that is different
from the time zone in which the calendar was created, the times and
dates will be displayed in the computer's local time zone.  For example,
if the calendar was created in time zone -05:00 and
is opened in a time zone -04:00, you will see 10:00 AM time instead of the 09:00 AM.
This happens even though the calendar still has the time stored as 09:00 AM in time zone -05:00.
- When using editors with calendar functions such as the business
process editor, test client, debugger, human tasks editor, monitor
toolkit and so on, the dates are based on Coordinated Universal Time
(UTC) and rendered in the calender type you have selected from the
Preferences page (for example, Hijri calendar). You therefore see
dates and times in UTC format in the logs.
- The XPATH expression builder in the BPEL process editor uses the
Gregorian calendar for calculations even if another calendar type
such as Hijri is set as the preference.