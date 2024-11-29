<!-- image -->

# Timezone parameter

Time zones can differ between the client that starts the query
and the server that processes the query. Use the time-zone parameter
to specify the time zone of the time-stamp constants used in the where
clause, for example, to specify local times. The dates returned in
the query result set have the same time zone that is specified in
the query.

If the parameter is set to null, the timestamp
constants are assumed to be Coordinated Universal Time (UTC) times.

## Examples of time-zone parameters

- process.query("ACTIVITY.AIID",
              "ACTIVITY.STARTED > TS('2005-01-01T17:40')",
               (String)null,
               (Integer)null,
               java.util.TimeZone.getDefault() ); Returns
object IDs for activities that started later than 17:40 local time
on 1 January 2005.
- process.query("ACTIVITY.AIID",
              "ACTIVITY.STARTED > TS('2005-01-01T17:40')",
               (String)null, (Integer)null, (TimeZone)null); Return
object IDs for activities that started later than 17:40 UTC on 1 January
2005. This specification is, for example, 6 hours earlier in Eastern
Standard Time.