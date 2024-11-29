# TRACKINGPOINTVALUE view

The TRACKINGPOINTVALUE view includes the following
columns:

| Column              | Description                                                                                                                                                  |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TRACKING\_POINT\_ID   | The primary key of the tracking point. This column links to the TRACKINGPOINTS view.                                                                         |
| TASK\_ID             | The primary key in the Business Performance Data Warehouse of the task that corresponds to this tracking point. This column links to the TASKS view.         |
| FUNCTIONAL\_TASK\_ID  | The primary key in the Business Performance Data Warehouse of the BPD instance that corresponds to this tracking point. This column links to the TASKS view. |
| TIME\_STAMP          | The date and time at which the tracking point was traversed.                                                                                                 |
| SNAPSHOT            | The snapshot (version) of the task that corresponds to this tracking point. If no snapshots exist, a Null value is stored in this column.                    |
| ACRONYM             | The acronym of the process application or toolkit that contains the task that corresponds to this tracking point.                                            |
| TIME\_STAMP\_DAYS     | TIME\_STAMP truncated to days.                                                                                                                                |
| TIME\_STAMP\_WEEKS    | TIME\_STAMP truncated to weeks.                                                                                                                               |
| TIME\_STAMP\_MONTHS   | TIME\_STAMP truncated to months.                                                                                                                              |
| TIME\_STAMP\_QUARTERS | TIME\_STAMP truncated to quarters.                                                                                                                            |
| TIME\_STAMP\_YEARS    | TIME\_STAMP truncated to years.                                                                                                                               |