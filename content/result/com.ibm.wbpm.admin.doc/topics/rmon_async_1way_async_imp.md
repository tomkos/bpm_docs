<!-- image -->

# Asynchronous one way with asynchronous implementation

## Parameters

Event monitoring for Service Component Architecture (SCA) components includes the event points
that are shown in black , while the event points shown in blue  are used only to calculate and fire PMI/ARM statistics.

| Type      | Statistics           | Formula      | ARM Transaction   |
|-----------|----------------------|--------------|-------------------|
| Common    | TotalResponseTime    | t1 - t0      | X0.X1             |
| Common    | RequestDeliveryTime  | t'0 - t0     | X1.X2             |
| Common    | ResponseDeliveryTime | N/A          | N/A               |
| Common    | GoodRequests         | CountEXIT    | X1.X2             |
| Common    | BadRequests          | CountFAILURE | X1.X2             |
| Common    | ResponseTime         | t2 - t0      | X1.X2             |
| Reference | GoodRefRequest       | CountEXIT    | X0.X1             |
| Reference | BadRefRequest        | CountFAILURE | X0.X1             |
| Reference | RefResponseDuration  | t1 - t0      | X0.X1             |

Figure 1. An asynchronous one-way call with an asynchronous implementation

<!-- image -->