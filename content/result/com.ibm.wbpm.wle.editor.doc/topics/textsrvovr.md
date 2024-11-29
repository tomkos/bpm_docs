# Calling an external service

An external service provides an interface that you can use to model a connection to a service or
application from the designer. An external service defines operations, their inputs and outputs, and
a server that contains information on how to connect to the host server. How you create the external
service, and the information that it contains, depends on the type of service or application that
you want to call.

## REST service

- By selecting an operation in a service task, mapping the inputs and outputs, and calling the
service task in a service flow. When you discover a REST service, the operations that you select are
included in the external service and they are available for invocation by a service task. See Invoking a REST service.
- Some REST operations can only be invoked by using JavaScript. These operations are not available
for invocation by a service task. When you discover a service, you see a list of such operations,
and you can click View explanation for more information. You can view the
operations in the source view of the External Service editor. See Invoking a REST service by using JavaScript.Note: To make operations available for
invocation by using JavaScript, you must complete the service discovery and generate an external
service. The operation that you want to invoke must be visible in the source view of the external
service.

To invoke a REST service, you also need to specify the location of the host, authorization
credentials, and security credentials. This information is defined in a server.
An external service has a reference to the server that contains the connection information. See
Specifying a REST server.

Service providers often change or update their REST service, which requires you to update the
service in the designer. To update the service, you must rediscover it. When you discover a service
that already exists in the designer, you can choose to replace the existing service or create a new
one. Typically, you need to rediscover the service when an operation or its parameters change. If
the connection information changes, you do not need to rediscover the service. You can change the
properties in the server, or create a new server, and point the external service to it.

## Web service

The operations of the external service are available for invocation by a service task. See Invoking a web service.

You can configure a service task to catch errors that are defined as
faults in the WSDL. See Catching errors by using error boundary events.

## Java service

To invoke the Java class, select an operation in a service task, map the inputs and
outputs, and call the service task in a service flow. See Invoking a Java service.

## External implementation

To call an
external application, select an operation in a system task in a process, and map the inputs and
outputs. See Invoking an external implementation by using a user task .

- Invoking a REST service

Discover a REST service from an OpenAPI specification (formerly known as Swagger) and generate an external service based on the discovered REST service. You can then use the external service in a service flow to invoke the REST service.
- Invoking web services in the designer

You can discover a web service that is hosted on an external system, and use a service task in a service flow to invoke the web service.
- Invoking a Java service

To call a Java service, you can discover a Java class and generate an external service. You can then use the external service in a service flow to call the Java service.
- Building an Advanced Integration Service in the Process Designer

 Traditional: 
 Create an Advanced Integration Service (AIS) to call a service that is implemented in IBM Integration Designer .
- Invoking an Advanced Integration Service in the Process Designer

 Traditional: 
 Invoke an Advanced Integration Service (AIS) from a process or a service flow.