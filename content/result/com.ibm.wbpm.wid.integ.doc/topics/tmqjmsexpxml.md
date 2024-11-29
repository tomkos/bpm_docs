<!-- image -->

# Creating an MQ JMS export to communicate with an MQ JMS or
JMS client

## Before you begin

## Procedure

1. In order for your SOA application to communicate to an
existing JMS client, you will need to have created a business object
and an interface that would represent your JMS client application
in an SOA manner. Mapping a message to an SCA interface provides
guidance on how to create such a business object and interface.
2. You must create a component that will enable your existing
SOA application to communicate with the existing JMS client application.
To do this, you will create an export and add a binding type of MQ
JMS to it.  There are two main types of information
that need to be captured by the MQ JMS binding. One set of information
is needed by the service component architecture (SCA). This includes
information such as the interface, which we discussed earlier, and
the serialization type, which we will discuss later. The other set
of information is the configuration needed to communicate using JMS
such as the specification of JMS destination objects, which we will
also discuss later. 
Open the assembly editor. Under Inbound
Exports, select MQ JMS and drag
it to the assembly editor. Select an interface or create one.
Alternately,
under Components, select Export and
drag it on to the canvas. An export with no implementation and no
interface is created. Right-click the component, select Add
Interface from the menu and add the interface created
in step 1. Generate the JMS skeleton binding by selecting the component
and from the menu select Generate Binding > Messaging Binding >
MQ JMS Binding.
3. The Configure WebSphere MQ JMS Export Service window
appears.  You may select the JMS messaging domain as
either Publish-Subscribe or Point-to-Point.
The consequences of selecting publish-subscribe is that the values
for the JMS Destination type will default to use javax.jms.Topic.
Similarly, the consequences of selecting point-to-point is that the
values for the JMS Destination type will be default to use javax.jms.Queue.
You may change these defaults within the wizard. If your interface
contains a request-response operation, the wizard will default the
JMS messaging domain to point-to-point.
Select if you want to Configure
new messaging provider resources (the default) or Use
pre-configured messaging provider resources. If you choose
pre-configured, then add the JNDI names for the connection factory
and the send destination for a one-way operation, and send and receive
destinations for a request-response operation. We chose to configure
the messaging resources. With the MQ JMS binding, you must specify
the WebSphere® MQ queue
name for the receive destination and send destination (for request-response
operations, which in our case we will be using). The WebSphere MQ queue manager must also be
specified. The existing default queue manager is selected by default. 
In
the Security configuration section, the J2C
Authentication Data Entry property lets you specify an
authentication alias that should be configured on the server with
a userid and password.
You must choose the serialization type
that is expected by the JMS client application, as defined by the
data binding. The serialization type is used to map between the business
object used in your SOA application and the message format expected
by the JMS client application. There are several serialization types
provided as listed below. For serialization types beginning Simple
JMS, you must have previously created the business objects
required (see the Prerequisites section of Generating an MQ JMS export binding for a quick way of creating these
business objects). 
The data binding selection is discussed
in Prepackaged JMS data format transformations.
The Function
selector section determines which FunctionSelector class
to use. A function selector selects an operation to invoke on your
component at run time. The operation maps to a function to be performed
based on the content of the JMS message. For example, the message
may contain an Employee record and be used to create, update, retrieve,
or delete the an Employee record. The actual operation to invoke is
determined from content in the header or body of the JMS message.
The
function selector selection is discussed in Prepackaged JMS function selectors.
The
standard way of defining a message class with subclasses for the message
body has its own function selector. See Overview of JMS function selectors for more information. 
In
this task, the JMS client is sending XML in a JMS text message so
we chose the appropriate data format transformation, which is Serialized
Java Object (JMS) and will use the default function selector.
4. The MQ JMS binding is created and shown in the properties
view when the Binding tab is selected. The
following chart provides some guidance for the configuration you see
in the next few screen captures. 
Table 1. Relationship
of request and response to configuration

Request or response
Connection factory
Send destination
Receive destination
Activation specification (ActivationSpec)
Correlation scheme

Configuration elements in a request or response
Creates the connection to the messaging provider.
Destination where the message is sent.
Destination where the response message is received. 
A class used to activate a message endpoint
and associate it with a Message Driven Bean (MDB).
Correlates response messages with request messages
in request-response operations. 

Export request
A JNDI name or one created with default settings
when the application is deployed.
Not applicable
A JNDI name or the queue name of the WebSphere MQ queue manager.
A name is created on deployment or one that
is specified by you.
Not applicable

Export response
Uses the same connection factory as the request
or one that is specified by you.
A JNDI name or the queue name of the WebSphere MQ queue manager.
Not applicable
Not applicable
Adds a request ID to the request message (default)
or adds a correlation ID to the request message.

Select the End-point configuration tab
under the Binding tab. Under the Request tab,
opens the activation specification (ActivationSpec class) properties
and receive destination properties. You can also specify a JNDI name
for the activation specification if it has been pre-configured on
the messaging provider resource. 
The ActivationSpec
Properties section specifies the message configuration
properties such as the transport. We chose a BINDINGS transport
option, which is the default. With this setting, you do not need to
specify host name, channel or port as WebSphere MQ JMS classes will use the Java™ Native Interface (JNI) to call
directly into the existing queue manager API rather than communicating
through a network. Bindings is a shared memory protocol and may offer
better performance. An alternative is the CLIENT setting,
which means you must specify the values for the client configuration
including host name, channel and port and optionally the client channel
definition table. The WebSphere MQ
client connection is used to connect to the queue manager. 
Expanding Receive
Destination Properties, you can specify a JNDI name or
you can accept the defaults, in which case the tools create the properties.
Specify the appropriate settings to ensure your SOA application is
able to communicate to the JMS client. For this task, we accepted
the defaults for the settings but provided the receive destination,
which was specified earlier when we created the bindings. The name
contains the WebSphere MQ
queue name.
5. For Send Destination Properties beneath
the Response tab, we accepted the defaults
but specified the send destination, which we entered earlier when
creating the binding. It contains the WebSphere MQ queue name.
6. As mentioned earlier, the existing JMS client may send
in a message header property the targeted operation name that the
message is intended for. To make sure the message invokes the correct
business method, you need to specify for each business method the
operation name from the JMS client application that maps to it.  This
is done under the Method bindings tab under
the Binding tab.  For each business method,
specify the JMS client application operation name that maps to it
under the field Native Method.
7. The Message Configuration tab shows
the correlation scheme for the response message. Request
Message ID to Correlation ID adds a request ID to the
request message. It is expected that the reply copies the request
ID to the correlation ID field of the response message so that the
caller can correlate the reply message with the request message. Request
Correlation ID to Correlation ID adds the correlation
ID to the request message. It is expected that the reply copies the
request correlation ID to the correlation ID field of the response
message so that the caller can correlate the reply message with the
request message.  The Asynchronous Reliability property
can have these values: assured (default) or bestEffort.
Select assured if you want a message to persist
through a transaction. In other words, if you want guaranteed delivery
of the message. Select bestEffort if you want
a high throughput of messages and your application can accept and
handle the loss of a message, as persistence is not guaranteed. Event
sequence required specifies if the same order of events
as received from WebSphere MQ
must be followed by the component receiving the events.
8. Selecting the Summary tab specifies
the receive and send destination (in the case of a request-response
operation) JNDI names, request and response connection factory JNDI
names, listener port name, function selector class name and data binding
class name. With the exception of the function selector class name
and data binding class name, they are names generated by the SCA JMS
handler if you did not specify any custom JNDI names. This is a page
you should check to verify the configured resources.

## What to do next