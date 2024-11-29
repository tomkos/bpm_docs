# TRACKINGPOINTS view

The TRACKINGPOINTS view includes the following columns:

| Column            | Description                                                                                                                                               |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| TRACKING\_POINT\_ID | The primary key of the tracking point.                                                                                                                    |
| TRACKING\_GROUP\_ID | The primary key of the tracking group to which this tracking point belongs. This column links to the TRACKINGGROUPS view.                                 |
| NAME              | The name assigned to the tracking point in Process Designer. When autotracking is enabled, this entry corresponds to the name of the associated activity. |
| DESCRIPTION       | The description of the tracking point (if one was provided in Process Designer).                                                                          |
| SNAPSHOT          | The snapshot (version) of the process application or toolkit that contains the tracking point.                                                            |
| ACRONYM           | The acronym of the process application or toolkit that contains the tracking point.                                                                       |