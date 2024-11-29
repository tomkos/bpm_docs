# Type Filter mediation primitive

## Introduction

You can use the Type Filter
mediation primitive with XPath expressions to direct messages down
different paths of a flow, based on their type.

The Type Filter
mediation primitive has one input terminal (in),
one fail terminal (fail), and multiple output
terminals, (one of which is the default terminal).
The in terminal is wired to accept a message
and the other terminals are wired to propagate a message.

Each
of the output terminals, apart from the default terminal,
is associated with an XPath expression and a type. The elements of
the message identified by the XPath expressions are compared, in turn,
with the associated type. The primitive always uses the first matching
output terminal. The default terminal is used
if the message meets none of the conditions.

If an exception
occurs during the filtering, the fail terminal
propagates the original message, together with any exception information.

## Usage

You can use the Type Filter mediation
primitive to check that the inbound message has elements of a specific
type. If the criterion is not met you can raise a fault using the
Fail mediation primitive, or send an error response.

- Type Filter mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)