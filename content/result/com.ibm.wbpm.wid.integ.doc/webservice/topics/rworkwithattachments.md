<!-- image -->

# Working with attachments

The following sections provide some conceptual
information on attachments.

- Bindings and protocols that can be used with attachments
- Types of attachments
- Unreferenced attachments
- Threshold attribute for MTOM
- Routing, storing and manipulating attachments
- Testing attachments
- Security
- Limitations

## Bindings and protocols that can be used
with attachments

Only the Java API for XML Web Services
(JAX-WS) based binding supports attachments in version 6.2.0.1 or
higher. Only the SOAP 1.2/HTTP or SOAP1.1/HTTP transport protocols
can be used with attachments.

## Types of attachments

There are
four types of attachments: MTOM, referenced, swaRef type and unreferenced.

MTOM
attachments use the SOAP Message Transmission Optimization Mechanism
(MTOM) (http://www.w3.org/TR/soap12-mtom/) specified encoding.  MTOM attachments are
enabled through a configuration option in the import and export bindings
as described in Enabling MTOM support in JAX-WS bindings and should be
used to encode attachments for new applications. Note that the MTOM
optimization is only available for the xs:base64Binary data type.

Referenced
attachments are referenced from the SOAP body; that is, the attachment
is defined in the WSDL portType schema for the input or output message
for the operation, and the reference appears in the SOAP body as an
element that references the attachment using the attachment's content-Id. Referenced and swaRef-type attachments shows you how to create
a referenced attachment.

A SOAP with attachment  (swaRef) type
attachment uses the Web Services Interoperability Organization (WS-I)
Attachments Profile. Referenced and swaRef-type attachments shows
you how to create a swaRef-type of attachment.

Unreferenced
attachments do not have a reference from the SOAP body to the attachment.
Unreferenced attachments are discussed in the next section.

In
any of the types of attachments, the attachment data itself does not
appear inline in the SOAP body XML.

## Unreferenced attachments

Unreferenced
attachments do not have a reference from the SOAP body to the attachment.

Unreferenced
attachments are not modeled in the WSDL portType of messages and do
not appear in the business object representation. They can only be
accessed through the Service Message Object (SMO). Each attachment
appears as a separate element in the attachments list of the SMO.
See Service message objects.

## Threshold attribute for MTOM

1. Export (MTOM in) -- connected directly --- Import (MTOM out)
2. Export (MTOM in) -- MFC (do nothing or do not touch data in MFC
) --- Import (MTOM out)

## Routing, storing and manipulating attachments

Using
a mediation flow, you can route, store or manipulate an attachment
passed in as a SMO attachment. You could route the attachment based
on the type of attachment, or use a custom primitive to load or save
attachment data. See Building mediation flows for ESB logic to see
how to route, store and manipulate elements in messages with mediation
flows.

## Testing attachments

You can
test applications that use attachments in the same way as other applications.
The Integration Test Client can be used with little difference in
how you use it to test an application using attachments. See Testing web service exports with SOAP messages.
Note that you must have enabled your server to work with attachments.

## Security

A Web Services Security
(WS-Security) policy set can be applied when using attachments, however,
any privacy or integrity settings will not apply to the attachment
data. In order to secure the entire message when using attachments,
you should enable transport level security using HTTPS instead of
HTTP, by attaching an appropriate policy set. This makes the entire
HTTP message secure, including attachments

## Limitations

- An application using attachments can only be run on a 6.2.0.1
or higher runtime environment. Running the application on a lower
level runtime environment will result in a runtime error.
- There are some limitations for MTOM enablement:
    - MTOM is not supported when the business object parsing mode is
set to eager parsing (support is limited to a JAX-WS web service using
business object lazy parsing mode).
    - MTOM is not supported when using a JAX-WS handler (support is
limited to a JAX-WS web service which does not use any JAX-WS handlers).
The JAX-WS handlers specified on the web service should be removed.
    - When using a service gateway mediation module, the Data Handler
primitive cannot be used with MTOM messages. If direct access to the
MTOM attachment data is required within the module, then a non-service
gateway module must be used.
    - When MTOM is enabled on a JAX-WS export binding, all responses
will be sent using MTOM. If some clients do not support MTOM, use
two JAX-WS exports - one with MTOM enabled and one with it disabled
and ensure client applications use the correct endpoint address.
    - MTOM is not supported when using the JAX-RPC binding for SOAP/HTTP
or SOAP/JMS.