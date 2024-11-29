# Adding events to a BPD (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

An example of an event is a message received from an external
system. You can specify the trigger type of an event and represent
the event with a meaningful icon in your process diagram.

Events
in Business Automation Workflow can
be triggered by the passing of a due date, an exception, or the arrival
of a message. The trigger determines the type of event that you choose
to implement. For information about available event types and their
triggers, see Modeling events.

You can
attach intermediate events (timer, message, and error events) to activities
in your business process definitions (BPDs) to create boundary events
or you can include intermediate events in the process flow by using
sequence lines. Other events must be part of the process flow.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application that contains a BPD.
3. In the Designer view, click the Diagram tab.
4. Drag the event from the palette. If you want
to create a boundary event by attaching an intermediate event to an
activity, drop the event onto the activity node. To verify the attachment,
select the activity. If the outline of the activity includes the event,
the event is attached. By default, attached intermediate events are Error events.
5. Select the event. In the event properties, click the Implementation option.
6. Select the type of event from the available options.
7. For attached intermediate events, select Interrupt
activity if you want the activity to close when the message
is received.
8. In the Trigger section,
you can select or create an undercover agent (UCA) to attach to the
event. See the topic in the related tasks section. Each
event must be associated with a UCA. When you run the process, the
associated UCA carries out the required action when the event is triggered.