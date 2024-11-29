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

## Interface ServiceCallback

- public interface ServiceCallback
The callback interface is implemented by service components that need to handle asynchronous callback interactions.

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
onInvokeResponse(Ticket ticket,
                java.lang.Object output,
                java.lang.Exception exception)
Callback method invoked by the SCA runtime to pass an asynchronous response to a service component.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - onInvokeResponse
void onInvokeResponse(Ticket ticket,
                    java.lang.Object output,
                    java.lang.Exception exception)
Callback method invoked by the SCA runtime to pass an asynchronous response to a service component.
Parameters:ticket - The ticket identifying the asynchronous invocation, initially returned by the invokeAsyncWithCallback() method.output - The business data returned by the target business operation.exception - Any exception thrown from the target business operation.