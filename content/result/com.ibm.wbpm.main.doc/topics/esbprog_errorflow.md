<!-- image -->

# Error flow

- An Error Input node, which has a catchAll terminal, with the type set to anyType. The Error
Input node propagates the Service Message Object (SMO) from the unwired terminal, that contains the
error information.
- An Input Response node for (request and response) operations. You can use this node to return a
message from the source operation.
- An Input Fault node, created when a source operation has a WSDL fault message defined. The Input
Fault node has an input terminal for each fault message type that is defined in the source
operation. Any message that is sent to an Input Fault node results in a WSDL fault error message
being returned from the source operation.

You can use an error flow to audit any unhandled errors that may occur in the operation request
or response flows. For example, you can use a Message Logger mediation primitive to capture the SMO,
and then wire the Log mediation primitive to a Fail primitive.

Figure 1. An example error flow to return a modelled fault

<!-- image -->