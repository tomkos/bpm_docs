<!-- image -->

# Web service bindings overview

With a web service binding, you access external services using
interoperable SOAP messages and qualities of service (QoS).

You use Integration Designer to
generate and configure web service bindings on imports and exports
in SCA modules. The following types of web service bindings are available:

- SOAP1.2/HTTP and SOAP1.1/HTTP These bindings are based on Java™ API for XML Web Services (JAX-WS),a Java programming API for creatingweb services. Important: When you deployan application with a web service (JAX-WS) binding, the target servermust not have the Start components as needed optionselected. See Checking the server configuration for details. Whenyou select one of these bindings, you can send attachments with yourSOAP messages. The web service bindings work with standard SOAPmessages. Using one of the web service JAX-WS bindings, however, youcan customize the way that SOAP messages are parsed or written. Forexample, you can handle nonstandard elements in SOAP messages or applyadditional processing to the SOAP message. When you configure thebinding, you specify a custom data handler that performs this processingon the SOAP message. You can use policy setswith a web service (JAX-WS) binding. A policy set is a collectionof policy types, each of which provides a quality of service (QoS).For example, the WSAddressing policy set provides a transport-neutralway to uniformly address web services and messages. You use Integration Designer to selectthe policy set for the binding.Note: If you want to use a SecurityAssertion Markup Language (SAML) policy set, you must perform someadditional configuration, as described in Importing SAML policy sets .
    - Use SOAP1.2/HTTP if your web service conforms to the SOAP 1.2
specification.
    - Use SOAP1.1/HTTP if your web service conforms to the SOAP 1.1
specification.

When
you select one of these bindings, you can send attachments with your
SOAP messages.

The web service bindings work with standard SOAP
messages. Using one of the web service JAX-WS bindings, however, you
can customize the way that SOAP messages are parsed or written. For
example, you can handle nonstandard elements in SOAP messages or apply
additional processing to the SOAP message. When you configure the
binding, you specify a custom data handler that performs this processing
on the SOAP message.

- SOAP1.1/HTTP Use this binding if you want
to create web services that use a SOAP-encoded message based on Java API for XML-based RPC (JAX-RPC).
- SOAP1.1/JMS Use this binding to send or receive SOAP messages
using a Java Message Service
(JMS) destination.

- SOAP 1.1/JMS and SOAP 1.1/HTTP using JAX-RPC
- SOAP 1.1/HTTP using JAX-RPC and SOAP 1.1/HTTP using JAX-WS
- SOAP 1.1/HTTP using JAX-RPC and SOAP 1.2/HTTP using JAX-WS

After the SCA module that contains the web service binding is deployed
to the server, you can use the administrative console to view information
about the binding or to change selected properties of the binding.

- The Web Services Description Language (WSDL) file that is used
to access a web service export includes a non-empty SOAP action value
for each operation in the interface.
- The web service client sets either the SOAPAction header or the
wsa:Action header when sending messages to a web service export.