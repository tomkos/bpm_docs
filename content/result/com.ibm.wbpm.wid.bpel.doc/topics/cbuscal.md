<!-- image -->

# Business calendars

- Monday to Friday (9:00 a.m. - 5:00 p.m.)
- Saturday and Sunday are weekends
- January 1, May 31, July 4, September 1, November 24, November
25, December 24, December 25 are holidays

- February 8 is a Friday. 1 business day from February 8 should
be Monday, February 11.
- July 3 is a Thursday. July 3 plus 2 business days should be Tuesday,
July 8.
- If the current time is Thursday, March 6 at 4:00 p.m., the current
time plus 26 hours should be Monday, March 9 at 10 a.m.

- Time intervals (one or more)
- Exceptions (optional)
- Inclusive calendars (optional)
- Exclusive calendars (optional)

- Begin and optional end date-time
- Schedule - Once, Daily, Weekdays, Weekends, Weekly, Monthly, Quarterly,
Yearly, or Always
- Repetition - Once, number of times, or Forever

## Scheduling options

| Schedule   | Options                                                                                                          |
|------------|------------------------------------------------------------------------------------------------------------------|
| Once       | Specific Date                                                                                                    |
| Daily      | Every [n] days or selected days of each month [ 1, 2, 7, 22, 30]                                                 |
| Weekly     | Every [n] weeks or selected weeks of the year [5, 9, 15, 16] and  check-marked days [Mo, Tu, We, Th, Fr, Sa, Su] |
| Monthly    | [n or last] day of the month or [first-second-…-last] [Mo…Sun]  of check-marked months [1…12]                    |
| Yearly     | On [Month-Day]                                                                                                   |
| By Hour    | Every [n] hour(s)                                                                                                |
| By Minute  | Every [n] minute(s)                                                                                              |
| By Second  | Every [n] second(s)                                                                                              |

The business calendar model is based on the iCalendar
specification (RFC 2445) from the Internet Engineering Task Force
(IETF). It is based on xCal, an XML-compliant representation of the
iCalendar standard, which provides the ability to operate with other
calendar systems. xCal maps the iCalendar format to XML. It is a simple
one-to-one mapping with iCalendar components and properties mapped
to XML elements.

## Scope

The business calendar is uniquely
identified by a target namespace and a name.  The scope of the calendar
is limited to the module with which the calendar is deployed.  When
multiple modules need to reuse the same calendar, the recommendation
is to place it in a library in IBM Integration
Designer and
have the modules reference the library.

## Time zone support

Business calendars have
dates that have offsets based on GMT (Greenwich Mean Time). The time
zone defined in the business calendar is the time zone used at run
time, even if the server is in a different time zone. For example,
if a business calendar was created in New York with the parameters
Monday to Friday 9:00a.m. - 5:00p.m. (GMT-5) to be run on a server
in California (GMT-8) the server will still honor the offset of GMT-5.

All date-times specified within a single calendar must
be in the same time zone. Referenced calendars might have a different
time zone.

## Included and excluded calendars

- There can be both included and excluded calendars.
- Exclusions take priority over inclusions.
- Other (included or excluded) calendars exist as separate files
and are referenced from the main calendar by its namespace and name.