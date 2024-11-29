<!-- image -->

# Comparison of the Service Invoke mediation primitive and the Callout node

- The in terminal of the Service Invoke mediation primitive corresponds to the in terminal of the
Callout node.
- The out terminal of the Service Invoke mediation primitive corresponds to the out terminal of
the Callout Response node.
- The fail terminal of the Service Invoke mediation primitive corresponds to the fail terminal of
the Callout Response node (for an unmodeled fault).
- A modelled fault output terminal of the Service Invoke mediation primitive, corresponds to a
modelled fault terminal of the Callout Fault node.

- The Service Invoke mediation primitive does not switch from request flow to response flow.
- The Service Invoke mediation primitive does not modify either the transient context or the
correlation context.
- A Service Invoke mediation primitive has a separate timeout terminal. A Callout node only has a
fail terminal.

| Use the Service Invoke if                                                                                                                                                                                                                                                           | Use the Callout if                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| You need to call a service and return the response within a mediation flow.                                                                                                                                                                                                         | You need to mediate a message (without calling an intermediate service) and then call a service provider. The Callout provides the simplest model for this configuration. |
| You need to interact with multiple services, and produce an output that combines service responses.                                                                                                                                                                                 |                                                                                                                                                                           |
| You need to call an intermediate service. For example, you might use an intermediate service to adjust a message, or validate a message externally. The mediation flow contains a Service Invoke mediation primitive, and a Callout node that is connected to the service provider. |                                                                                                                                                                           |