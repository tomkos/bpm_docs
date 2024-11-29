# Adding a message event to a BPD

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application in the Designer view.
3. Create a simple BPD that contains two activities. (If
you need detailed instructions, see Creating a business process definition (BPD) .)
4. Drag an Intermediate Event component from the palette onto
the BPD diagram so that it falls between the two activities.
5. In the text box that displays over the event, type a name
for the event. For this sample, you can type: Incoming Message
Event.
6. Click the Implementation tab in the properties. The default
implementation for intermediate events that are included in the process
flow is Message.
7. If not already selected, click the drop-down list and choose Receiving from
the available message types.
8. Use the Sequence Flow tool to connect the BPD components
as shown in the following example:
9. Save your work.