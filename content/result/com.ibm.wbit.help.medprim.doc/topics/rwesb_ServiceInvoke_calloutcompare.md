# Comparison of Service Invoke and callout

## Comparing
the Service
Invoke and the callout

Figure 1. How Service Invoke terminals map to callout
terminals

<!-- image -->

- The in terminal of
the Service Invoke corresponds
to the in terminal of the callout.
- The out terminal
of the Service Invoke
corresponds to the out terminal of the callout
response.
- The fail terminal of the
Service Invoke
corresponds to the fail terminal of the callout
response (for an unmodeled fault).
- A modeled fault output
terminal of the Service Invoke, corresponds
to a modeled fault terminal of the callout fault.

- The Service Invoke mediation primitive does
not switch from request
flow to response flow.
- The Service Invoke mediation primitive
does not modify either
the transient context or the correlation context.

## Usage considerations

- If you need to call a service and return the response,
consider
using the Service Invoke mediation primitive.
- If you need
to interact with multiple services, and produce output
that combines service responses, consider using multiple Service Invoke
mediation primitives. In this type of configuration a callout node
might not be necessary; you might be able to configure all the Service
Invoke mediation primitives in the request flow.
- If you need
to call an intermediate service, you can use a Service
Invoke mediation primitive. For example, you might use an intermediate
service to adjust a message, or validate a message externally. The
mediation flow would contain a Service Invoke mediation primitive
and a callout to the final service provider.
- If you need to
mediate a message (without calling an intermediate
service) and then call a service provider, the use of a callout is
appropriate. The callout provides the simplest model for this configuration.