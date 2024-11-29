<!-- image -->

# XPath Example: Mediation Flow

The Message Filter primitive takes XPath expressions as
properties and decides where the input message will be routed based
on the expressions entered. If none of the expressions evaluate to
true, the message is routed to the default terminal.

This example
illustrates a simple order processing scenario. Each order contains
a field for the age of the order and one for the priority of the order,
along with customer information. In this example, an order will be
given high priority if its age is greater than 14 days. The priority
can also be changed manually if needed.

<!-- image -->

- shipTo - holds the customer's name and address.
- orderDate - holds the date on which the order was placed.
- orderAge - of integer type, holds the age of the order
in days based on the current date and when the order was placed.
- highPriority - of boolean type, allows the order to be
given high priority manually. The default value is 'false.'

<!-- image -->

- getPO - request-response operation which takes in an object
of type PurchaseOrderType and outputs an object of the same type.

<!-- image -->

- Routing - Message Filter primitive with a default and highPriority
output terminal.
- Normal\_Priority - Mapping primitive to transform the message
into a normal priority message.
- High\_Priority -  Mapping primitive to transform the message
into a high priority message.

When the Message Filter primitive is
dropped on the canvas, it has a default terminal, a match terminal
and a fail terminal as outputs. To add another terminal, right click
the primitive and select Add Output Terminal. Name the new terminal highPriority. We are
now ready to set the primitive's properties.

<!-- image -->

<!-- image -->

<!-- image -->

In
the Add/Edit properties wizard, the Patterns field shows the completed
XPath expression /body/getPO/input/orderAge > '14'.

<!-- image -->

Follow
the same procedure to add the second condition to the message filter.
The XPath Expression you want is /body/getPO/input/highPriority
= 'true'. You can also copy and paste this expression
or type it in the pattern field to save time.

At run time, the
order will enter the Message Filter primitive where it will be analyzed.
If the age of the order is greater than 14 days or if it has been
given a high priority, it will be sent to the high priority terminal.
Otherwise, it will continue to the default output terminal.