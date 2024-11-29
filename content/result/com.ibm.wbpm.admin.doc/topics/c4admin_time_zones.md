<!-- image -->

# How time zones are handled in Business Process Choreographer

Depending on the client that you are using, times are displayed
in your browser in the local time of the client or the server.

For administrative scripts, time parameters end with the postfix Local or UTC,
which indicates whether the times are interpreted as being in the
scripting client's local time or in Coordinated Universal Time
(UTC). By using the Local version
of the time parameters you can avoid having to perform any calculations
to adjust for time zones and daylight saving time.

| Client or interface                     | Time zone used or displayed              |
|-----------------------------------------|------------------------------------------|
| Administrative console                  | Server local time zone                   |
| Business Process Choreographer Explorer | Client local time zone                   |
| Business Space                          | Client local time zone                   |
| Administrative scripts                  | UTC or the scripting client's local time |
| APIs                                    | UTC                                      |

For example, the deleteCompletedProcessInstances script
can be given time stamp values for the -validFromUTC, -completedAfterLocal, -completedAfterUTC, -completedBeforeLocal,
and -completedBeforeUTC parameters. The parameter
name suffixes show whether the time must be specified in UTC or in
the scripting client's local time.

For time zones where daylight saving time is observed, the local
times displayed are adjusted for daylight saving time if the date
and time being displayed falls in the period when daylight saving
is observed.

The administrative script parameter -validFromUTC is
used to distinguish between different template versions and must always
be specified exactly to the second. For other script parameters that
take a time, like -completedAfterLocal, -completedAfterUTC, -completedBeforeLocal,
and -completedBeforeUTC, if you specify a date
with no time, it defaults to 00:00:00.

<!-- image -->