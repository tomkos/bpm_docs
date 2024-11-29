# Setting the target for a UCA message
event

You can include an intermediate message event in your process or BPD when
you want to model a message event that is sent or received while a process is running, or you can
use a start event to receive a message event or use an end event to send a message event.

The default behavior for intermediate incoming message events is
that they are received by all snapshots in all process applications
that refer to the undercover agent and that have event message properties
that match the correlation values.

For start message events, the default behavior is that they are used on the tip
in Workflow Center and in the
default snapshot on the workflow server.

You can change the default behavior when you are configuring the undercover agent for a message
event in your process or service flow, by clicking the Target current
snapshot
check box in the Event Properties section. If you select the
check box, at run time start message events are targeted in the same snapshot of the process
application that contains the process, BPD, or service that sends the message event. If the process,
BPD, or service of the sending message event is in a toolkit, the snapshot of the process
application (which is the root container) is used.

When the check box is selected, you are limiting the responding listener to the start message
event and to the intermediate incoming message events in that specific process
application snapshot.