<!-- image -->

# Deferred response with asynchronous implementation

## Parameters

Event monitoring for Service Component Architecture (SCA) components includes the event points
that are shown in black , while the event points shown in blue  are used only to calculate and fire PMI/ARM statistics.

In the following table and diagram, the current ARM transaction (denoted as
X1) is created when the calling service component was invoked for the
first time. If the caller is not a service component, the current ARM transaction is used, or a new
one is created. If it is not the starting transaction, it has a parent, as represented in the
following table and diagram with the notation Xn.Xn+1. The
notation is used to show the transaction lineage. Every SCA invocation starts a new transaction,
which is parented by the current transaction of the caller. You can create new transactions and you
can access the current transaction, but you cannot modify the SCA transaction lineage.

| Type        | Statistics           | Formula      | ARM Transaction   |
|-------------|----------------------|--------------|-------------------|
| Common      | TotalResponseTime    | t3 - t0      | X0.X1             |
| Common      | RequestDeliveryTime  | t'0 - t0     | X1.X2             |
| Common      | ResponseDeliveryTime | t'03 - t'2   | X1.X2             |
| Common      | GoodRequests         | CountEXIT    | X1.X2             |
| Common      | BadRequests          | CountFAILURE | X1.X2             |
| Common      | ResponseTime         | t'3 - t'0    | X1.X2             |
| Reference A | GoodRefRequest       | CountEXIT    | X0.X1             |
| Reference A | BadRefRequests       | CountFAILURE | X0.X1             |
| Reference A | RefResponseTime      | t1 - t0      | X0.X1             |
| Target A    | GoodTargetSubmit     | CountEXIT    | X1.X2             |
| Target A    | BadTargetSubmit      | CountFAILURE | X1.X2             |
| Target A    | TargetSubmitTime     | t'1 - t'0    | X1.X2             |

<!-- image -->

| Type        | Statistics                 | Formula      | ARM Transaction   |
|-------------|----------------------------|--------------|-------------------|
| Reference B | GoodResultSubmit           | CountEXIT    | X0.X1             |
| Reference B | BadResultSubmit            | CountFAILURE | X0.X1             |
| Reference B | ResultResponseTime         | t'3 - t'2    | X0.X1             |
| Target B    | GoodResultRetrieve         | CountEXIT    | X1.X2             |
| Target B    | BadResultRetrieve          | CountFAILURE | X1.X2             |
| Target B    | ResultRetrieveResponseTime | Σ t3 - t2    | X1.X2             |
| Target B    | ResultRetrieveWaitTime     | Σ timeout    | X1.X2             |