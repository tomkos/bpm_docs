<!-- image -->

# Deferred response with asynchronous result retrieve

## Parameters

Event monitoring for Service Component Architecture (SCA) components includes the event points
that are shown in black , while the event points shown in blue  are used only to calculate and fire PMI/ARM statistics.

| Type        | Statistics            | Formula               | ARM Transaction   |
|-------------|-----------------------|-----------------------|-------------------|
| Common      | TotalResponseTime     | t3 - t0               | X0.X1             |
| Common      | RequestDeliveryTime   | t'0 - t0              | X1.X2             |
| Common      | ResponseDeliveryTime  | N/A                   | N/A               |
| Common      | GoodRequests          | CountEXIT             | X1.X2             |
| Common      | BadRequests           | CountFAILURE          | X1.X2             |
| Common      | ResponseTime          | See specific diagrams | X1.X2             |
| Reference A | GoodReferenceRequest  | CountEXIT             | X1.X2             |
| Reference A | BadReferenceRequests  | CountFAILURE          | X1.X2             |
| Reference A | ReferenceResponseTime | t1 - t0               | X1.X2             |

Figure 1. A deferred response with an asynchronous result retrieve

<!-- image -->

| Type        | Statistics                 | Formula      | ARM Transaction   |
|-------------|----------------------------|--------------|-------------------|
| Reference B | GoodRetrieveResult         | CountEXIT    | X'0.X'1           |
| Reference B | BadRetrieveResult          | CountFAILURE | X'0.X'1           |
| Reference B | RetrieveResultResponseTime | Σ t3 - t2    | X'0.X'1           |
| Reference B | RetrieveResultWaitTime     | Σ timeout    | X'0.X'1           |