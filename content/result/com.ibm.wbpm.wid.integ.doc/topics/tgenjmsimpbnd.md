<!-- image -->

# Generating a JMS import binding

## Before you begin

If you intend
to use the standard JMS message class with a body type containing
the message then you must use the business objects provided for these
body types (see Working with the simple JMS data bindings).

## About this task

## Procedure

1. Open the assembly editor. Under Outbound Imports,
select JMS and drag it to the assembly editor.
Select an interface or create one. Alternately, select Import under Component on
the palette and drag it on to the canvas. An import component with
no implementation and no interface is created. Right-click the component,
select Add Interface from the menu and add an interface describing
your interaction with a JMS client. Generate the JMS binding by selecting
the component and from the menu selecting Generate Binding >
Messaging Binding > JMS Binding.
2 The Configure JMS Import Service windowbox opens. The window is similar for both an interface with a one-wayoperation or a request-response operation. However, an interface witha request-response operation has an additional field for a receivedestination. Select the messaging domain: Point-to-Point or Publish-Subscribe . Selectif you want to Configure new messaging provider resources (thedefault) or Use pre-configured messaging provider resources .If you choose pre-configured, then add the JNDI names for the connectionfactory and the send destination for a one-way operation, and sendand receive destinations for a request-response operation. You should periodically check your binding configuration information at run time in theadministrative console. In particular check the state of the endpoint. Under some conditions theendpoint may go into a paused state and you will need to restart it (see Viewing or changing the state of an endpoint ). Ifyou specify JNDI names and then switch to specifying your own configurationproperties both sets of values remain in memory until you close theeditor. You are saved from reentering the values while you decide. Inthe Default data format field, select how thedata will be serialized between the business object and the JMS messagewith a binding. To change the default, click Select besidethe field to launch the Data Transformation Configuration window.Your selections are as follows: In the next section, if you want to use the TargetFunctionNamemessage header property to be used with module to module communication,select it. If you want to use the default module to module fault handling,which is a SOAP transport, select it. A common way for specifyinga userid and password is through using the Java EE Connector (J2C)authentication data entries. The entries are defined on the server.In the Security configuration section, select Specifya Java Authentication and Authorization Services (JAAS) alias securitycredential when server security is enabled , if it is usedby your organization. Enter the Java EE Connector (J2C) authenticationdata entry. Click OK . The JMS binding is created andshown in the properties view when the Binding tabis selected.

Select the messaging domain: Point-to-Point or Publish-Subscribe.

Select
if you want to Configure new messaging provider resources (the
default) or Use pre-configured messaging provider resources.
If you choose pre-configured, then add the JNDI names for the connection
factory and the send destination for a one-way operation, and send
and receive destinations for a request-response operation.

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

Click OK. The JMS binding is created and
shown in the properties view when the Binding tab
is selected.

3. Selecting the Binding tab shows
the adapter type and serialization type.
4. Selecting the End-point configuration tab
and Connection tab allows you to specify a
JNDI lookup name. If a JNDI lookup name is specified then you are
using a managed connection factory configured on the server, so the
managed connection factory class and its properties will not be shown
here. In addition, all sections except method bindings properties
and authentication properties on the Security attributes tab
will not be shown. In our case, a JNDI lookup name was not specified,
so the managed connection factory will be created on the server using
the properties specified here. The default messaging provider provides
a domain-independent managed connection factory (conforming to the
JMS 1.1 specification), which is selected by default.  The Managed
Connection Factory Properties section specifies the managed
connection factory class and its properties such as the service bus
name and quality of service with respect to persistence, in the case
of the WebSphere default
messaging provider resource adapter. The necessary fields are completed
for you. Advanced indicates quality of service
properties such as persistence properties and if this is a shared
property.
5. Expanding Admin Connection Properties provides connection
pool properties and configuration properties if you would like custom
names and values. If you had specified an JNDI name earlier, it is
empty since the server is determining connection pooling values.
6. Selecting the JMS Destinations tab
lists the sending, receiving and callback properties. In the Send
Destination Properties section, the type of destination
and its properties are listed and can be changed. If you specify a
JNDI name, this information is not available as it is configured on
the server; that is, the destination specified on the server under
this JNDI name will be used.  Note: If you specify nothing
in the Queue Name or Topic Space field,
a default value will be created. If you specify a queue name or a
topic space, this value will remain even if you then clear the field.
The only way to change the value is to specify a different value.
A name is required because you initially generated a one-way or request-response
operation, which requires a name for the destination.
7. In the Receive Destination Properties section,
the type of destination and its properties are listed and can be changed.
If you specify a JNDI name, this information is not available as it
is configured on the server.  Note: If you specify nothing
in the queue name or topic space field, a default value will be created.
If you specify a queue name or a topic space, this value will remain
even if you then clear the field. The only way to change the value
is to specify a different value. A name is required because you initially
generated a request-response operation, which requires a name for
the destination.
8. In the Callback Destination Properties section,
the callback destination type may be specified or a JNDI name where
the same information is specified. The Response
Connection tab allows you to specify properties on the
response connection in the case of a request-response operation. You
can specify an ActivationSpec class name, a listener type and a function
selector.
9. Selecting Method bindings shows
the bound methods. By default, all methods are bound. However, some
of these methods may not be needed for JMS usage. If so, clear the Bind check
box under the Generic tab. You may also add
a description of the method binding.  The Data
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
The JMS Type property conforms to the JMSType specified in
the JMS specification. This property contains
a message type identifier supplied by a client when a message is sent.
The JMS Correlation ID property conforms to the JMSCorrelationID
in the JMS specification. A typical use is to link a response message
with its request message. In IBM® Integration
Designer,
the ID is used by the message selector to select only messages with
that ID. It can be any string value. JMS message properties can effectively
be used to add optional header fields to a message. Custom Headers allows
you to specify a name, type and value for a property.
10 Selecting the Faults configuration tablets you configure the faults specified on the operations in the interface.The configuration of faults is optional. The configuration can applyto all operations or a specific operation. If faultconfiguration is new to you, see Handling faults in bindings for an overview. Click Select beside Faultselector to configure a fault. Your selections are asfollows: Specifying a fault selector requires that you also specifythe data format for the fault. Click Select beside Businessfault data format . Your selections are as follows: Expanding Advanced , lets you alsospecify the data format for a runtime exception.

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

11. Selecting Security attributes shows
the authentication properties under Authentication Properties section.
The J2C Authentication Data Entry property
is available if you want to specify a name. If Advanced is
selected, authentication properties are shown such as the level of
the authentication; for example, at the container level.  The Response
Connection tab can be used to set the same properties
on the response connection in the case of a request-response operation.
12. The Message Configuration tab shows
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
13. The Propagation tab lets you select
two types of context propagation. Context propagation takes information
associated with a runtime or an application and passes it along with
requests that are the result of interactions with that runtime or
application. The default is to use runtime context propagation. See Propagation.
14. Selecting the Summary tab specifies
the send and receive (in the case of a request-response operation)
JNDI names and managed connection factory name. They are names generated
by the SCA JMS handler or defined by yourself when the application
is deployed. These JNDI names may be necessary when authoring the
targeted JMS application.

## What to do next

## Related tasks

- Generating a JMS export binding