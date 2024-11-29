# SLATHRESHOLDTRAVERSALS view

The SLATHRESHOLDTRAVERSALS view includes the
following columns:

| Column              | Description                                                                                                                                                                                           |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| METRIC\_GUID         | The GUID of the metric referenced in the SLA.                                                                                                                                                         |
| METRIC\_VALUE        | The value of the metric referenced in the SLA.                                                                                                                                                        |
| TARGET\_VALUE        | The value that the metric is compared to in the SLA.                                                                                                                                                  |
| TRACKING\_POINT\_GUID | The GUID of the tracking point corresponding to where this traversal occurred, which is the end autotracking point for the activity.                                                                  |
| VIOLATION\_LEVEL     | An indication of how much of a violation this particular occurrence is. This value is only relevant and, thus, populated for greater than SLA conditions, and is basically METRIC\_VALUE/TARGET\_VALUE. |
| TRACKING\_GROUP\_ID   | The primary key of the Tracking Group to which this entry corresponds. This column links to the TRACKINGGROUPS view.                                                                                  |
| TRACKING\_POINT\_ID   | The primary key of the Tracking Point to which this entry corresponds. This column links to the TRACKINGPOINTS view.                                                                                  |
| TASK\_ID             | The primary key of the task to which this entry corresponds. This column links to the TASKS view.                                                                                                     |
| FUNCTIONAL\_TASK\_ID  | The primary key of the BPD instance to which this entry corresponds. This column links to the TASKS view.                                                                                             |
| TIME\_STAMP          | The date and time at which the corresponding tracking point was traversed.                                                                                                                            |
| SNAPSHOT            | The snapshot (version) of the process application or toolkit to which this entry corresponds. If no snapshots exist, a Null value is stored in this column.                                           |
| ACRONYM             | The acronym of the process application or toolkit to which this entry corresponds.                                                                                                                    |
| TIME\_STAMP\_DAYS     | TIME\_STAMP truncated to days.                                                                                                                                                                         |
| TIME\_STAMP\_WEEKS    | TIME\_STAMP truncated to weeks.                                                                                                                                                                        |
| TIME\_STAMP\_MONTHS   | TIME\_STAMP truncated to months.                                                                                                                                                                       |
| TIME\_STAMP\_QUARTERS | TIME\_STAMP truncated to quarters.                                                                                                                                                                     |
| TIME\_STAMP\_YEARS    | TIME\_STAMP truncated to years.                                                                                                                                                                        |