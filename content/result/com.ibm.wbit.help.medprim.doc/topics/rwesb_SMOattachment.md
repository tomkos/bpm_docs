# SMO attachments

## Introduction

The SMO attachments elements
let you send and receive SOAP messages that have attachments of various
types.

You might want to send SOAP messages with attachments
and let the attachments pass through the mediation flow unchanged,
or you might want to create new attachments, perhaps from information
in the message or from an external source.

## Details

A SOAP/HTTP
message with attachments consists of a MIME multipart message
in which the SOAP body is the first part and the attachments are subsequent
parts (as defined in the SOAP
Messages with Attachments specification and in the SOAP
Message Transmission Optimization Mechanism (MTOM) specification).

- Referenced attachments, which are defined in a WSDL port type
as parts within an input or output message and which have a binary
type, do not have their data stored in the SMO; instead, the path
to the message body element that holds the data is contained in the bodyPath element.
- Unreferenced attachments, which are not defined in a WSDL port
type, have their data placed in the data element
in the SMO and have no bodyPath element.

- A contentID elementThe contentID element
contains the value of the Content-ID header of the MIME part and uniquely
identifies the attachment in the message.
- A contentType elementThe contentType element
contains the value of the Content-Type header of the MIME part and
defines the type of data held by the attachment (for example, text/xml or image/gif).
- A bodyPath element (used for referenced attachmentsonly)The bodyPath element contains the path tothe message body element where a referenced attachment is held. Notethat MTOM can support attachment elements within nested structuresmeaning that the bodyPath for MTOM attachments arethe xpath location for the element where the MTOMattachment is held. The computing logic for bodyPath is strictly following the schema to generate the xpath locationas shown in the examples below:

The bodyPath element contains the path to
the message body element where a referenced attachment is held.

    - For a non-array type (maxOccurs is 1):  /sendImage/input/imageData
    - For an array type (maxOccurs  > 1):  /sendImage/input/imageData[1]
- A data element (used for unreferenced attachments
only)The data element contains the attachment
data for unreferenced attachments.

- Web service binding: SOAP 1.1/HTTP using JAX-WS
- Web service binding: SOAP 1.2/HTTP using JAX-WS
- SCA binding

- If you use /body as the root of the XML map, all attachments
are propagated across the map by default.
- If you use / as the root of the map, you can control the
propagation of attachments.