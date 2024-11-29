<!-- image -->

# Aggregation

- A car comparison insurance quote system where a single request is submitted to an ESB that
causes multiple insurance service providers to be queried before the best quote is returned.
- A holiday booking request arrives at the ESB and needs to be forwarded to separate hotel, flight
and car hire booking systems, before a combined response can be returned.
- A store ordering system, where a salesperson can submit a request for a number of orders and
have them dispatched. The original message coming into the ESB identifies the customer for each
order via a customer ID. So, the order request message needs to be enriched with each customer's
shipping details so that the dispatch step has all the information it needs to succeed.

- The Fan Out mediation primitive
- The Fan Out context
- The Fan In mediation primitive
- The Service Invoke mediation primitive
- Aggregation block
- Shared context
- Special considerations

## Fan Out mediation primitive

Figure 1. The Fan Out mediation primitive properties view

<!-- image -->

## Fan Out context

```
<FanOutContext>
	<iteration>0</iteration>
		<occurrence>
			<order>
				<id>1234567890</id>
			</order>
		</occurrence>
</FanOutContext>
```

## Fan In mediation primitive

- Simple count: the output terminal is fired when a set number of messages is received at
the input terminal. However, more messages might be sent out by the Fan Out mediation primitive,
because the Fan In mediation primitive count decision point can be reached more than once, resulting
in multiple firings of the output terminal.
- XPath decision: the output terminal is fired if an XPath expression evaluation of the
incoming message evaluates to true. It is possible for the output terminal to
fire multiple times.
- Iterate: the Fan In mediation primitive waits to receive all messages produced by the
corresponding Fan Out mediation primitive. All of the occurrences in the repeating element have been
processed.

Figure 2. The Fan In mediation primitive properties view

<!-- image -->

The Fan In mediation primitive has two input terminals (in and
stop), two output terminals (out and
incomplete) and a fail terminal (fail). The input
terminals are wired to accept a message and the other terminals are wired to propagate a message.

The in terminal accepts input messages until a decision point is
reached. When a decision point is reached the out terminal is fired. Although
the out terminal is fired when a decision point is reached, the
in terminal can still accept input messages, under some circumstances. For
example, if the count value is reached, the out terminal is fired. However,
if the Fan Out mediation primitive is still sending messages, the Fan In mediation primitive can
still receive messages.

## Service Invoke mediation primitive

## Aggregation block

Figure 3. Example of an aggregation block

<!-- image -->

## Shared context

- Data stored in the Transient context is available within either a request or response flow.
- Data stored in the Correlation context is available in both the request and response flows.
- Data stored in the Shared context is available in all branches and executions of an aggregation
block.

Figure 4. Shared context example

<!-- image -->

## Aggregation mediation programming model special considerations

- The Shared context is part of the SMO, and is designed for use inside aggregation blocks because
the data put into it is available in all the branches of a flow. The design of the Shared context
structure is essential to a successful aggregation design. The goal is to store the response from
each service invocation into a structure that can then be converted into a single response message
after the aggregation block.
- The Shared context is shared across SMOs and should be considered read-only outside the
aggregation block.
- At development time it is difficult to determine which SMO body type will be emitted from the
Fan In mediation primitive output terminal. Mediation primitives after the Fan In mediation
primitive should be used to generate a new message body using the information in the Shared context.
- If a message arrives at a Fan Out mediation primitive, one or more output terminals of the Fan
In mediation primitive will fire (assuming no ServiceRuntimeExceptions occur within the aggregation
block, for example, as a result of running a Fail mediation primitive), even if a message is not
received by the Fan In mediation primitive. Table 1 highlights this behavior.Note: In some circumstances it is possible that none of the messages
sent by the Fan Out mediation primitive arrive at the corresponding Fan In mediation primitive.
Using Figure 4 to illustrate, consider this example:
if the second output terminal on primitives branch 1 and branch 2 are fired, this does not cause the
messages to arrive at the Fan In mediation primitive, because there is no wired path. This is
represented in Table 1 by the message result
No.

| Fan In mediation primitive mode   | Message arrives at Fan In mediation primitive             | Output terminal fired   | SMO of Fan In mediation primitive                                                               |
|-----------------------------------|-----------------------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------|
| Iterate                           | No                                                        | Complete                | Message body empty; SMO headers and context are the same as the message received at the Fan Out |
| Iterate                           | Yes (in terminal)                                         | Complete                | Last message received at the Fan In mediation primitive input terminal                          |
| Iterate                           | Yes (stop terminal)                                       | Incomplete              | Last message received at the Fan In mediation primitive input terminal                          |
| Simple count/XPath                | No                                                        | Incomplete              | Message body empty; SMO headers and context are the same as the message received at the Fan Out |
| Simple count/XPath                | Yes (in terminal)                                         | Incomplete/Complete *   | Last message received at the Fan In mediation primitive input terminal                          |
| Simple count/XPath                | Yes (stop terminal)                                       | Incomplete              | Last message received at the Fan In mediation primitive input terminal                          |
| Iterate/Simple count/XPath        | Yes, timeout value expired and decision type not complete | Incomplete              | Last message received at the Fan In mediation primitive input terminal                          |
| Iterate/Simple count/XPath        | Yes, timeout value expired and decision type complete     | Complete                | Last message received at the Fan In mediation primitive input terminal                          |

- Aggregation patterns

This section explains aggregation patterns and how they are constructed.
- Error handling within an aggregation block

To handle an error condition within an aggregation block a Stop or Fail mediation primitive can be used. Alternatively, you can wire to the Stop input terminal of the Fan In mediation primitive.
- Asynchronous parallel processing

To reduce the overall processing time of an aggregation you can call multiple services concurrently, instead of processing each service in series.
- Performance considerations when using aggregation

When using aggregation, there are some performance considerations to be aware of.

<!-- image -->