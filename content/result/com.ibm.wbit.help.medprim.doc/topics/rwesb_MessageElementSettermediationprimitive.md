# Message Element Setter mediation primitive

## Introduction

You can use the Message Element
Setter mediation primitive to provide a simple mechanism for setting
message content, it does not change the type of the message. You can
change, add or delete message elements by setting the mediation primitive
properties.

If you want multiple message changes you can set
multiple targets. Multiple target elements are set sequentially, in
the order in which they are specified; this means that elements can
build on each other.

You can set target elements to a constant
value, or to a value copied from somewhere in the input service message
object (SMO). If a target element you specify does not exist, it is
created in the SMO. You can also delete message elements, if they
are optional or repeating elements.

Target elements are specified
as XPath expressions using the Target property. If
you set a target element to a constant value, the target XPath must
resolve to a single leaf in an SMO node. If you set a target element
from a source element, both the source and target XPaths must resolve
to a single element (a single leaf or subtree). You can use the Value property
to specify either a constant value or a source XPath expression.

The
Message Element Setter mediation primitive has one input terminal
(in), one output terminal (out)
and a fail terminal (fail). The in terminal
is wired to accept a message and the other terminals are wired to
propagate a message. If the mediation is successful, the out terminal
propagates the modified message. If an exception occurs during the
transformation, the fail terminal propagates
the original message, together with any exception information contained
in the failInfo element.

## Usage

Because the operations you define
occur sequentially, a later operation can depend on an earlier operation.
For example, you could define a copy operation
to copy a new element into the SMO, and a later operation to set a
value in the newly copied element.

It is often useful to combine
the Message Element Setter mediation primitive with other mediation
primitives. For example, you can use the Message Element Setter mediation
primitive if you need to manipulate data, before or after the Database
Lookup mediation primitive is invoked.

You can also use the
Message Element Setter mediation primitive to change messages after
filtering them, using the Message Filter mediation primitive. You
might want to update or delete certain message elements after filtering.

- Message Element Setter mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)