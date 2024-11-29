<!-- image -->

# Performing chained aggregation

## What to do next

<!-- image -->

1. ServiceInvoke\_A calls Service A and populates the body of the
message with its response.
2. Using XSLTransformation1 you can extract and store parts or the
whole message in the transient context.
3. ServiceInvoke\_B then calls Service B which repopulates the message
body with its response.
4. Finally, XSLTransformation2 aggregates the current body of the
message (response from Service B) with the contents of the transient
context (stored response from Service A).