<!-- image -->

# ACTIVITY\_SERVICE view

| Column name    | Type   | Comments                                                       |
|----------------|--------|----------------------------------------------------------------|
| EIID           | ID     | The ID of the event instance.                                  |
| AIID           | ID     | The ID of the activity instance that is waiting for the event. |
| PIID           | ID     | The ID of the process instance that contains the event.        |
| VTID           | ID     | The ID of the service template that describes the event.       |
| PORT\_TYPE      | String | The name of the port type.                                     |
| NAME\_SPACE\_URI | String | The URI of the namespace.                                      |
| OPERATION      | String | The operation name of the service.                             |