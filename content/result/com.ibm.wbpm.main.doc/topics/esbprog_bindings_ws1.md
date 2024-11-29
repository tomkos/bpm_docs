<!-- image -->

# Web service binding

## What is a web service?

IBM® Workflow
Server defines a web service as an application that has
an interface and uses SOAP messages to communicate over a network. The interface is described using
a Web Services Description Language (WSDL). Both WSDL and SOAP are XML-based formats.

- the network endpoints where the service can be found
- the network protocol used to communicate with the service
- the operations that can be carried out by the service
- the format of the messages that can be received and produced by each operation

- SOAP body, which contains the actual message data in the format described by the WSDL.
- SOAP header, which can contain additional contextual data about the message, for example;
security, routing or quality of service information.

The WSDL and SOAP specifications are extensible, allowing further specifications to be built on
top, to provide additional functionality. For example, the WS-Security specification extends SOAP,
to add security to web services. There are many extension specifications and they are collectively
referred to as WS-* standards.

Using the web service binding, Workflow Server can send and receive SOAP version
1.1 and SOAP version 1.2 messages and can be configured to send and receive messages over the HTTP,
HTTPS and JMS protocols.

Workflow Server uses WSDL version 1.1 as the primary interface specification for SCA
components. When an export uses the web service binding, the interface WSDL is extended with
additional network endpoint and protocol information to form a complete description of the web
service that Workflow Server is now providing.

Workflow Server allows access to both the SOAP body data in the SMO body section and
the SOAP header data in the SMO header section, allowing mediation flows to alter, append or remove
SOAP message data as required. The web service binding always handles request/response interactions
synchronously, regardless of the transport protocol that is used to convey the SOAP message. This
means that a mediation flow that calls a web service import binding is blocked until a response is
received from the web service provider.

- Available web service bindings

Web service import and export bindings are generated and configured in Integration Designer.
- JAX-WS and JAX-RPC bindings

JAX-WS and JAX-RPC are Java programming APIs that are used in the web service bindings, to create and consume SOAP messages. JAX-WS is the successor to JAX-RPC. This topic describes the similarities and differences between the two.
- Protocol headers

When handling SOAP messages you can access information from certain transport protocol headers in messages that are received, ensure that messages with transport headers are sent with specific values, and allow transport headers to pass across a module by configuring the web service binding to propagate transport headers.
- SOAP/JMS and SOAP/HTTP transport protocols

SOAP/JMS and SOAP/HTTP are responsible for transporting messages between network applications.

<!-- image -->