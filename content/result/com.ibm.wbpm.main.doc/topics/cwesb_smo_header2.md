<!-- image -->

# SMO structure

The structure of a SMO is shown in Figure 1
.

Figure 1. Overview of SMO structure. The context, headers, body and attachments of a ServiceMessageObject

<!-- image -->

The ServiceMessageObject Java™ interface provides access to
the message headers, message body, message context and message attachments.

## SMO headers

The SMO headers carry header information for different types of messages.

- SOAP
- HTTP
- JMS
- WebSphere® MQ
- SCA
- Web services
- WebSphere Adapters

## SMO context

The SMO context lets mediation primitives pass data that is not part of the message payload,
between themselves.

SMO context objects are either user-defined or system-defined.

## System-defined context objects

- failInfo. The failInfo context object is used to hold exception information
- primitiveContext. The primitiveContext object contains information used by specific mediation
primitives
- dynamicProperty. The dynamicProperty object is used to override promoted
properties

## User-defined context objects

User-defined context objects can be used to store properties that mediation primitives use later
in the flow.

- correlation context is used for mediation primitives to pass values from the request flow to the
response flow.
- transient context is used for passing values between mediation primitives in the current flow.
Values in the transient context are not shared between the request and the response flows or between
branches of the same flow.
- shared context is a storage area you can use if you want to aggregate data. The shared context
is shared between all branches of a flow. It is not shared between the request and the response
flows or between branches of the same flow.
- user context is slightly different to other user-defined context objects. It is
used to pass data that is not part of the message payload, between multiple SCA components in the
same module or across SCA module boundaries.

## SMO body

The body of a SMO is a business object that is defined by reference to a Web Services Description
Language (WSDL) message.

For each part defined by the WSDL message there is one element under the SMO body. The contents
of the SMO elements are of the structure of the WSDL part definition. The element names depend upon
the kind of WSDL message that the SMO is defined from.

## SMO attachments

The SMO contains an attachments element for each attachment associated with a
SOAP message.

The SMO attachments element let you send and receive SOAP messages that have
attachments of various types.

You might want to send SOAP messages with attachments and let the attachments pass through the
mediation flow unchanged, or you might want to create new attachments, perhaps from information in
the message or from an external source.