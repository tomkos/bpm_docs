<!-- image -->

# Asynchronous callback with synchronous implementation

## Parameters

Event monitoring for Service Component Architecture (SCA) components includes the event points
that are shown in black , while the event points shown in blue  are used only to calculate and fire PMI/ARM statistics.

| Type      | Statistics           | Formula      | ARM Transaction   |
|-----------|----------------------|--------------|-------------------|
| Common    | TotalResponseTime    | t2 - t0      | X0.X1             |
| Common    | RequestDeliveryTime  | t'0 - t0     | X1.X2             |
| Common    | ResponseDeliveryTime | t2 - t'1     | X1.X2             |
| Common    | GoodRequests         | CountEXIT    | X1.X2             |
| Common    | BadRequests          | CountFAILURE | X1.X2             |
| Common    | ResponseTime         | t3 - t2      | X1.X2             |
| Reference | GoodRefRequest       | CountEXIT    | X1.X2             |
| Reference | BadRefRequests       | CountFAILURE | X1.X2             |
| Reference | RefResponseTime      | t'1 - t'0    | X1.X2             |

Figure 1. Diagram of an asynchronous callback with a synchronous implementation

<!-- image -->

| Type     | Statistics    | Formula      | ARM Transaction    |
|----------|---------------|--------------|--------------------|
| Callback | GoodCB        | CountEXIT    | X1.X3              |
| Callback | BadCB         | CountFAILURE | X1.X3              |
| Callback | CBTime        | t3 - t2      | X1.X3              |