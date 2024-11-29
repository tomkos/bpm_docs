<!-- image -->

# Creating a JMS export to communicate with a JMS client

## Before you begin

## Procedure

1. In order for your SOA application to communicate to an
existing JMS client, you will need to have created a business object
and an interface that would represent your JMS client application
in an SOA manner. Mapping a message to an SCA interface provides
guidance on how to create such a business object and interface.
2. You must create a component that will enable your existing
SOA application to communicate with the existing JMS client application.
To do this, you will create an export and add a binding type of JMS
to it.  There are two main types of information that
need to be captured by the JMS binding. One set of information is
needed by the Service Component Architecture (SCA). This includes
information such as the interface, which we discussed earlier, and
the serialization type, which we will discuss later. The other set
of information is the configuration needed to communicate using JMS
such as the specification of JMS destination objects, which we will
also discuss later. 
Open the assembly editor of your module.
From the palette, select an export and drag it on to the canvas. An
export with no implementation and no interface is created. Right-click
the export, select Add Interface from the menu
and add the interface created in step 1. Generate the JMS skeleton
binding by selecting the component and from the menu select Generate
Binding > Messaging Binding > JMS Binding.
3. The JMS Export Binding window appears. 
You can select the JMS messaging domain as either Publish-Subscribe or Point-to-Point.
The consequences of selecting publish-subscribe is that the values
for the JMS Destination type will default to use javax.jms.Topic.
Similarly, the consequences of selecting point-to-point is that the
values for the JMS Destination type will be default to use javax.jms.Queue.
You can change these defaults within the wizard. If your interface
contains a request-response operation, the wizard will default the
JMS messaging domain to point-to-point.
In the Data format section,
you must choose the serialization type that is expected by the JMS
client application, as defined by the data binding. The serialization
type is used to map between the message format expected by the JMS
client application and the business object used in your SOA application.
There are several default serialization types provided. For serialization
types beginning Simple JMS, you must have previously
created the business objects required (see the Prerequisites section
of Generating a JMS export binding for a quick way of creating
these business objects). 
The Function selector section
determines which FunctionSelector class to use. A function selector
selects an operation to invoke on your component at run time. The
operation maps to a function to be performed based on the content
of the JMS message. For example, the message can contain an Employee
record and be used to create, update, retrieve, or delete the an Employee
record. The actual operation to invoke is determined from content
in the header or body of the JMS message.
In
this task, the JMS client is sending XML in a JMS text message so
we chose the appropriate data format transformation, which is Serialized
Java Object (JMS). In addition, because the existing JMS
client is using the message header JMSType to specify
the business method, you will clear the Use the default
JMS Function Selector class and specify the function selector
class that would provide the correct function in using the JMSType message
header property.
4. The JMS binding is created and shown in the properties
view when the Binding tab is selected. You
need to specify the administered objects that were configured. The
following chart provides some guidance in this area. 
Table 1. Relationship of usage, configuration, activation specification,
destination and response connection information

Usage and configuration
Activation specification
Receive destination
Send destination
Callback destination
Response connection

Usage
A configuration used to associate the message
endpoint with the messaging system.
The destination where the message would be received. 
The destination where the response message (if
any) would be sent.
A destination used for internal purposes.
A factory used to create the connection to the
messaging system for the sending of response messages

Configuration
If your administrator provided an administered
activation spec object, use the JNDI name.If you do not use a JNDI
name, a new activation spec will be created using the default settings
when the SOA application is deployed. Your administrator should check
that the default activation spec can appropriately communicate with
the messaging system when the message endpoint is activated. 

If your administrator provided an administered
destination object where messages would be received from the JMS client,
use the JNDI name.If you do not use a JNDI name, a new destination
would be created when the SOA application is deployed and this would
be used as the destination where the messages are received. Your administrator
should then pass this JNDI name to the JMS client.

If your administrator provided an administered
destination object where response messages should be sent, use the
JNDI name.If you do not use a JNDI name, a new destination would
be created when the SOA application is deployed and this would be
used as the destination for the response message. Your administrator
should then pass this JNDI name to the JMS client.
Note: If the
JMS inbound message contains a destination object reference in the JMSReplyTo header
property, the JNDI name under the Send Destination or
the default Send Destination that was created would not be used in
runtime but would be replaced by the value in the JMSReplyTo property
instead. 
Note: The SCA architecture uses a specific correlation
scheme to correlate response messages.  By default, the application
will populate the response message header property JMSCorrelationID with
the value found in the inbound message header property JMSMessageID.

You can specify a JNDI name of an existing administered
destination object for performance reasons. If you do not specify
a JNDI name, a new destination would be created each time the SOA
application is deployed.

If your administrator provided an administered
connection factory object, use the JNDI name.If you do not use
a JNDI name, a new connection factory would be created using the default
settings when the SOA application is deployed. Your administrator
should check that the connections resulting from this factory is appropriate
to connect to the messaging system to send the response message.

To specify the administered objects, select the End-point
configuration tab under the Binding tab.
Under the Connection tab, you can specify a
bound activation specification (Activation Spec) to connect to the
Websphere Business Automation Workflow Default
JMS provider. You can also accept the defaults, in which case the
tools would create an activation specification when the application
is deployed on the server.  Because the activation spec that would
be created with the default settings is sufficient for this task,
you will accept the defaults.
Under the JMS Destinations tab,
you can specify the administered destination objects to receive and
send messages or you can accept the defaults, in which case the tools
would create them. Specify the appropriate settings to ensure your
SOA application is able to communicate to the JMS client. For this
task, the administrator provided the JNDI name of the bound destination
object to receive the message from the existing JMS client and so
you will specify the JNDI name for it. 
Note: Because the JMS client
is populating the message header JMSReplyTo, you
would not bother with the Send Destination object
since this would be replaced during run time by this value.
Under
the Response Connection tab, you can specify
a bound connection factory to connect to the IBM® Workflow
Server Default
JMS provider. You can also accept the defaults, in which case the
tools would create a connection factory when the application is deployed
on the server.  This connection factory will be used in sending the
response message to the JMS Client.  Because the connection factory
that would be created with the default settings is sufficient for
this task, you will accept the defaults.
5. As mentioned earlier, the existing JMS client can send
in a message header property the targeted operation name that the
message is intended for.  To make sure the message invokes the correct
business method, you need to specify for each business method the
operation name from the JMS client application that maps to it.  This
is done under the Method bindings tab under
the Binding operation tab.  For each business
method, specify the JMS client application operation name that maps
to it under the field Native Method.
6. The export that will communicate with the existing JMS
client application is completed. You should test accessing the target
component of the export before you attach the export to your SOA application
to ensure it is working as designed. To test access to the target
component of the export, use the test component feature of the integration
test client. Once you are certain that your export can access the
target component, you can then connect your SCA application to the
export you just created.

## Related tasks

- Creating a JMS import to communicate with a JMS client
- Creating a JMS client to receive messages from a JMS import
- Creating an import from an export using a JMS binding
- Creating a user-defined JMS data binding