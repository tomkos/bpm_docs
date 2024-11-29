<!-- image -->

# Creating a JMS import to communicate with a JMS client

## Before you begin

Prerequisite:  The JMS administered objects are
configured for the JMS Client and known. In addition, there should
be a module that contains your service-oriented architecture application.
 The message format expected by the JMS client is also known

## About this task

## Procedure

1. In order for your SOA application to communicate to an
existing JMS client, you will need to have created a business object
and an interface that would represent your JMS client application
in an SOA manner. Mapping a message to an SCA interface provides
guidance on how to create such a business object and interface.
2. You must create a component that will enable your existing
SOA application to communicate to the existing JMS client application.
To do this, you will create an import and add a binding type of JMS
to it.   There are two main types of information that
need to be captured by the JMS binding. One set of information is
needed by the Service Component Architecture (SCA). This includes
information such as the interface, which we discussed earlier, and
the serialization type, which we will discuss later. The other set
of information is the configuration needed to communicate using JMS
such as the specification of JMS destination objects, which we will
also discuss later. 
Open the assembly editor of your module.
From the palette, select an import and drag it on to the canvas. An
import with no implementation and no interface is created. Right-click
the import, select Add Interface from the menu
and add the interface created in step 1. Generate the JMS skeleton
binding by selecting the import and from the menu select Generate
Binding > Messaging Binding > JMS Binding.
3. The JMS Import Binding window opens.
You can select the JMS messaging domain as either Publish-Subscribe or Point-to-Point.
The consequences of selecting publish-subscribe is that the values
for the JMS Destination type will default to use javax.jms.Topic.
Similarly, the consequences of selecting point-to-point is that the
values for the JMS Destination type will be default to use javax.jms.Queue.
You can change these defaults within the wizard. If your interface
contains a request-response operation, the wizard will default the
JMS messaging domain to point-to-point.
You must choose the
serialization type that is expected by the JMS client application,
as specified by the data binding. The serialization type is used to
map between the business object used in your SOA application and the
message format expected by the JMS client application. There are several
default serialization types provided. For serialization types beginning Simple
JMS, you must have previously created the business objects
required.
 In the Function selector section,
if you do not want to use the TargetFunctionName message header property
for the default JMS function selector class, clear it. 
In this
task, the JMS client is expecting XML in a JMS text message so we
chose the appropriate data format transformation, which is Serialized
Java Object (JMS). In addition, because you are communicating
with an existing JMS client, you will clear the Generate
"TargetFunctionName" message header property for default JMS Function
Selector because the JMS client would not know how to
handle the custom JMS header tag that would have been generated if
it were checked.
4. The JMS binding is created and shown in the properties
view when the Binding tab is selected. You
need to specify the administered objects that were configured. The
following chart provides some guidance in this area.  
Table 1. Relationship of usage, configuration, connection factory and
destination information

Usage and configuration
Managed connection factory
Send destination
Receive destination
Callback destination

Usage
A factory used to create the connection to the
messaging provider.
The destination where the message would be sent.
The destination where the response message would
be received. This value is specified in the JMSReplyTo field
of the sent message.
A destination used for internal purposes.

Configuration
If your administrator provided an administered
connection factory object, use the JNDI name.If you do not use
a JNDI name, a new connection factory will be created using the default
settings when the SOA application is deployed. Your administrator
should check that the connections resulting from this factory is appropriate
to connect to the messaging provider.

If your administrator provided an administered
destination object where messages should be sent to the JMS client,
use the JNDI name.If you do not use a JNDI name, a new destination
would be created when the SOA application is deployed and this would
be used as the destination for the sent message. Your administrator
should then pass this JNDI name to the JMS client.

If your administrator provided an administered
destination object where messages should be received (if any), use
the JNDI name.If you do not use a JNDI name, a new destination
would be created when the SOA application is deployed and this would
be used as the destination for the receive message (if any). Your
administrator should then pass this JNDI name to the JMS client.
Note: The
SCA application will be listening to messages on the Receive Destination
using a specific correlation scheme.  The received message is expected
to have the sent message's message id.  That is, the receive message
needs to have its message header property JMSCorrelationID to
match the sent message header property JMSMessageID.
 The JMS client must ensure that response messages it sends to the
SOA application have the message header property JMSCorrelationID specified
correctly, otherwise the SOA application will not receive the message.

You can specify a JNDI name of an existing administered
destination object for performance reasons. If you do not specify
a JNDI name, a new destination would be created each time the SOA
application is deployed.

To specify the administered objects, select the Endpoint
configuration tab under the Binding tab.
Under the Connection tab, you can specify a
bound connection factory class to connect to the IBM® Business Automation
Workflow default
JMS provider. You could also accept the defaults, in which case the
tools would create a connection factory when the application is deployed
on the server. Because the connection factory that would be created
with the default settings is sufficient for this task, you will accept
the defaults.
Under the JMS Destinations tab,
you can specify the administered destination objects to send and receive
messages or you can accept the defaults, in which case the tools would
create them. Specify the appropriate settings to ensure your SOA application
is able to communicate to the JMS client. For this task, the administrator
provided JNDI names for the bound destination objects to send and
receive a message to the existing JMS client and so you will specify
the JNDI names for them. For the Send Destination Properties section,
select the button Specify JNDI name for pre-configured
messaging provider resource. Specify the JNDI name of
the bound destination where you want to send your messages. Similarly,
for the Receive Destination Properties section,
select the button of Specify JNDI name for pre-configured
messaging provider resource. Specify the JNDI name of
the bound destination where you are to receive your messages.
5. The existing JMS client might expect certain header properties
to be configured. You can specify these under the Method
bindings tab under the Binding tab.
For each business method that represents a corresponding JMS client
application method, you can specify unique JMS message header properties
required. For example, if the existing JMS client application requires
the message header JMSType to specify the application
method name for which the JMS message is targeted, you will specify
it here. Specify the application method name. Select Bound
Methods for your business methods and specify the appropriate
value in the JMS Type text field.
6. The import that will communicate to the existing JMS client
application is completed. You should test it before you attach it
to your SOA application to ensure it is working as designed. To do
this, you can use the test component feature of the integration test
client. Once you are certain that it is correct, you can then connect
your SOA application to the import you just created.

## Related tasks

- Creating a JMS export to communicate with a JMS client
- Creating a JMS client to receive messages from a JMS import
- Creating an import from an export using a JMS binding
- Creating a user-defined JMS data binding