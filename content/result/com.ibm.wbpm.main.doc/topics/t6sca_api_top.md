<!-- image -->

# Developing web services API client applications for BPEL processes
and human tasks

## About this task

- Beginning with WebSphere® Process
Server Version
7, the JAX-WS-based web services API replaces the JAX-RPC-based Business
Process Choreographer web services API. The JAX-RPC-based Business
Process Choreographer web services API is deprecated. You should implement
new web service client applications using the JAX-WS-based API.
- Beginning with IBM® Business Process Manager
Advanced Version
8, the SOAP/JMS API replaces the Business Process Choreographer JMS
API. The Business Process Choreographer JMS API is deprecated. Use
the JAX-WS-based API to implement new web service client applications.

You can develop client applications in any web services
client environment. The following steps provide an overview of the
actions you need to take to develop such an application.

## Procedure

1. Decide which web services API your client application needs
to use: the Business Flow Manager API, Human Task Manager API, or
both.
2. Export the necessary files from the Workflow Server environment.
3. In your client application development environment, generate
a web service proxy using the exported artifacts.
4. Develop the code for your client application.
5. Add any necessary security or transaction policies to your
client application.

- Web service components and sequence of control

In web services applications, a number of client-side and server-side components participate in the sequence of control that represents a web service request and response.
- Web service API requirements for BPEL processes and human tasks (deprecated)

BPEL processes and human tasks developed with IBM Integration Designer to run on Business Process Choreographer must conform to specific rules to be accessible through the web services APIs.
- File artifacts and XML namespaces for the JAX-WS-based Business Process Choreographer web services APIs

The JAX-RPC-based Business Process Choreographer web services API supports the HTTP and JMS transport layer protocols for sending and receiving SOAP messages. Interfaces are provided for both of these transport layers. Each of these interfaces has its own file artifacts and XML namespaces.
- Business Process Choreographer web services API: Standards

The Business Process Choreographer web services APIs support a variety of industry standards.
- Publishing and exporting artifacts from the server environment for web services client applications

Before you can develop client applications to access the Business Process Choreographer web services APIs, you must publish and export a number of artifacts from the server environment.
- Developing client applications in the Java web services environment

You can use any Java-based development environment compatible with Java™ web services to develop client applications for the Business Process Choreographer web services APIs.
- Adding security to Business Process Choreographer web services applications

The Business Process Choreographer web service requires that you configure your client application for an authentication mechanism.
- Adding transaction support to Business Process Choreographer web services applications

Web service client applications can be configured to allow server-side request processing to participate in the client's transaction, by passing a client application context as part of the service request. This atomic transaction support is defined in the Web Services-Atomic Transaction (WS-AT) specification.