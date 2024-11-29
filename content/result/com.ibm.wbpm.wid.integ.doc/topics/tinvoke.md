<!-- image -->

# Invoking a service

1. If you need to, create an interface and the operation.
2. Click the operation to open its implementation.
3 You now have two options:
    1. To invoke the service inline, add the Service Invoke primitive
to the canvas.
    2. To use a callout invoke, add a callout to the canvas.
4. Select the reference and operation that you want to invoke.
5. Wire the primitives as you normally would and set their properties.

- Invoking a service by using a callout

Invoking or calling a service in a mediation flow by using a callout is discussed. In this case, the response is in a different transaction, in a response flow. The call is made at the end of a request flow.
- Invoking a service within a flow

Use a Service Invoke mediation primitive to call an intermediate service as part of a normal mediation flow. The result of the call is returned in the same transaction.
- Retrying a failed service invocation

Callout and Service Invoke primitives provide retry capabilities for failed service invocations.