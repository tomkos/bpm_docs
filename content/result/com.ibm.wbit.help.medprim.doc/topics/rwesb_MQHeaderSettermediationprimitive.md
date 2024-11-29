# MQ Header Setter mediation primitive

## Introduction

You can use the MQ Header Setter
mediation primitive to provide a mechanism for managing MQ headers
in a message. You can change, copy, add, or delete MQ headers by setting
the mediation primitive properties.

If you want multiple header
changes you can set multiple actions. Multiple actions are acted on
sequentially, in the order you specify; this means that header changes
can build on each other.

The MQ Header Setter mediation primitive
has one input terminal (in), one output terminal
(out) and a fail terminal (fail).
The in terminal is wired to accept a message
and the other terminals are wired to propagate a message. If the mediation
is successful, the out terminal propagates
the modified message. If an exception occurs during the transformation,
the fail terminal propagates the original message,
together with any exception information contained in the failInfo
element.

## Details

You can create a new MQ header (apart
from the MQMD header) and specify the header field values. The new
MQ header element is added to the service message object (SMO); if
a header of the same type already exists the new header is appended
to the end of the header list.

You can also search for MQ headers
that already exist in the SMO, by specifying the header type to match
on. If matching headers are found, you can set the header fields to
the values you specify, or you can delete the headers (other than
the MQMD header). Alternatively, you can copy the first matching MQ
header to another location in the SMO.

Generally, you specify
the field values of MQ headers, using either a literal value or an
XPath expression.

## Usage

You can use the MQ Header Setter mediation
primitive to ensure that when an MQ message is sent to another system,
the headers that are sent with the message are correctly set.

Because
the operations you define occur sequentially, a later operation can
depend on an earlier operation. For example, you could create a new
header, copy it to elsewhere in the SMO and then delete it from the
list of headers it was initially appended to.

You can also use
the MQ Header Setter mediation primitive to help to filter messages,
using the Message Filter mediation primitive. You might want to find
a particular header and make it available to be used in the filtering.
For example, you could copy an MQ header to a more accessible place,
and the Message Filter primitive could then use the details inside
the header.

- MQ Header Setter mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)