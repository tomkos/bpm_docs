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

## Interface Service

- public interface Service
The Service interface provides information about, and access to, an SCA service. The object returned by the ServiceManager.locateService() method implements
 this interface.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
ASYNC
Used to indicate an asynchronous preferred interaction style

static java.lang.String
COPYRIGHT 

static int
NOWAIT
Used to specify a timeout on the invokeResponse() method.

static java.lang.String
SYNC
Used to indicate a synchronous preferred interaction style

static int
WAIT
Used to specify a timeout on the invokeResponse() method.
    - Method Summary

Methods 

Modifier and Type
Method and Description

EndpointReference
getEndpointReference()
Returns an endpoint reference representing the endpoint of the target service.

java.lang.String
getPreferredInteractionStyle(OperationType operationType)
Returns the preferred interaction style for the specified operation.

Reference
getReference()
Returns the SCDL reference object representing the reference to the target service.

java.lang.Object
invoke(OperationType operationType,
      java.lang.Object input)
Synchronously invokes a business operation on the target service.

java.lang.Object
invoke(java.lang.String operationName,
      java.lang.Object input)
Synchronously invokes a business operation on the target service.

Ticket
invokeAsync(OperationType operationType,
           java.lang.Object input)
Sends an asynchronous request to a business operation on the target service.

Ticket
invokeAsync(java.lang.String operationName,
           java.lang.Object input)
Sends an asynchronous request to a business operation on the target service.

Ticket
invokeAsyncWithCallback(OperationType operationType,
                       java.lang.Object input)
Sends an asynchronous request to a business operation on the target service.

Ticket
invokeAsyncWithCallback(java.lang.String operationName,
                       java.lang.Object input)
Sends an asynchronous request to a business operation on the target service.

java.lang.Object
invokeResponse(Ticket ticket,
              long timeout)
Retrieves the response to an asynchronous request.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- WAIT
static final int WAIT
Used to specify a timeout on the invokeResponse() method.
 The response operation will not return until the response data is available.
See Also:Constant Field Values

- NOWAIT
static final int NOWAIT
Used to specify a timeout on the invokeResponse() method.
 The response operation will return the response if available otherwise it will throw a ServiceTimeoutRuntimeException
See Also:Constant Field Values

- SYNC
static final java.lang.String SYNC
Used to indicate a synchronous preferred interaction style
See Also:Constant Field Values

- ASYNC
static final java.lang.String ASYNC
Used to indicate an asynchronous preferred interaction style
See Also:Constant Field Values

- Method Detail

### Method Detail

    - invoke
java.lang.Object invoke(java.lang.String operationName,
                      java.lang.Object input)
                        throws ServiceBusinessException
Synchronously invokes a business operation on the target service.
Parameters:operationName - The name of the operation.input - The input business data.
Returns:The output business data.
Throws:
ServiceBusinessException - Business exception thrown by the target business operation.
    - invoke
java.lang.Object invoke(OperationType operationType,
                      java.lang.Object input)
                        throws ServiceBusinessException
Synchronously invokes a business operation on the target service.
Parameters:operationType - The OperationType representing the target operation.input - The input business data.
Returns:The output business data.
Throws:
ServiceBusinessException - Business exception thrown by the target business operation.
    - invokeAsync
Ticket invokeAsync(java.lang.String operationName,
                 java.lang.Object input)
Sends an asynchronous request to a business operation on the target service.
 The asynchronous response can be retrieved later by calling the invokeResponse method.
Parameters:operationName - The name of the operation.input - The input business data.
Returns:The ticket representing the asynchronous invocation.
    - invokeAsync
Ticket invokeAsync(OperationType operationType,
                 java.lang.Object input)
Sends an asynchronous request to a business operation on the target service.
 The asynchronous response can be retrieved later by calling the invokeResponse method.
Parameters:operationType - The OperationType representing the target operation.input - The input business data.
Returns:The ticket identifying the asynchronous invocation.
    - invokeAsyncWithCallback
Ticket invokeAsyncWithCallback(java.lang.String operationName,
                             java.lang.Object input)
Sends an asynchronous request to a business operation on the target service.
 The current component will be called back later and passed the asynchronous response.
Parameters:operationName - The name of the operation.input - The input business data.
Returns:The ticket identifying the asynchronous invocation.
    - invokeAsyncWithCallback
Ticket invokeAsyncWithCallback(OperationType operationType,
                             java.lang.Object input)
Sends an asynchronous request to a business operation on the target service.
 The current component will be called back later and passed the asynchronous response.
Parameters:operationType - The OperationType representing the target operation.input - The input business data.
Returns:The ticket identifying the asynchronous invocation.
    - invokeResponse
java.lang.Object invokeResponse(Ticket ticket,
                              long timeout)
                                throws ServiceBusinessException
Retrieves the response to an asynchronous request.
Parameters:ticket - The ticket identifying the asynchronous interaction, returned from a previous call to the invokeAsync() method.timeout - The time to wait for the response in milliseconds.
Returns:Object The output business data.
Throws:
ServiceBusinessException - Business exception thrown by the target business operation.
    - getPreferredInteractionStyle
java.lang.String getPreferredInteractionStyle(OperationType operationType)
Returns the preferred interaction style for the specified operation.
Parameters:operationType - The OperationType representing the target operation.
Returns:The preferred interaction style.
    - getReference
Reference getReference()
Returns the SCDL reference object representing the reference to the target service.
Returns:The SCDL reference object.
    - getEndpointReference
EndpointReference getEndpointReference()
Returns an endpoint reference representing the endpoint of the target service.
Returns:The endpoint reference for the target service.