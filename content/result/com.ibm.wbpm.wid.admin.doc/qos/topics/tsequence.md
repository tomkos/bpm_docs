<!-- image -->

# Processing events in a sequence

## About this task

Sometimes you need to ensure that the data is processed
in order. For example, you want to be sure that an employee record
is created before any update event for that employee record is processed.
Clients determine the sequence in which events are sent to a component,
but controlling the sequence in which clients contribute events to
a queue is not always enough. The event that would add a new employee
record might process slowly while an update event might go through
quickly. You can establish a qualifier for such events to ensure that
they will be processed in the order they are received.

When
a service receives events, those events join a queue. The events are scheduled
to be processed in the order they are received, but the runtime environment
is a multithread environment. Multiple processes serve the queue,
and each process can progress at a different speed, so the events
might be processed in an order different from that in which they were
delivered to the queue. There is a delay between the time that one
event is taken off the queue and the corresponding operation on the
service is invoked. In that window, the next event might be taken
off the queue and its corresponding operation might be invoked. Processing
delays could cause the second event to be processed before the first
event. When processing sequence is important, you can provide a means
to control it with the event sequencing qualifier.

Once
you have decided that you need event sequencing qualifiers for a component,
you need to plan how you want to use them. First, look at the operations
on the interfaces for the component. Identify the operations that
you want to include in the sequence. You might find that you need
two or more sequences because a component manipulates various kinds
of objects. For example, a general hotel component might have one
set of operations for booking hotel rooms and another set for booking
convention halls.

The group identifies which operations
will participate in a sequence. For example, put reserve\_hotel\_room
and clean\_hotel\_room in one group and put book\_convention\_hall and
set\_up\_convention\_hall in another group, assuming operations on hotel
rooms are completely independent from operations on convention halls.

The key identifies
the object being manipulated. The keys for the first set of operations
are the room numbers, such as 201 (second floor, room 01). The keys
for the second set of operations might be room names like "Main ball
room" and "West projection room." Once you have identified those properties,
you need to add an event sequencing qualifier on all the operations,
specifying that key. The instructions below explain how to carry out
these tasks.

An event sequencing qualifier causes a lock to
be acquired before the event is sent to the target component. When
the execution of the business logic completes, the lock is released.
Because one task must complete before the next task can begin, you
need to be careful where you apply this feature. Make sure that you
are not going to tie up an essential process for an unacceptable time
because you have applied sequencing to some situation where events
might take a long time to complete.

To establish a sequence
for events related to an operation, follow these steps:

## Procedure

1. In the module assembly diagram, select the component you
want to qualify. The component must have a WSDL interface;
you cannot set event sequencing qualifiers on a component with a Java™ interface.
2. In the Properties view, click the Details tab,
which shows the component's interfaces and references. If
you are trying to control the sequence relating to updating employee
records, you would choose the component that controls those updates
and establish a sequence based on employee identification, probably
a name or a number.
3. Expand the tree and select an operation of the component's
WSDL interface.
4. Click Qualifiers, click Add,
and select Event Sequencing from the list provided.
The event sequencing qualifier is added to the operation.
When you select that qualifier, you can see its properties in a subordinate
view.
5. Create or select a name for the group to which this operation
belongs. Events for all the operations in the same group
are considered together for sequencing. They are kept in a different
sequence from events for operations in other groups. Events in the
same group that have the same key value are guaranteed to be delivered
in the order that they arrive.
6. In the Properties of Qualifier Event sequencing view, click
in the table cell for Parameter name and select
the relevant parameter from the list provided. The parameters
are business objects or simple types.
7. Provide an XPath expression to identify the simple type
that will be used in the key. You can type an XPath expression in
the field provided, or you can select the table cell and click the
ellipsis (...) button to open the XPath Expression Builder wizard,
which will help you through the process. Just select a business object
attribute, and the wizard will construct the XPath expression for
you. Each row in the table contributes to the key. Each
XPath expression should evaluate to a simple type. The key value is
composed of one or more fields, which you have defined in the table.
Events from the same group with the same key value (for example, employee
number 1234 or room number 201) are processed in the order they are
received by the component.
8. If you want to add more parameters, click Add and
repeat steps 5 and 6. If there are two or more attributes
in the key, then their order is important. For example, suppose that
in the hotel example room numbers are represented as two fields, floor
number and number of the room on that floor. You have created a sequence
that allows you to lock a room in the event queue while it is being
renovated. Then, you need to assure that the qualifier that you defined
for renovate\_room and the one you defined for reserve\_room have the
fields for room and floor in the same order in the key definition
tables. Otherwise, the hotel staff could not reserve room 03 on floor
08 until the renovations were completed on room 08 on floor 03. If
the parameters in the table were reversed, renovate\_room would obtain
a lock for key value 0803 (room 8 on floor 3) but reserve\_room would
interpret that lock as applying to room 03 on floor 08. In this example,
the floor number field must always precede the room number field in
the keys table. You can use the arrow buttons in the view to change
the position of the selected field in the key.
9 Both processing errors or unavailable resources can causea sequenced event to fail. The way that any remaining events in thesequence are handled is determined by the Process requestswhen error encountered check box of the event sequencingqualifier. To control the processing of dependent events when a sequencedevent fails, complete one of the following steps: Note: You can use the failed event manager to quickly identifyfailed sequenced events and resubmit them for processing.
    - If you want the processing of event sequences to continue
regardless of whether any of the events fail, ensure that the Process
requests when error encountered check box is selected.
    - If you want to suspend the processing of dependent events
until the failure of a sequenced event is resolved, clear the Process
requests when error encountered check box.
10. Save your changes in the assembly editor. You
can change the parameter name or XPath expression at any time.