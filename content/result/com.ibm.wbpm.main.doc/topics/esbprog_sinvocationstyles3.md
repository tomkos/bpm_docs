<!-- image -->

# Asynchronous invocation

With asynchronous invocation in SCA, there are three types of asynchronous interaction styles
available: one way, deferred response, and request with callback. With all three types of
asynchronous invocation, the service requester receives control back immediately from the SCA
runtime.

- Asynchronous with deferred response, where the service requester calls an operation on
the service provider, and then continues processing. At a later time, the service requester calls
the service provider for a response.
- Asynchronous with callback, where the service requester calls an operation on the service
provider and specifies a callback handler. When the response is available, the SCA runtime returns
the response to the requester by calling this callback handler.

## Asynchronous with deferred response SCA invocation

Asynchronous with deferred response SCA invocation is useful if the service requester has further
processing to perform that does not depend on information to be returned in the response.

Figure 1. Asynchronous with deferred response SCA invocation

<!-- image -->

## Example scenario for asynchronous with deferred response SCA invocation

Figure 2. Car insurance comparison website using asynchronous with deferred response invocation

<!-- image -->

The service requester creates a request to service provider A, and calls the SCA runtime. The SCA
runtime returns control to the requester immediately, allowing it to continue processing. The
service requester is then able to create a second request for service provider B.

The service requester makes further calls to the SCA runtime to collect the responses. These are
processed, and the final response is then returned to the user.

## Asynchronous with callback SCA invocation

In this invocation style, the calling component (service requester) specifies a callback handler
that will be used to receive and process the response. After the service requester has sent the
request, the thread that made the request completes processing. SCA runtime resources associated
with that thread are then released. When the response from the service provider is available, a new
SCA runtime thread is used to call the callback handler to perform the processing required by the
service requester.

Figure 3.  Asynchronous with callback SCA invocation

<!-- image -->

## Example scenario asynchronous with callback SCA invocation

A company would prefer to use this style of invocation if they perform audits. The service
requester wants to update employees' payment details, and only needs to be notified when the
update has been made.

The service requester sends a series of calls to update employees' payment details, to the
service provider. The service provider invokes an audit service for each request. The audit can take
from a few hours to a whole day to make a record of each employees payment details. When the audit
service is complete, the response is returned to the service requester using a callback handler, and
an email is sent to the user to notify them that the update has been successful.