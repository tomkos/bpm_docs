<!-- image -->

# Generating an MQ JMS export binding

## Before you begin

If you intend
to use the standard JMS message class with a body type containing
the message then you must create business objects for these body types.
A function is provided that will create the entire set of business
objects for the JMS body types. In your module, open the dependencies
editor. Under Predefined Resources, select Native
Body schema for Native Body DataHandler. Save your work
and close the dependencies editor. In the navigation view under Data
Types, the business objects are created.

Afterward,
create an interface for your export that contains the appropriate
data types for input and output. For example, if you were using the
TextMessage body, create an interface with an operation such as handleText
with an input type of TextBody and an output type of TextBody. These
data types will be selectable from the types in the interface editor.

## About this task

## Procedure

1. Open the assembly editor. Under Inbound Exports,
select MQ JMS and drag it to the assembly editor.
Select an interface or create one. Alternately, under Components,
select Export and drag it on to the canvas.
An export with no implementation and no interface is created. Right-click
the export, select Add Interface from the menu and add an interface
that describes your interaction with a WebSphere MQ application. Create an export
with an MQ JMS binding by right-clicking the export and from the menu
selecting Generate Binding > Messaging Binding >MQ
JMS Binding.
2 The Configure WebSphere MQ JMS Export Service windowbox opens. There is a slight difference between an interface witha one-way operation and an interface with a request-response operation.An interface with a request-response operation has an additional fieldfor a send destination. Select the messaging domain: Point-to-Point or Publish-Subscribe . Selectif you want to Configure new messaging provider resources (thedefault) or Use pre-configured messaging provider resources . Ifyou choose Configure new messaging provider resources ,enter the WebSphere MQ queue name for the receive destination fora one-way request operation, and send and receive destination fora request-response operation. You may specify the WebSphere MQ queue manager or use the defaultqueue, which is preselected. If you choose Use pre-configuredmessaging provider resources , enter the JNDI name forthe ActivationSpec and receive destination for a one-way operation.Enter receive and send destinations for a request-response operationand the connection factory JNDI name. If you are using a remotequeue manager, specify the name and, after you generate the binding,update the CLIENT transport properties in the endpoint configurationsection. You should periodically check your binding configuration information at run time in theadministrative console. In particular check the state of the endpoint. Under some conditions theendpoint may go into a paused state and you will need to restart it (see Viewing or changing the state of an endpoint ). Ifyou specify JNDI names and then switch to specifying your own configurationproperties both sets of values remain in memory until you close theeditor. You are saved from reentering the values while you decide. Inthe Default data format field, select how thedata will be serialized between the business object and the JMS messagewith a binding. To change the default, click Select besidethe field to launch the Data Transformation Configuration window.Your selections are as follows: In the Function selector section,select the function selector configuration you want to use. A functionselector selects an operation to invoke on your component at run time.Clicking Select beside the Functionselector field, launches the Function SelectorConfiguration window and provides the following selections: In the next section, if you want to use the default moduleto module fault handling, which is a SOAP transport, select it. Acommon way for specifying a userid and password is through using theJava EE Connector (J2C) authentication data entries. The entries aredefined on the server. In the Security configuration section,select Specify a Java Authentication and AuthorizationServices (JAAS) alias security credential when server security isenabled , if it is used by your organization. Enter theJava EE Connector (J2C) authentication data entry. Click OK .The MQ JMS binding is created and shown in the properties view whenthe Binding tab is selected. Sub tabs under the binding tabprovide binding information details, which are discussed in the nextsteps.

Select the messaging domain: Point-to-Point or Publish-Subscribe.

Select
if you want to Configure new messaging provider resources (the
default) or Use pre-configured messaging provider resources.

If
you choose Configure new messaging provider resources,
enter the WebSphere MQ queue name for the receive destination for
a one-way request operation, and send and receive destination for
a request-response operation. You may specify the WebSphere MQ queue manager or use the default
queue, which is preselected.

If you choose Use pre-configured
messaging provider resources, enter the JNDI name for
the ActivationSpec and receive destination for a one-way operation.
Enter receive and send destinations for a request-response operation
and the connection factory JNDI name.

