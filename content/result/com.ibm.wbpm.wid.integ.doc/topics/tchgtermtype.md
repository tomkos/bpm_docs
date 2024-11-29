<!-- image -->

# Changing the message type of a mediation primitive terminal

## Before you begin

## About this task

## Procedure

1. Hover over the terminal to view its type.
2. Right click the terminal and select Change Message
Type .
3 The Change Message Type window appears, showingthe current message type of the terminal.

<!-- image -->

    - Automatically determined message type When you drop a primitive onto the editor, the terminals have
no message type, and this is the default method of determining the
terminal type. When the terminal is wired, its message type is deduced
by the mediation flow editor. Typically, it takes on the type of the
terminal to which it is wired.
    - Any message typeYou can change a
terminal type to Any message type, which means
that the terminal will accept all messages regardless of the type.
This is useful in a generic error message flow, for example you can
wire a number of fail primitives to a Fail primitive or a Message
Logger that has an input terminal of Any message type. 
You
can cast the any type to a concrete type later in the flow by using
a Set Message Type or Type Filter mediation primitive. Note: In this
case, Any refers to any wsdl message, not to xsd:any
    - Specific message typeYou can choose
a specific message type from the list of available types.

## Results

## Example

<!-- image -->