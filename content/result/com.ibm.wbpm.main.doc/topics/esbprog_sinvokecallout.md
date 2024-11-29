<!-- image -->

# Service Invoke and Callout nodes

## Service Invoke mediation primitive

A Service Invoke mediation primitive is used to call a service from inside a mediation flow,
rather than waiting until the end of the mediation flow and using the Callout node. The input
message is used to call the service, and if the call is successful, the response is used to create
the output message. If the call is unsuccessful, you can retry the same service or call another
service.

You can have multiple Service Invoke mediation primitives inside one mediation flow. Therefore,
you can have a series of service calls. You can use the Service Invoke mediation primitive in a
request or response mediation flow.

## Callout node

The Callout receives the message and calls the requested service and operation. There is a
Callout node for each connected target operation in the mediation flow.

If the call is successful, the Callout Response node in the response flow receives the response
message.

If the call is unsuccessful, the Callout can be set to retry service invocations depending on the
type of fault received.

- Comparison of the Service Invoke mediation primitive and the Callout node

You can call a service using either a Service Invoke mediation primitive or a Callout node. You must consider the similarities and differences between using either the Service Invoke mediation primitive and the Callout node.
- Retry

Callout nodes and Service Invoke mediation primitives provide retry capabilities for failed service invocations. A number of properties need to be set in order to enable and configure the retry.