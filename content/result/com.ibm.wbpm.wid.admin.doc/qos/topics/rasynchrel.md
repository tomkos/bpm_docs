<!-- image -->

# Asynchronous reliability qualifiers

You can specify, asynchronous
reliability qualifiers for the reference to support asynchronous invocation of components. They
only take effect when asynchronous programming calls are used by the
client to invoke the service. The reliability, request expiration,
and response expiration reference qualifiers are ignored by the runtime
functions for synchronous interactions.

## Reliability

The reliability  qualifier
determines the quality of the delivery of an asynchronous message.
In general, better performance usually means less reliable message
delivery.

Location: A reliability qualifier is set on
a reference.

- Assured (persistent) - The client application
cannot tolerate the loss of a request or response message.
- Best effort (nonpersistent) - The client
application can tolerate the possible loss of the request or response
message.

## Request expiration

Request expiration is
the length of time, measured in milliseconds, after which an asynchronous
request will be discarded if it has not been delivered, beginning
from the time when the request is issued. A zero (0) denotes an indefinite
expiration.

Location: A request expiration qualifier
is set on a reference.

## Response expiration

Response expiration is
the length of time, measured in milliseconds, that the runtime environment
must retain an asynchronous response or must provide a callback, beginning
from the time when the request is issued. A zero (0) denotes an indefinite
expiration.

Location: A response expiration qualifier
is set on a reference.