<!-- image -->

# Using document binding style with multipart messages

These sections explain how to use the document binding
style with multipart messages:

- Document binding style and the WS-I Basic Profile
- Multipart messages used with exports
- Multipart messages used with imports
- Recommended way of working with multipart messages

## Document binding style and the WS-I
Basic Profile

The Web Services Interoperability (WS-I) organization
has defined a set of rules regarding how web services should be described
in Web Services Description Language (WSDL). It has also defined how
the corresponding SOAP messages should be formed, in order to ensure
interoperability.  These rules are specified in the WS-I Basic Profile.

For a document style
SOAP binding, the WS-I profile conformance requires that in a WSDL
document, for an operation that uses the document style, only a single
message part is ever bound to the SOAP body, and that the SOAP message
corresponding to this message part contains a single child element
matching the part that was so bound.

This means that when using
a document style SOAP binding for an operation whose messages (input,
output or fault) are defined with multiple parts, only one of those
parts should be bound to the SOAP body in order to be compliant with
the WS-I Basic Profile 1.1.

## Multipart messages used with exports

The following approach is used when WSDL descriptions are generated
for exports with web service (JAX-WS and JAX-RPC) bindings in this
case:

- The first message part is bound to the SOAP body
- For the JAX-WS binding, all other message parts of type hexBinary or base64Binary are bound as Referenced and swaRef-type attachments.
- All other message parts are bound as SOAP headers

## Multipart messages used with imports

The JAX-RPC and JAX-WS import bindings will honour the SOAP binding
in an existing WSDL document with multi-part document style messages
even if the SOAP binding does bind multiple parts to the SOAP body.
However you will not be able to generate web service clients for such
WSDL documents in IBM® Integration
Designer (note that the JAX-RPC binding does not support attachments in any
case).

## Recommended way of working with multipart
messages

The recommended way of working with multipart messages
with an operation which has a document style SOAP binding is as follows:

- Use the document literal wrapped style. Messages always have a
single part, however, attachments may be Working with attachments or Referenced and swaRef-type attachments.
- You may also use the RPC literal style. In this case there are
no restrictions on the WSDL binding in terms of the number of parts
bound to the SOAP body. The SOAP message that results always has a
single child that represents the operation being invoked, with the
message parts being children of that element.
- For the JAX-WS binding, have the first message part be one that
is not of type hexBinary or base64Binary, and all other parts be of one of those two types. Then all parts
will be bound as attachments.
- Any other cases will be subject to the behavior described above.