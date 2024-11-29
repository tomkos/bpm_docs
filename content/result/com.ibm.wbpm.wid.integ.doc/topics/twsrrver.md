<!-- image -->

# Return endpoint matching latest compatible service version

## Before you begin

## About this task

Follow these steps to create an example mediation flow
that uses an Endpoint Lookup primitive to retrieve a service endpoint
from the WSRR and routes the message to the retrieved endpoint.

## Procedure

1. Create a mediation flow component, and add a source interface
that contains the source operation.
2. Click the source operation to open its implementation.
3. Drop a callout or service invoke primitive onto the editor.
4. Select the reference and operation that you want to invoke.
5. In order for the runtime to implement dynamic routing on
a request, the callout node or service invoke primitive must be set
to use the dynamic endpoint. Select the callout node, and click the
details page in the properties view. Ensure that the Use dynamic endpoint
check box is selected.
6. Optional: Promote the Use dynamic endpoint property
so that the administrator can change it at run time. Click the Promoted
properties page, and select the promoted check box for the property.
7 Drop an Endpoint Lookup primitive onto the mediation flowcanvas, and select the properties that you want to use to query theWSRR registry. At run time, a single endpoint that matches the querywill be retrieved from the WSSR and placed in the target address elementof the SMOHeader in the message (/headers/SMOHeader/Target/address),and the message will be routed to the URI specified in the addresselement, shown in the image below: For valid URI formats for the supported target types, see Dynamic endpoint example URIs .
    1. Choose a Match Policy of Return
endpoint matching latest compatible service version
    2. Set the Version property to be
the version of the SCA module. The asterisk (*) wildcard character
is supported for the version number (for example, 1.1.*).
    3. Set the Module  property to the
name of the module. This must be the original name of the module,
without the version number.
    4. Set Export to the name of the
export with SCA binding that you want to invoke.

<!-- image -->

For valid URI formats for the supported target types, see Dynamic endpoint example URIs.

8. The message containing the retrieved endpoint information
will be propagated through the output terminal of the Endpoint Lookup
primitive, and no further mediation is required to select the endpoint.
You can directly wire the output terminal of the Endpoint Lookup to
the callout node or service invoke, or to another primitive to perform
the next processing step of your flow.
9. Optional: Promote the query properties of Endpoint
Lookup, such as User properties, so that you can change the query
to the registry at run time without redeploying the mediation module.
10 Optional: You can specify a default endpoint thatthe runtime uses if it cannot find a dynamic endpoint. For example:

- Wire an import to a reference in the mediation flow editor, and
wire the noMatch terminal to the corresponding node in the mediation
flow editor.
- Wire the noMatch terminal to another primitive (such as MessageSetter
or Custom Mediation) which updates the /headers/smoHeaders/target/address
element with the next location. Enable dynamic lookup on the callout
node or service invoke primitive.
11. Optional: If there are no endpoints matching the
search criteria in the WSRR, the message is propagated to the noMatch
terminal of the Endpoint Lookup primitive. You can wire the noMatch
terminal to a mediation primitive for notification, such as an Event
Emitter.