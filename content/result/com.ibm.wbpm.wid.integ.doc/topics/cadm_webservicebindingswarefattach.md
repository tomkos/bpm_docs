<!-- image -->

# Referenced attachments: swaRef-typed elements

An swaRef-typed element is defined in the Web Services Interoperability
Organization (WS-I) Attachments Profile Version 1.0 (http://www.ws-i.org/Profiles/AttachmentsProfile-1.0.html), which defines how message
elements are related to MIME parts.

Figure 1. A SOAP message with an swaRef element

<!-- image -->

```
<element name="sendPhoto">
       <complexType>
          <sequence> 
            <element name="Photo" type="wsi:swaRef"/>
          </sequence> 
       </complexType> 
      </element>
```

Attachments represented as swaRef-typed elements can be propagated
only across mediation flow components. If an attachment must be accessed
by or propagated to another component type, use a mediation flow component
to move the attachment to a location that is accessible by that component.

## Inbound processing of attachments

Figure 2. How the web service (JAX-WS) export binding processes a SOAP
message with an swaRef attachment

<!-- image -->

## Accessing attachment metadata in a mediation flow
component

As shown in Figure 3, when swaRef
attachments are accessed by components, the attachment content identifier
appears as an element of type swaRef.

Each attachment of a
SOAP message also has a corresponding attachments element
in the SMO. When using the WS-I swaRef type, the attachments element
includes the attachment content type and content ID as well as the
actual binary data of the attachment.

Figure 3. How swaRef attachments appear in the SMO

<!-- image -->

For details about the structure
of the SMO, see the information in "Related topics".

## Outbound processing

You use Integration Designer to configure
a web service (JAX-WS) import binding to invoke an external web service.
The import binding is configured with a WSDL document that describes
the web service to be invoked and defines the attachment that will
be passed to the web service.

When an SCA message is received
by a web service (JAX-WS) import binding, swaRef-typed elements are
sent as attachments if the import is wired to a mediation flow component
and the swaRef-typed element has a corresponding attachments element.

Figure 4. How
the web service (JAX-WS) import binding generates a SOAP message with
an swaRef attachment

<!-- image -->

## Setting attachment metadata in a mediation flow component

Figure 5. How an swaRef attachment
in the SMO is accessed to create the SOAP message

<!-- image -->

The attachments element is present in
the SMO only if a mediation flow component is connected directly to
the import or export; it does not get passed across other component
types. If the values are needed in a module that contains other component
types, a mediation flow component should be used to copy the values
into a location where they can then be accessed in the module, and
another mediation flow component used to set the correct values before
an outbound invocation by way of a web service import.

- If you use /body as the root of the XML map, all attachments
are propagated across the map by default.
- If you use / as the root of the map, you can control the
propagation of attachments.

## Related information

- How to choose the appropriate attachment style
- MTOM attachments: top-level message parts
- Referenced attachments: top-level message parts
- Unreferenced attachments