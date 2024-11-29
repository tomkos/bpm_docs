# SOAP Header Setter mediation primitive

## Introduction

You can use the SOAP Header
Setter mediation primitive to provide a mechanism for managing SOAP
headers in the message. You can change, copy, add, or delete SOAP
headers by setting the mediation primitive properties.

If you
want multiple header changes you can set multiple actions. Multiple
actions are acted on sequentially, in the order you specify; this
means that header changes can build on each other.

You can search
for SOAP headers that already exist in the service message object
(SMO) by specifying values to match on. If matching headers are found,
they can then be deleted from the message, copied to another location
in the SMO, or have fields set to specified values. If matching headers
are not found, new headers can be created using specified header field
values.

The SOAP Header Setter mediation primitive has one input
terminal (in), one output terminal (out)
and a fail terminal (fail). The in terminal
is wired to accept a message and the other terminals are wired to
propagate a message. If the mediation is successful, the out terminal
propagates the modified message. If an exception occurs during the
transformation, the fail terminal propagates
the original message, together with any exception information contained
in the failInfo element.

## Details

You can create a new SOAP header
and specify the values it contains. The new SOAP header element is
added to the service message object (SMO) by appending it to the end
of the SOAP header list.

You can also find specific SOAP headers,
in the list of SOAP headers that a message contains, and set or update
the header values.

Alternatively, you can copy the first SOAP
header that matches your search criteria to another location in the
SMO (either in the SMO context or body).

Finally, you can find
specific SOAP headers in the list of SOAP headers that a message contains,
and delete the headers.

Defining
the search criteria can be relatively complex, because a SOAP message
can contain multiple SOAP headers with the same name. When you define
the search criteria you can specify the SOAP header name, type, and
namespace, as well as the values of certain fields. For example, you
might want to search for all SOAP header of type WS-Addressing.
Alternatively, you might want to search for a SOAP header that contains
a field called name whose value is Smith.

Generally,
you specify the field values of SOAP headers, using either a literal
value or an XPath expression.

## Usage

You can use the SOAP Header Setter
mediation primitive to ensure that when a SOAP message is sent to
another system, the headers that are sent with the message are correctly
set.

Because the operations you define occur sequentially, a
later operation can depend on an earlier operation. For example, you
could create a new header, copy it to elsewhere in the SMO and then
delete it from the list of headers it was initially appended to.

You
can also use the SOAP Header Setter mediation primitive to help to
filter messages, using the Message Filter mediation primitive. You
might want to find a particular header and make it available to be
used in the filtering. For example, you could copy a SOAP header to
a more accessible place, and the Message Filter primitive could then
use the details inside the header. You might need to use the Set Message
Type mediation primitive between the SOAP Header Setter primitive
and the Message Filter primitive, (in order to do type casting).

- SOAP Header Setter mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)