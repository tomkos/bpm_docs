<!-- image -->

# Tips for creating Custom mediation primitives

Consider these tips when creating your custom mediation primitive.

## Ready-made visual snippets

<!-- image -->

## Specify the message type in the Properties view

For
most mediation primitives, the mediation flow editor detects the message
types and only allows you to wire primitives that have compatible
message types. However for custom mediation primitives, the message
type is unknown to the editor. Before you wire your custom mediation
primitive, specify its message type in the Terminals tab of the Properties
view to ensure that the primitive can be wired only to primitives
of a compatible type:

To specify the message
type in the Terminals tab view, select the terminal, and click Change,
as shown below: .