# Removing process instances from the Process database

## Before you begin

Run the query during an off period or maintenance window.
When thousands of instances and data are purged, this process might
cause a strain on the LSW\_TASK and LSW\_BPD\_INSTANCE tables, which
are core product tables. Running a clean-up job outside of normal
business hours is a good practice.

If you want to archive data
rather than deleting it, copy the data into a custom-built table outside
of the product schema.

## About this task

Completed BPD instances are not deleted from the system automatically. After a process instance
is completed, the instance is typically no longer needed, so it can be removed from the Process
database. The recommended approach is to use the BPMProcessInstancesPurge
command. For information, see BPMProcessInstancesPurge command.

When an instance completes and all of its associated
tasks are closed, future work is not possible with the instance. You
cannot restart it, assign it to someone, or edit old work. When a
user logs in to Process Portal, various
tables are queried to gather data on the active tasks for that user.
The operation involves full table scans, so even if only 35% of the
data is relevant, it is going to take a while to pull the tasks needed
for the user. If the other 65% is deleted, there is less data to scan.

If
you do not delete the old completed instances, your team experiences
slow performance on Process Portal and
a potentially unusable state. Ignoring increases in database size
cause an increase in backup time and disk space.

Deleting old
instances affects only the search for history items from Process Portal. When
you run the delete queries, you can specify to delete only completed
processes that are older than 30 days. Store any data that you really
need in either the performance database or in another system of record
for auditing or metrics.

- How many instances are closed in a specified time period (for
example, a week or month)
- How large the data is in each task (including execution context
and document attachments)
- How many tasks there are in a process instance