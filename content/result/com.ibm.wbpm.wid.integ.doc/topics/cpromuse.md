<!-- image -->

# Example: Promoting properties

A financial services company provides an interactive web-based
stock market service to its customers. The company uses two different
stock quote services to receive stock prices; a delayed service and
a real-time service. The following diagram shows the response to the
stock quote request that is returned from each service. Each response
message is transformed and then logged before it is returned to the
client.

<!-- image -->

The Promoted properties view of the LogMessage primitive shows
that the Root property is promoted and its value is /body:

<!-- image -->

When a promoted property's value is changed at run time, the timeliness
of the update might vary. In a cell environment, the change needs
to be synchronized across all nodes. .