<!-- image -->

# Using event handlers

In the Graphical User Interface environment, events usually signify
that the user has made a demand on the system, and the application
must respond to it appropriately. In such cases, a receive or pick
activity can usually be used, but they have limitations. For example,
they can only be used when a process is functioning normally, and
they can only be implemented once. This effectively means that you
have to know ahead of time how many events to expect, and when to
expect them.

Event handlers make a BPEL process more dynamic by dealing with
events that happen independently of, or asynchronously to the processing
of the application. They can respond to events that happen at any
time during an application's lifetime, or as many times as those events
repeat.

## Configuring an event handler

You can define
and configure an event handler either on individual scopes within
the process, or for the whole process in its entirety.

1. Hover either over a scope activity or the green start node that
represents the process a whole until the action bar appears as shown
in this screen cap.
2. Click the Add event handler icon. An event
handler will appear that is populated with an OnEvent element as shown here:

| Element         | Icon   | Description                                                                                                                                                                                                                                                                                                                                                           |
|-----------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OnEvent element |        | Use this element to create a control path and specify the operation that will cause this path to be followed.                                                                                                                                                                                                                                                         |
| Timeout element |        | Use this element to create a control path that is followed when a specified time has either been reached or has elapsed. This element is used on a single path, and is configured to specify either a specific date, or period of time. When the process is running, this path is chosen when no input is received within this time period, or by the specified date. |

## Lifecycle of an event handler

Each event
handler is enabled when the process or scope it is associated with
starts. Each event handler is disabled when the process or scope it
is associated with ends. Multiple instances of each event handler
can be started as long as the event handler is enabled. If instances
of event handlers are still running when a scope ends, then they are
allowed to complete.

It is important to distinguish between
enablement and dispatching. An event handler is said to be enabled
once the associated scope starts.  An onEvent event handler instance
is said to be dispatched when the event handler is enabled, and the
associated operation is invoked on the process.  Similarly, an onAlarm
event handler instance is dispatched when the event handler is enabled,
and the specified timeout is reached.

## Fault handling

Event handlers are considered
a part of the normal processing of a scope. Faults within event handlers
are treated like faults in the associated scope. If a fault occurs
within a scope (or in an event handler associated with the scope)
the fault handler disables all event handlers associated with the
scope and then implicitly terminates all activities directly enclosed
within the scope that are currently active. This includes the activities
within currently active event handlers.

## Concurrency

Multiple onEvent and timeout
events can occur concurrently and they are treated as concurrent activities.
An event handler is permitted to have several simultaneously active
instances. A private copy of all process data and control behavior
defined within an event handler is provided to each instance of an
event handler.

## Restrictions

Business Process Choreographer
is even more restrictive in its concurrency requirements. Because
it cannot distinguish incoming messages based on correlation sets
or partner links,  Business Process Choreographer does not allow more
than one receive or pick activity to be active with the same port
type and operation in a given process instance.

- A receive or pick activity with a certain port type and operation
is activated while another pick or receive activity with the same
port type and operation is already waiting
- An event handler with a certain port type and operation is enabled
and then a receive or pick activity with the same port type and operation
is activated
- A receive or pick activity with a certain port type and operation
is waiting and then an event handler with the same port type and operation
is enabled.

Business Process Choreographer only allows one concurrently active
request-response operation per process instance, port type, and operation.
The effect of this is that if an event handler implements a request-response
operation, then only one instance of such an event handler may be
active at any point in time.

<!-- image -->

This sample BPEL process is for
a job posting on an internet bulletin board.

The process begins
when input is received that specifies a job description and the number
of days that the offering should appear on the board. Then, a snippet
activity post the information live, and a reply activity returns a
posting number to the partner who initiated the process instance.
At this point, the process enters a scope activity with a nested wait
activity within it. The wait activity will keep the process instance
active for the required number of days, and wait for input. The input
is governed by an event handler that is set on the scope activity.
The event handler has two control paths in it. The first begins with
an OnEvent element, and is followed when an external user applies
for the job. Activities on this path will then add the application
to the list, and return a confirmation message to the user. The second
control path begins with a timeout activity, and is set to deliver
a daily report on the number of applications that have been received.

When the posting period expires, the wait activity resumes the
BPEL process. At this point, a snippet activity deletes the job posting,
and a complete list of all applications is sent to the human resources
department.

## Related concepts

- Replacement variables and context variables
- Using Java methods in process snippets
- Using custom properties for human tasks

## Related tasks

- Modifying the properties of an activity
- Modifying the type of an activity
- Working with basic activities
- Working with structured activities
- Modeling human workflows