<!-- image -->

# Deferred response with synchronous implementation

## Parameters

Event monitoring for Service Component Architecture (SCA) components includes the event points
that are shown in black , while the event points shown in blue  are used only to calculate and fire PMI/ARM statistics.

| Type        | Statistics           | Formula      | ARM Transaction   |
|-------------|----------------------|--------------|-------------------|
| Common      | TotalResponseTime    | t3 - t0      | X0.X1             |
| Common      | RequestDeliveryTime  | t'0 - t0     | X1.X2             |
| Common      | ResponseDeliveryTime | N/A          | N/A               |
| Common      | GoodRequests         | CountEXIT    | X1.X2             |
| Common      | BadRequests          | CountFAILURE | X1.X2             |
| Common      | ResponseTime         | t'1 - t'0    | X1.X2             |
| Reference A | GoodRefRequest       | CountEXIT    | X1.X2             |
| Reference A | BadRefRequests       | CountFAILURE | X1.X2             |
| Reference A | RefResponseTime      | t1 - t0      | X1.X2             |

Figure 1. Graphic representation of a deferred response with synchronous implementation

<!-- image -->

| Type        | Statistics                 | Formula      | ARM Transaction    |
|-------------|----------------------------|--------------|--------------------|
| Reference B | GoodRetrieveResult         | CountEXIT    | X1.X2              |
| Reference B | BadRetrieveResult          | CountFAILURE | X1.X2              |
| Reference B | ResultRetrieveResponseTime | Σ t3 - t2    | X1.X2              |
| Reference B | ResultRetrieveWaitTime     | Σ timeout    | X1.X2              |