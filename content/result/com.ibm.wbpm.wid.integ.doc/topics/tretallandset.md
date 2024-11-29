<!-- image -->

# Return all matching endpoints and set routing targets

## Before you begin

If no matches are
found, the noMatch terminal is fired and both the Target and AlternateTarget(s)
are left unchanged.

## About this task

## Procedure

1. Create a mediation flow component, and add a source interface
that contains the source operation.
2. Click the source operation to open its implementation.
3. Drop a callout or service invoke primitive onto the editor.
4. Select the reference and operation that you want to invoke.
5. In order for the runtime to implement dynamic routing on
a request, the callout node or service invoke primitive must be set
to use the dynamic endpoint. Select the callout node or service invoke
primitive, and click the details page in the properties view. Ensure
that the Use dynamic endpoint check box is selected.
6. Drop an Endpoint Lookup primitive on the canvas and select
the Return all matching endpoints and set alternate routing
targets Match Policy in its Properties view.
7. Wire the primitive to the rest of the mediation flow.
8. Optional: Promote the Use dynamic endpoint property
so that the administrator can change it at run time. Click the Promoted
properties page, and select the promoted check box for the property.
9. Optional: Promote the query properties of Endpoint
Lookup such as User properties so that you can change the query to
the registry at run time without re-deploying the mediation module.
Click the Promoted properties page, and select the promoted check
box for the property
10. Optional: You can specify a default endpoint that
the runtime uses if it cannot find a dynamic endpoint. You specify
a default endpoint by wiring an import to the mediation flow component.
11. Optional: If there are no endpoints matching the
search criteria in the WSRR, the message is propagated to the noMatch
terminal of the Endpoint Lookup primitive. You can wire the noMatch
terminal to a mediation primitive for notification, such as a Message
Log or Event Emitter.