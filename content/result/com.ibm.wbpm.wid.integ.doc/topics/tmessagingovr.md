<!-- image -->

# Accessing external services with messaging systems

## About this task

- Messaging architecture
- Point-to-point distribution of messages
- Publish-subscribe distribution of messages
- Message producer
- Message consumer
- One-way interaction between a message producer and a message provider
- Request-reply interaction between a message producer and a message consumer
- Connectivity between an application and a messaging provider

Asynchronous messaging does not communicate immediately like a synchronous method of
communicating. Instead, applications send messages to the messaging provider. The messaging provider
delivers the message to the target application, similar to the postal service. Like the postal
service, the messaging provider offers the application levels of quality of service, which come at a
price such as performance degradation. This quality of service guarantees that messages are
delivered, that there are no duplicates, that a message sequence is maintained, and so on. Sending
and receiving applications do not need to know of each other's existence or the nature of the
messages that each application understands. Each application is concerned with defining the format
of the messages that it will use to communicate and establishing access to the services offered by
the messaging provider. The messaging provider provides services to dynamically route and optionally
transform the message so it can be understood by the receiving application.

Although messaging
is only asynchronous, there is also synchronous messaging, which means that both applications are
available simultaneously and communicate directly in a tightly coupled manner. Synchronous messaging
can be used when the performance degradation added by introducing an intermediary is not justified
or when guaranteed delivery is not as high a priority. Response time is often an important aspect of
synchronous messaging. Synchronous messaging means that updates and changes to an application must
be known to its messaging partner.

In enterprises, many applications need to interact with one
another in support of a business. These applications change as the business itself changes.
Therefore, loosely-coupled applications using a messaging provider is usually a key to getting
disparate applications distributed across the enterprise exchanging and using data. Not
surprisingly, asynchronous messaging plays a significant role in service-oriented architecture
(SOA). The following messaging architecture diagram presents loosely-coupled business applications
connected to a messaging provider such as IBM
WebSphere® MQ and exchanging messages in order to perform
business functions. Each message has data that can be independent of the applications using it, such
as a list of inventory items. Typically, they are self-contained and can be processed independently
but messages can be ordered and processed sequentially.

<!-- image -->

In point-to-point messaging there is only one consumer. The application identifies the
target destination of the message. The messaging provider delivers the message to the destination
where the receiving application retrieves it. It is a one-to-one relationship. If the same message
must be sent to several applications then the sending application must send it separately to each
one. Point-to-point messaging is suitable to when an application communicates with another single
application or few applications. For example, an application sends a message to a human resources
application that updates an employee record.

<!-- image -->

In publish-subscribe messaging a topic defines a subject that is associated with
messages. Applications interested in that subject subscribe to that topic. An application
subscribing to a topic is a subscriber. An application that sends the messages for a topic is
a publisher. The messaging provider matches the message's topic with the subscription list.
Publish-subscribe messaging is generally a one-to-many relationship between publisher and subscriber
though it is possible to have only one or even zero subscribers. Publish-subscribe messaging is
suitable when data needs to be distributed to a varying number of applications, which can change at
any time. Publish-subscribe messaging is often used with event-driven situations. For example, an
application publishes stock prices to a set of subscribing financial applications.

<!-- image -->

A message producer is the term for the application sending a message to the message
provider. The message can be delivered using either point-to-point or publish-subscribe messaging.
Before sending, the messaging provider checks the quality of service. For example, a message
could be marked persistent, meaning that the message should be written to a storage
mechanism, such as a database, until the message has been read. This ensures that the message is not
lost should the system fail due to a hardware failure, power failure, and so on. The higher the
quality of service, the greater the performance degradation. Quality of service is determined by
business needs. Some messages do not need to be stored, such as publishing the latest stock market
prices. But a financial record must be stored. An application sending a message often expects a
reply indicating the receiving application has completed a task.

<!-- image -->

