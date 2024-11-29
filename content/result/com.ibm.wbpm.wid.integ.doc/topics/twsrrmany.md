<!-- image -->

# Return all matching endpoints

## About this task

When a number of endpoints are retrieved from the registry,
the list of endpoints is placed in the EndpointLookupContext in the
message context. Another primitive is required to select an endpoint
from the list and place it in the target address in the message header,
and the message is then routed to the endpoint in the target address
element.

## Procedure

1. Create a mediation flow component, and add a source interface
that contains the source operation.
2. Click the source operation to open its implementation.
3. Drop a callout or service invoke primitive onto the editor.
4. Select the reference and operation that you want to invoke.
5. In order for the runtime to implement dynamic routing
on a request, the callout node or service invoke primitive must be
set to use the dynamic endpoint. Select it, and click the details
page in the properties view. Ensure that the Use dynamic endpoint
check box is selected.
6. Optional: Promote the Use dynamic endpoint property
so that the administrator can change it at run time. Click the Promoted
properties page, and select the promoted check box for the property.
7. Drop an Endpoint Lookup primitive onto the mediation flow
canvas, and select the properties that you want to use to query the
WSRR registry. At run time, all the endpoints matching
the query will be retrieved from the WSSR and placed in the context/primtiveContext/EndpointLookupContext element
of the message, as shown below:The message containing the retrieved endpoint information
will be propagated through the output terminal of the Endpoint Lookup
primitive.
8. Wire the output terminal of the Endpoint Lookup to another
mediation primitive such as a Message Element Setter or Custom Mediation
primitive in order to select a single service endpoint from the t/endpointReference/Address
element of EndpointLookupContext, and place it in the target address
element of the SMOHeader (/headers/SMOHeader/Target/address) shown
below: 
For valid URI formats for the supported target types,
see Dynamic endpoint example URIs.
9. You can then wire the output terminal of the Custom Mediation
primitive to the callout node, or to another primitive to perform
the next processing step of your flow.
10. Optional: Promote the query properties of Endpoint
Lookup such as User properties so that you can change the query to
the registry at run time without re-deploying the mediation module.
Click the Promoted properties page, and select the promoted check
box for the property
11. Optional: You can specify a default endpoint that
the runtime uses if it cannot find a dynamic endpoint. You specify
a default endpoint by wiring an import to the mediation flow component.
12. Optional: If there are no endpoints matching the
search criteria in the WSRR, the message is propagated to the noMatch
terminal of the Endpoint Lookup primitive. You can wire the noMatch
terminal to a mediation primitive for notification, such as a Message
Log or Event Emitter.

## Example

The following image shows an example
mediation flow when match policy is return all matching
endpoints.