<!-- image -->

# Common patterns of usage for error handling

## Synchronous invocation

Figure 1. Synchronous invocation error handling

<!-- image -->

As shown in Figure 1 there are no queues in a
synchronous flow. If an unhandled error occurs at any point in the flow, any active transactions
will rollback and an unmodeled fault is returned to the service requester.

## Asynchronous invocation

When a service component is called asynchronously, the service requester and the service provider
run in different threads of execution. The SCA runtime returns control to the requester
immediately.

Figure 2. Asynchronous invocation error handling

<!-- image -->

Figure 2 shows how errors can be handled within
an asynchronous flow. The flow has been split into transaction boundaries (A, B, C, D), each new
boundary is marked by a new queue (1, 2, 3, 4). If an error occurs within a transaction boundary,
the message is rolled back to the queue at the start of the transaction. For example, if an error
occurs within the mediation flow component, the message is rolled back to queue number 2, because it
is within the transaction boundary B.

Figure 3. Asynchronous invocation error handling without queue 2

<!-- image -->

Figure 4. Asynchronous invocation error handling

<!-- image -->

As a default, when a message is rolled back to an internal module destination, SCA
retry logic indicates that the message will be redelivered up to five times. If the message fails
again, it will be automatically forwarded to the defined exception destination. This can be viewed
via the Service Integration Bus Explorer in the Administrative Console. If the
Failed Event Manager is enabled, messages on the exception destination are removed and stored in a
database as failed events. Each module has its own internal exception queue. Binding retries can be
configured at the binding, or on the messaging provider. Binding retries occur at least once, so
that the Failed Event Manager can be aware of any fault.

The Failed Event Manager is a web-based client for working with and resubmitting
the failed invocations. It is an integration application and is available in the Administrative
console. It displays the number of failed events and provides a number of search capabilities.
Messages that exceed their retry count are automatically retrieved by the Failed Event Manager.
Asynchronous export and import bindings can be configured to send failed messages to the Failed
Event Manager before they exceed their retry count.

## Mixed invocation styles

When a service requester calls a service provider, the invocation can be made either
synchronously or asynchronously. There are situations where the service requester makes a
synchronous call, but the service provider must be called asynchronously by the mediation flow
component. In this occasion, queues 1 and 2, and boundaries A and B will not exist, and the flow
will look similar to Figure 5. In this situation,
if an error occurs before boundary C, it will be sent back to the service requester.

Figure 5. Synchronous and asynchronous invocation error handling

<!-- image -->

If the service requester performs an asynchronous invocation, and the service provider is a
synchronous service, the mediation flow component will call the import synchronously. In this
situation, queues 3 and 4, and boundaries C and D will not exist within Figure 6. In this situation, if an error occurs after
boundary B, it will be sent back to the service provider.

Figure 6. Asynchronous and synchronous invocation error handling

<!-- image -->