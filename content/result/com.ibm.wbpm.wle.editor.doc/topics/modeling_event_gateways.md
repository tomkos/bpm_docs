# Modeling event gateways

## About this task

An event gateway represents a branching point in a process execution where only one of several
paths can be followed, depending on events that occur. A specific event, such as the receipt of a
message or timer event, determines the path that will be taken. The event gateway represents a
single point of behavior that is spread out across multiple process components connected by sequence
flow. The following types of events can directly follow an event gateway (connected by a single
sequence flow):

- Intermediate message event (receiving)
- Intermediate timer event

When creating an event gateway, you must connect at least two intermediate events to the gateway.
And, when connected to an event gateway, an intermediate event is not allowed to have additional
incoming sequence flow.

## Procedure

1. Open a process and add an event gateway to the process diagram.
2. Add any additional events required by the gateway configuration by dragging them from the
palette. Only intermediate message events and intermediate timer events are allowed. The minimum
number of events is two, and you can add as many as you require.
3 Click one of the connected events and then select theGeneral tab in the properties.
    1. To configure an intermediate message event, follow the steps in Using intermediate and boundary message events to receive messages.
    2. To configure an intermediate timer event, follow the steps in Modeling delays, escalations, and timeouts.
4. Click Save or Finish Editing.