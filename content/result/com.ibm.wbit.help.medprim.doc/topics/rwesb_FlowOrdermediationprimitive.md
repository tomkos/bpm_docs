# Flow Order mediation primitive

## Introduction

You can use the Flow Order
mediation primitive to customize the flow by specifying the output
terminals to be fired. The Flow Order mediation primitive does not
change the input message.

The Flow Order mediation primitive
has one input terminal (in) and any number
of output terminals. The in terminal is wired to accept a message
and the other terminals are wired to propagate a message.

## Details

The output terminals are fired in
the order that they are defined on the primitive, with each branch
completing before the next starts. Each output terminal is fired with
an unmodified copy of the input message.

## Usage

You can use the Flow Order mediation
primitive anywhere that you want to branch a flow. A named output
terminal is created for each branch. Each branch of the flow is completed
before the next terminal is fired. The only exception to this rule
is that if an Asynchronous Service Invoke mediation primitive is reached,
the service is called but the Flow Order does not wait for the service
invocation to complete before moving on to the next branch. If an
exception is thrown by any of the down stream mediation primitives
and they do not handle it themselves (for example, via their fail
terminal), any remaining flow branches are not fired.

- Flow Order mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)