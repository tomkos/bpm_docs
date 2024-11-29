<!-- image -->

# Dynamic endpoint selection

- Endpoint Lookup mediation primitive

Use the Endpoint Lookup mediation primitive to dynamically route messages to appropriate service endpoints. The Endpoint Lookup searches for service information in a WSRR registry.
- UDDI Endpoint Lookup mediation primitive

Use the UDDI Endpoint Lookup mediation primitive to retrieve service endpoint information from a UDDI version 3 registry. The UDDI registry only holds web services information.
- Service Level Agreement Endpoint Lookup mediation primitive

Use the Service Level Agreement (SLA) Endpoint Lookup mediation primitive to look up endpoints referenced from an active service level agreement (SLA) between a service consumer and a service provider.
- Custom Endpoint Lookup mediation primitive

There are situations in which the supplied Endpoint Lookup mediation primitives are not sufficiently flexible. In these circumstances, use a Custom mediation primitive. If you need to access data in a WSRR registry, use the WSRR proxy.