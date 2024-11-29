<!-- image -->

# Aggregation of data from multiple sources

## Design the aggregation

The input into the flow is the InsuranceQuote interface, which specifies a Quote business object
with the relevant data. The first step in planning the aggregation architecture is to determine if
all data required to call the subsequent services are available in the inbound message, or if
message enrichment is required. In this scenario, the Quote object contains all the information for
both services. If this is not the case, then use a combination of this pattern and the batch
processing with message enrichment pattern.

The mediation flow includes a Fan Out mediation primitive (operating in Once mode) receiving the
Quote message as input and branching the logic to each insurance back-end service (InsuranceCompanyA
and InsuranceCompanyB). Before each Service Invoke mediation primitive, a
Mapping mediation primitive converts the body of the
message to the correct format, and immediately after the Service Invoke mediation primitive, a
Message Element Setter mediation primitive stores the response within the Shared context for later
retrieval when building the aggregated response. These two branches are then collected by a Fan In
mediation primitive (operating in Count mode). When the second message arrives at the Fan In
mediation primitive, its output terminal fires with this message, and then a final Mapping mediation primitive transforms the
values within the Shared context into the aggregated response message. This is illustrated in Figure 1.

Figure 1. Aggregation Fan Out branching

<!-- image -->

Figure 2. Shared context response messages

<!-- image -->

This is a simple but powerful usage pattern for aggregation, especially when it is combined into
a more complex scenario.