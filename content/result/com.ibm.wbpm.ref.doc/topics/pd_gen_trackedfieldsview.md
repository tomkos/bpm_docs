# TRACKEDFIELDS view

The TRACKEDFIELDS view includes the following
columns:

| Column            | Description                                                                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TRACKED\_FIELD\_ID  | The primary key of the tracked field.                                                                                                                        |
| TRACKING\_GROUP\_ID | The primary key of the tracking group to which this tracked field belongs. This column links to the TRACKINGGROUPS view.                                     |
| NAME              | The name assigned to the tracked field in the Process Designer. When autotracking is enabled, this entry corresponds to the name of the associated activity. |
| DESCRIPTION       | The description of the tracked field (if one was provided in the Process Designer).                                                                          |
| FIELD\_TYPE        | The type of the tracked field as follows: 0= string, 1= number, 2= date.                                                                                     |
| SNAPSHOT          | The snapshot (version) of the process application or toolkit that contains the tracked field. If no snapshots exist, a Null value is stored in this column.  |
| ACRONYM           | The acronym of the process application or toolkit that contains the tracked field.                                                                           |