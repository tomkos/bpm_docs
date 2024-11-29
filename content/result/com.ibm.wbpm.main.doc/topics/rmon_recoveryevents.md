<!-- image -->

# Recovery events

| Event Name                     | Event Nature    | Event Contents      | Type      |
|--------------------------------|-----------------|---------------------|-----------|
| recovery:WBI.Recovery.FAILURE  | FAILURE         | MsgId               | string    |
| recovery:WBI.Recovery.FAILURE  | FAILURE         | DestModuleName      | string    |
| recovery:WBI.Recovery.FAILURE  | FAILURE         | DestComponentName   | string    |
| recovery:WBI.Recovery.FAILURE  | FAILURE         | DestMethodName      | string    |
| recovery:WBI.Recovery.FAILURE  | FAILURE         | SourceModuleName    | string    |
| recovery:WBI.Recovery.FAILURE  | FAILURE         | SourceComponentName | string    |
| recovery:WBI.Recovery.FAILURE  | FAILURE         | ResubmitDestination | string    |
| recovery:WBI.Recovery.FAILURE  | FAILURE         | ExceptionDetails    | string    |
| recovery:WBI.Recovery.FAILURE  | FAILURE         | SessionId           | string    |
| recovery:WBI.Recovery.FAILURE  | FAILURE         | FailureTime         | dateTime  |
| recovery:WBI.Recovery.FAILURE  | FAILURE         | ExpirationTime      | dateTime  |
| recovery:WBI.Recovery.FAILURE  | FAILURE         | Status              | int       |
| recovery:WBI.Recovery.FAILURE  | FAILURE         | MessageBody         | byteArray |
| recovery:WBI.Recovery.FAILURE  | FAILURE         | Deliverable         | boolean   |
| recovery:WBI.Recovery.DEADLOOP | DEADLOOP        | DeadloopMsgId       | string    |
| recovery:WBI.Recovery.DEADLOOP | DEADLOOP        | SIBusName           | string    |
| recovery:WBI.Recovery.DEADLOOP | DEADLOOP        | QueueName           | string    |
| recovery:WBI.Recovery.DEADLOOP | DEADLOOP        | Reason              | string    |
| recovery:WBI.Recovery.RESUBMIT | RESUBMIT        | MsgId               | string    |
| recovery:WBI.Recovery.RESUBMIT | RESUBMIT        | OriginalMesId       | string    |
| recovery:WBI.Recovery.RESUBMIT | RESUBMIT        | ResubmitCount       | int       |
| recovery:WBI.Recovery.RESUBMIT | RESUBMIT        | Description         | string    |
| recovery:WBI.Recovery.DELETE   | DELETE          | MsgId               | string    |
| recovery:WBI.Recovery.DELETE   | DELETE          | deleteTime          | dateTime  |
| recovery:WBI.Recovery.DELETE   | DELETE          | Description         | string    |