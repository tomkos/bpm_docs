<!-- image -->

# Quality of service: Qualifiers for business services

The assembly editor tries to anticipate your needs by generating
quality of service qualifiers when you add interfaces and partner
references and when you generate an implementation or synchronize
from an implementation. You can also add your own qualifiers to the
module.

Service Components Architecture (SCA) allows quality of service
qualifiers, such as transactions, security, and reliable asynchronous
invocation, to be applied to components without requiring programming
or a change to the service implementation code. IBM® Integration
Designer gives you the tools to quickly and easily compose an integrated
business application that wires together components in modules that
can be deployed to the IBM Business Automation
Workflow. When wiring the components, you can specify qualifiers to provide
extended quality of service to the components, as well as to the clients
accessing the service. Sometimes, implementations require that qualifiers
are set in particular ways; see the explanation of the Join transaction qualifier for one example.

- Join transaction set to "true"
- Transaction set to "global"

The topic Transactions in IBM Integration Designer provides an overview
of how QoS settings influence transactions. You can also find individual
reference topics with details about each qualifier.

## Qualities of service qualifiers

Qualifiers are QoS specifications that define a set of communication
characteristics required by an application for transmission priority,
level of route reliability, transaction management, and security level.
This topic introduces the qualifiers that are specified in these components:

- Implementation
- Interfaces
- References

At run time, these specifications determine how the clients
interact with the target components. Depending on the qualifiers specified,
the runtime environment supplies any required additional processing.

## Qualifiers in the Properties view

The Properties
view of the assembly editor provides information about where and how
qualifiers are set in the module. It is the place to see and edit
quality of service settings and to add new ones.

The Details
page shows qualifiers that have been set on an element in the assembly
diagram.

<!-- image -->

## Qualifiers for implementation

Qualifiers for implementation identify the service's authority
and express its requirements for a transactional environment. These
are the qualifiers that are set on an implementation:

- Activity session
- Transaction
- Security identity

Microflows run on one physical thread from start to
end without interruptions. As the name suggests, microflows are small
in footprint and fast in execution. A microflow requires a transaction,
but that can be a global transaction or a local one inside an activity
session.

## Qualifiers for interfaces

Interface qualifiers are used to advertise the qualifiers supported
by a target service, and therefore represent a contract with a client
of the service. Qualifiers establish the preferred interaction style
for the interfaces. These are the qualifiers that can be set for interfaces:

- Data validation
- Event sequencing
- Join activity session
- Join transaction
- Security permission

- For all of its interfaces
- For an individual interface
- For an individual operation of an interface

When you add an interface to a component, a join transaction
qualifier and a preferred interaction style are automatically added
and set.

A deployment error occurs when the component's interface
qualifier conflicts with its export interface's qualifier.

The qualifier of the operation overrides the qualifier of the interface;
the qualifier of the interface overrides the qualifiers of all the
interfaces for a component or import. Inherited qualifiers listed
in the Properties view are gray and the assigned ones are in black.

Event sequencing is supported only for components
that are invoked using the SCA asynchronous invocation style. Invocations
have parameters, which are business objects or simple types. The key
is a combination of one or more business object attributes. You can
set the event sequencing qualifier after you develop the business
logic; it is independent of the implementation. See the related tasks
at the end of this topic for a link to information about using event
sequencing.

## Qualifiers for references

References qualifiers specify the reliability for asynchronous invocations
and whether a target component's methods should be federated as part
of any client transaction.

These are the reference qualifiers:

- Asynchronous invocation
- Asynchronous reliability
- Suspend transaction
- Suspend activity session

You can specify reference qualifiers that would apply
to all the references of a service component or the stand-alone
references. If required, you can also specify these qualifiers for
each individual reference, in which case they would override the overall
qualifiers. Inherited qualifiers listed in the Properties view are
gray and the assigned ones are in black.

If the qualifier is set to "call",
the message is immediately placed on an outbound message queue. That
placement means that the message is sent regardless of whether or
not the caller's global transaction commits or rolls back. That method
of invocation might break the integrity of the application; for example,
it might debit a customer account in spite of the fact that something
causes a purchase order to fail before it has completed.

This
weakness is most obvious when the transaction includes a long-running
process. The asynchronous invocation qualifier controls whether a
component sends a request message in a transaction with a commit requirement
or as a call that does not require a response. You only need to worry
about the nature of the invocation if the completion of a transaction
involves human approval or some other response that might delay completion.
If the caller is in a global transaction and the message requires
a response in order to complete, that condition causes a problem if
the call is made to a long-running process at commit time. A deadlock
occurs; the message is sent when the global transaction commits, but
the caller waits until the reply is returned before continuing its
processing and eventually performing the commit.

```
CWSCA2010W: SCA Component \"{0}\" has attempted to make an asynchronous invocation using the deferred response invocation style against reference \"{1}\". This reference has the qualifier ''deliverAsyncAt'' = \"Commit\". This is a conflict that will cause the invocation to fail. Change the "deliverAsyncAt" qualifier on \"{2}\" to \"Call\".
```

- Reliability
The reliability  qualifier
determines the quality of the delivery of an asynchronous message.
In general, better performance usually means less reliable message
delivery. With an Assured (persistent) specification,
the client application cannot tolerate the loss of a request or response
message. With a Best effort (nonpersistent) specification, the client application can tolerate the possible
loss of the request or response message. In this context, persistent means saved to disk, so the request is recoverable if the server
goes down before the target service is invoked,  and nonpersistent means not saved to disk, so the request is lost if the server goes
down before the target  service is invoked.
- Request expiration (milliseconds)
Request expiration is the length of time after which an asynchronous request will be
discarded if it has not been delivered, beginning from the time when
the request is issued. A zero (0) denotes an indefinite expiration.
- Response expiration (milliseconds)
Response
expiration is the length of time that the runtime environment
must retain an asynchronous response or must provide a callback, beginning
from the time when the request is issued. A zero (0) denotes an indefinite
expiration.

If the implementation is running in a global transaction,
that transaction is propagated on all synchronous invocations to the
target components by default. If those target components can join
the global transaction and you do not want this to happen, add this
qualifier and set its value to "true". However, when suspend transaction
is set to true, the target component's effective transaction environment
is either a new global transaction or a local transaction.

This reference qualifier
is ignored if the invocation occurs using any of the asynchronous
interaction styles. The client activity session is not propagated
if the client uses any asynchronous interaction styles. This reference
qualifier is also ignored if the invocation occurs outside the scope
of an activity session.

This qualifier does not affect the
activity session environment of the target component. That is, the
target component's hosting container is still entirely responsible
for providing the activity session environment that is required by
the implementation.