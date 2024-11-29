<!-- image -->

# Generating an MQ JMS import binding

## Before you begin

If you intend
to use the standard JMS message class with a body type containing
the message then you must use the business objects provided for these
body types (see Working with the simple JMS data bindings).

## About this task

## Procedure

1. Open the assembly editor. Under Outbound Imports,
select MQ JMS and drag it to the assembly editor.
Select an interface or create one. Alternately, select Import under Component on
the palette and drag it on to the canvas. An import with no implementation
and no interface is created. Right-click the import, select Add
Interface from the menu and add an interface describing your interaction
with a WebSphere MQ client.
Generate the MQ JMS binding by right-clicking the import and from
the menu selecting Generate Binding > Messaging Binding >MQ
JMS Binding.
2 The Configure WebSphere MQ JMS Import Service windowbox opens. The window is similar for both an interface with a one-wayoperation or a request-response operation. However, an interface witha request-response operation has an additional field for a receivedestination. In the case of a request-response operation you mustenter an MQ queue name for the send destination and the receive destinationto proceed. Select the messaging domain: Point-to-Point or Publish-Subscribe . Selectif you want to Configure new messaging provider resources (thedefault) or Use pre-configured messaging provider resources . Ifyou choose Configure new messaging provider resources ,enter the WebSphere MQ queue name for the send destination for a one-wayrequest operation, and send and receive destination for a request-responseoperation. You may specify the WebSphere MQqueue manager or use the default queue, which is preselected. Ifyou choose Use pre-configured messaging provider resources ,enter the JNDI name for the ActivationSpec and send destination fora one-way operation. Enter send and receive destinations for a request-responseoperation and the connection factory JNDI name. If you areusing a remote queue manager, specify the name and, after you generatethe binding, update the CLIENT transport properties in the endpointconfiguration section. You should periodically check your binding configuration information at run time in theadministrative console. In particular check the state of the endpoint. Under some conditions theendpoint may go into a paused state and you will need to restart it (see Viewing or changing the state of an endpoint ). Ifyou specify JNDI names and then switch to specifying your own configurationproperties both sets of values remain in memory until you close theeditor. You are saved from reentering the values while you decide. Inthe Default data format field, select how thedata will be serialized between the business object and the JMS messagewith a binding. To change the default, click Select besidethe field to launch the Data Transformation Configuration window.Your selections are as follows: In the next section, if you want to use the TargetFunctionNamemessage header property to be used with module to module communication,select it. If you want to use the default module to module fault handling,which is a SOAP transport, select it. A common way for specifyinga userid and password is through using the Java EE Connector (J2C)authentication data entries. The entries are defined on the server.In the Security configuration section, select Specifya Java Authentication and Authorization Services (JAAS) alias securitycredential when server security is enabled , if it is usedby your organization. Enter the Java EE Connector (J2C) authenticationdata entry. Click OK . The MQ JMS binding is created andshown in the properties view when the Binding tab is selected.Sub tabs under the binding tab provide binding information details,which are discussed in the next steps.

Select the messaging domain: Point-to-Point or Publish-Subscribe.

Select
if you want to Configure new messaging provider resources (the
default) or Use pre-configured messaging provider resources.

If
you choose Configure new messaging provider resources,
enter the WebSphere MQ queue name for the send destination for a one-way
request operation, and send and receive destination for a request-response
operation. You may specify the WebSphere MQ
queue manager or use the default queue, which is preselected.

If
you choose Use pre-configured messaging provider resources,
enter the JNDI name for the ActivationSpec and send destination for
a one-way operation. Enter send and receive destinations for a request-response
operation and the connection factory JNDI name.

If you are
using a remote queue manager, specify the name and, after you generate
the binding, update the CLIENT transport properties in the endpoint
configuration section.

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

In the next section, if you want to use the TargetFunctionName
message header property to be used with module to module communication,
select it. If you want to use the default module to module fault handling,
which is a SOAP transport, select it.

A common way for specifying
a userid and password is through using the Java EE Connector (J2C)
authentication data entries. The entries are defined on the server.
In the Security configuration section, select Specify
a Java Authentication and Authorization Services (JAAS) alias security
credential when server security is enabled, if it is used
by your organization. Enter the Java EE Connector (J2C) authentication
data entry.

Click OK. The MQ JMS binding is created and
shown in the properties view when the Binding tab is selected.
Sub tabs under the binding tab provide binding information details,
which are discussed in the next steps.

