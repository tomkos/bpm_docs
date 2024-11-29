<!-- image -->

# Error handling in the mediation flow

- Fail terminal
- Runtime failure in a mediation
primitive
- Failure information in the message
- Stop mediation primitive
- Fail mediation primitive
- Example: Error handling mediation
flow
- Fault nodes for WSDL fault messages
- Unmodeled faults
- Error Flows

## Fail terminal

Mediation
primitives that process messages have a fail terminal, which propagates
exception information along with the input message when there is a
failure in the mediation primitive. The exception information is stored
in the failInfo element in the message context. You must wire the
fail terminal of a mediation primitive to another primitive in order
to access the failInfo. The fail terminal of a primitive only propagates
failure information for failure within the logic of that primitive,
and not for any downstream primitives.

If a primitive's fail
terminal is not wired, the failure information is not stored in the
failInfo element. In this case, the flow fails and only the exception
information is seen in the server output logs.

## Runtime failure in a mediation primitive

When
an execution failure occurs in a mediation primitive, the fail terminal
is fired. A runtime exception is thrown, and the flow is considered
to have failed. If the mediation flow component is running under a
global transaction, primitives that use resources and participate
in the global transaction can choose to rollback.

We will use
the example flow shown below to illustrate the rollback behavior when
the mediation flow component is running under a global transaction.

In
this flow assume that a global transaction is not configured, and
a failure occurs in the Custom primitive. As the fail terminal has
not been wired the flow fails. The work done by the Transform primitive
is ignored as it does not persist information and does not interact
with a resource external to the flow. The Log however, would still
complete as the mediation flow component is not under a global transaction
and therefore still logs to the database. This is because it interacts
with an external resource.

In the same flow, if a global transaction
is configured and a failure occurs again in the Custom primitive then
the work done by the Transform primitive is ignored again. However,
if the Log primitive has its transaction mode property set to same,
the transaction will be rolled back and no entry will occur in the
database. If the transaction mode property was set to new ,
then the transaction commits outside the global transaction so an
entry will still occur in the database.

By default, a mediation
flow component is not set with a global transaction qualifier. You
can add a qualifier to run the mediation flow component under a global
transaction. This is done by setting a qualifier on the mediation
flow component in the assembly editor; in the implementation page
of the properties view, add a Transaction qualifier with a property
of global.

## Failure information in the message

When
there is a failure in a mediation primitive, the exception information
is stored in the failInfo element of the message context. Here is
an image of a message in the XPath Expression Builder, showing the
failnfo:

<!-- image -->

## Stop mediation primitive

The Stop
primitive has one input terminal and no output terminals. When a mediation
primitive's fail or output terminal is wired to the Stop primitive,
messages that go to that terminal are consumed by the Stop primitive,
and that particular flow path is terminated.

The mediation
flow editor generates warnings if a mediation primitive's output terminal
is not wired. Use the Stop terminal to suppress these warnings.  In
the runtime, output terminals that are not wired are automatically
propagated to Stop.

In the following example, the fail terminal
of the Message Filter primitive is wired to a Message Logger in order
to store the failed message. To indicate that no more actions are
needed, the Message Logger is wired to a Stop primitive.

<!-- image -->

## Fail mediation primitive

Use
the Fail primitive if you want to stop the flow and throw an exception.
You can wire a primitive's output or fail terminal to the Fail primitive.
If the mediation flow component is running under a global transaction,
primitives that use resources and participate in the global transaction
can choose to rollback.

## Example: Error handling mediation flow

You
can create special mediation flows for handling errors, and call these
flows from another mediation flow. For example, suppose you have a
mediation module called ErrorFlowModule that has a mediation flow
component called ErrorFlow and an export called ErrorFlowExport. In
the mediation flow component, you could have a Message Filter primitive
that has a number of error codes defined as patterns that are associated
to terminals. Depending on the error code, the message is routed to
a different path in the flow.

