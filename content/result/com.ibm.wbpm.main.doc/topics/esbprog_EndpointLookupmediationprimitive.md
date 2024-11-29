<!-- image -->

# Endpoint Lookup mediation primitive

You can use the Endpoint Lookup mediation primitive to retrieve service endpoint information from
a WSRR registry that can be local or remote. The service endpoint information can relate directly to
web services, or to SCA module exports, or to manually defined MQ, JMS and HTTP services.

- If you want to extract service endpoint information about web services, your WSRR registry must
contain either the appropriate WSDL documents, or SCA modules that contain exports using web service
bindings.
- If you want to extract service endpoint information about exports that use the other SCA
bindings, your WSRR registry must contain the appropriate SCA modules.
- If you want to extract service endpoint information about services that are accessed using MQ,
JMS or HTTP but are not defined in a SCA module, your WSRR registry must contain an appropriate
Manual JMS/HTTP/MQ endpoint with associated Interface Business Object with the endpoint
information and associated interface correctly set.

- Web services using SOAP/HTTP.
- Web services using SOAP/JMS.
- SCA module exports with web service bindings, using SOAP/HTTP.
- SCA module exports with web service bindings, using SOAP/JMS.
- SCA module exports with the default SCA binding.
- SCA module exports with the MQ binding.
- SCA module exports with the MQ JMS binding.
- SCA module exports with the JMS binding.
- SCA module exports with the Generic JMS binding.
- SCA module exports with the HTTP binding.
- Manually defined MQ endpoints with associated interfaces.
- Manually defined JMS endpoints with associated interfaces.
- Manually defined HTTP endpoints with associated interfaces.

When the Endpoint Lookup mediation primitive receives a message it sends a search query to the
registry. The search query is constructed using the Endpoint Lookup properties that you specify and
the query might return nothing, or it might return one or more service endpoints.

The Endpoint Lookup primitive will update the target structure in the SMO header with the first
service endpoint. The Endpoint Lookup primitive will then update the alternative target list with
the remaining service endpoints.

## Example scenario

Figure 1. Endpoint Lookup within a mediation flow

<!-- image -->

The fictional company Personal Holidays is making an internal service available to external
clients using a mediation flow. If the server that runs the internal service fails, one or more back
up servers which are also hosting the internal service are called instead, as shown in Figure 1.

Figure 2. Endpoint Lookup mediation primitive properties

<!-- image -->

Figure 3. Try alternate endpoint property of the Callout node

<!-- image -->

By storing the service endpoints in WSRR, Personal Holidays can update their back up services at
any time, without needing to modify the mediation flow component.