If you are using a remote
queue manager, specify the name and, after you generate the binding,
update the CLIENT transport properties in the endpoint configuration
section.

You should periodically check your binding configuration information at run time in the
administrative console. In particular check the state of the endpoint. Under some conditions the
endpoint may go into a paused state and you will need to restart it (see Viewing or changing the state of an endpoint).

If
you specify JNDI names and then switch to specifying your own configuration
properties both sets of values remain in memory until you close the
editor. You are saved from reentering the values while you decide.

In
the Default data format field, select how the
data will be serialized between the business object and the JMS message
with a binding. To change the default, click Select beside
the field to launch the Data Transformation Configuration window.
Your selections are as follows:

    - Use a data format transformation in the binding registry. This
list includes the Prepackaged JMS data format transformations. Selecting Show
the deprecated data format transformations adds previous
transformations that have been deprecated.
    - Use a custom data format transformation you have created in your
workspace
    - Create a new Creating a data format transformation resource configuration.

In the Function selector section,
select the function selector configuration you want to use. A function
selector selects an operation to invoke on your component at run time.
Clicking Select beside the Function
selector field, launches the Function Selector
Configuration window and provides the following selections:

    - Use an existing function selector (default)
lists the function selector configurations available. This list includes
the Prepackaged JMS function selectors.
    - Use a custom function selector that you have created in your workspace.
    - Create a new Creating a function selector resource configuration.

In the next section, if you want to use the default module
to module fault handling, which is a SOAP transport, select it.

A
common way for specifying a userid and password is through using the
Java EE Connector (J2C) authentication data entries. The entries are
defined on the server. In the Security configuration section,
select Specify a Java Authentication and Authorization
Services (JAAS) alias security credential when server security is
enabled, if it is used by your organization. Enter the
Java EE Connector (J2C) authentication data entry.

Click OK.
The MQ JMS binding is created and shown in the properties view when
the Binding tab is selected. Sub tabs under the binding tab
provide binding information details, which are discussed in the next
steps.

3. Selecting the End-point configuration tab
and the Request tab, opens the activation specification
(ActivationSpec class) properties and receive destination properties
under ActivationSpec Properties. You may specify
a JNDI lookup name. A JNDI lookup name points to a preconfigured set
of values specified on the target server. Using a JNDI name often
occurs when a system administrator sets up the connection information
for you. You will also see a JNDI lookup name field for Failed
Event Replay Connection Factory, which lets you replay
events that have failed. Use the select button or enter the JNDI lookup
name for the connection factory configuration that is used to replay
failed events. The ActivationSpec Properties section
specifies the message configuration properties such as the transport,
which defaults to BINDINGS. With the bindings
mode, WebSphere MQ JMS
classes use the Java™ Native
Interface (JNI) to call directly into the existing queue manager API
rather than communicating through a network. Since bindings is a shared
memory protocol, it may offer better performance. 
If you are
using a remote queue manager requiring a client binding or you have
chosen to use a client binding, then select CLIENT.
The client configuration properties become active requiring you to
either specify the host name, channel and port or the client channel
definition table URI. See Using
binding or client transports for more information. Further
down this page, though not shown in the screen capture below, are
MQ local address properties. Advanced specifies
some lower level properties.
Enable connection on
startup specifies that a connection should be made according
to the messaging endpoints when the application starts (default).
If deselected, the connection will not be made and the application
can determine the flow of messages. 
Enable XA specifies
whether the connection factory is for XA or non-XA coordination of
messages. XA should be selected if multiple resources are used in
the same transaction (default). If deselected, the resource manager
is used for local transaction calls (session.commit and session.rollback)
instead of XA calls. This selection can mprove performance but only
a single resource can be enlisted in a transaction. 
Receive
Destination Properties specifies the type of receive destination,
queue or topic, the destination name that you specified earlier and
the target client type, JMS by default though MQ is selectable. Alternately,
you can use a JNDI name.
4. Selecting the Response tab in the
case of a request-response operation has connection factory fields
for the send destination properties similar to the receive destination
properties of the request. If you specify a JNDI name, this information
is not available as it is configured on the server; that is, the destination
specified on the server under this JNDI name will be used. The default
encoding properties for integer, decimal and floating point numbers
are listed.
5. Selecting Method bindings shows
the bound methods. By default, all methods are bound. If you add a
method to the interface after you created the binding, however, a Bind
operation check box becomes available for you to add it
to the bound methods.  The Generic tab
lets you add a description of the method binding.
 The Data
