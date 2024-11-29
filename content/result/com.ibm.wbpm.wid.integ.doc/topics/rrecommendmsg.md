<!-- image -->

# Recommendations when using messaging bindings

- Request-response messages
- Callback queues
- Quality of service

## Request-response messages

Messages
can be either one way, often called a fire and forget message, or
two-way, that is, a request and a response. Although a one-way message
is simple enough for IBM® Integration
Designer,
request-response messages pose a challenge in that the response messages
must be coordinated. Remember that in messaging systems, a response
is asynchronous; that is, it can come back at any time. It is independent
of time. Consider this case: message A is sent to a queue followed
by message B to the same queue and then message C to the same queue.
They are all request-response messages. When a response is returned
from one of these messages, how does IBM Integration
Designer determine
which request it matches? The following section on callback queues
answers this question more completely but in a nutshell a correlation
identifier maps a response with the correct request.

For a single
application, coordinating request and response messages is handled
easily by IBM Integration
Designer.
However, where you can get in trouble is when you have two or more
applications using the same queue. In this case, a response can come
back that is picked up by the wrong application and a correlation
matching error can occur. Recommendation: always use a separate queue
for each application.

## Callback queues

Any Service
Component Architecture (SCA) service can be accessed in a synchronous
or asynchronous manner, independent of whether the service itself
is synchronous or asynchronous. However, SCA services that access
messages asynchronously require callback methods and correlation objects.

An
SCA service interface is always defined in the synchronous form. Additional
interfaces are created to support the asynchronous model.  These interfaces
pass a callback object with the asynchronous request.  Once the called
service finishes processing the request, it returns the results to
the callback object.  A correlation object, known as a ticket,
is used to correlate the response with the original request.

Both
the JMS import and export use a destination, the callback destination,
to store callback information. This is an internal SCA JMS service
mechanism used to support SCA asynchronous invocations, which has
been exposed to allow performance customization.

When a JMS
import is invoked in a synchronous manner, it will put the JMS message
onto the send destination and store the callback information in the
callback destination using the correlation scheme of the request JMS
message.  The JMS import then uses a Message Driven Bean (MDB) to
listen for the reply message.  When the reply message arrives, the
MDB uses its correlation ID to retrieve the callback information.
 It then uses the callback information to invoke the callback object
with the response.

A JMS export uses a MDB to listen on the
receive destination.  When a message is received it will dispatch
the request to the SCA runtime and will store JMS response information
in the callback destination using the ID of the ticket.  When the
callback is invoked it will retrieve the JMS response information
from the callback destination using the ID of the ticket such as the
'send' destination, the correlation ID and its output data binding.
 Then the callback's response argument and the JMS response information
is used to create the response JMS message and send it to the reply
destination.

Recommendation: Using the asynchronous interaction
style is suitable for most circumstances. Since calls are not blocked
to wait for a particular response, choose asynchronous if performance
is important to your application. However, if a response has a high
importance to your application then selecting the synchronous interaction
style is preferable. In this case, your application will be listening
for the response, which means calls will be blocked. Using a timeout
value can minimize the effect of waiting too long for a response.

## Quality of service

Quality
of service defines the communication characteristics of a service.
One characteristic we have already discussed in the callback queues
section is asynchronous versus synchronous interaction styles

Event
sequencing specifies if the sequence of messages is ordered and requires
responses in the same order. Since there is a performance cost to
selecting event sequencing, it is recommended that you use it only
if the sequence of returned responses is critical to your application.

The
asyncReliability attribute is available on a JMS export binding's
performance attributes tab.  This attribute specifies the reliability
that the SCA runtime uses during asynchronous invocation of the export's
target component.  When it is set to assured, delivery of the message
is guaranteed.  The message will be persisted if necessary. When the
attribute is set to bestEffort, the delivery of the message may fail
in the event of system failure.  Recommendation: Message persistence
has a performance price.  If your application does not need guaranteed
message delivery you should set the attribute to bestEffort to improve
the performance of the transaction. The default value for this attribute
is assured.

Failed message recovery mode lets
you allow the binding to manage the recovery of failed messages, which
is the default. Binding errors are handled as failed events that can
be retrieved later. You can also select transport-specific recovery,
which does not set up a recovery mechanism. Recommendation: If your
application does not need the binding to manage the recovery of failed
messages or the messages themselves are not critical, select transport-specific
recovery to improve performance.

If you are using MQ bindings,
you can set a transport field that determines how the queue manager
is accessed. Selecting the Client option means a connection is made
when you provide the host name, server channel and port number. A
Client channel definition table (CCDT) selection means the connection
values are specified in a client channel definition table. A Bindings
selection means Java Native Interface (JNI) bindings are used to connect
to the queue manager. Bindings is a shared memory protocol and can
only be used with the queue manager is running locally. A Bindings
then client selection means a Bindings connection is attempted and,
if unsuccessful, a Client connection is made. Recommendation: A Bindings
connection is fastest but less secure than a Client connection.

## Related concepts

- Java Message Service (JMS)
- WebSphere MQ Java Message Service (MQ JMS)
- Generic JMS
- WebSphere MQ (WMQ)

## Related reference

- Mapping a message to an SCA interface
- Language support in non-EIS bindings