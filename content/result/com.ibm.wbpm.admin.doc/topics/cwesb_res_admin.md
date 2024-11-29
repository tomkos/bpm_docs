<!-- image -->

# Resources for service modules

For more information about managing resources for service modules, see the related topics.

## Service integration technologies

<!-- image -->

For each of the destinations, a queue point is also created and defined on the messaging engine
of the relevant bus member.

You can deploy and use service modules without needing to manage these resources. However, you
might want to adjust the configuration of the resources (for example, to modify the maximum
messaging quality of service used) or to use them in locating messages for troubleshooting.

## Java
Message Service (JMS)

JMS resources enable a service module to use asynchronous messaging as a method of communication
based on the Java Message Service (JMS) programming interface. The JMS support used depends on the JMS
binding of the module. For example, a module with a JMS binding uses a JMS connection factory
configured on the default messaging provider provided by the underlying WebSphere Application
Server, while a module with a WebSphere MQ JMS binding
uses a JMS connection factory configured on WebSphere MQ as the JMS provider. To manage use of the
Java
Message Service, you can administer the following resources:

## Common Event Infrastructure (CEI)

CEI resources enable a service module to use standard formats and mechanisms for managing event
data. To manage use of the Common Event Infrastructure, you can administer the following
resources: