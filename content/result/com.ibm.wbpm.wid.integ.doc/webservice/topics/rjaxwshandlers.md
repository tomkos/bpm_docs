<!-- image -->

# Java API for XML Web Services (JAX-WS) handlers

A JAX-WS handler provides a range of handling
tasks. For example, a JAX-WS handler could log a message, or transform
an incoming or outgoing message. JAX-WS handlers can be chained together
to produce complex operations.

There are two types of JAX-WS
handlers - logical and protocol. Logical handlers process the message
payload and the properties stored in the message context. Protocol
handlers operate on protocol-specific messages and message context
properties. Currently, only SOAP-specific configurations are implemented.

A
JAX-WS handler can be used with an export or an import.

You
can create your own JAX-WS handler. If you do, the classes in your
JAX-WS handler must implement the javax.xml.ws.handler.LogicalHandler or
the javax.xml.ws.handler.soap.SOAPHandler interfaces.
Alternately, you can choose to create a JAX-WS handler at the time
you work in the properties with them. In making a selection of the
handler type, one of these interfaces will be chosen.

## Exports

To work with JAX-WS handlers, open
the properties view of the export and click the JAX-WS
handlers tab.

1. To add a JAX-WS handler, click Add in the
left pane. The available handlers are listed in a handler selection
window. You may also create a JAX-WS handler at this time by clicking New,
selecting a handler type (SOAP or logical handler), and proceeding
with the wizard to create a new JAX-WS handler.
2. Select the handlers you want to consider for your binding. They
are added to a list which you can order. You can also make deletions
from the list.
3. Once you have the handlers you want to work with, select one you
want to examine for your binding and its properties are then shown
on the right pane.
4. Once you have made your selection of a handler for your binding
and possibly updated the message context properties, save the file.

## Imports

To work with JAX-WS handlers, open
the properties view of the import and click the JAX-WS
handlers tab.

The steps to work with and select
a JAX-WS handler for your import binding are the same as an export.