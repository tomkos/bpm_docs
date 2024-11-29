# Process components and monitoring events

All events
contain information about their origin, or emission point. Using this information, which is grouped
in the event point data section of the event, the step, the execution, the process, and the server
where the event originated are determined. In addition, many events have an application data
section, which contains custom business data. For auto-tracking events, the application data section
contains the parameters and variables that you designated for auto-tracking in the process
definition. For user-defined custom tracking events, the application data section contains the
fields defined in the custom tracking group to which that event belongs. Custom tracking groups are
data structures defined in a process application specifically for tracking purposes.

- Process execution monitoring events
- Activity monitoring events
- Event monitoring events
- Gateway events

## Process execution monitoring events

| Process state                    | Process icon   | Emitted monitoring event   |
|----------------------------------|----------------|----------------------------|
| The process is started.          |                | bpmnx:PROCESS\_STARTED      |
| The process is completed.        |                | bpmnx:PROCESS\_COMPLETED    |
| The process has been terminated. |                | bpmnx:PROCESS\_TERMINATED   |
| The process has been deleted.    |                | bpmnx:PROCESS\_DELETED      |
| The process has failed.          |                | bpmnx:PROCESS\_FAILED       |

## Activity monitoring events

| Activity state                                                                                       | Activity icon   | Emitted monitoring event         |
|------------------------------------------------------------------------------------------------------|-----------------|----------------------------------|
| An activity is ready.                                                                                |                 | bpmnx:ACTIVITY\_READY             |
| An activity is active.                                                                               |                 | bpmnx:ACTIVITY\_ACTIVE            |
| An activity is completed; the activity work has finished, but some finalization is still completing. |                 | bpmnx:ACTIVITY\_COMPLETED         |
| An activity is terminated.                                                                           |                 | bpmnx:ACTIVITY\_TERMINATED        |
| A resource, such as a user, group or organization, is associated with an activity.                   |                 | bpmnx:ACTIVITY\_RESOURCE\_ASSIGNED |

You can configure activities for simple or multi-instance loops in a business process
definition. Loops allow an action to be repeated a specified number of times, or until a specific
condition is false. In a process definition, simple or multi-instance loop activities are identified
by an indicator in the activity icon. Activities configured for loops emit the following events to
report the loop control behavior. These events are reported in addition to the usual activity
events, listed in the previous table, which occur for every repeated execution. An
ACTIVITY\_TERMINATED event is emitted when a looped activity cancels the remaining action instances
because a complex flow condition is met.

| Type of looped activity                                                      | Looped activity icon   | Emitted monitoring event                                               |
|------------------------------------------------------------------------------|------------------------|------------------------------------------------------------------------|
| Activity with simple loops; activity with sequential multiple-instance loops |                        | bpmnx:ACTIVITY\_LOOP\_CONDITION\_TRUE bpmnx:ACTIVITY\_LOOP\_CONDITION\_FALSE |
| Activity with parallel multiple-instance loops                               |                        | bpmnx:ACTIVITY\_PARALLEL\_INSTANCES\_STARTED bpmnx:ACTIVITY\_TERMINATED    |

## Event monitoring events

You can model catching
or throwing events in a process definition. These events are part of the process logic and must not
be confused with the monitoring events shown in the following table. Events can appear at the
beginning of a process or subprocess, end of a process, or during a process or subprocess.

| Event in the process definition                       | Process definition icon   | Emitted monitoring event               |
|-------------------------------------------------------|---------------------------|----------------------------------------|
| None start event                                      |                           | bpmnx:EVENT\_CAUGHT                     |
| Message start event                                   |                           | bpmnx:EVENT\_CAUGHT                     |
| Ad hoc start event                                    |                           | bpmnx:EVENT\_CAUGHT                     |
| Event subprocess interrupting message start event     |                           | bpmnx:EVENT\_CAUGHT                     |
| Event subprocess interrupting timer start event       |                           | bpmnx:EVENT\_CAUGHT                     |
| Event subprocess interrupting error start event       |                           | bpmnx:EVENT\_CAUGHT                     |
| Event subprocess non-interrupting message start event |                           | bpmnx:EVENT\_CAUGHT                     |
| Event subprocess non-interrupting timer start event   |                           | bpmnx:EVENT\_CAUGHT                     |
| Catching message intermediate event                   |                           | bpmnx:EVENT\_EXPECTEDbpmnx:EVENT\_CAUGHT |
| Catching timer intermediate event                     |                           | bpmnx:EVENT\_EXPECTEDbpmnx:EVENT\_CAUGHT |
| Boundary interrupting message intermediate event      |                           | bpmnx:EVENT\_CAUGHT                     |
| Boundary interrupting timer intermediate event        |                           | bpmnx:EVENT\_CAUGHT                     |
| Boundary interrupting error intermediate event        |                           | bpmnx:EVENT\_CAUGHT                     |
| Boundary non-interrupting message intermediate event  |                           | bpmnx:EVENT\_CAUGHT                     |
| Boundary non-interrupting timer intermediate event    |                           | bpmnx:EVENT\_CAUGHT                     |
| Send message intermediate event                       |                           | bpmnx:EVENT\_THROWN                     |
| Tracking intermediate event                           |                           | bpmnx:EVENT\_THROWN                     |
| None end event                                        |                           | bpmnx:EVENT\_THROWN                     |
| Message end event                                     |                           | bpmnx:EVENT\_THROWN                     |
| Error end event                                       |                           | bpmnx:EVENT\_THROWN                     |
| Terminate event                                       |                           | bpmnx:EVENT\_THROWN                     |

## Gateway events

| Type of gateway     | Gateway icon   | Emitted monitoring event                       |
|---------------------|----------------|------------------------------------------------|
| Exclusive gateway   |                | bpmnx:GATEWAY\_ACTIVATEDbpmnx:GATEWAY\_COMPLETED |
| Inclusive gateway   |                | bpmnx:GATEWAY\_ACTIVATEDbpmnx:GATEWAY\_COMPLETED |
| Parallel gateway    |                | bpmnx:GATEWAY\_ACTIVATEDbpmnx:GATEWAY\_COMPLETED |
| Event-based gateway |                | bpmnx:GATEWAY\_ACTIVATEDbpmnx:GATEWAY\_COMPLETED |