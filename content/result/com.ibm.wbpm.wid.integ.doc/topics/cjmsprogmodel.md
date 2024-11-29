<!-- image -->

# Java Message Service
(JMS) programming model

JMS defines an API for accessing services from a messaging provider;
that is, it is not a product itself. It is a set of interface classes
that messaging provider vendors implement. Applications that use the
JMS API can then communicate with the messaging provider the vendor
supplies. The JMS API has become the industry standard interface for Java™ applications to create, send,
receive and read messages using messaging providers that support the
JMS API. The standard is associated with the Java Platform, Enterprise Edition (Java EE)
platform. Java EE is a set of standards for a component-based way
to develop, assemble and deploy enterprise applications. Java EE containers
implement a standard runtime environment that provides quality of
service items such as security, transaction support and thread pooling.

In the following diagram, the JMS provider implements the
JMS API. It is the entity with which the JMS client interacts.
The JMS client establishes a connection and a session through which
the interaction takes place. The JMS client establishes the connection
based on configuration information in the connection factory and
identifies where a message is to be sent to or retrieved from based
on the destination. Both the connection factory and destination
objects are listed in the Java Naming
and Directory Interface (JNDI) namespace. JNDI is the Java industry standard API for accessing naming
and directory services. Since the connection factory and destination
are administered objects by JNDI, it means the JMS client can connect
to different JMS providers without changing JMS client code; that
is, it creates portability. It also means that attributes which often
can and do change dynamically such as the destination can be changed
independent of the JMS client code.

<!-- image -->

| Common              | Point-to-Point              | Publish-Subscribe        |
|---------------------|-----------------------------|--------------------------|
| ConnectionFactory * | QueueConnectionFactory *    | TopicConnectionFactory * |
| Connection          | QueueConnection             | TopicConnection          |
| Destination *       | Queue *                     | Topic *                  |
| Session             | QueueSession                | TopicSession             |
| MessageProducer     | QueueSender                 | TopicPublisher           |
| MessageConsumer     | QueueReceiver, QueueBrowser | TopicSubscriber          |

The JMS application is written to use only references to interfaces.
Vendor-specific information is encapsulated in implementations of
the following JMS administered objects: QueueConnectionFactory, TopicConnectionFactory,
Queue and Topic.

These JMS administered objects are built using a vendor-supplied
administration tool and stored on a JNDI namespace. A JMS application
can retrieve these objects from the namespace and use them without
needing to know which vendor provided the implementation.

At run time, the JMS client retrieves the connection factory (ConnectionFactory
object) from a JNDI namespace and uses it to create a connection.
The connection creates a session, which, in turn, creates a message
producer or message consumer or both. The session also creates messages,
which are sent to or retrieved from a destination (retrieved from
a JNDI namespace) using the message producer and message consumer.

A recommended book that discusses JMS and its relationship to WebSphere® in detail is Enterprise Messaging Using JMS and IBM® WebSphere by
Kareem Yusuf.