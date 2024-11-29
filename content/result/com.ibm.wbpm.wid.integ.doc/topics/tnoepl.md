<!-- image -->

# Selecting endpoints dynamically without using a registry

## Before you begin

## About this task

Dynamic routing is enabled by the Use dynamic
endpoint property in the callout node that sets the callout
to be dynamic. When the dynamic callout is invoked, it checks the /headers/SMOHeader/Target/address element
in the message header for a service endpoint address, and routes the
message to the address of that endpoint. If no address exists in the
target address element, a service will be selected statically, if
an import is wired to the associated reference of the callout in the
mediation flow component. By default, the Use dynamic endpoint is
enabled.

The target address element in the message header can
be updated in a number of ways. You can use a Database Lookup primitive
to retrieve a service endpoint from a database and place the retrieved
URI directly into the target address element of the message. Or, you
can use a Message Element Setter or Custom Mediation primitive to
process the message and update the target address.

Follow these
steps to create a mediation flow that uses a Database Lookup primitive
to query a database and set the target endpoint address in the message
header. .

## Procedure

1. Create a mediation flow component, and add a source interface
that contains the source operation.
2. Click the source operation to open its implementation.
3. Drop a callout or service invoke primitive onto the editor.
4. Select the reference and operation that you want to invoke.
5. Select the callout node, and click the details page in
the properties view. Ensure that the Use dynamic endpoint check
box is selected.
6. Optional: Promote the Use dynamic endpoint property
so that the administrator can change it at run time. Click the Promoted
properties page, and select the promoted check box for the property.
7. Drop a Database Lookup primitive onto the mediation flow
canvas, and enter your query properties, as well as the column that
contains the endpoint addresses. Set the Message element property
to /headers/SMOHeader/Target/address in order
to place the retrieved endpoint address into the dynamic callout target
address. For more information, see the properties example at the end
of this topic.
8. Optional: Promote the key path and key column name
properties of Database Lookup so that you can change your query at
run time. Click the Promoted properties page, and select the promoted
check box for the property.
9. Optional:   You can specify a default endpoint that
the runtime uses if it cannot find a dynamic endpoint. You specify
a default endpoint by wiring an import to the mediation flow component.
10. Optional: If there are no endpoints matching the
search criteria in the database, the message is propagated to the
keyNotFound terminal of the Database Lookup primitive. You can wire
the keyNotFound terminal to a mediation primitive for notification,
such as a Message Log or Event Emitter.
11. Note: Fault,
failure and time-out messages returned from a service invocation will
retain the value of the original SMO's address field for use in additional
routing or error handling.

## Example

The
following image shows an example mediation flow using the Database
Lookup primitive.

The following example shows the properties of the Database
Lookup primitive: