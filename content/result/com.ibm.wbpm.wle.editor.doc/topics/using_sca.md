<!-- image -->

# Using Service Component Architecture to interact with processes

There are several ways to start and interact
with process instances using Service Component Architecture (SCA).
You can use receiving message events to create or interact with process
instances.

To interact with receiving message events, you can
use SCA as the triggering mechanism as an alternative to using undercover
agents (UCA). A receiving message event can be a start message event,
intermediate message event, boundary message event, or the start event
of an event subprocess.

The use of SCA as the triggering mechanism
makes it possible to use instance-based correlation that always delivers
the message to exactly one event of one instance. By contrast, correlation
that is supported by undercover agent invocations permits multiple
instances and events (of the same or different models) to receive
the same message.

## Supported interaction patterns that use receiving
message events

## Supported interaction patterns that use input and
output variables

## Instance-based correlation

If a request message must be received by an existing instance of a process, you must specify a
correlation variable to identify the intended instance that receives the message.

If a message is posted
before the a suitable message receive event is in a waiting state,
the message is stored. The message will be received by the first matching
message receive event that goes into the waiting state.

To avoid the
arbitrary selection, when you model a process in IBM Process
Designer that
invokes a subprocess by using a Linked Process activity, mark the
Linked Process activity as Run Sequential instead
of Run in Parallel.

## Defining a service that can trigger different events
in a process

In general, when receiving message events are
used with SCA, the corresponding service interfaces of the process
are derived from the message event's service identifier and message
object type.

- If a process instance matches the instance identifier value inthe message, then the following rules are applied:
    - If the instance has exactly one matching event (intermediate,
boundary, or a start event for an event subprocess) that is in the
waiting state, the matching event receives the message.
    - If the instance has multiple matching events that are in the waiting
state, one of them is selected arbitrarily to receive the message.
    - If the instance does not have any matching event in the waiting
state, the message is stored until an event that can receive the message
becomes active.
- If no process instance matches the instance identifier value in
the message and there is a start process message event that matches
the message type, a new instance of the process is created, and the
start message event receives the message.

## Rules for instance migration

To allow instance migration of processes that contain SCA message events and variables that are
marked as process instance identifiers, you must conform to the rules for what cannot be changed or
deleted when you create a new version of a process that is already deployed. The rules are described in Development strategies for migrating instances.

## Task overview

1 Using Process Designer :Youcan either use the implicitly provided services of the process, oruse the services that are provided for a receiving message event inwhich SCA is specified as the triggering mechanism. For the formeryou do not have to do anything, for the latter you must specify thecorresponding receiving message events.

You
can either use the implicitly provided services of the process, or
use the services that are provided for a receiving message event in
which SCA is specified as the triggering mechanism. For the former
you do not have to do anything, for the latter you must specify the
corresponding receiving message events.

    1. If SCA messages interact with existing process instances, use
instance-based correlation for the message event subprocess, intermediate
receiving message events, or boundary message events. For that, you
must mark one or more of the process variables as process instance
identifiers. See Declaring variables for a process or service.
    2. Ensure that the process variable that identifies a process instance
is assigned a suitable value. The value must be assigned before any
SCA message can arrive for the instance.
    3. Optional: Add a start message event to your process. See Using start message events.
    4 If you want message event subprocesses or receiving message eventsin a process to be able to receive SCA messages:
        1. Add intermediate receiving message events and boundary message
events as necessary. See Using intermediate and boundary message events to receive messages.
        2. Add a message event subprocess, with a corresponding start message
event where required. See Using start message events.
        3. For each receiving message event, as a part of the data mapping,
select the variable that uniquely identifies each process instance.
See Mapping input and output data for an activity or step.
2 Switch to using Integration Designer , and completethe following actions:

1. Drag the process onto the design canvas, and select which interfaces
to include in the SCA import. See Creating an import to start a business process definition.
2. In the assembly editor, you can use the SCA import to invoke and
communicate with a process instance using SCA messages.