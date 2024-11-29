<!-- image -->

# Selecting appropriate bindings

The bindings available in IBM® Integration
Designer provide
a range of choices. In this list, you can determine which type of
binding might be most suitable for the needs of your application.

- All services are contained in modules; that is, there are no external
services.
- You want to separate function into different SCA modules that
interact directly with each other.
- The modules are tightly coupled.

- You need to access an external service over the Internet or provide
a service over the Internet.
- The services are loosely coupled.
- Synchronous communication is preferred; that is, a request from
one service can wait for a response from another.
- The protocol of the external service you are accessing or the
service you want to provide is SOAP/HTTP or SOAP/JMS.

- You need to access an external service over the Internet or provide
a service over the Internet and you are working with other web services
such as GET, PUT, and DELETE.
- The services are loosely coupled.
- Synchronous communication is preferred; that is, a request from
one service can wait for a response from another.

- The binding is for an imported service that is itself an EJB or
that needs to be accessed by EJB clients.
- The imported service is loosely coupled.
- Stateful EJB interactions are not required.
- Synchronous communication is preferred; that is, a request from
one service can wait for a response from another.

- You need to access a service on an EIS system using a resource
adapter.
- Synchronous data transmission is preferred over asynchronous.

- You need to access a messaging system.
- The services are loosely coupled.
- Asynchronous data transmission is preferred over synchronous.

- You need to access a non-IBM vendor messaging system.
- The services are loosely coupled.
- Reliability is more important than performance; that is, asynchronous
data transmission is preferred over synchronous.

- You need to access a WebSphere® MQ messaging system and need to use the MQ native functions.
- The services are loosely coupled.
- Reliability is more important than performance; that is, asynchronous
data transmission is preferred over synchronous.

- You need to access a WebSphere MQ messaging system but can do so within a JMS context; that is,
the JMS subset of functions is sufficient for your application.
- The services are loosely coupled.
- Reliability is more important than performance; that is, asynchronous
data transmission is preferred over synchronous.

## Related concepts

- Service import and export binding types