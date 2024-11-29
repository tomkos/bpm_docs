<!-- image -->

# Service Level Agreement Endpoint Lookup mediation primitive

- Whether the consumer of the endpoint has a valid SLA for the endpoint.
- Whether the particular SLA is active.
- Whether the endpoint is online.
- Whether the endpoint has a certain required classification; for example, whether it is
Production or Development.
- The Service Level Definition of the provider is in the subscribable
state.Note: This factor applies to WSRR Version 8.0 only.

## Example scenario

The fictional company Personal Holidays is making an internal service available to external
clients using a mediation flow. They want to use the WSRR GEP to ensure that only consumers with a
valid SLA can access the internal service.

Figure 1. SLA Endpoint Lookup

<!-- image -->