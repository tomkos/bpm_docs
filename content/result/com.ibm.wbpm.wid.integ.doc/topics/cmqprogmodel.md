<!-- image -->

# WebSphere MQ programming
model

Message queuing (MQ) is a way to have application-to-application
communication in an asynchronous manner instead of the tightly-coupled
synchronous manner. Applications write and retrieve messages (or data)
using queues without requiring a direct connection. Using queues means
that the sending and receiving applications do not need to be running
concurrently. Simply put, message queues allow applications to be
loosely coupled, a goal in service oriented applications. IBM® WebSphere MQ products let applications
send and receive messages across a network of operating systems, subsystems
and protocols making WebSphere MQ
products widely used in the computer industry. WebSphere MQ products are particularly
of importance to developers building applications which require a
reliable means of delivering data between applications.

Two different application programming interfaces, Message Queueing
Interface (MQI) and MQ Java™ Message
Service (JMS), are supported. MQ JMS is MQ's support for the JMS API.
MQ JMS is discussed in the WebSphere MQ JMS programming model section. One important
feature of MQI is that it has few commands, this ease-of-use combined
with the widespread use of WebSphere MQ
products means that MQI has become a de facto standard for many developers
as the message queuing interface. In the diagram below the WMQ client
application interacts with the WMQ server through the MQI Application
Programming Interface (API).

The diagram shows the basic elements of how a service component
architecture (SCA) application developed in IBM Integration
Designer interacts
with a WebSphere MQ application.
The SCA application is running on a server. It uses the Java Naming and Directory Interface (JNDI) to
retrieve configuration information when it is invoked. Both the MQ
queue manager and the MQ queues have been registered in the JNDI directory.
They can be registered in JNDI automatically.

The MQ bindings that allow the SCA application to interact with
the WMQ client application through the WMQ server are either import
bindings or export bindings. An import allows the SCA application
to initiate the sending and receiving (in the case of a request-response
operation) of messages to the WMQ client. An export is the reverse.
The WMQ client application initiates the sending and receiving (in
the case of a request-response operation) of messages to the SCA application.

To enable this communication, the SCA import or export must have
the host name of the WMQ server, its port number, its send and receive
destination queues (for one-way communication, only one queue destination
is needed), and its server channel.

<!-- image -->