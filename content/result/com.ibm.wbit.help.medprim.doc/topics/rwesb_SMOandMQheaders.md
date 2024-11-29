# MQ header information in the SMO

## Introduction

- md, which represents the MQ message descriptor
(MQMD).
- control, which contains format information relating
to the message body.
- header, which optionally repeats, and represents
header structures contained in the WebSphere MQ
message.

The md element contains all the fields
from the MQMD definition (see the WebSphere MQ
documentation), except for certain control fields that carry no useful
data (such as StrucId and Version)
and message format fields (Encoding, CodedCharSetId and Format).

The control element
carries the Encoding, CodedCharSetId and Format fields,
which describe the message body. If the WebSphere MQ
message contains any message headers (for example, MQRFH2), the Encoding, CodedCharSetId and Format fields
that describe the header are carried in the header element.

- A header explicitly modeled in the SMO: an RFH version 1 or 2.
- A header following the standard MQ header structure, but not explicitly
modeled. These have MQ format identifiers beginning MQH.
These headers are represented as unstructured binary data in the SMO.
- A header handled by a user-supplied MQ header data binding.
- A header not explicitly modeled in the SMO,
but handled by a supplied MQ header data binding, such as MQCIH.

The header element contains Encoding, CodedCharSetId and Format fields,
which describe the header. The Format field, in particular,
must be set correctly; for example, MQHRF2 for
an MQRFH2 header. In addition, the CodedCharSetId and Encoding fields
are important for opaque data. When rendered as a WebSphere MQ
message, this format information is written into the previous MQ header
(or into the MQMD if there is no previous header).

## Header subelements

- For each of the explicitly modeled headers a subelement: rfh or rfh2.
- For unmodeled, standard, MQ headers a subelement: opaque.
- For user-supplied MQ headers a subelement: value.
- For other supplied or user-supplied MQ headers,
a type: mqcih.

Precisely one of these four sub elements must be set:
it is an error to have more than one of these set in any header element.
The value subelement stores the structure used by
the user-supplied header data binding; the other three elements (rfh, rfh2 and opaque)
are described in the following sections.

If you use a mediation
module to invoke an import with a native MQ binding, and you create
the MQ header by setting the MQ header fields in the SMO, you must
ensure that the format field of the header is set. Otherwise, a NullPointerException is
thrown at run time. You can set the format field of the MQ header
by using one of the supplied mediation primitives. For example, the
Mapping mediation primitive or the Message Element mediation Setter
primitive. The IBM WebSphere MQ documentation documents the values
supported for the format field. For example, MQHRF2 for
an MQRFH2 header.

## RFH headers

A WebSphere MQ RFH header
contains a string of name-value pairs, where each name and value is
a text string. This is represented, in SMO, as a repeating property
element, containing a name and a value element.

## RFH2 headers

A WebSphere MQ RFH2 header
contains zero or more named folders, each of which contains a sequence
of properties and groups. A property has a name, optional type and
value (all represented as string). A group has a
name and itself contains a sequence of properties and groups. The
SMO representation of an RFH2 header also contains a NameValueCCSID element,
which determines the CCSID used to encode the folders in the WebSphere MQ message.

## MQCIH headers

A WebSphere MQ CIH header
can be modeled using the supplied type com.ibm.websphere.sca.mq.structures,
and will appear under the value sub-client of the MQ header structure.

## Unmodeled standard WebSphere MQ
headers

The opaque element represents any WebSphere MQ header of the standard structure.
Fields common to all such headers (StrucId, Version and Flags)
are represented as elements. There is also a data element
that contains the unmodeled portion of the header as hexBinary data.
When using the opaque element, it is usually important
to keep the correct Encoding and CodedCharSetId values
associated with the header to avoid data corruption.

## Types for WebSphere MQ header information

The WebSphere MQ header fields are defined
using the same set of types used by WebSphere MQ
itself. MQLONG fields are represented as int; MQBYTEnn fields
as hexBinary data limited to nn in
length; and MQCHARnn fields as string data
limited to nn characters in length.