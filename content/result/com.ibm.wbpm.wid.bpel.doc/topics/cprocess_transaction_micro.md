<!-- image -->

# Transactional behavior of microflows

Microflows are not interruptible. Therefore, a microflow cannot
contain activities that wait for an external event, or for a user
interaction, for example, human task activities.

Microflows are transient. The process instance state of a microflow
is held in memory, and not stored in the runtime database. However,
the state of a microflow instance can be persisted in the audit log
or in Common Base Events.

<!-- image -->

## Invoked services and microflow transactions

A
microflow runs in one transaction. However, the services that the
microflow invokes can involve more than one transaction. This is because
a service that is called through an invoke activity can either participate
in the transaction of the microflow, or it can run in its own transaction.

- The interaction style that is used to call the service.The
interaction style can be synchronous or asynchronous. The style is
determined by the preferred interaction style of the target Service
Component Architecture (SCA) component or the SCA import, and whether
the operation is one-way operation or a request-response operation
as shown in the following table:
Table 1. 

Preferred interaction style of the target component
or import 
One-way operation 
Request-response operation 

Any
Asynchronous invocation
Synchronous invocation

Synchronous
Synchronous invocation
Synchronous invocation

Asynchronous
Asynchronous invocation
Synchronous invocation

Note: The invocation from a microflow of a request-response
operation with a preferred interaction style of asynchronous is
an example of an antipattern for service invocation. When the invoked
service is a long-running process, the microflow transaction can time
out before the long-running process completes, and a runtime error
occurs.
- The SCA transaction qualifiers that are specifiedfor the process and the service that is called:
    - The suspendTransaction qualifier on the reference
of the process component specifies whether the transaction context
of the process is propagated to the services to be invoked.
    - The joinTransaction qualifier on the service
interface specifies whether a service participates in the transaction
of its caller if a transaction is propagated.

Based on these settings, the following rules apply to
the invoked service:

|  joinTransaction        | suspendTransaction = true                                     | suspendTransaction = false                                    |
|-------------------------|---------------------------------------------------------------|---------------------------------------------------------------|
| joinTransaction = true  | The service does not participate in the microflow transaction | The service participates in the microflow transaction         |
| joinTransaction = false | The service does not participate in the microflow transaction | The service does not participate in the microflow transaction |

If a service participates in a microflow transaction, the
changes that are made by the service to the transactional resources
are persisted only if the microflow transaction commits. If a service
does not participate in the microflow transaction, the changes that
are made by the service to the transactional resources might be persisted
even if the transaction is rolled back. You can use compensation to
undo the changes made by the service.