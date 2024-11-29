<!-- image -->

# Structure of BPEL process events for AuditLog

The Audit Log State Observer is one of the creators of BPEL process events. It stores the
events into a database table (AUDIT\_LOG\_T) that you can see in the AUDIT\_LOG database
view.

The following table describes the columns in the AUDIT\_LOG database view.

| Column name      | Description                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------|
| ALID             | ID of the audit log entry                                                                                         |
| eventTime        | Local time when the event occurred                                                                                |
| eventUTC         | Time when the event occurred                                                                                      |
| auditEvent       | Event type. For more information, see Process events.                                                             |
| PTID             | ID of the process template                                                                                        |
| PPID             | ID of the process instance                                                                                        |
| AIID             | <empty>                                                                                                           |
| SIID             | <empty>                                                                                                           |
| scopeName        | <empty>                                                                                                           |
| processTemplName | Name of the process template                                                                                      |
| processInstName  | Name of the process instance                                                                                      |
| topLevelPiName   | Name of the top level process instance                                                                            |
| topLevelPIID     | ID of the top level process instance                                                                              |
| parentPiName     | Name of the parent process instance                                                                               |
| parentPIID       | ID of the parent process instance                                                                                 |
| validFrom        |                                                                                                                   |
| validFromUTC     |                                                                                                                   |
| principal        | Name of the principal on whose request the event was triggerred                                                   |
| description      | Resolved description string, where placeholders in the template description are replaced by their current values. |
| userName         | The Workitem owner of a deleted or created Workitem.                                                              |
| additionalInfo   | Additional information about the event                                                                            |