<!-- image -->

# JMS temporary dynamic response destination correlation scheme

The static response destination specified in the import is used
to derive the nature of the temporary dynamic destination queue or
topic. This is set in the ReplyTo field of
the request, and the JMS import listens for responses on that destination.
When the response is received it is requeued to the static response
destination for asynchronous processing. The CorrelationID field
of the response is not used, and does not need to be set.

## Transactional issues

When a temporary dynamic destination is being used, the response must be consumed in the same
thread as the sent response. The request must be sent outside the global transaction, and must be
committed before it is received by the back-end service, and a response returned.

## Persistence

Temporary dynamic queues are
short-lived entities and do not guarantee the same level of persistence
associated with a static queue or topic. A temporary dynamic queue
or topic will not survive a server restart and neither will messages.
After the message has been requeued to the static response destination
it retains the persistence defined in the message.

## Timeout

The import waits to receive the
response on the temporary dynamic response destination for a fixed
amount of time. This time interval will be taken from the SCA Response
Expiration time qualifier, if it is set, otherwise the time defaults
to 60 seconds. If the wait time is exceeded the import throws a ServiceTimeoutRuntimeException.