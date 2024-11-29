<!-- image -->

# Generating a JMS export binding

## Before you begin

If you intend
to use the standard JMS message class with a body type containing
the message then you must use the business objects provided for these
body types (see Working with the simple JMS data bindings).

## About this task

## Procedure

1. Open the assembly editor. Under Inbound Exports,
select JMS and drag it to the assembly editor.
Select an interface or create one. Alternately, under Components,
select Export and drag it on to the canvas.
An export with no implementation and no interface is created. Right-click
the component, select Add Interface from the menu and add an
interface that describes your interaction with a JMS application.
Create an export with a JMS binding by right-clicking the component
and from the menu selecting Generate Binding > Messaging
Binding > JMS Binding.
2 The Configure JMS Export Service windowbox opens. There is a slight difference between an interface witha one-way operation and an interface with a request-response operation.An interface with a request-response operation has an additional fieldfor a send destination. Select the messaging domain: Point-to-Point or Publish-Subscribe . Selectif you want to Configure new messaging provider resources (thedefault) or Use pre-configured messaging provider resources .If you choose pre-configured, then add the JNDI names for the activationspecification and the receive destination for a one-way operation,and receive and send destinations for a request-response operation. You should periodically check your binding configuration information at run time in theadministrative console. In particular check the state of the endpoint. Under some conditions theendpoint may go into a paused state and you will need to restart it (see Viewing or changing the state of an endpoint ). Ifyou specify JNDI names and then switch to specifying your own configurationproperties both sets of values remain in memory until you close theeditor. You are saved from reentering the values while you decide. Inthe Default data format field, select how thedata will be serialized between the business object and the JMS messagewith a binding. To change the default, click Select besidethe field to launch the Data Transformation Configuration window.Your selections are as follows: In the Function selector section,select the function selector configuration you want to use. A functionselector selects an operation to invoke on your component at run time.Clicking Select beside the Functionselector field, launches the Function SelectorConfiguration window and provides the following selections: In the next section, if you want to use the default moduleto module fault handling, which is a SOAP transport, select it. Acommon way for specifying a userid and password is through using theJava EE Connector (J2C) authentication data entries. The entries aredefined on the server. In the Security configuration section,select Specify a Java Authentication and AuthorizationServices (JAAS) alias security credential when server security isenabled , if it is used by your organization. Enter theJava EE Connector (J2C) authentication data entry. Click OK .The basic JMS binding is created and shown in the properties viewwhen the Binding tab is selected.

Select the messaging domain: Point-to-Point or Publish-Subscribe.

Select
if you want to Configure new messaging provider resources (the
default) or Use pre-configured messaging provider resources.
If you choose pre-configured, then add the JNDI names for the activation
specification and the receive destination for a one-way operation,
and receive and send destinations for a request-response operation.

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
The basic JMS binding is created and shown in the properties view
when the Binding tab is selected.

