<!-- image -->

# Generating an MQ import binding

## Before you begin

## About this task

In this set of steps, you will learn how you create an
MQ binding for an import. An MQ binding is used when you want to access
the WebSphere® MQ Messaging
Provider.

If you intend to use the standard JMS message class
with a body type containing the message then you must use the business
objects provided for these body types (see Working with the simple JMS data bindings).

## Procedure

1. Open the assembly editor. Under Outbound Imports,
select MQ and drag it to the assembly editor.
Select an interface or create one. Alternately, select Import under Component on
the palette and drag it on to the canvas. An import component with
no implementation and no interface is created. Right-click the import,
select Add Interface from the menu and add an interface describing
your interaction with a WebSphere MQ
client. Generate the MQ JMS binding by selecting the import and from
the menu selecting Generate Binding > Messaging Binding
>MQ Binding.
2 The MQ Import Binding window opens.You must enter an MQ queue manager name, an MQ queue name for thesend destination, host name, server channel name and port to proceed.An interface with a request-response operation produces a similarwindow to a one-way request with an additional field for a receivedestination. Beneath End-point Configuration ,select Specify properties for configuring WebSphere MQresources (the default) or Specify JNDI namefor pre-configured WebSphere MQ resources . If you choosepre-configured, then add the JNDI names for the connection factoryand the send destination for a one-way operation, and send and receivedestinations for a request-response operation. Also add the JNDI namefor the activation specification (ActivationSpec class), which containsthe configuration information for a message end point. Typically,you would choose pre-configured if your system administrator had setup the configuration for you. You should periodically check your binding configuration information at run time in theadministrative console. In particular check the state of the endpoint. Under some conditions theendpoint may go into a paused state and you will need to restart it (see Viewing or changing the state of an endpoint ). Ifyou specify JNDI names and then switch to specifying your own configurationproperties both sets of values remain in memory until you close theeditor. You are saved from reentering the values while you decide. Howdoes binding work when you choose pre-configured resources? The MQconnection factory JNDI name means the name used to bind the MQ connectionfactory object to the JNDI namespace. The MQ send destination queueJNDI name means the name used to bind the MQ send destination queueobject to the JNDI namespace. The MQ ActivationSpec JNDI name meansthe name used to bind the MQ ActivationSpec object to the JNDI namespace.The MQ receive destination queue JNDI name means the name used tobind the MQ receive destination queue object to the JNDI namespace. The Transport fieldspecifies how the queue manager is accessed. The following selectionscan be made: A bindings connection is fastest but less secure than a clientconnection. In the Default data format field,select how the data will be serialized between the business objectand the MQ message with a binding. To change the default, click Select besidethe field to launch the Data Transformation Configuration window.Your selections are as follows: In the next section, if you want to use the default module-to-modulefault handling, which is a SOAP transport, select it. Click OK .The basic MQ binding is created and shown in the properties view whenthe Binding tab is selected. You do not see a selectionfor a messaging domain such as point-to-point or publish-subscribebecause the binding generator only supports point-to-point. The MQJMS binding, however, does support publish-subscribe.

Beneath End-point Configuration,
select Specify properties for configuring WebSphere MQ
resources (the default) or Specify JNDI name
for pre-configured WebSphere MQ resources. If you choose
pre-configured, then add the JNDI names for the connection factory
and the send destination for a one-way operation, and send and receive
destinations for a request-response operation. Also add the JNDI name
for the activation specification (ActivationSpec class), which contains
the configuration information for a message end point. Typically,
you would choose pre-configured if your system administrator had set
up the configuration for you.

You should periodically check your binding configuration information at run time in the
administrative console. In particular check the state of the endpoint. Under some conditions the
endpoint may go into a paused state and you will need to restart it (see Viewing or changing the state of an endpoint).

If
you specify JNDI names and then switch to specifying your own configuration
properties both sets of values remain in memory until you close the
editor. You are saved from reentering the values while you decide.

How
does binding work when you choose pre-configured resources? The MQ
connection factory JNDI name means the name used to bind the MQ connection
factory object to the JNDI namespace. The MQ send destination queue
JNDI name means the name used to bind the MQ send destination queue
object to the JNDI namespace. The MQ ActivationSpec JNDI name means
the name used to bind the MQ ActivationSpec object to the JNDI namespace.
The MQ receive destination queue JNDI name means the name used to
bind the MQ receive destination queue object to the JNDI namespace.

    - Client: An MQ client connection to the
queue manager is made where you specify the host name and the server
channel and port number are supplied.
    - Client channel definition table (CCDT):
The connection values are specified in a client channel definition
table.
    - Bindings: Java Native Interface (JNI) bindings
are used to connect to a queue manager. Bindings is a shared memory
protocol and can only be used when the queue manager is running locally.
    - Bindings then client: A bindings connection
is attempted and, if unsuccessful, a client connection is made.

In the Default data format field,
select how the data will be serialized between the business object
and the MQ message with a binding. To change the default, click Select beside
the field to launch the Data Transformation Configuration window.
Your selections are as follows:

    - Use a data format transformation in the binding registry. This
list includes the Prepackaged MQ data format transformations. Selecting Show the
deprecated data format transformations adds previous transformations
that have been deprecated.
    - Use a custom data format transformation you have created in your
workspace
    - Create a new Creating a data format transformation resource configuration.

In the next section, if you want to use the default module-to-module
fault handling, which is a SOAP transport, select it.

Click OK.
The basic MQ binding is created and shown in the properties view when
the Binding tab is selected.

You do not see a selection
for a messaging domain such as point-to-point or publish-subscribe
because the binding generator only supports point-to-point. The MQ
JMS binding, however, does support publish-subscribe.

