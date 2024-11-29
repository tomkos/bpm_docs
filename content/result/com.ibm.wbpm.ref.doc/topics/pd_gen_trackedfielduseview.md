# TRACKEDFIELDUSE view

The TRACKEDFIELDUSE view includes the following columns:

| Column               | Description                                                                                                                                     |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| TRACKED\_FIELD\_USE\_ID | The unique identifier (primary key) for this use of the tracked field.                                                                          |
| TRACKING\_GROUP\_ID    | The primary key of the tracking group to which this tracked field belongs. This column links to the TRACKINGGROUPS view.                        |
| TRACKING\_POINT\_ID    | The primary key of the tracking point that uses this tracked field. This column links to the TRACKINGPOINTS view.                               |
| TRACKED\_FIELD\_ID     | The primary key of the tracked field. This column links to the TRACKEDFIELDS view.                                                              |
| SNAPSHOT             | The snapshot (version) of the tracking group to which this tracked field belongs. If no snapshots exist, a Null value is stored in this column. |
| ACRONYM              | The acronym of the process application or toolkit that contains the tracking group to which this tracked field belongs.                         |