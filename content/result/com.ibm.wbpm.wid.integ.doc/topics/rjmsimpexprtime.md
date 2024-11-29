<!-- image -->

# JMS imports and exports at run time

## JMS import

The sequence
of the methods used at run time is shown in the following diagram.
Using getter and setter methods, the import first gets the message
type and then sets the data object before writing out the message.
Some methods, setObject and setObjectType, are only used if a JMSObjectDataBinding
is used.

In the case of a request-response operation, another
set of methods is used with the output data binding. The import first
reads the message, determines if it is an exception and then gets
the data object. Some methods, isObjectType and getObject, are only
used if a JMSObjectDataBinding is used.

<!-- image -->

## JMS export

The sequence
of the methods used at run time is shown in the following diagram.
The function name is first generated. Then the message is read and
the data object received from the input data binding. At that point,
the message is checked in case it is an exception. Some methods, isObjectType
and getObject, are only used if a JMSObjectDataBinding is used.

In the case of a request-response operation, another
set of methods is used with the output data binding. The export first
sets the business exception flag to indicate if an exception is being
returned. Then it sets the data object field and writes the message
out. Some methods, setObject and setObjectType, are only used if a
JMSObjectDataBinding is used.

<!-- image -->