A message consumer is the term for the application receiving the message from the
messaging provider. Two modes describe how the messages are received. In the first mode, the
messaging provider starts the application when the message arrives. In the second mode, the
application polls the messaging provider for a message. A message consumer could be an application
listening for events such as a news update. Once the message arrives, the message consumer processes
it. If there are errors and the message consumer cannot process it, the message is sent again until
message retrying expires. The number of retries is determined by the quality of service.

<!-- image -->

Message producers often communicate with message consumers using the one-way pattern.
For example, a message producer could be keeping a consumer informed of current international
currency rates, in which case there is no need to transmit information back to the producer.

<!-- image -->

Message producers and message consumers sometimes communicate using the request-reply
pattern, which is a conversation between the two about a set of related messages. A request-reply
pattern is similar to two one-way messages. With a request-reply pattern, an application is both a
producer and a consumer. For example, an application as a requester sends a message requesting an
order and another application as a responder sends a reply to the requester with a status of that
order. From the requester's perspective, its application is sending a message to the responder and
receiving a message from the responder. From the responder's perspective, its application is
receiving a message from the requester and sending a message to the requester. When several requests
are sent to the same responder, then correlation identifiers distinguish between the replies
from the responder so that a specific reply matches a specific request.

<!-- image -->

How does an application connect to a messaging provider and use its services? A messaging
provider does have APIs and one way to get to that API with a minimum of coding is to use a resource
adapter. The resource adapter is an implementation that can communicate to an EIS system, including
a messaging provider. Java™ Message Service (JMS) provides
client Application Programming Interfaces (APIs) to interact with the messaging provider. The
resource adapter can be the interactive link between application and messaging provider, both of
which interact with the resource adapter.

A resource adapter allows a Java EE server to
communicate to an EIS system. An adapter that is JCA 1.5 compliant and JMS 1.1 compliant provides
JMS as a managed resource. Using such a resource adapter means good integration, allowing its
lifecycle, quality of service and resources to be managed by an application
server.

Using a resource adapter or using the JMS API directly are two ways to
connect to a messaging provider. Another way is to use native calls to a messaging provider such as
used by IBM
WebSphere MQ. These calls are made using the Message
Queue Interface (MQI). MQ JMS uses the JMS API (as opposed to MQI) to access WebSphere MQ. A key decision by developers is choosing the best strategy
for a particular application. If you are working with native JMS applications then use JMS. If you
are working with JMS applications that are using the MQ backbone then use MQ JMS. If you are working
with native MQ applications then use MQI.

The portability versus performance tradeoff is
another factor to consider. If portability is important, choose JMS. If performance is important,
using WebSphere MQ with native calls might be the
appropriate choice. MQ JMS provides some portability with some performance benefits over JMS. The
choice of strategy decides what type of binding to select. These types of messaging bindings, all of
which are available in IBM Integration
Designer, are
discussed in this section.

- Mapping a message to an SCA interface

An import with a messaging binding such as JMS, MQ, MQ JMS or generic JMS that exchanges messages with an export with a messaging binding could be considered as messaging clients to each other. In order for your service component architecture (SCA) application to communicate with an existing JMS, MQ or MQ JMS messaging client, certain SCA artifacts need to be created.
- Java Message Service (JMS)

JMS is a standard API for sending and receiving messages. It allows components based on the Java Platform, Enterprise Edition (Java EE) to create, send, receive, and read messages.
- WebSphere MQ Java Message Service (MQ JMS)

MQ JMS is a set of Java classes that enables JMS applications using WebSphere MQ as the messaging provider.
- Generic JMS

The generic JMS binding should be used for applications working with a generic JMS provider.
- WebSphere MQ (WMQ)

IBM's WebSphere MQ (WMQ) is a popular middleware set of products that provide a well-known set of messaging communications between applications, which can themselves be on many dissimilar systems.
- Recommendations when using messaging bindings

Messaging bindings have some common recommended patterns of use.
- Language support in non-EIS bindings

In creating EIS bindings such as bindings for a CICS system, you can use source files such as COBOL to create your business objects. You can also create business objects from language source files that can be used in non-EIS bindings like JMS.