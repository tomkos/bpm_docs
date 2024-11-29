<!-- image -->

# Performance considerations when using aggregation

Aggregation patterns often require multiple requests to be built from a single input request and
multiple responses to be merged into a single response. You can build these responses by using
BOMapper mediation primitives, as shown in the examples in other Aggregation topics. Performance
will be significantly improved by using Business Object Maps, if there are no complex operations
required in these transformations, and if the data is simply being moved from one part of the
message to another. This can be done using either the BO Mapper mediation primitive or the Mapping mediation primitive, which is set to use the Business Object Map
engine. The performance improvement is
also relevant for larger messages. If you have complex operations, use the Mapping mediation primitive, set to use either the XSLT
1.0 or XSLT 2.0 engine. The Data Transformation section discusses these
mediation primitives in more detail.

## Batch processing considerations

In the batch processing
scenario it is important to consider the impact that processing large batched requests may
have on other applications hosted on the same server. Processing requests with a large number of
repeating elements; for example, a large number of sales orders, can use a significant amount of
system memory, which will remain in use until all processing is complete. Depending on the response
times of the services being called within the aggregation block processing may slow down system
resources for long periods. If the same server used for processing batch requests is also being used
to host applications that need to respond quickly to requests, you can see a degradation in service
while the batched request is being processed. You can avoid this issue by processing large batched
requests on a separate server or by processing the requests during periods of low system usage.

For the reasons explained before, it is important to minimize the amount of memory used when
processing large batched request messages. When using the batched processing pattern, the body of
the original request message is rarely required inside the aggregation block because the Fan Out
mediation primitive stores the current instance of a repeating element in the Fan Out context. In
this example it is the sales order that is being processed. At the end of the aggregation block the
response data is held in the Shared context and it is used to build a new response message body. If
the request is large, then significant savings in memory usage and reductions in processing time can
be achieved by deleting the message body immediately after it has been processed in the Fan Out
mediation primitive, by using the Message Element Setter mediation primitive, as shown in Figure 1.

Figure 1. Deleting the message body

<!-- image -->

## Other memory considerations

After an aggregation block is completed the responses that have been stored in the Shared context
are combined into a new response message body. This is done immediately after the Fan In mediation
primitive, as shown in the BOMapper in Figure 1 and in Figure 6 .

Figure 2. Aggregation context mapping

<!-- image -->