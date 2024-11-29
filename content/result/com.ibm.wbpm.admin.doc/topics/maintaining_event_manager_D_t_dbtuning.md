# Tuning databases for the Event Manager

## About this task

The Event Manager is one of IBM Business Automation Workflow core
components. It handles the communications between business process
definitions (BPD) and services, schedules events, and runs undercover
agents (UCA). The Event Manager consists of multiple Java threads
and database tables. All events are recorded and tracked in the LSW\_EM\_TASK
and LSW\_EM\_TASK\_KEYWORDS tables. For high workloads, database tuning
is essential for the Event Manager to work properly.

- SQL execution plans that use full table scans
- High CPU use
- Fragmented tables and indexes
- Significant contention on records or data pages

## Procedure

To prevent events from affecting how the Event Manager
performs, consider completing the following tuning tasks in this order
until performance improves.

- Update the database optimizer statistics for the Event
Manager tables.   Plan the update carefully because
the workload on the Event Manager changes frequently. That is, the
number of records in the database tables is volatile. The statistics
must reflect heavy or peak workload for an SQL execution plan to make
sense for the whole spectrum of workloads. It is unnecessary to update
the optimizer statistics when the workload is close to null.
If
this action does not solve the performance issues, you might have
specific high-load scenarios. Try the next steps in order.
- Periodically reorganize the Event Manager tables and indexes.
This action typically solves the most common performance issues. 
 Because the workload is volatile and because new records
are in ascending order (task\_id, scheduled\_time, discriminator columns),
periodically reorganize the Event Manager tables and more importantly,
reorganize the indexes. To decide whether reorganizing is necessary,
you can use the information that is returned by the database catalog
tables or by a command that checks reorganization, such as the reorgchk DB2
command.
If this action does not solve the performance issues,
you might have specific high-load scenarios. Try the next steps in
order.
- Tune the indexes by reviewing the SQL execution plans for
queries on Event Manager tables.  If the execution plan
shows a full table scan or numerous read requests and if the number
of records is significant, consider providing an extra index that
is more suitable than the default Business Automation Workflow indexes.
These indexes work well for most use cases but some database systems
might prefer a different index. Use your database vendor's advisor
tool to determine whether a more suitable index is available for your
database system.
- On Oracle, reduce the contention. Increase the INITRANS
values for tables and indexes.  Increase the INITRANS
values for tables and indexes. Specifically on Oracle, you might observe
contention that is related to blocks, for example interested translation
list (ITL) wait events. Such events are reported in an Automatic Workload
Repository (AWR) report. In this case, increase the INITRANS values
for tables and indexes that are listed in the AWR report.