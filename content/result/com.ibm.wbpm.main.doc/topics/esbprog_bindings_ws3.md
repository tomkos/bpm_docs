<!-- image -->

# JAX-WS and JAX-RPC bindings

Using the web service binding, you can specify that messages are processed by handlers. Handlers
on incoming messages are invoked before the message is delivered to the web service operation, and
handlers on outgoing messages are invoked after the web service operation has completed. Handlers
can be used for a variety of purposes. Examples include message logging, audit trails, and message
transformations. Handlers should not be used to implement security or encryption or to manage the
redirection of messages; those facilities are provided by other mechanisms.

## JAX-RPC and JAX-WS

- JAX-RPC and JAX-WS both support SOAP 1.1 over HTTP 1.1, so interoperability is not affected.
- JAX-RPC and JAX-WS both support WSDL 1.1.

- JAX-WS must be used in service gateway patterns, because the service gateway has special
handling that requires JAX-WS.

- JAX-RPC must be used for RPC encoded SOAP messages.

- To define and configure your WS-Security requirements
    - using JAX-WS, you must create policy sets
    - using JAX-RPC, you can use the deployment editor

- SOAP 1.2
    - JAX-RPC and JAX-WS both support SOAP 1.1.
    - JAX-WS also supports SOAP 1.2.
- XML/HTTP

- The WSDL 1.1 specification defines an HTTP binding, which is used to send XML messages over HTTP
without SOAP.
- JAX-RPC ignores the HTTP binding. JAX-WS adds support for it.
- WS-I's Basic Profiles

- JAX-RPC supports the Basic Profile version 1.0 of WS-I. JAX-WS supports BP 1.1. (WS-I is the web
services interoperability organization.)
- The handler model

- The handler model has changed from JAX-RPC to JAX-WS.
- JAX-RPC handlers rely on SAAJ 1.2. JAX-WS handlers rely on the new SAAJ 1.3 specification.