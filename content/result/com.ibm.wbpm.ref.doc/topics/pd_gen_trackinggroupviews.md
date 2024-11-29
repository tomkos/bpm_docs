# Business Performance Data Warehouse tracking group views

Tracking group views contain the same data as the Tracking Group tables. This data includes a
column for each tracked variable and several columns to capture timing and other important task
information. The Business Performance Data Warehouse creates a view for each tracking group defined
in the Process Designer and gives each view the same name
as the corresponding tracking group in the Process Designer. When you use one tracking group in multiple process applications, all data is stored in a single
view, with an ID to distinguish each implementation.

The Tracking Group tables in the Business Performance Data Warehouse database differ from the
views in that they contain all tracked data, including data for those variables that you might have
stopped tracking during the lifetime of your process. Only the views are updated when you make such
changes to your tracking requirements.

The following general rules apply to how Business Performance Data Warehouse manages changes to
an existing tracking group:

- When a tracking group is renamed (in Process Designer),
the Tracking Group view is renamed, but the name of the Tracking Group table does not change.
- When a tracking group is deleted, the view is deleted and the tracking group in the table is
marked as deleted, but the table does not change.
- When a new field is added to an existing tracking group, a field of the same name is added to
the view whose name matches the name of the tracking group. Additionally, a new column with a unique
name that is similar (but not necessarily identical) to the name of the field is added to the
table.
- When a field is deleted from a tracking group (in Process Designer), the field remains in both the table and the view.
If a snapshot that contains particular fields in a tracking group is archived using the Business
Performance Data Warehouse command-line tool (perfsvrtool), those fields are
removed from the view and marked as deleted. If the snapshot is restored, those fields are added
back to the view.
- When a field is renamed, both the old name and the new name are present in the view and the
table.
- When the type of a field (string, number, or date/time) is changed, a new column with a unique
name that is similar (but not necessarily identical) to the name of the field in the tracking group
is added to the table, and the view is updated to use the new column. The formerly used column does
not change. You must manually migrate the data for the modified field to the new column. This is
also true for type changes from one version (snapshot) to another.

Tracking group views include the following columns:

| Column                | Description                                                                                                                                                 |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| business data columns | One column for each variable in the corresponding tracking group. Each column has the same name as the corresponding tracked field.                         |
| TRACKING\_GROUP\_ID     | The primary key of the tracking group to which this entry corresponds. This column links to the TRACKINGGROUPS view.                                        |
| TRACKING\_POINT\_ID     | The primary key of the tracking point to which this entry corresponds. This column links to the TRACKINGPOINTS view.                                        |
| TASK\_ID               | The primary key in the Business Performance Data Warehouse of the task to which this entry corresponds. This column links to the TASKS view.                |
| FUNCTIONAL\_TASK\_ID    | The primary key in the Business Performance Data Warehouse of the BPD instance to which this entry corresponds. This column links to the TASKS view.        |
| SNAPSHOT              | The snapshot (version) of the process application or toolkit to which this entry corresponds. If no snapshots exist, a Null value is stored in this column. |
| ACRONYM               | The acronym of the process application or toolkit to which this entry corresponds.                                                                          |
| TIME\_STAMP            | The date and time at which the corresponding tracking point was traversed.                                                                                  |
| TIME\_STAMP\_DAYS       | TIME\_STAMP truncated to days.                                                                                                                               |
| TIME\_STAMP\_WEEKS      | TIME\_STAMP truncated to weeks.                                                                                                                              |
| TIME\_STAMP\_MONTHS     | TIME\_STAMP truncated to months.                                                                                                                             |
| TIME\_STAMP\_QUARTERS   | TIME\_STAMP truncated to quarters.                                                                                                                           |
| TIME\_STAMP\_YEARS      | TIME\_STAMP truncated to years.                                                                                                                              |

- SNAPSHOTS view

The SNAPSHOTS view contains one row for each snapshot defined in the Workflow Center.
- TASKS view

The TASKS view contains one row for each task that is run and an additional row for each process instance that is started.
- TRACKINGGROUPS view

The TRACKINGGROUPS view contains one row for each tracking group defined in IBM Business Automation Workflow.
- TIMINGINTERVALS view (deprecated)

The TIMINGINTERVALS view contains one row for every timing interval defined in IBM Process Designer. When autotracking is enabled, Business Automation Workflow adds a timing interval for every activity in an autotracked BPD.
- TIMINGINTERVALVALUE view

In the TIMINGINTERVALVALUE view, a row is recorded each time a timing interval is traversed. When autotracking is enabled, a row is recorded each time an autotracked task is run.
- TRACKEDFIELDS view

The TRACKEDFIELDS view contains one row for every tracked field defined in the Process Designer.
- TRACKEDFIELDUSE view

In the TRACKEDFIELDUSE view, a row is recorded when a tracked field from a tracking group is used by a specific tracking point.
- TRACKINGPOINTS view

The TRACKINGPOINTS view contains one row for every tracking point defined in IBM Process Designer. When autotracking is enabled, two tracking points are created for each autotracked activity in order to mark the beginning and end of a task.
- TRACKINGPOINTVALUE view

In the TRACKINGPOINTVALUE view, a row is recorded each time a tracking point is traversed. When autotracking is enabled, there are two rows for every task that is run, because autotracking defines start and end tracking points for each autotracked activity.
- SLASTATUS view

The SLASTATUS view is an implicit tracking group view that tracks the status of each SLA as a result of an SLA roll-up.
- SLATHRESHOLDTRAVERSALS view

The SLATHRESHOLDTRAVERSALS view is an implicit tracking group view that tracks a value whenever an activity with an attached SLA completes. An activity has an attached SLA if there is an SLA with a condition dependent on a metric of that activity.