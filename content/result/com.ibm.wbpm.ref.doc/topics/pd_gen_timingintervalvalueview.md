# TIMINGINTERVALVALUE view

The TIMINGINTERVALVALUE view includes the
following columns:

| Column                  | Description                                                                                                                                                 |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TIMING\_INTERVAL\_ID      | The primary key of the timing interval. This column links to the TIMINGINTERVALS view.                                                                      |
| START\_TRACKING\_POINT\_ID | The primary key of the tracking point that marks the beginning of the timing interval. This column links to the TRACKINGPOINTS view.                        |
| END\_TRACKING\_POINT\_ID   | The primary key of the tracking point that marks the end of the timing interval. This column links to the TRACKINGPOINTS view.                              |
| START\_TIME              | The date and time that the timing interval started.                                                                                                         |
| END\_TIME                | The date and time that the timing interval ended.                                                                                                           |
| DURATION                | The duration of the timing interval in milliseconds.                                                                                                        |
| START\_TASK\_ID           | The primary key in the Business Performance Data Warehouse of the task where this timing interval began. This column links to the TASKS view.               |
| END\_TASK\_ID             | The primary key in the Business Performance Data Warehouse of the task where this timing interval ended. This column links to the TASKS view.               |
| FUNCTIONAL\_TASK\_ID      | The primary key in the Business Performance Data Warehouse of the BPD instance that started this timing interval. This column links to the TASKS view.      |
| START\_SNAPSHOT          | The snapshot (version) of the tracking point that marks the beginning of the timing interval. If no snapshots exist, a Null value is stored in this column. |
| END\_SNAPSHOT            | The snapshot (version) of the tracking point that marks the end of the timing interval. If no snapshots exist, a Null value is stored in this column.       |