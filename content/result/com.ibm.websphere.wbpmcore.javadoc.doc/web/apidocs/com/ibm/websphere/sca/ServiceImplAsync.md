- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Interface ServiceImplAsync

- public interface ServiceImplAsync
The ServiceImplAsync interface is implemented by service components that need to handle asynchronous service invocations generically.
 Typically the component implementation will look at the operationType representing the invoked business operation and will dispatch
 to the corresponding business logic.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

void
invokeAsync(OperationType operationType,
           java.lang.Object input,
           ServiceCallback callback,
           Ticket ticket)
Handles an asynchronous service invocation.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - invokeAsync
void invokeAsync(OperationType operationType,
               java.lang.Object input,
               ServiceCallback callback,
               Ticket ticket)
Handles an asynchronous service invocation.
Parameters:operationType - The OperationType representing the business operation.input - The input business data.callback - An instance of ServiceCallback that the service component must use to send an asynchronous response.ticket - A ticket identifying the current asynchronous interaction..
Throws:
ServiceBusinessException - An exception representing a business exception.