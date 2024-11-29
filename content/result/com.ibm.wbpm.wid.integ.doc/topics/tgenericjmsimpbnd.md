<!-- image -->

# Generating a generic JMS import binding

## Before you begin

If you intend
to use the standard JMS message class with a body type containing
the message then you must use the business objects provided for these
body types (see Working with the simple JMS data bindings).

## About this task

## Procedure

1. Open the assembly editor. Under Outbound Imports,
select Generic JMS and drag it to the assembly
editor. Select an interface or create one. Alternately,
from the palette under Components, select Import and
drag it on to the canvas. An import with no implementation and no
interface is created. Right-click the import, select Add Interface from
the menu and add an interface describing your interaction with a generic
JMS client. Generate the generic JMS binding by selecting the import
and from the menu selecting Generate Binding > Messaging
Binding > Generic JMS Binding.
2 The Configure Generic JMS Import Service windowbox opens. The window is similar for both an interface with a one-wayoperation or a request-response operation. However, an interface witha request-response operation has an additional field for a receivedestination. Select the messaging domain: Point-to-Point or Publish-Subscribe . Selectif you want to Configure new messaging provider resources (thedefault) or Use pre-configured messaging provider resources . Whenyou configure the generic messaging provider resources using provider-specificfacilities and select the first option, specify the generic messagingprovider name and the JNDI lookup names for the connection factoryand the send destination for a one-way operation, and send and receivedestinations for a request-response operation. These resources aretreated as external resources. The deployment will automatically createthe JMS resources (aliases) required in IBM® Business AutomationWorkflow forthese external resources. If you choose pre-configured messagingprovider resources, then add the JNDI names for the connection factoryand the send destination for a one-way operation, and send and receivedestinations for a request-response operation. These are resourcesconfigured in the IBM WorkflowServer administrativeconsole that wrap external resources. Note: It is your responsibilityto set up the third-party messaging provider and map the messagingprovider's connection factory and send and receive destination queuesto these JNDI names. If you specify JNDI names and then switchto specifying your own configuration properties both sets of valuesremain in memory until you close the editor. You are saved from reenteringthe values while you decide. In the Default dataformat field, select how the data will be serialized betweenthe business object and the JMS message with a binding. To changethe default, click Select beside the fieldto launch the Data Transformation Configuration window.Your selections are as follows: In the next section, if you want to use the TargetFunctionNamemessage header property to be used with module to module communication,select it. If you want to use the default module to module fault handling,which is a SOAP transport, select it. A common way for specifyinga userid and password is through using the Java EE Connector (J2C)authentication data entries. The entries are defined on the server.In the Security configuration section, select Specifya Java Authentication and Authorization Services (JAAS) alias securitycredential when server security is enabled , if it is usedby your organization. Enter the Java EE Connector (J2C) authenticationdata entry. Click OK . The generic JMS binding is createdand shown in the properties view when the Binding tab is selected.

Select the messaging domain: Point-to-Point or Publish-Subscribe.

Select
if you want to Configure new messaging provider resources (the
default) or Use pre-configured messaging provider resources.

When
you configure the generic messaging provider resources using provider-specific
facilities and select the first option, specify the generic messaging
provider name and the JNDI lookup names for the connection factory
and the send destination for a one-way operation, and send and receive
destinations for a request-response operation. These resources are
treated as external resources. The deployment will automatically create
the JMS resources (aliases) required in IBM® Business Automation
Workflow for
these external resources.

If you choose pre-configured messaging
provider resources, then add the JNDI names for the connection factory
and the send destination for a one-way operation, and send and receive
destinations for a request-response operation. These are resources
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

Click OK. The generic JMS binding is created
and shown in the properties view when the Binding tab is selected.

3. Selecting the End-point configuration tab
and Request tab displays the external JNDI
name for the connection factory you added earlier. Advanced allows
you to specify connection pool properties like a timeout value.Send
Destination Properties displays the external JNDI name
for the send destination you added earlier. You have the option of
changing these JNDI names or using JNDI names that map to a pre-configured
messaging provider resource.
4. Selecting the Response tab in the
case of a request-response operation has a field for the listener
port name and specifies the number of retries and sessions for the
listener port. It displays the receive destination external JNDI name
added earlier, which you can change, and the connection factory properties.
By default, response is handled by the same connection factory as
request. Selecting Configure response connection allows
you to use a different JNDI name for the response connection factory.
5. Selecting Method bindings shows
the bound methods. By default, all methods are bound. If you add a
method to the interface after you created the binding, however, a Bind
operation check box becomes available for you to add it
to the bound methods. The Generic tab
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
be used to add optional header fields to a message.
JMS delivery
mode can be persistent or non-persistent and the JMS priority sets
the priority of the message in a 0 to 9 range, with 9 the highest
in priority. If no selection is made then the priority is determined
by the application. Custom Headers allows you to specify a
name, type and value for a property.
6 Selecting the Faults configuration tablets you configure the faults specified on the operations in the interface.The configuration of faults is optional. The configuration can applyto all operations or a specific operation. If faultconfiguration is new to you, see Handling faults in bindings foran overview. Click Select beside Faultselector to configure a fault. Your selections are asfollows: Specifying a fault selector requires that you also specifythe data format for the fault. Click Select beside Businessfault data format . Your selections are as follows: Expanding Advanced , lets you alsospecify the data format for a runtime exception.

If fault
configuration is new to you, see Handling faults in bindings for
an overview.

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
8. The Message Configuration tab shows
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
9. The Propagation tab lets you select
two types of context propagation. Context propagation takes information
associated with a runtime or an application and passes it along with
requests that are the result of interactions with that runtime or
application. The default is to use runtime context propagation. See Propagation.
10. Selecting the Summary tab specifies
the send and receive (in the case of a request-response operation)
JNDI names and connection factory name and data binding class name.
They are names generated by the SCA JMS handler or defined by yourself
when the application is deployed. You may need the JNDI names if you
are authoring the targeted JMS application.

## What to do next