3. Selecting the Binding tab shows
the serialization type, data binding class and header information. WebSphere MQ headers have
specific data types and parsers for them determine the data type of
each field in the header. Support is provided for the MQRFH and MQRFH2
header. You can also create your own header by implementing the com.ibm.websphere.sca.mq.data.MQHeaderDataBinding
class.
4 The End-Point Configuration tabshows the values you entered earlier for queue manager, send destinationand, for a request-response operation, receive destination under MessagingResource Configuration Properties . Also, the client configurationinformation is specified if you selected Use host clientconnection property earlier. Enableconnection on startup specifies that a connection shouldbe made according to the messaging endpoints when the applicationstarts (default). If deselected, the connection will not be made andthe application can determine the flow of messages. EnableXA specifies whether the connection factory is for XAor non-XA coordination of messages. XA should be selected if multipleresources are used in the same transaction (default). If deselected,the resource manager is used for local transaction calls (session.commitand session.rollback) instead of XA calls. This selection can mproveperformance but only a single resource can be enlisted in a transaction. Selecting SpecifyJNDI name for pre-configured WebSphere MQ resources removesthe fields and lets you enter the JNDI lookup names for the connectionfactory, send and receive queues, and the activation specification(ActivationSpec class), which contains the configuration informationfor a message end point. Under Connection Configuration isfound the connection information to access the server. The valuesyou entered at binding creation time are shown and can be changed. The Transport fieldspecifies how the queue manager is accessed. The following selectionscan be made: A bindings connection is fastest but less secure than a clientconnection.

Enable
connection on startup specifies that a connection should
be made according to the messaging endpoints when the application
starts (default). If deselected, the connection will not be made and
the application can determine the flow of messages.

Enable
XA specifies whether the connection factory is for XA
or non-XA coordination of messages. XA should be selected if multiple
resources are used in the same transaction (default). If deselected,
the resource manager is used for local transaction calls (session.commit
and session.rollback) instead of XA calls. This selection can mprove
performance but only a single resource can be enlisted in a transaction.

Selecting Specify
JNDI name for pre-configured WebSphere MQ resources removes
the fields and lets you enter the JNDI lookup names for the connection
factory, send and receive queues, and the activation specification
(ActivationSpec class), which contains the configuration information
for a message end point.

Under Connection Configuration is
found the connection information to access the server. The values
you entered at binding creation time are shown and can be changed.

- Client: An MQ client connection to the
queue manager is made where you specify the host name and the server
channel and port number are supplied.
- Client channel definition table (CCDT):
The connection values are specified in a client channel definition
table.
- Bindings: Java Native Interface (JNI) bindings
are used to connect to a queue manager. Bindings is a shared memory
protocol and can only be used when the queue manager is running locally.
- Bindings then client: A bindings connection
is attempted and, if unsuccessful, a client connection is made.
5. The Message Configuration tab shows
the request and response (for a request-response operation) correlation
options.  In the Request Message ID Options field, New
Message ID lets the queue manager select a unique message
ID for the request (default). Copy from SCA message sets
the message ID to be the same as the one carried in the headers of
the SCA message or create one if not found.
Set message
type to MQMT\_DATAGRAM or MQMT\_REQUEST for request-response operation means
you have the option of overriding the MessageType field.Override
reply to queue of request message means you have the option
of overriding the ReplyTo. The import will, by default, force the
ReplyTo and MessageType fields to be appropriate values. Advanced
users can switch this off, but you will have to use a mediation module
to set the fields to whatever you want. Since you can easily break
the import by getting these fields wrong, it is recommended you leave
these options checked.
In the Response Correlation
Schema field, Correlation ID copy from Request
Message ID (default) means the response message's correlation
ID will be set to the request message's message ID. Response
Message ID copy from Request Message ID means the response
message will have a message ID field set to the request message's
message ID. Correlation ID copy from Request Correlation
ID means the response message will have a correlation
ID set to the request message's correlation ID.
Failed
message recovery mode lets you allow the binding to manage
the recovery of failed messages (the default) or rely on the transport-specific
method of recovery. Allow binding to manage recovery for
failed messages creates a recovery queue on deployment
to handle failed messages. Binding errors are handled as failed events
that can be retrieved later. Rely on transport-specific
recovery for failed events does not set up a recovery
mechanism.
6. The Method Bindings tab shows the
bound methods. By default, all methods are bound. If you add a method
to the interface after you created the binding, however, a Bind
operation check box becomes available to add it to the
bound methods. The output and input data serialization types are shown.
They are by default the same as the serialization types specified
earlier.
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
list includes the Prepackaged MQ data format transformations.
- Use a custom data format transformation you have created in your
workspace
- Create a new Creating a data format transformation resource configuration .

Expanding Advanced, lets you also
specify the data format for a runtime exception.

8. Selecting the Security Attributes tab
specifies the Secure Sockets Layer (SSL) encryption properties if
required. The Cipher Suite field lists the cipher types supported.
The Peer Name specifies the SSL peer name used
in channel negotiation. Selecting FIPS required checks
that the client connection uses a cipher suite supported by the Federal
Information Processing Standards (FIPS)-approved Java™ Secure Sockets extension (JSSE) provider. Reset
count specifies the number of bytes transmitted before the SSL
encryption key is renegotiated. Certificate Revocation specifies
a Lightweight Directory Access Protocol (LDAP) server with a list
of SSL certificates which have been revoked; that is, they are no
longer valid.
9. The Propagation tab lets you select
two types of context propagation. Context propagation takes information
associated with a runtime or an application and passes it along with
requests that are the result of interactions with that runtime or
application. The default is to use runtime context propagation. See Propagation.

## What to do next

## Related tasks

- Generating an MQ export binding