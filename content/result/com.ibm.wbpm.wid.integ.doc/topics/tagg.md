<!-- image -->

# Aggregating and broadcasting messages

## Before you begin

- Shared context

Shared context is a thread-based memory location that is shared across all instances of the service message object that are running within the same thread for the request or response flow. The shared context is used during a Fan Out / Fan In aggregation to temporarily store service responses.
- Combining results from different services

You can send one request to multiple services by using the Fan Out primitive, receive responses from those services and then use a Fan in primitive and a Mapping primitive to combine the responses into a new message.
- Broadcasting messages

For broadcasting, you use the Fan Out primitive in isolation to send a message one way such as when you want to send a notification and do not need a response.
- Performing chained aggregation

You can invoke multiple services sequentially from a mediation flow using the Service Invoke primitive and aggregate the response from each service. This type of chained aggregation is achieved by using the Service Invoke primitive to invoke the first service, and then storing the service response in a placing the service response in the transient context by using a Mapping primitive. The message is then propagated to a second Service Invoke primitive.
- Example: Fan Out and Fan In

This example shows how elements in an array of business objects are updated with the result of a service invocation response. This is achieved by using the Fan Out, Service Invoke, Mapping (using XSL Transformation) and Fan In primitives.