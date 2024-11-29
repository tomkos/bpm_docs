# Modeling event subprocesses

## About this task

The event subprocess is a specialized subprocess that you can use to model event-handling logic
for a process or subprocess. It is triggered upon occurrence of a configured start event, and as a
result it is not connected to other steps through sequence flow. It has access to the business
objects (variables) of its parent process and so can encapsulate steps that use those variables.
When triggered, an event subprocess can either interrupt the execution of its parent or it can run
in parallel.

You can use event subprocesses to handle exceptional process flows within your process. For
example, an event subprocess can be used to handle an out-of-stock situation that arises during an
order-fulfilment process. The out-of-stock event in the parent process triggers the start event in
the event subprocess, which contains activities to order more stock or to check supplies at other
locations.

| Start event implementation type   | Event subprocess visualization   |
|-----------------------------------|----------------------------------|
| Error                             |                                  |
| UCA Message                       |                                  |
| SCA Message                       |                                  |
| ECM Content                       |                                  |
| Timer                             |                                  |

- Message event subprocesses are triggered by a message event that often originates from outside
the process in which the event subprocess is contained. A message start event might be used in a
situation similar to the situation described previously, where a message, such as an out-of-stock
message, is received by the event subprocess and triggers a sequence of activities.
- A timer start event might be used to model the steps to take when an activity within the parent
process is not completed after a specified amount of time. For example if a requested item cannot be
located within a certain amount of time, the out-of-stock subprocess can be triggered by a timer
start event.
- An error start event might be triggered when something goes wrong in the process, for example,
the order fulfilment system is non-responsive. Error start events can be triggered only from within
the parent process or its subprocesses.

A parent process cannot complete until all active event subprocesses are complete, unless the
parent is terminated by a terminate end event. A terminate end event in an event subprocess
terminates only the activities that are contained within that event subprocess.

Boundary events cannot be attached to event subprocesses. To handle exceptions within an event
subprocess, for example, errors that arise during the event subprocess execution, event subprocesses
can themselves contain event subprocesses.

To add an event subprocess to your process:

## Procedure

1. Open the parent process in the designer.
2. Drag an event subprocess from the palette onto the diagram area. By default, new event
subprocesses are assigned an error start event.
3. To change the start event type and properties and to add activities to the event
subprocess, double-click the event subprocess activity to expand it.
4. Select the start event and, from the General tab in the
properties view, select a new implementation type from the list.
5. The start events for event subprocesses can be interrupting or non-interrupting. When
triggered, event subprocesses with an interrupting start event terminate all activities in the
parent process. Activities in an event subprocess with a non-interrupting start event run in
parallel with the parent process. You can specify whether the start event of the event subprocess is
interrupting or non-interrupting by selecting or by clearing Interrupt Parent
Process. 

Note: Error start events in an event subprocess always interrupt the parent process and cannot be
set to non-interrupting.
6. To configure an event subprocess to be repeatable, select
Repeatable on the General tab. When you
select this property, the event subprocess might run several times during the execution of a
process, and might have multiple instances that run in parallel. 
Note: Unlike subprocesses, looping behavior is not supported for event subprocesses.
7. Drag elements from the palette onto the canvas. The names of the activities
that you create in your subprocess must be different from the names of the activities in the
top-level process or any other subprocess or event subprocess under the same top-level
process.
Any swimlanes or phases that you add to your subprocess are independent from the swimlanes and
phases that are contained in the parent process.
8. Like subprocesses, event subprocesses have access to the data of the parent process. Data
mapping is not required to pass data into or out of the event subprocess. You can also declare
private variables within the event subprocess itself, which are not visible to the parent process.
See Modeling subprocess data.
9. Click Save or Finish Editing.

## What to do next