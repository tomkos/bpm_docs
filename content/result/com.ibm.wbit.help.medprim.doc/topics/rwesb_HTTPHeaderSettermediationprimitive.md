# HTTP Header Setter mediation primitive

## Introduction

You can use the HTTP Header
Setter mediation primitive to provide a mechanism for managing HTTP
headers in the message. You can change, copy, add, or delete HTTP
headers by setting the mediation primitive properties.

If you
want multiple header changes you can set multiple actions. Multiple
actions are acted on sequentially, in the order in which they are
specified; this means that header changes can build on each other.

You
can create new HTTP headers by specifying header field values. You
can search for HTTP headers that already exist in the SMO by specifying
the header name to match on. If a matching header is found, it can
then be deleted from the message, copied to another location in the
SMO, or have the value set. If a matching header is not found, a new
header can be created using a specified header field value.

The
HTTP Header Setter mediation primitive has one input terminal (in),
one output terminal (out) and a fail terminal (fail). The in terminal
is wired to accept a message and the other terminals are wired to
propagate a message. If the mediation is successful, the out terminal
propagates the modified message. If an exception occurs during the
transformation, the fail terminal propagates the original message,
together with any exception information contained in the failInfo
element.

- HTTP Control Headers, which have their own schema in the SMO,
located at /headers/HTTPHeader/control. The names of these headers
are relative XPaths.
- HTTP Spec Headers, which are listed in the SMO at /headers/HTTPHeader/header.
The names of these headers are from the HTTP 1.1 spec
- Any other headers are User Headers and are listed at /headers/properties.

## Usage

You can use the HTTP Header Setter
mediation primitive to ensure that when a HTTP message is sent to
another system, via the HTTP binding, the headers that are sent with
the message are correctly set.

Because the operations you define
occur sequentially, a later operation can depend on an earlier operation.
For example, you could create a new header, copy it to elsewhere in
the SMO and then delete it from the list of headers it was initially
appended to.

You can also use the HTTP Header Setter mediation
primitive to help to filter messages, using the Message Filter mediation
primitive. You might want to find a particular header and make it
available to be used in the filtering.

- HTTP Header Setter mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)