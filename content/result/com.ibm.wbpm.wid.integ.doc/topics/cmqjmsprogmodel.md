<!-- image -->

# WebSphere MQ JMS
programming model

IBM® WebSphere MQ classes for Java™ Message Service (also referred to as WebSphere MQ JMS) is a set
of Java classes that enables
JMS applications that use WebSphere MQ
systems as its messaging provider. Both the point-to-point and publish-subscribe
models of JMS are supported. These Java classes
are available as part of the IBM WebSphere MQ client support.

The JMS application is written to use only references to interfaces.
Vendor-specific information is encapsulated in implementations of
the following JMS administered objects: QueueConnectionFactory, TopicConnectionFactory,
Queue and Topic.

These JMS administered objects are built using a vendor-supplied
administration tool and stored on a JNDI namespace. A JMS application
can retrieve these objects from the namespace and use them without
needing to know which vendor provided the implementation, which, in
this case, is the IBM WebSphere MQ JMS provider.

The following diagram shows the relationship between an IBM Integration
Designer application
running on the IBM Workflow
Server and
a Java Message Service (JMS)
client application in the WebSphere MQ
JMS programming model.

<!-- image -->