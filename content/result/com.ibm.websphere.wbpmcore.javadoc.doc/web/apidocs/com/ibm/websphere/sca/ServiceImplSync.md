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

## Interface ServiceImplSync

- public interface ServiceImplSync
The ServiceImplSync interface is implemented by service components that need to handle synchronous service invocations generically.
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

java.lang.Object
invoke(OperationType operationType,
      java.lang.Object input)
Handles a synchronous service invocation.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - invoke
java.lang.Object invoke(OperationType operationType,
                      java.lang.Object input)
                        throws ServiceBusinessException
Handles a synchronous service invocation.
Parameters:operationType - The OperationType representing the business operation.input - The input business data.
Returns:Object The output business data.
Throws:
ServiceBusinessException - An exception representing a business exception.