3. Selecting the Binding tab shows
the adapter type, default data format selector, fault selector, runtime
exception selector, and function selector that you previously specified. 
You can change the selections and, in the case of the data
format, use a data handler if you are using a custom data format.
4. Selecting the End-point configuration tab
and the Connection tab, opens the connection
properties. You may specify a JNDI lookup name. If a JNDI lookup name
is specified then you are using an ActivationSpec configured on the
server, so the ActivationSpec class and its properties will not be
shown here. In addition, all sections except method bindings properties
and authentication properties on the Security attributes tab
will not be shown. In our case, a JNDI lookup name was not specified
so the ActivationSpec will be created on the server using the properties
specified here.  The ActivationSpec Properties section
specifies the properties for the ActivationSpec class, which represents
the configuration required to establish the connection between the
service and the messaging provider. Specifically, these properties
specify the bus name, durability, destination type and mode, and advanced
properties for concurrency and sharing of durable subscriptions. Advanced specifies
the listener type.
5. Beneath JMS Destinations in the Receive
Destination Properties section, the type of destination
and its properties are listed and can be changed. If you specify a
JNDI name, this information is not available as it is configured on
the server.  Note: If you specify nothing in the Queue
Name or Topic Space field, a default
value will be created. If you specify a queue name or a topic space,
this value will remain even if you then clear the field. The only
way to change the value is to specify a different value. A name is
required because you initially generated a one-way or request-response
operation, which requires a name for the destination.
Selecting
the Send Destination Properties section, specifies
the type of destination and its properties for a send destination
in a response-request operation. If you specify a JNDI name, this
information is not available as it is configured on the server; that
is, the destination specified on the server under this JNDI name will
be used. 
Note: If you specify nothing in the queue name or
topic space field, a default value will be created. If you specify
a queue name or a topic space, this value will remain even if you
then clear the field. The only way to change the value is to specify
a different value. A name is required because you initially generated
a request-response operation, which requires a name for the destination.
In
the Callback Destination Properties section,
the callback destination type may be specified or a JNDI name where
the same information is specified.
6. Selecting the Response Connection tab
lists the managed connection factory properties and the administration
connection properties of the response connection. The Managed
Connection Factory Properties section specifies the managed
connection factory class and its properties such as the service bus
name and quality of service with respect to persistence, in the case
of the WebSphere default
messaging provider resource adapter. Other JMS resource adapters would
have different properties. The necessary fields are completed for
you. Advanced indicates if this is a shared
connection property.  Expanding Admin Connection
Properties provides connection pool properties and configuration
properties if you would like custom names and values. If you had specified
an JNDI name earlier, it is empty since the server is determining
connection pooling values and only an information name is present.
7. Selecting Method bindings lists
the methods beneath the Generic tab. By default,
all methods are bound. However, some of these methods may not be needed
for JMS usage. If so, clear the Bind method check
box. The method binding has a native method attribute, which contains
an identifier representing a JMS message. By default, the value of
native method is set to the interface operation name when the JMS
export is created. The JMS export utilizes a function selector to
inspect an incoming message and return the name of the native method
from a value in the message header.   Data
Serialization lets you specify serialization types for
each input and output data binding in each method beneath the  tab. 
Message
type is used by the server to create and send the outgoing
message. It is used with some data format transformers. If the server
does not use the message type specified then it is disabled. Valid
types are byte, map, object, stream or text.
8 Selecting the Faults configuration tablets you configure the business fault data format for the faults inthe interface. The configuration of faults is optional. The configurationcan apply to all operations, a specific operation or a specific fault. If fault configuration is new to you, see Handling faults in bindings for an overview. Click Select beside Businessfault data format . Your selections are as follows:

If fault configuration is new to you, see Handling faults in bindings for an overview.

- Use a data format transformation in the binding registry. This
list includes the Prepackaged JMS data format transformations.
- Use a custom data format transformation you have created in your
workspace
- Create a new Creating a data format transformation resource configuration .
9. Selecting the Security attributes tab
and the Connection tab and expanding the Authentication
Properties section opens the authentication properties for a connection.
The J2C Authentication Data Entry property
is available if you want to specify a name. If Advanced is
selected, authentication properties are opened such as the level of
the authentication; for example, at the container level.  Selecting Response
Connection and expanding the Authentication Properties section
opens the authentication properties for the response connection. The J2C
Authentication Data Entry property is available if you
want to specify a name. If Advanced is selected, authentication
properties are opened such as the level of the authentication; for
example, at the container level.
10. Selecting the Message Configuration tab
shows the correlation scheme for the response message.Request
Message ID to Correlation ID adds a request ID to the
request message. It is expected that the reply copies the request
ID to the correlation ID field of the response message so that the
caller can correlate the reply message with the request message. Request
Correlation ID to Correlation ID adds the correlation
ID to the request message. It is expected that the reply copies the
request correlation ID to the correlation ID field of the response
message so that the caller can correlate the reply message with the
request message.  The Asynchronous reliability property
can have these values: assured (default) or bestEffort.
Select assured if you want a message to persist
through a transaction. In other words, if you want guaranteed delivery
of the message. Select bestEffort if you want
a high throughput of messages and your application can accept and
handle the loss of a message, as persistence is not guaranteed.
Event
sequence required specifies if the sequence of messages
is ordered and requires responses in the same order.
Failed
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
the receive and send (in the case of a request-response operation)
JNDI names for destinations, the activation specification, and the
response managed connection factory. The function selector class name
is also specified. The JNDI names are generated by the SCA JMS handler
or defined by yourself when the application is deployed. These JNDI
names may be necessary when authoring the targeted JMS application.

## What to do next

## Related tasks

- Generating a JMS import binding