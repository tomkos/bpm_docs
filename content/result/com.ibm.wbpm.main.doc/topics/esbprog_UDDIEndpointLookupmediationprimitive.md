<!-- image -->

# UDDI Endpoint Lookup mediation primitive

To use the UDDI Endpoint Lookup mediation primitive you need to add service endpoint information
to your registry.

- Web Services using SOAP/HTTP.
- Web Services using SOAP/JMS.

When the UDDI Endpoint Lookup mediation primitive receives a message it sends a search query to
the registry. The search query is constructed using the UDDI properties that you specify and the
query might return nothing, or it might return one or more service endpoints.

The UDDI Endpoint Lookup primitive will update the target structure in the SMO Header with the
first service endpoint. The UDDI Endpoint Lookup mediation primitive will then update the
alternative target list with the remaining service endpoints.

The UDDI Endpoint Lookup Example scenario, can be implemented with a UDDI version 3 registry, and a UDDI Endpoint Lookup mediation
primitive in place of WSRR.