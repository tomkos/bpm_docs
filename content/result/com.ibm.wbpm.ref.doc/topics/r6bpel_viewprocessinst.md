<!-- image -->

# PROCESS\_INSTANCE view

| Column name                         | Type      | Comments                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PTID                                | ID        | The process template ID.                                                                                                                                                                                                                                                                                                  |
| PIID                                | ID        | The process instance ID.                                                                                                                                                                                                                                                                                                  |
| COMPLETED                           | Timestamp | The time the process instance completed.                                                                                                                                                                                                                                                                                  |
| CONTINUE\_ON\_ERROR                   | Boolean   | Specifies what happens to a process if an unexpected fault is raised and a fault handler is not defined for that fault. Possible values are: True Standard fault handling is applied. False Navigation of the process stops so that the process can be repaired.                                                          |
| CREATED                             | Timestamp | The time the process instance is created.                                                                                                                                                                                                                                                                                 |
| CUSTOM\_TEXT1  through  CUSTOM\_TEXT8 | String    | Inline custom properties that can be set for a BPEL process. The values of these fields can be set either in Integration Designer, or by using the Business Flow Manager EJB API.                                                                                                                                         |
| DESCRIPTION                         | String    | If the description of the process template contains placeholders, this column contains the description of the process instance with the placeholders resolved.                                                                                                                                                            |
| IS\_MIGRATED                         | Boolean   | Specifies whether the process instance has been migrated from an older version of the process. If this attribute is set to TRUE, the process instance has been migrated.                                                                                                                                                  |
| NAME                                | String    | The name of the process instance.                                                                                                                                                                                                                                                                                         |
| PARENT\_NAME                         | String    | The name of the parent process instance.                                                                                                                                                                                                                                                                                  |
| PARENT\_PIID                         | ID        | The ID of the parent process instance.                                                                                                                                                                                                                                                                                    |
| RESUMES                             | Timestamp | The time when the process instance is to be resumed automatically.                                                                                                                                                                                                                                                        |
| STARTER                             | String    | The principal ID of the starter of the process instance.                                                                                                                                                                                                                                                                  |
| STARTED                             | Timestamp | The time the process instance started.                                                                                                                                                                                                                                                                                    |
| STATE                               | Integer   | The state of the process instance. Possible values are: STATE\_READY (1)  STATE\_RUNNING (2)  STATE\_FINISHED (3)  STATE\_COMPENSATING (4)  STATE\_INDOUBT (10)  STATE\_FAILED (5)  STATE\_TERMINATED (6)  STATE\_COMPENSATED (7)  STATE\_COMPENSATION\_FAILED (12)  STATE\_TERMINATING (8)  STATE\_FAILING (9)  STATE\_SUSPENDED (11) |
| TEMPLATE\_DESCR                      | String    | Description of the associated process template.                                                                                                                                                                                                                                                                           |
| TEMPLATE\_NAME                       | String    | The name of the associated process template.                                                                                                                                                                                                                                                                              |
| TOP\_LEVEL\_PIID                      | ID        | The process instance ID of the top-level process instance. If there is no top-level process instance, this is the process instance ID of the current process instance.                                                                                                                                                    |
| TOP\_LEVEL\_NAME                      | String    | The name of the top-level process instance. If there is no top-level process instance, this is the name of the current process instance.                                                                                                                                                                                  |