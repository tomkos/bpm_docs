<!-- image -->

# Asynchronous callback with asynchronous implementation

## Parameters

Event monitoring for Service Component Architecture (SCA) components includes the event points
that are shown in black , while the event points shown in blue  are used only to calculate and fire PMI/ARM statistics.

| Type        | Statistics           | Formula      | ARM Transaction   |
|-------------|----------------------|--------------|-------------------|
| Common      | TotalResponseTime    | t2 - t0      | X0.X1             |
| Common      | RequestDeliveryTime  | t'0 - t0     | X1.X2             |
| Common      | ResponseDeliveryTime | t2 - t'2     | X1.X2             |
| Common      | GoodRequests         | CountEXIT    | X1.X2             |
| Common      | BadRequests          | CountFAILURE | X1.X2             |
| Common      | ResponseTime         | t'3 - t'0    | X1.X2             |
| Reference A | GoodRefRequest       | CountEXIT    | X0.X1             |
| Reference A | BadRefRequests       | CountFAILURE | X0.X1             |
| Reference A | RefResponseTime      | t1 - t0      | X0.X1             |
| Target A    | GoodTargetSubmit     | CountEXIT    | X1.X2             |
| Target A    | BadTargetSubmit      | CountFAILURE | X1.X2             |
| Target A    | TargetSubmitTime     | t'1 - t'0    | X1.X2             |

Figure 1. An asynchronous callback with an asynchronous implementation

<!-- image -->

| Type        | Statistics    | Formula      | ARM Transaction   |
|-------------|---------------|--------------|-------------------|
| Reference B | GoodCBSubmit  | CountEXIT    | X1.X2             |
| Reference B | BadCBSubmit   | CountFAILURE | X1.X2             |
| Reference B | CBSubmitTime  | t'3 - t'2    | X1.X2             |
| Target B    | GoodCB        | CountEXIT    | X0.X1             |
| Target B    | BadCB         | CountFAILURE | X0.X1             |
| Target B    | CBTime        | t3 - t2      | X0.X1             |