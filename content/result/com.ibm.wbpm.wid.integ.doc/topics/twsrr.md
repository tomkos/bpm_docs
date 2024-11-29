<!-- image -->

# Selecting endpoints dynamically from WSRR

## About this task

The Endpoint Lookup primitive queries the WSRR based on
the properties specified in the details page of the properties view.
The service information of each retrieved endpoint is placed in a primitiveContext/EndpointLookupContext element
in the message context. Through the match policy you can:

- Return all matching endpoints

If you want to retrieve a number of service endpoints from the WebSphere Service Registry and Repository (WSRR) and do further processing to select a service to invoke, then set the Match Policy property to return all matching endpoints.
- Return first matching endpoint and set routing target

If you want to select a single service endpoint from the WebSphere Service Registry and Repository (WSRR) using only the Endpoint Lookup mediation primitive, then set the Match Policy property to return one matching endpoint.
- Return all matching endpoints and set routing targets

The first match is used as the target and the rest are used as alternate targets. This is useful if you have multiple services which perform the same operation.
- Return endpoint matching latest compatible service version

If you want to route to a service retrieved from a WSRR registry based on the service version of an SCA module, choose a Match Policy of Return endpoint matching latest compatible service version.
- Runtime behavior of the Endpoint Lookup primitive

A summary of the resulting endpoint invoked by the message flow, depending on various conditions, when an Endpoint Lookup primitive is used: