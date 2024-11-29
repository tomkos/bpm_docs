<!-- image -->

# Available web service bindings

- SOAP 1.1 over HTTP - this protocol is based on the Java API for XML Web Services (JAX-WS) (a
Java programming API for creating web services), and is used when the web service conforms to the
SOAP 1.1 specification. The JAX-WS technology allows you to send attachments with the SOAP message,
as well as allowing additional message handling, policy sets and service gateway scenarios.
- SOAP 1.2 over HTTP - this protocol is also based on JAX-WS and is used when the web service
conforms to the SOAP 1.2 specification.
- SOAP 1.1 over HTTP using JAX-RPC - this protocol is based on the Java API for XML-based RPC
(JAX-RPC) (a Java programming API for creating web services that precedes JAX-WS.)
- SOAP 1.1 over JMS - this protocol is used to send or receive SOAP 1.1 messages using a Java
Message Service (JMS) destination.

- SOAP 1.1 over HTTP using JAX-RPC and SOAP 1.1 over JMS
- SOAP 1.1 over HTTP using JAX-RPC and SOAP 1.1 over HTTP using JAX-WS
- SOAP 1.1 over HTTP using JAX-RPC and SOAP 1.2 over HTTP using JAX-WS

## Supported WS-* standards

There are many extension specifications to web services, and they are collectively referred to as
WS-* standards.

Some of the WS-* standards that are supported by Business Automation Workflow and the web services binding include the following:

- Web services Security (WS-Security) - adds support for various security protocols, allowing you
to sign, encrypt and authenticate SOAP messages. You can propagate WS-Security headers from JAX-WS
or JAX-RPC based web service import or export bindings, into a mediation module. When a mediation
module receives a message with WS-Security headers, the headers are stored in the SOAPHeader section
of the SMO. When you propagate WS-Security headers from an export, through a module and then on
to an import, the handling of the headers depends on the security policy setting on the import and
export bindings, as described in Table 1:
Table 1. How WS-Security headers are passed through a module

 
Export binding with no security policy
Export binding with security policy

Import binding with no security policy 

Security headers are passed through the module. They are not decrypted.
The headers are sent outbound in the same form in which they were received.
The digital signature might become invalid.

Security headers are decrypted and passed though the module with signature verification and
authentication.
The decrypted headers are sent outbound.
The digital signature might become invalid.

Import binding with security policy 

Security headers are passed through the module. They are not decrypted.
The headers must not be propagated to the import. Errors can occur because of duplication.

Security headers are decrypted and passed though the module with signature verification and
authentication.
The headers must not be propagated to the import. Errors can occur because of duplication.
- Web Services Addressing (WS-Addressing) - allows you to add message routing data to the SOAP
message. You can reroute a message to alternative network endpoints. You can propagate WS-Addressing
headers from an import or export, with a JAX-WS based web service binding into a mediation module.
When a mediation flow receives a message that contains WS-Addressing headers, those headers are set
into the WSAHeader section of the SMO Header structure and not the SOAPHeader section. The values in
the WSAHeader section are not used when sending messages from a mediation flow. If WS-Addressing
headers are required, they can be set in the SOAPHeader section of the SMO.
- Web Services Atomic Transaction (WS-AT) - allows SOAP messages to propagate transactional
context from the service requester. If the service requester and provider both have web services
bindings, and the service requester is using WS-AT, the mediation flow can be made part of the
global transaction by simple configuration of the SCA module.
- Web Services Reliable Messaging (WS-ReliableMessaging) - allows SOAP messages to be reliably
delivered between the service requester, the mediation module and the service provider.