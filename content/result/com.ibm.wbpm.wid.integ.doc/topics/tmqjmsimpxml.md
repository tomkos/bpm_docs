<!-- image -->

# Creating an MQ JMS import to communicate with an MQ JMS or
JMS client

## Before you begin

Prerequisite: The JMS administered objects are configured
for the MQ JMS or JMS client and known. In addition, there should
be a module that contains your service-oriented architecture application.
 The message format expected by the JMS client is also known

## About this task

## Procedure

1. For your SOA application to communicate to an existing
MQ JMS or JMS client, you must first create a business object and
an interface that would represent your JMS client application in an
SOA manner. Mapping a message to an SCA interface provides guidance
on how to create such a business object and interface.
2. You must create a component that will enable your existing
SOA application to communicate to the existing JMS client application.
To do this, create an import and add a binding type of MQ JMS to it. 
 There are two main types of information that must be captured
by the MQ JMS binding. One set of information is needed by the service
component architecture (SCA). This includes information such as the
interface, which we discussed earlier, and the serialization type,
which we will discuss later. The other set of information is the configuration
needed to communicate using JMS such as the specification of JMS destination
objects, which we will also discuss later. 
Open the assembly
editor. Under Outbound Imports, select MQ
JMS and drag it to the assembly editor. Select an interface
or create one.
Alternately, select Import under Component on
the palette and drag it on to the canvas. An import with no implementation
and no interface is created. Right-click the import, select Add
Interface from the menu and add the interface created
in step 1. Generate the MQ JMS binding by selecting the import and
from the menu select Generate Binding > Messaging Binding
> MQ JMS Binding.
3. The Configure WebSphere MQ JMS Import Service window
opens. You can select the JMS messaging domain as either Publish-Subscribe or Point-to-Point.
The consequences of selecting publish-subscribe is that the values
for the JMS Destination type will default to use javax.jms.Topic.
Similarly, the consequences of selecting point-to-point are that the
values for the JMS Destination type will default to use javax.jms.Queue.
You can change these defaults within the wizard. If your interface
contains a request-response operation, the wizard defaults the JMS
messaging domain to point-to-point.
Select if you want to Configure
new messaging provider resources (the default) or Use
pre-configured messaging provider resources. If you choose
pre-configured, then add the JNDI names for the connection factory
and the send destination for a one-way operation, and send and receive
destinations for a request-response operation. Also add the JNDI name
for the activation specification (ActivationSpec class), which contains
the configuration information for a message end point. With the MQ
JMS binding, you must specify the WebSphere® MQ
queue name for the send destination and receive destination (for request-response
operations, which in our case we will be using). The WebSphere MQ queue manager must also be
specified. The existing default queue manager is selected by default. 
In
the Security configuration section, the J2C
Authentication Data Entry property lets you specify an
authentication alias that should be configured on the server with
a userid and password.
In the Data format section, select
how the data will be serialized between the business object and the
JMS message with a data binding. If you intend to use one of the default
data bindings beginning Simple JMS, you must
have previously created the business objects required (see the Prerequisites section). 
The
data binding selection is discussed in Prepackaged JMS data format transformations.
 In
the Function selector section, if you do not
want to use the TargetFunctionName message header property for the
default JMS function selector class, clear it. 
The FunctionSelector
class provides a valuable service at run time. It selects an operation
to start on the component. The operation maps to a function to be
performed based on the content of the JMS message. For example, the
message might contain an employee record and be used to create, update,
retrieve, or delete an employee record. The actual operation to invoke
is determined from content in the header or body of the JMS message.
In
this task, the JMS client is expecting XML in a JMS text message so
we chose the appropriate data format transformation, which is Serialized
Java Object (JMS). In addition, because you are communicating
with an existing JMS client, you will clear the Generate
"TargetFunctionName" message header property for default JMS Function
Selector because the JMS client would not know how to
handle the custom JMS header tag that would have been generated if
it were checked.
4. The MQ JMS binding is created and shown in the properties
view when the Binding tab is selected. The
following chart provides some guidance for the configuration properties. 

Table 1. Relationship of request and response to configuration

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

Import request
A JNDI name or one created with default settings
when the application is deployed.
A JNDI name or the queue name of the WebSphere MQ queue manager.
Not applicable
Not applicable
Adds a request ID to the request message (default)
or adds a correlation ID to the request message.

Import response
Uses the same connection factory as the request
or one that is specified by you.
Not applicable
A JNDI name or the queue name of the WebSphere MQ queue manager.
A name is created on deployment or one that
is specified by you.
Not applicable

 Select the End-point configuration tab
under the Binding tab. Under the Request tab,
you can accept the defaults and the tools will create a connection
factory when the application is deployed or you can specify a connection
factory JNDI name if it has been pre-configured on the messaging provider
resource. In our case, we accepted the defaults. 
We chose a BINDINGS transport
option, which is the default. With this setting, you do not need to
specify host name, channel or port as WebSphere MQ JMS classes will use the Java™ Native Interface (JNI) to call
directly into the existing queue manager API rather than communicating
through a network. Bindings is a shared memory protocol and might
offer better performance. An alternative is the CLIENT setting,
which means you must specify the values for the client configuration
including host name, channel and port and optionally the client channel
definition table. The WebSphere MQ
client connection is used to connect to the queue manager.
Expanding Send
Destination Properties, you can specify a JNDI name or
you can accept the defaults, in which case the tools create the properties.
Specify the appropriate settings to ensure your SOA application is
able to communicate to the JMS client. For this task, we accepted
the defaults for the settings but provided the send destination, which
was specified earlier when we created the bindings. The name contains
the WebSphere MQ queue
name.
5. For the Receive Destination Properties section
beneath the Response tab, we accepted the defaults
but specified the receive destination, which we entered earlier when
creating the binding. It contains the WebSphere MQ queue name. It lists the activation
specification (ActivationSpec class) configuration properties.
6. The existing JMS client might expect certain header properties
to be configured. You can specify these under the Method
bindings tab. For each business method that represents
a corresponding JMS client application method, you can specify unique
JMS message header properties required. For example, if the existing
JMS client application requires the message header JMSType to
specify the application method name for which the JMS message is targeted,
you will specify it here.
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
request message.
8. Selecting the Summary tab specifies
the send and receive destination (in the case of a request-response
operation) JNDI names, request and response connection factory JNDI
names, listener port name and data binding class name. This is a page
you should check to verify the configured resources.

## What to do next