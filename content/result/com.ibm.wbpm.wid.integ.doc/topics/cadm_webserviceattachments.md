<!-- image -->

# Attachments in SOAP messages

- MTOM attachments use the SOAP Message Transmission Optimization
Mechanism (http://www.w3.org/TR/soap12-mtom/) specified encoding.  MTOM attachments are
enabled through a configuration option in the import and export bindings
and are the recommended way to encode attachments for new applications.
- As a wsi:swaRef-typed element in the
message schemaAttachments defined
using the wsi:swaRef type conform to the Web Services Interoperability
Organization (WS-I) Attachments Profile Version 1.0 (http://www.ws-i.org/Profiles/AttachmentsProfile-1.0.html), which defines how message
elements are related to MIME parts.
- As a top-level message part, using a binary schema typeAttachments
represented as top-level message parts conform to the SOAP Messages
with Attachments (http://www.w3.org/TR/SOAP-attachments)
specification.
Attachments
represented as top-level message parts can also be configured to ensure
that the WSDL document and messages produced by the binding conform
to the WS-I Attachments Profile Version 1.0 and the WS-I Basic
Profile Version 1.1 (http://www.ws-i.org/Profiles/BasicProfile-1.1.html).

In all cases, except MTOM attachments, the WSDL
SOAP binding should include a MIME binding
for attachments to be used, and the maximum size
of the attachments should not exceed 20 MB.

- How to choose the appropriate attachment style

When designing a new service interface that includes binary data, consider how that binary data is carried in the SOAP messages that are sent and received by the service.
- MTOM attachments: top-level message parts

You can send and receive web service messages which include SOAP Message Transmission Optimization Mechanism (MTOM) attachments. In a MIME multipart SOAP message, the SOAP body is the first part of the message, and the attachment or attachments are in subsequent parts.
- Referenced attachments: swaRef-typed elements

You can send and receive SOAP messages that include attachments represented in the service interface as swaRef-typed elements.
- Referenced attachments: top-level message parts

You can send and receive SOAP messages that include binary attachments that are declared as parts in your service interface.
- Unreferenced attachments

You can send and receive unreferenced attachments that are not declared in the service interface.