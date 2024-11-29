<!-- image -->

# JMS features

- Callback destination
- Fault handling
- Quality of service
- JMS header properties
- Correlation schemes

## Callback destination

SCA services
that access messages asynchronously require callback methods and correlation
objects, which are explained in this section.

Any SCA service
can be accessed in a synchronous or asynchronous manner, independent
of whether the service itself is synchronous or asynchronous.

An
SCA service interface is always defined in the synchronous form. 
Additional interfaces are created to support the asynchronous model.
 These interfaces pass a callback object with the asynchronous request.
 Once the called service finishes processing the request, it returns
the results to the callback object.  A correlation object, known as
a ticket, is used to correlate the response with the original
request.

Both the JMS import and export use a destination, the callback
destination, to store callback information. This is an internal
SCA JMS service mechanism used to support SCA asynchronous invocations,
which has been exposed to allow performance customization.

When
a JMS import is invoked in a synchronous manner, it will put the JMS
message onto the send destination and store the callback information
in the callback destination using the correlation scheme of the request
JMS message.  The JMS import then uses a Message Driven Bean (MDB)
to listen for the reply message.  When the reply message arrives,
the MDB uses its correlation ID to retrieve the callback information.
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

## Fault handling

JMS fault
handling is used to handle exceptions at run time.

You can configure
your import and export bindings to handle faults (for example, business
exceptions). A fault handler can be set up at three levels: you can
associate a fault handler with a fault, with an operation, or with
a binding. For import bindings, you can also set up a fault selector
to determine whether a response is a fault and, if so, the name of
the fault. See Handling faults in bindings for more information.

Several
prepackaged fault selectors are available. See Prepackaged JMS and MQ fault selectors.

## Quality of service

An attribute, asyncReliability,
is available on a JMS export binding's performance attributes tab.
 This attribute specifies the reliability that the SCA runtime uses
during asynchronous invocation of the export's target component. 
When it is set to assured, delivery of the
message is guaranteed.  The message will be persisted if necessary.
When the attribute is set to bestEffort, the
delivery of the message may fail in the event of system failure. 
Message persistence requires a cost to performance.  If your application
does not need guaranteed message delivery you should set the attribute
to bestEffort.  The default value for this attribute is assured.

## JMS header properties

JMS
header properties can be set from the JMS import method binding. 
One special user property is TargetFunctionName.
 This property can be used in conjunction with the supplied default FunctionSelector,
in a JMS export, to control how a message is mapped to a service method.
 JMS header properties can be dynamically accessed and set using an
XSL transformation in a mediation flow. A mediation flow can take
an incoming message header property and transform it using an XML
map.

## Correlation schemes

For
request-response or two-way operations, the JMSCorrelationID of
the response message must contain the request message's JMSMessageID.
This JMSMessageID is used to retrieve the callback
information, to return the response to the calling service.  When
an SCA JMS import is used to invoke a JMS client, the JMS client must
take the JMSMessageID from the request message and
set it into the JMSCorrelationID of the response
message.