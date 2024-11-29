# Sending messages to undercover agents

To send a message to an undercover agent (UCA) during the execution of a service flow or
heritage human service, you can add an intermediate message event to the service flow
diagram.

You can include one or more send message events that have incoming and outgoing connections in
the service flow. When you add message events to a process or service flow, you should be aware of
the general information in Modeling message events that applies to all types of
message events.

## Procedure

1. Open the designer.
2. Create or open a service flow or heritage human service and drag an intermediate event of
Message (sending) type () from the palette onto the diagram.
3. Edit the default name of the message event as required.
4. Connect the message event in the diagram as needed, and then select the event node.
5. In the Properties view, click Implementation.
Under Intermediate Event Type, ensure that
the implementation type is set to Message (sending).
6. Attach the UCA to the send message event: under Event Properties,
click Select next to Attached message UCA to select an
existing UCA.  See Attaching the undercover agent to the message event.
7. Set the target for the message event: select Target
current snapshot to ensure that the incoming message event
is received only by a process that is in the same process application
snapshot as this event. By default, incoming message events
are received by all snapshots in all process applications that refer
to the UCA (and that have event message properties that match the
correlation values). If this service flow is in a toolkit, the snapshot
of the root process application is used. See Setting the target for a UCA message event.
8. Click Save or Finish Editing.