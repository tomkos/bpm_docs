<!-- image -->

# MIGRATION\_FRONT view

| Column name    | Type      | Comments                                                                                                                                                                                                                                                                                                                          |
|----------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PIID           | ID        | The process instance ID.                                                                                                                                                                                                                                                                                                          |
| SOURCE\_PTID    | ID        | The ID of the process template that is associated with the process instance before migration.                                                                                                                                                                                                                                     |
| TARGET\_PTID    | ID        | The ID of the process template that is associated with the process instance after migration.                                                                                                                                                                                                                                      |
| AIID           | ID        | The ID of an activity that was part of the process navigation front when the process was migrated. The migration front consists of the last activity reached by the process navigation on each parallel branch when the process was migrated.                                                                                     |
| SOURCE\_ATID    | ID        | The ID of the activity template before migration.                                                                                                                                                                                                                                                                                 |
| TARGET\_ATID    | ID        | The ID of the activity template after migration. If the activity was completed before the process instance was migrated, the activity template ID does not change.                                                                                                                                                                |
| MIGRATION\_TIME | Timestamp | The time that the process instance was migrated.                                                                                                                                                                                                                                                                                  |
| STATE          | Integer   | The state of the activity when the process instance was migrated. Possible values are:STATE\_READY (2)  STATE\_RUNNING (3)  STATE\_SKIPPED (4)  STATE\_FINISHED (5)  STATE\_FAILED (6)  STATE\_TERMINATED (7)  STATE\_CLAIMED (8)  STATE\_TERMINATING (9)  STATE\_FAILING (10)  STATE\_WAITING (11)  STATE\_EXPIRED (12)  STATE\_STOPPED (13) |
| SUBSTATE       | Integer   | The substate of the activity when the process instance was migrated. Possible values are:SUB\_STATE\_NONE (0)  SUB\_STATE\_EXPIRING (1)  SUB\_STATE\_SKIPPING (2)  SUB\_STATE\_RESTARTING (3)   SUB\_STATE\_FINISHING (4)  SUB\_STATE\_FAILING (5)                                                                                            |
| STOP\_REASON    | Integer   | The reason why the activity stopped. Possible values are:STOP\_REASON\_UNSPECIFIED (1)   STOP\_REASON\_ACTIVATION\_FAILED (2)   STOP\_REASON\_IMPLEMENTATION\_FAILED (3)   STOP\_REASON\_FOLLOW\_ON\_NAVIGATION\_FAILED (4)   STOP\_REASON\_EXIT\_CONDITION\_FALSE (5)                                                                             |