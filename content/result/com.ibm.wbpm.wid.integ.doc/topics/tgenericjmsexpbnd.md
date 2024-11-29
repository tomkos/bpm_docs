<!-- image -->

# Generating a generic JMS export binding

## Before you begin

If you intend
to use the standard JMS message class with a body type containing
the message then you must use the business objects provided for these
body types (see Working with the simple JMS data bindings).

## About this task

## Procedure

1. Open the assembly editor. Under Inbound Exports,
select Generic JMS and drag it to the assembly
editor. Select an interface or create one. Alternately,
from the palette under Components, select an
export and drag it on to the canvas. An export with no implementation
and no interface is created. Right-click the export, select Add
Interface from the menu and add an interface that describes your
interaction with a JMS application. Create an export with a JMS binding
by right-clicking the export and from the menu selecting Generate
Binding > Messaging Binding > Generic JMS Binding.
2 The Configure Generic JMS Export Service windowbox opens. There is a slight difference between an interface witha one-way operation and an interface with a request-response operation.An interface with a request-response operation has an additional fieldfor a send destination. Select the messaging domain: Point-to-Point or Publish-Subscribe . Selectif you want to Configure new messaging provider resources (thedefault) or Use pre-configured messaging provider resources . Whenyou configure the generic messaging provider resources using provider-specificfacilities and select the first option, specify the generic messagingprovider name and the JNDI lookup names for the connection factoryand the receive destination for a one-way operation, and send andreceive destinations for a request-response operation. These resourcesare treated as external resources. The deployment will automaticallycreate the JMS resources (aliases) required in IBM® Business AutomationWorkflow forthese external resources. If you choose pre-configured messagingprovider resources, then add the JNDI names for the connection factoryand the receive destination for a one-way operation, and send andreceive destinations for a request-response operation. These are resourcesconfigured in the IBM WorkflowServer administrativeconsole that wrap external resources. Note: It is your responsibilityto set up the third-party messaging provider and map the messagingprovider's connection factory and send and receive destination queuesto these JNDI names. If you specify JNDI names and then switchto specifying your own configuration properties both sets of valuesremain in memory until you close the editor. You are saved from reenteringthe values while you decide. In the Default dataformat field, select how the data will be serialized betweenthe business object and the JMS message with a binding. To changethe default, click Select beside the fieldto launch the Data Transformation Configuration window.Your selections are as follows: In the Function selector section,select the function selector configuration you want to use. A functionselector selects an operation to invoke on your component at run time.Clicking Select beside the Functionselector field, launches the Function SelectorConfiguration window and provides the following selections: In the next section, if you want to use the default moduleto module fault handling, which is a SOAP transport, select it. Acommon way for specifying a userid and password is through using theJava EE Connector (J2C) authentication data entries. The entries aredefined on the server. In the Security configuration section,select Specify a Java Authentication and AuthorizationServices (JAAS) alias security credential when server security isenabled , if it is used by your organization. Enter theJava EE Connector (J2C) authentication data entry. Click OK .The basic generic JMS binding is created and shown in the propertiesview when the Binding tab is selected.

Select the messaging domain: Point-to-Point or Publish-Subscribe.

Select
if you want to Configure new messaging provider resources (the
default) or Use pre-configured messaging provider resources.

When
you configure the generic messaging provider resources using provider-specific
facilities and select the first option, specify the generic messaging
provider name and the JNDI lookup names for the connection factory
and the receive destination for a one-way operation, and send and
receive destinations for a request-response operation. These resources
are treated as external resources. The deployment will automatically
create the JMS resources (aliases) required in IBM® Business Automation
Workflow for
these external resources.

If you choose pre-configured messaging
provider resources, then add the JNDI names for the connection factory
and the receive destination for a one-way operation, and send and
receive destinations for a request-response operation. These are resources
configured in the IBM Workflow
Server administrative
console that wrap external resources.

If you specify JNDI names and then switch
to specifying your own configuration properties both sets of values
remain in memory until you close the editor. You are saved from reentering
the values while you decide.

In the Default data
format field, select how the data will be serialized between
the business object and the JMS message with a binding. To change
the default, click Select beside the field
to launch the Data Transformation Configuration window.
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
The basic generic JMS binding is created and shown in the properties
view when the Binding tab is selected.

3. Selecting the End-point configuration tab
and the Request tab, displays the external
JNDI name for the connection factory you added earlier. Advanced allows
you to specify connection pool properties like a timeout value. Listener
Port Properties provides a field for the listener port
name and specifies the number of retries and sessions for the listener
port. Receive Destination Properties displays the external JNDI name
for the recieve destination you added earlier. You have the option
of changing these JNDI names or using JNDI names that map to a pre-configured
messaging provider resource.
4. Selecting the Response tab in the
case of a request-response operation, displays the send destination
external JNDI name added earlier, which you can change, and the connection
factory properties. By default, response is handled by the same connection
factory as request. Selecting Configure response connection allows
you to use a different JNDI name for the response connection factory.
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
The JMS Type property conforms to the JMSType specified in
the JMS specification. This property contains
a message type identifier supplied by a client when a message is sent.
The JMS Correlation ID property conforms to the JMSCorrelationID
in the JMS specification. A typical use is to link a response message
with its request message. In IBM Integration
Designer,
the ID is used by the message selector to select only messages with
that ID. It can be any string value. JMS message properties can effectively
be used to add optional header fields to a message. Custom Headers allows
you to specify a name, type and value for a property.
6 Selecting the Faults configuration tablets you configure the business fault data format for the faults inthe interface. The configuration of faults is optional. The configurationcan apply to all operations, a specific operation or a specific fault. If fault configuration is new to you, see Handling faults in bindings foran overview. Click Select beside Businessfault data format . Your selections are as follows:

If fault configuration is new to you, see Handling faults in bindings for
an overview.

- Use a data format transformation in the binding registry. This
list includes the Prepackaged JMS data format transformations.
- Use a custom data format transformation you have created in your
workspace
- Create a new Creating a data format transformation resource configuration .
7. Selecting Security attributes shows
the authentication properties under Authentication Properties section.
The J2C Authentication Data Entry property
is available if you want to specify a name. If Advanced is
selected, authentication properties are shown such as the level of
the authentication; for example, at the container level.  Selecting Response and
expanding the Authentication Properties section opens the authentication
properties for the response connection, if you had specified one earlier
in the end-point configuration. The J2C Authentication
Data Entry property is available if you want to specify
a name. If Advanced is selected, authentication properties
are opened such as the level of the authentication; for example, at
the container level.
8. Selecting the Message Configuration tab
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
9. The Propagation tab lets you select
two types of context propagation. Context propagation takes information
associated with a runtime or an application and passes it along with
requests that are the result of interactions with that run time or
application. The default is to use runtime context propagation. See Propagation.
10. Selecting the Summary tab specifies
the receive and send (in the case of a request-response operation)
JNDI names for destinations and the request and response connection
factories. The listener port name, function selector class name and
data binding class name are also specified. The JNDI names are generated
by the SCA JMS handler or defined by yourself when the application
is deployed. You might need the JNDI names if you are authoring the
targeted JMS application.

## What to do next