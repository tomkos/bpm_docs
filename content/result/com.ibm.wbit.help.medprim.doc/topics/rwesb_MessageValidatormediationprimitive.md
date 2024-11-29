# Message Validator mediation primitive

## Introduction

You can use the Message Validator
mediation primitive to validate messages.

The Message Validator
mediation primitive has one input terminal (in),
one output terminal (out), and one fail terminal
(fail). The in terminal
is wired to accept a message and the other terminals are wired to
propagate a message. At run time, if no validation exception occurs
during the processing of the input message, the out terminal
propagates the validated message. If a validation exception occurs,
the fail terminal is fired, and stores the
exception information in the FailInfo element
of the service message object (SMO).

## Details

After you create your mediation
flow, and configure your mediation primitives, you can insert the
Message Validator mediation primitive into the flow to validate some,
or all, parts of the message.

The Message Validator mediation
primitive validates the message and also validates any weakly-typed
message fields that have been set to strongly-typed message fields
earlier in the mediation flow. You can set weakly-typed message fields
to strongly-typed message fields using the Set Message Type primitive
or the Type Filter primitive. Alternatively, you can use the input
node to set the weakly-typed fields in the correlation, transient,
or shared context.

## Usage

You can use the Message Validator
mediation primitive whenever you want to validate incoming messages.
The validation includes checking that any weakly-typed message fields
that have been set to strongly-typed message fields, are of the specified
strong type.

- Message Validator mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)