<!-- image -->

# MQ imports and exports at run time

## MQ import

The sequence
of the methods used at run time is shown in the following diagram.
The import first sets the request body fields including the format,
a boolean flag to indicate an exception and then sets the data object
field. It then writes the message and gets the format for that message.
Some methods, setObject and setObjectType, are only used if a JMSObjectDataBinding
is used. Next, the header fields are set. The format is checked to
determine if the format is supported and then the Coded Character
Set Identifier (CCSID) and character encoding fields are set. The
data object field is set and the message is written out including
the message descriptor and headers. Since there can be a chain of
messages, the relationship is that the preceding header gives the
format, CCSID and encoding of the next header in the chain. The last
header gives the format, CCSID and encoding of the body.

In
the case of a request-response operation, another set of methods is
used. The import first checks the header information in the response
to see if the format in the response is supported. Then it reads the
message and gets the next format, CCSID and encoding of the following
header in a chain. It then reads the response body information. It
checks if the body contains an exception first and then gets the message.
Some methods, isObjectType and getObject, are only used if an MQObjectDataBinding
is used.

<!-- image -->

## MQ export

The sequence
of the methods used at run time is shown in the following diagram.
First, a check is made that the format of the incoming message is
supported. Then the message is read. The header information is examined
to get the data object, the format, CCSID and encoding of the next
header and then the function name is generated. The body of the input
message is read including the message descriptor and headers with
an initial analysis to see if it is an exception. Then the data object
is retrieved. Some methods, isObjectType and getObject, are only used
if an MQObjectDataBinding is used.

In the
case of a request-response operation, another set of methods is used
for the output header and output body for the response. The export
first sets the format of the message in the body and then sets the
business exception flag to indicate if an exception is being returned.
Then it sets the data object field and writes the message out including
the message descriptor and headers. Some methods, setObject and setObjectType,
are only used if an MQObjectDataBinding is used. It then gets the
format and turning to the output header checks if the format is supported.
It then sets the CCSID, encoding and format for the body, sets the
data object and writes the message.

<!-- image -->