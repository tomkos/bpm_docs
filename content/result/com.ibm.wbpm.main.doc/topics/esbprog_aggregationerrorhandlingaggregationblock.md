<!-- image -->

# Error handling within an aggregation block

- The Stop mediation primitive stops the current branch of execution and the aggregation will
continue to either another branch or iteration.
- The Fail mediation primitive terminates the entire mediation flow and return a
ServiceRuntimeException to the caller of the mediation. In general, the Fail mediation primitive
should not be used within an aggregation, unless you want to terminate the processing of the entire
flow immediately.
- The Fan In mediation primitive provides a Stop input terminal that can be wired to signal that
the aggregation should be terminated. When a message arrives at the Stop terminal the incomplete
output terminal is fired. Additional mediation primitives can then be wired to handle this situation
and if required this could include a Fail mediation primitive.

The Fan In mediation primitive includes a property that specifies the timeout value. The timeout
period starts when the associated Fan Out mediation primitive fires an output terminal for the first
time. If a message arrives at the Fan In mediation primitive in terminal
after this timeout period, it is considered late, and the incomplete terminal is fired. The default
value for the timeout property is -1, which means there is no timeout, and no
messages are considered late.