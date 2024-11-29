<!-- image -->

# Generating a web service proxy (Java web services)

## About this task

- HTTP transport layer
- JMS transport layer

A web service proxy for Java web services contains a number
of JavaBeans classes that
the client application calls to perform web service requests. The web service proxy handles
the assembly of service parameters into SOAP messages, sends SOAP
messages to the web service over HTTP or JMS, receives responses from
the web service, and passes any returned data to the client application.

Basically,
therefore, a web service proxy allows a client application to call a web service as if
it were a local function.

In the IBM® web
services environment, you can generate a web service proxy in
one of the following ways.

- Use Rational® Application
Developer or IBM Integration
Designer integrated
development environments.
- Use the wsimport command-line tool.

Other Java web services
development environments usually include either the wsimport tool
or proprietary client application generation facilities.

- Using Rational Application Developer to generate a web service proxy for a web services application

You can use the Rational Application Developer integrated development environment to generate a web service proxy for your web services client application.
- Using the wsimport command-line tool to generate a web service proxy for a web services application

You can use the wsimport command-line tool to generate a web service proxy for a web services application.