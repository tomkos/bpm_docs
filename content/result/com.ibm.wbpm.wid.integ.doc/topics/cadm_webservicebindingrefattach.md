<!-- image -->

# Referenced attachments: top-level message
parts

In a MIME multipart SOAP message, the SOAP body is the first part
of the message, and the attachment
or attachments are in subsequent parts.

What is the advantage of sending or receiving a referenced attachment
in a SOAP message? The binary data that makes up the attachment (which
is often quite large) is held separately from the SOAP message body
so that it does not need to be parsed as XML. This results in more
efficient processing than if the binary data were held within an XML
element.

## Types
of SOAP messages with referenced attachments

- WS-I-compliant messagesThe runtime can generate SOAP
messages that comply with the WS-I Attachments Profile Version
1.0 and the WS-I Basic Profile Version 1.1. In
a SOAP message that is compliant with these profiles, only one message
part is bound to the SOAP body; for those that are bound as attachments,
the content-id part encoding (as described in the WS-I Attachments
Profile Version 1.0) is used to relate the attachment to the
message part.
- Non-WS-I-compliant messagesThe runtime can generate
SOAP messages that do not comply with the WS-I profiles but that are
compatible with the messages generated in Version 7.0 or 7.0.0.2 of IBM Integration
Designer. The
SOAP messages use top-level elements named after the message part
with an href attribute that holds the attachment content-id,
but the content-id part encoding (as described in the WS-I Attachments
Profile Version 1.0) is not used.

## Selecting
WS-I compliance for web service exports

- Use WS-I AP 1.0 compliant SOAP messageIf
you select this option, you also specify which message part should
be bound to the SOAP body.Note: This option can be used only when
the corresponding WSDL file is also WS-I compliant. A WSDL file
that is generated by Integration Designer Version
7.0.0.3 is compliant with WS-I. However, if you import a WSDL file
that is not compliant with WS-I, you cannot select this option.
- Use non WS-I AP 1.0 compliant SOAP messageIf
you select this option, which is the default, the first message part
is bound to the SOAP body.

- The value of the name attribute of the wsdl:part element
referenced by the mime:content
- The character =
- A globally unique value, such as a UUID
- The character @
- A valid domain name

## Inbound processing of referenced attachments

Figure 1. How the web service (JAX-WS)
export binding processes a WS-I compliant SOAP message with a referenced
attachment

<!-- image -->

## Accessing attachment metadata in a mediation flow
component

As shown in Figure 1, when referenced
attachments are accessed by components, the attachment data appears
as a byte array.

Figure 2. How referenced
attachments appear in the SMO

<!-- image -->

For
details about the structure of the SMO, see the information in "Related
topics".

## How outbound
SOAP messages are constructed

- Use WS-I AP 1.0 compliant SOAP messageIf
you select this option, you also specify which message part should
be bound to the SOAP body; all others are bound to attachments or
headers.  Messages sent by the binding do not include elements in
the SOAP body that refer to the attachments; the relationship is expressed
by way of the attachment content ID including the message part name.
- Use non WS-I AP 1.0 compliant SOAP message If
you select this option, which is the default, the first message part
is bound to the SOAP body; all others are bound to attachments or
headers. Messages sent by the binding include one or more elements
in the SOAP body that refer to the attachments by way of an href attribute.

## Outbound processing of referenced
attachments

Figure 3. How
the referenced attachment in the SMO is accessed to create the SOAP
message

<!-- image -->

The attachments element is present in
the SMO only if a mediation flow component is connected directly to
the import or export; it does not get passed across other component
types. If the values are needed in a module that contains other component
types, a mediation flow component should be used to copy the values
into a location where they can then be accessed in the module, and
another mediation flow component used to set the correct values before
an outbound invocation by way of a web service import.

- Whether there is a WSDL MIME binding for the top-level binary
message part and, if so, how the content type is defined
- Whether there is an attachments element in the
SMO whose bodyPath value references a top-level binary
part

## How attachments are created when an attachment element
exists in the SMO

| Status of WSDL MIME binding for top-level binary message part                                                                                 | How message is created and sent                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Present with one of the following:  No defined content type for the message part Multiple content types defined Wildcard content type defined | Message part is sent as an attachment.  Content-Id is set to the value in the attachments element if present; otherwise, one is generated.  Content-Type is set to the value in the attachments element if present; otherwise, it is set to application/octet-stream.                                                                                                                                                                                  |
| Present with single, non-wildcard content for the message part                                                                                | Message part is sent as an attachment.  Content-Id is set to the value in the attachments element if present; otherwise, one is generated.  Content-Type is set to the value in the attachments element if present; otherwise, it is set to the type defined in the WSDL MIME content element.                                                                                                                                                         |
| Not present                                                                                                                                   | Message part is sent as an attachment. Content-Id is set to the value in the attachments element if present; otherwise, one is generated.  Content-Type is set to the value in the attachments element if present; otherwise, it is set to application/octet-stream.  Note: Sending message parts as attachments when not defined as such in the WSDL may break compliance with the WS-I Attachments Profile 1.0 and so should be avoided if possible. |

## How attachments are created when no attachment element
exists in the SMO

| Status of WSDL MIME binding for top-level binary message part                                                                                 | How message is created and sent                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Present with one of the following:  No defined content type for the message part Multiple content types defined Wildcard content type defined | Message part is sent as an attachment. Content-Id is generated.  Content-Type is set to application/octet-stream.                              |
| Present with single, non-wildcard content for the message part                                                                                | Message part is sent as an attachment.  Content-Id is generated.     Content-Type is set to the type defined in the WSDL MIME content element. |
| Not present                                                                                                                                   | Message part is not sent as an attachment.                                                                                                     |

- If you use /body as the root of the XML map, all attachments
are propagated across the map by default.
- If you use / as the root of the map, you can control the
propagation of attachments.

## Related information

- How to choose the appropriate attachment style
- MTOM attachments: top-level message parts
- Referenced attachments: swaRef-typed elements
- Unreferenced attachments