3. Selecting the End-point configuration tab
and Request tab allows you to specify JNDI
names for the connection factory or send destination or properties
to create a new server connection factory or destination on deployment.
These names can be specified for a request or a response (in which
case the names are applicable to a listener port and a receive destination).
If a JNDI lookup name is specified most of the lower level fields
are not shown as the JNDI name points to a preconfigured set of values
specified on the target server. Using a JNDI name often occurs when
a system administrator sets up the connection information for you.
If you use JNDI, you will still need to set up the MQ queue manager
though again this might be done by a system administrator. In our
case, a JNDI name was not specified and so the fields are shown. 
The Connection Factory Properties section
specifies the connection factory properties such as the transport
mode, which defaults to BINDINGS. With the
bindings mode, WebSphere MQ
JMS classes use the Java™ Native
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
MQ local address properties. Advanced reveals
connection pool properties that you can override.
4. Send Destination Properties found
lower on this page specifies the type of destination, queue or topic,
the destination name that you specified earlier and the target client
type, JMS by default though MQ is selectable. Alternately, you may
specify a JNDI name. The default encoding properties for integer,
decimal and floating point numbers are listed.
5. Selecting the Response tab in the
case of a request-response operation lists the activation specification
(ActivationSpec class) configuration properties under ActivationSpec
Properties.  Enable connection
on startup specifies that a connection should be made
according to the messaging endpoints when the application starts (default).
If deselected, the connection will not be made and the application
can determine the flow of messages. 
Enable XA specifies
whether the connection factory is for XA or non-XA coordination of
messages. XA should be selected if multiple resources are used in
the same transaction (default). If deselected, the resource manager
is used for local transaction calls (session.commit and session.rollback)
instead of XA calls. This selection can mprove performance but only
a single resource can be enlisted in a transaction. 
It also
specifies also the receive destination properties similar to the send
destination properties under Receive Destination Properties.
If
you selected pre-configured resources earlier, you will see JNDI names
for the ActivationSpec properties and receive destination properties,
in the case of a request-response operation configuration. You will
also see a JNDI lookup name field for Failed Event Replay
Connection Factory, which lets you replay events that
have failed. Use the select button or enter the JNDI lookup name for
the connection factory configuration that is used to replay failed
events.
6. Selecting Method bindings shows
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
that ID. It can be any string value specified at run time. 
JMS
delivery mode can be either persistent, guaranteed delivery is
required, or non-persistent, an occasional lost message is tolerable. JMS
priority specifies a level priority value with 0 as the lowest
and 9 as the highest. 4, the default, is considered normal priority.Custom
Headers allow you to specify a name, type and value for a property.
The default TargetFunctionName property used by the function selector
appears in this table.
 Clicking Advanced found
lower on this page and not shown in this screen capture lets you specify
the input and output serialization types, which determines how the
data will be serialized between the business object and the JMS message.
7 Selecting the Faults configuration tablets you configure the faults specified on the operations in the interface.The configuration of faults is optional. The configuration can applyto all operations or a specific operation. If faultconfiguration is new to you, see Handling faults in bindings for an overview. Click Select beside Faultselector to configure a fault. Your selections are asfollows: Specifying a fault selector requires that you also specifythe data format for the fault. Click Select beside Businessfault data format . Your selections are as follows: Expanding Advanced , lets you alsospecify the data format for a runtime exception.

If fault
configuration is new to you, see Handling faults in bindings for an overview.

Click Select beside Fault
selector to configure a fault. Your selections are as
follows:

- Use a fault selector in the binding registry. This list includes
the Prepackaged JMS and MQ fault selectors.
- Use a custom fault selector you have created in your workspace
- Create a new Creating a fault selector resource configuration.

- Use a data format transformation in the binding registry. This
list includes the Prepackaged JMS data format transformations.
- Use a custom data format transformation you have created in your
workspace
- Create a new Creating a data format transformation resource configuration .

Expanding Advanced, lets you also
specify the data format for a runtime exception.

8. Selecting Security attributes with
the Request tab shows the authentication properties
under Authentication Properties section. The J2C
Authentication Data Entry property lets you specify an
authentication alias that should be configured on the server with
a userid and password. If Advanced is selected, authentication
properties are shown such as the level of the authentication; for
example, at the container level. If the connection transport type
has been set to CLIENT, then Secure Sockets
Layer (SSL) encryption can be enabled.
9. If you selected Configure response connection earlier
in the End-point configuration tab, then selecting
the Response tab will provide you with authentication
properties for the response connection. Also, if the connection transport
type has been set to CLIENT, then Secure Sockets
Layer (SSL) encryption can be enabled for the response.
10. The Message Configuration tab shows
the correlation scheme for the response message. Request
Message ID to Correlation ID adds a request ID to the
request message. It is expected that the reply copies the request
ID to the correlation ID field of the response message so that the
caller can correlate the reply message with the request message. Request
Correlation ID to Correlation ID adds the correlation
ID to the request message. It is expected that the reply copies the
request correlation ID to the correlation ID field of the response
message so that the caller can correlate the reply message with the
request message. Use a temporary dynamic destination for
receiving responses uses a temporary destination for each
request. This selection does not use a correlation ID as the import
listens for responses on that destination.  Failed
message recovery mode lets you allow the binding to manage
the recovery of failed messages (the default) or rely on the transport-specific
method of recovery. Allow binding to manage recovery for
failed messages creates a recovery queue on deployment
to handle failed messages. Binding errors are handled as failed events
that can be retrieved later. Rely on transport-specific
recovery for failed events does not set up a recovery
mechanism.
11. The Propagation tab lets you select
two types of context propagation. Context propagation takes information
associated with a runtime or an application and passes it along with
requests that are the result of interactions with that run time or
application. The default is to use runtime context propagation. See Propagation.
12. Selecting the Summary tab specifies
the send and receive destination (in the case of a request-response
operation) JNDI names, ActivationSpec JNDI name, connection factory
JNDI name, failed event replay JNDI name and the data format used
for data transformation. With the exception of the data format, they
are names generated by the SCA JMS handler if you did not specify
any custom JNDI names. You may need these JNDI names if you are authoring
the targeted JMS application.

## What to do next

## Related tasks

- Generating an MQ JMS export binding