Serialization tab lets you specify the input and output
serialization types, which determines how the data will be serialized
between the business object and the JMS message. 
Message
type is used by the server to create and send the outgoing
message. It is used with some data format transformers. If the server
does not use the message type specified then it is disabled. Valid
types are byte, map, object, stream or text.
Under JMS
Headers, the properties you can specify are as follows.
The JMS type property conforms to the JMSType specified in
the JMS specification. This property contains
a message type identifier supplied by a client when a message is sent.
The JMS correlation ID property conforms to the JMSCorrelationID
in the JMS specification. A typical use is to link a response message
with its request message. In IBM® Integration
Designer,
the ID is used by the message selector to select only messages with
that ID. It can be any string value specified at run time. JMS
delivery mode can be either persistent, guaranteed delivery is
required, or non-persistent, an occasional lost message is tolerable.
JMS priority specifies a level priority value with 0 as the lowest
and 9 as the highest. 4, the default, is considered normal priority.
Custom
Headers allow you to specify a name, type and value for a property.
Clicking Advanced found
lower on this page and not in this screen capture lets you specify
the input and output serialization types, which determines how the
data will be serialized between the business object and the JMS message.
6 Selecting the Faults configuration tablets you configure the business fault data format for the faults inthe interface. The configuration of faults is optional. The configurationcan apply to all operations, a specific operation or a specific fault. If fault configuration is new to you, see Handling faults in bindings for an overview. Click Select beside Businessfault data format . Your selections are as follows:

If fault configuration is new to you, see Handling faults in bindings for an overview.

- Use a data format transformation in the binding registry. This
list includes the Prepackaged JMS data format transformations.
- Use a custom data format transformation you have created in your
workspace
- Create a new Creating a data format transformation resource configuration .
7. Selecting Security attributes with
the Request tab shows the authentication properties
under Authentication Properties section. The J2C
Authentication Data Entry property lets you specify an
authentication alias that should be configured on the server with
a userid and password. If Advanced is selected, authentication
properties are shown such as the level of the authentication; for
example, at the container level. If the connection transport type
has been set to CLIENT, then Secure Sockets
Layer (SSL) encryption can be enabled.
8. If you selected Configure response connection earlier
in the End-point configuration tab, then selecting
the Response tab will provide you with authentication
properties for the response connection. Also, if the connection transport
type has been set to CLIENT, then Secure Sockets
Layer (SSL) encryption can be enabled for the response.
9. The Message Configuration tab shows
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
Failed
message recovery mode lets you allow the binding to manage
the recovery of failed messages (the default) or rely on the transport-specific
method of recovery. Allow binding to manage recovery for
failed messages creates a recovery queue on deployment
to handle failed messages. Binding errors are handled as failed events
that can be retrieved later. Rely on transport-specific
recovery for failed events does not set up a recovery
mechanism.
10. The Propagation tab lets you select
two types of context propagation. Context propagation takes information
associated with a runtime or an application and passes it along with
requests that are the result of interactions with that run time or
application. The default is to use runtime context propagation. See Propagation.
11. Selecting the Summary tab specifies
the receive and send destination (in the case of a request-response
operation) JNDI names, the connection factory JNDI name, ActivationSpec
JNDI name, failed event replay JNDI name, the function selector class
name and data format used for data transformation. With the exception
of the function selector class name and data format, they are names
generated by the SCA JMS handler if you did not specify any custom
JNDI names. You may need these JNDI names if you are authoring the
targeted JMS application.

## What to do next

## Related tasks

- Generating an MQ JMS import binding