<!-- image -->

# Aggregation patterns

- Aggregation of data from multiple sources: This pattern is useful if the results from
multiple service invocations need to be combined into a single message.
- Batch processing with message enrichment: This pattern is useful if the message to be
processed contains a repeating element, and each element needs to be enhanced separately.
- Batch processing requiring embedded aggregation: This pattern is useful if the scenario
is the basic batch processing pattern described in the second pattern, but the enhancement requires
information from multiple sources.
- Nested aggregation: This pattern is useful if the scenario is the basic batch processing
pattern described in the second pattern, but the repeating elements themselves contain repeating
elements.

- Aggregation of data from multiple sources

This scenario is based on an insurance quote comparison website that involves a web interface that allows users to specify details of their quote.
- Batch processing with message enrichment

This scenario is based on a store ordering system, where a salesperson can submit a request for a number of orders and have them dispatched. The original message that comes into the mediation flow identifies the customer for each order through a customer ID. The order request message needs to be enriched with each customer's shipping details so that the dispatch step has all the information it needs to succeed. This enrichment is done within the request flow by calling out to a customer information system, implemented using a Service Invoke mediation primitive.
- Batch processing requiring embedded aggregation

This scenario combines the two previously described examples, where an aggregation of data from multiple sources is embedded within a batch processing aggregation.
- Nested aggregation

This scenario is based on a supermarket company, where each outlet sends multiple restocking orders to a central company-wide system that batches the requests into a single message. This single message is submitted to the mediation flow where, for each order and for each branch, a separate invocation to the order system should occur.