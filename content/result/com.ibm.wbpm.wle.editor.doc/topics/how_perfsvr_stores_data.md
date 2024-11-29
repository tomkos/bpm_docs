# Data tracking considerations

## Supported data types

Data types that Business Automation Workflow tracks
include the following:

| Type of tracking   | Supported data types                        |
|--------------------|---------------------------------------------|
| Autotracking       | String, Integer, Decimal, Boolean, and Date |
| Tracking groups    | String, Number, and Date                    |

When you are tracking data, be aware of the following:

- A tracking group can have a maximum of 50 fields for each of the
data types. Do not increase the maximum number of fields because it
can affect the database table size and future migration to a new Business Automation Workflow release.
- Variables for which the Is List option
is enabled cannot be tracked.
- Complex types cannot be mapped directly; their fields must be
mapped individually.
- Variables of type ANY, Map, Record, XMLDocument, XMLElement, and
XMLNodeList cannot be tracked.

## Naming tracking groups

When naming
tracking groups and tracked fields, be aware of the following restrictions:

- Do not use SQL-92 reserved words. Several sources available on
the internet provide a complete list of SQL-92 reserved words.
- Do not use any of the names used for the views and fields in the
Business Performance Data Warehouse database schema.

## Tracking data across processes
and process applications

To track data from multiple processes
that reside in the same process application, create a tracking group
and implement it for as many processes as you like, mapping the tracked
fields to the appropriate variables for each process.

If you want to capture
data from multiple processes that reside in different process applications,
you can do so by using the same tracking group in each process application.
For example, you can create a tracking group in a toolkit, and then
create a dependency on that toolkit in each process application where
you want to use the tracking group. From each process application,
you can implement the tracking group one or more times, mapping the
tracked fields to variables within each application. When you send
tracking definitions and then run instances of the processes, the
data is captured in a single tracking group view as described in "Business
Performance Data Warehouse tracking group views." The data that Business Automation Workflow captures
enables you to analyze the tracked data in any way you choose. For
example, you can analyze the tracked fields as a whole or you can
compare the data from each process application or from each process.

## Working with versioned data

All data
tracked by Business Automation Workflow includes snapshot (version) information that enables you
to create reports to compare versions of your processes if you have
that requirement.

When tracking data, keep the following in
mind:

- Timing intervals work across snapshots (versions). For example,
a process that starts in one version (1.0) might be migrated to a
new version (2.0) before reaching the end of a timing interval. In
such a case, the data for the timing interval is captured in the Performance
Data Warehouse as expected with the version change noted.
- Data types of variables that are being stored (autotracked or
part of a tracking group) can change between versions. If data types
do change, a new column is created in the corresponding view as described
in "Performance Data Warehouse database architecture."