<!-- image -->

# Adding transaction support to Business Process Choreographer
web services applications

## About this task

- HTTP transport layer
- JMS transport layer

Business Process Choreographer runs each web service
operation request as a separate global transaction. Client applications
can be configured to use transaction support in one of the following
ways:

- Propagate the client's transaction context. Server-side request
processing is performed within the client application transaction
context and therefore committed (or backed out) together with the
client's transaction. Conversely, if the server encounters a
problem while the web service operation is running and requests a
rollback, the client application's transaction is also rolled back.
- Not use transaction support. Business Process Choreographer creates
a new global transaction in which to run the request, but server-side
request processing is not performed with the client application transaction
context.

The web service policy attached to the Business Process Choreographer
web service allows that each request message may contain a WS-AT transaction
context. If you choose to invoke the web service operations without
passing a client transaction context, it is safe to ignore the provider-side
transaction policy and configure the web service client without a
transaction policy.

For additional information about setting up WS-AT, see Avoid issues
when setting up Web Services Atomic Transaction (WS-AT).