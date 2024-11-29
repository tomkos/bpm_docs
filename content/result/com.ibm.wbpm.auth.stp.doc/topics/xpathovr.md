<!-- image -->

# XPath usage overview

## Assign activity

<!-- image -->

An XPath
expression can reference simple data types, such as strings and integers,
and complex data types. When you use the BPEL process editor, there
is no verification that an assignment is correct regarding the data
type of from-statement and to-statement parts. If you assign a part
of a BPEL variable that is a simple data type, the IBM® Workflow
Server converts
it to the appropriate target simple data type if applicable. For example,
you can assign an integer value to a string part of a variable. Nevertheless,
if you are working with business objects, the data is not converted.
You must make sure to assign only parts which are either convertible
(simple types) or identically typed (simple types and business objects).

While you can use arbitrary XPath functions (see BPEL processes: Predefined XPath extension functions) for the from part of an assign activity,
support for using them on the to part is limited
to the child:: and attribute:: axes.
For more information, see technote  http://www-1.ibm.com/support/docview.wss?&uid=swg21222985.

Be sure to address the to part by an XPath statement without functions, (for example, /customers/address[1]/name). If you fill an array property
using assign activities, be sure to access them sequentially for the to part. For example, you must fill /customers/address[1]/name before you fill /customers/address[2]/name (array
indexes in XPath start with index 1). Otherwise, you get an exception
during execution in IBM Workflow
Server,
which is thrown as the standard fault bpws:mismatchedAssignmentFailure. Also note that sibling functions are not allowed in a to-statement,
if the referenced node has not been initialized before.

## Conditions and expressions

At several places
in the BPEL process editor, you can also use XPath-based conditions
and expressions. This includes conditions on links in parallel activities,
the join behavior on arbitrary activities within parallel activities,
conditions in choice activities and while loop activities, expressions
in the wait activity and the timeout expression in the receive choice
activity. In addition, the ForEach activity can use XPath for its
start and end expressions, as well as an XPath condition for its exit
criterion.

In assign activities, XPath statements are used to
reference a from-part and a to-part to be used for an assignment.
Nevertheless, conditions and expressions must have a specific return
value. Therefore, you must make sure your XPath points to a part in
a BPEL variable that has the appropriate type (for example, Boolean
for conditions). Otherwise, you must use XPath to build such a type,
(for example, bpws:getVariableData("customer", "deliveraddress/zip")="12345").

## Example

## Related concepts

- Choosing between XPath and Java in your BPEL process
- XPath extension functions for BPEL processes