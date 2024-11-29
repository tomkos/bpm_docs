# Message Filter mediation primitive

## Introduction

You can use the Message Filter
mediation primitive with an XPath expressions to direct messages,
which meet certain criteria, down different paths of a flow.

The
Message Filter mediation primitive has one input terminal (in),
one fail terminal (fail), and multiple output
terminals, (one of which is the default terminal).
The in terminal is wired to accept a message
and the other terminals are wired to propagate a message.

Each
of the output terminals, apart from the default terminal,
is associated with a simple, conditional expression. The contents
of the input message are compared with each expression in turn and,
if the condition is met, the message is propagated to the associated
output terminal. The primitive can be configured either to use the
first matching output terminal, or all matching output terminals.
The default terminal is used if the message
meets none of the conditions.

If an exception occurs during
the filtering, the fail terminal propagates
the original message, together with any exception information.

## Usage

You can use the Message Filter mediation
primitive to check that the inbound message meets some criterion.
For example, that a required field is set. If the criterion is not
met you can raise a fault using the Fail mediation primitive, or send
an error response.

The Message Filter mediation primitive lets
different messages take different paths. For example, a message might
need forwarding to different service providers based on the request
details.

You can use the Message Filter mediation primitive
to bypass unnecessary steps. You can test if certain data is in a
message, and only perform a Database Lookup operation if the data
is missing.

When used in combination with a Database Lookup
primitive, the Message Filter can direct messages based on the contents
of an independently administered lookup table. For example, you could
route a message based on customer status even if the inbound message
contained only the customer identifier.

By configuring the primitive
to propagate messages to all matching terminals, you can trigger multiple
events each requiring different conditions. For example, you could
log requests relating to a particular account identifier and send
requests relating to a particular product to be audited.

- Message Filter mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)