<!-- image -->

# Use of WSDL document style binding with multipart messages

These rules are specified in the WS-I Basic Profile Version
1.1 (http://www.ws-i.org/Profiles/BasicProfile-1.1.html).  In particular, the
WS-I Basic Profile 1.1 R2712 states: "A document-literal binding MUST
be serialized as an ENVELOPE with a soap:Body whose child element
is an instance of the global element declaration referenced by the
corresponding wsdl:message part."

This means that, when using a document style SOAP binding for an
operation with messages (input, output, or fault) that are defined
with multiple parts, only one of those parts should be bound to the
SOAP body in order to be compliant with the WS-I Basic Profile 1.1.

Further, the WS-I Attachments Profile 1.0 R2941
states: "A wsdl:binding in a DESCRIPTION SHOULD bind every wsdl:part
of a wsdl:message in the wsdl:portType to which it refers to one of
soapbind:body, soapbind:header, soapbind:fault , soapbind:headerfault,
or mime:content.".

This means that, when using a document style
SOAP binding for an operation with messages (input, output, or fault)
that are defined with multiple parts, all parts other than the one
selected to be bound to the SOAP body must be bound as attachments
or headers.

- You can choose which message part is bound
to the SOAP body if there is more than one non-binary-typed element.
If there is a single non-binary typed element, that element is automatically
bound to the SOAP body.
- For the JAX-WS binding, all other message parts of type "hexBinary"
or "base64Binary" are bound as referenced attachments. See Referenced attachments: top-level message parts.
- All other message parts are bound as SOAP headers.

1. Use the document/literal wrapped style. In this case,
messages always have a single part; however, attachments have to be
unreferenced (as described in Unreferenced attachments) or
swaRef-typed (as described in Referenced attachments: swaRef-typed elements)
in this case.
2. Use the RPC/literal style. In this case, there are
no restrictions on the WSDL binding in terms of number of parts bound
to the SOAP body; the SOAP message that results always has a single
child that represents the operation being invoked, with the message
parts being children of that element.
3. For the JAX-WS binding,
have at most one message part that is not of type "hexBinary" or "base64Binary",
unless it is acceptable to bind the other non-binary parts to SOAP
headers.
4. Any other cases are subject to the behavior described.

- The first message part should be non-binary.
- When receiving multipart document-style SOAP messages with referenced
attachments, the JAX-WS binding expects each referenced attachment
to be represented by a SOAP body child element with an href attribute
value that identifies the attachment by its content ID.  The JAX-WS
binding sends referenced attachments for such messages in the same
way. This behavior is not compliant with the WS-I Basic Profile. To
ensure that your messages comply with the Basic
Profile, follow approach 1 or 2 in the previous list or avoid
the use of referenced attachments for such messages and use unreferenced
or swaRef-typed attachments instead.