<!-- image -->

# Implementing a mediation flow

## About this task

## Procedure

1. If the mediation flow does not have a source interface,
click Add interface to add an interface.
2. Click an operation in the source interface to open the
request flow. A request flow begins with an input node
on the left, which represents the source operation. The flow proceeds
sequentially from left to right.
3 Next, determine the end point for the flow.
    1. If you want to invoke a target operation at the end
of the request flow, and process the returning message in a response
flow, drop a Callout from the palette onto the request flow, and select
a reference and operation from the list that is presented. A
Callout appears on the canvas and a response node is created. The
message sent by the target operation will be returned to the response
flow.
    2. If you want to invoke a target operation from within
the request flow, drop a Service Invoke primitive from the palette
onto the request flow, and select a reference and operation from the
list that is presented.  No response node is created. The
message sent by the target operation will be returned to the request
flow.
    3. If you want to return the message to the source after
processing, right click the canvas and select Show Input
Response. An Input Response is created in the
request flow.
4. Drop mediation primitives from the palette onto the editor
from left to right in the sequence that you want them to be invoked
in the flow, between the input and callout or input response nodes.
5. Wire the primitives together.
6. Set the properties of each primitive to determine how the
primitive will process the message. To edit a property, right click
a primitive or node and select Show in Properties.
7. If you used a callout, click the Response flow tab
at the top of the editor. The Callout Response is the entry point
of the response flow, and the Input Response returns the message to
the source.
8. Build a response flow in the same manner as you built the
request flow.
9. Build an error flow to capture unhandled exceptions. You
can either use mediation primitives such as Message Logger or you
can define your error handling logic in a reusable subflow. If you
want to return the error information to the source, wire the Input
Response at the end of the error flow.

## Example

If you have WSDL faults
defined in your operation, fault nodes will be created in the request
and response flow. You can wire these nodes to create an error handling
path in the flow.