In your mediation module called
CreditCheckModule, create an import with SCA binding called ErrorFlow
that has the same interface as the export of mediation module ErrorFlowModule.
In the details page of the property view of the import, select the
import interface, right click and select Wire (Advanced) .
Select ErrorFlowModule and ErrorFlowExport as targets of this import.

In
the mediation flow component CreditCheck, you have a Message Filter
that sends its output message to the getAmount operation of the CreditLimitService
interface. The fail terminal of the Message Filter is wired to a Mapping
Primitive and then propagated to the ErrorFlowModule via the ErrorFlow
import interface.

The following image shows the CreditCheck
mediation flow component's request flow:

## Fault nodes for WSDL fault messages

WSDL
operations have three types of messages - input, output, and fault.
WSDL faults are business error conditions (for example. StockSymbolNotFound,
or NoSuchUser) that are defined in a WSDL operation.  In the mediation
flow diagram, WSDL faults are handled through input fault and callout
fault nodes, which have a terminal for each unique fault message type.
The input and callout fault nodes are created in the mediation flow
editor when there is a WSDL fault defined in the source or target
operation:

- An input fault node is created when a source operation has a WSDL
fault message defined. The input fault node has an input terminal
for each fault message type defined in the source operation. Any message
propagated to an input fault node will result in a WSDL fault error
message being returned from the source operation. Wiring to this node
means that the fault message is returned to the client. The input
fault node is created in the request and response and error flows.
- A callout fault node is created in the response flow for each
target operation that has a WSDL fault message defined. The callout
fault node has an output terminal for each fault message type defined
in the target operation. When a WSDL fault occurs, the callout fault
node propagates the message to the primitive or node to which it is
wired. Wiring from a callout node's output terminal identifies the
flow that will take effect when the call to that operation results
in that particular fault.

Let's use an example to illustrate how fault nodes are
wired. Assume that you have a source interface StockQuoteService with
an operation getQuote that requests a stock quote from a service provider's
DelayedServicePortType interface.

- The StockQuoteService interface has an operation getQuote which
has inputs named customerID and symbol, an output named value, and
two faults; invalidCustomerID, and invalidSymbol.
- The DelayedServicePortType interface has an operation getQuote
which has an input named stockSymbol, an output named stockValue,
and a fault named invalidSymbol.

<!-- image -->

In the response flow, you
could wire the callout fault node's invalid symbol terminal to the
input fault node's invalid symbol terminal, with a Mapping  Transformation
primitive in between. The following image shows the response flow:

If a fault is not wired, the behavior at run time will
be the same as if the fault were wired to the input response node.

## Unmodeled faults

Those errors
that are returned by a WSDL operation and are not defined as WSDL
faults are called unmodeled faults. There is no input or callout fault
node created for these types of faults in the mediation flow editor.
In this case, the input message type is propagated to the callout
response node's fail terminal. The failure information is captured
in the failinfo element of the message context.

To handle an
unmodeled fault, you can wire the fail terminal of a callout response
node to a mediation primitive. For example, you could wire the callout
response node's fail terminal to a message logger mediation primitive
to log all unmodeled faults. You can set a property on the callout
response node to determine whether the entire request message or just
the message header information should be logged.

If a fail
terminal is not wired and an unmodeled fault is received, a mediation
runtime exception will occur.

## Error Flows

A mediation
flow has an error flow for each source operation. The error flow acts
a catch all for unhandled errors.

- An error input node which has a catchAll terminal set to anyType.
the error input node receives the service message object that contains
the error information.
- An input response node for request response operations. You can
use this node to return the error message to the source operation.
- An input fault node is created when a source operation has a WSDL
fault message defined. The input fault node has an input terminal
for each fault message type defined in the source operation. Any message
propagated to an input fault node will result in a WSDL fault error
message being returned from the source operation. Wiring to this node
means that the fault message is returned to the client.

<!-- image -->

<!-- image -->