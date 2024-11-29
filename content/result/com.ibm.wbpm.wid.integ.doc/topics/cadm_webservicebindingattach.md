<!-- image -->

# Unreferenced attachments

Figure 1. A SOAP message with an unreferenced attachment

<!-- image -->

Figure 2. An attachment passing through
an SCA module

<!-- image -->

In Figure 2,
the SOAP message, with the attachment, passes through without modification.

Figure 3. A message processed
by a mediation flow component

<!-- image -->

Conversely, the mediation flow component can transform the incoming
message by extracting and encoding the attachment and then transmitting
the message with no attachments.

For details about the structure of the SMO,
see the information in "Related topics".

Figure 4. An attachment obtained from a database and added to the SOAP
message

<!-- image -->

Conversely, the mediation flow component can extract the attachment
from an incoming SOAP message and process the message (for example,
store the attachment in a database).

- If you use /body as the root of the XML map, all attachments
are propagated across the map by default.
- If you use / as the root of the map, you can control the
propagation of attachments.

## Related information

- How to choose the appropriate attachment style
- MTOM attachments: top-level message parts
- Referenced attachments: swaRef-typed elements
- Referenced attachments: top-level message parts