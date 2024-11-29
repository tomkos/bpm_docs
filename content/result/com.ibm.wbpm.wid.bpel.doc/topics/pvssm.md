<!-- image -->

# Choosing between a BPEL process editor and a business state
machine editor

You can use either the process editor or the business state machine
editor to compose business logic applications, but they use web services
differently. Although both editors model a programming language in
which individual nodes run in a specific order, in business processes,
the services run from the nodes themselves; in business state machines,
the services run either when entering, exiting, or moving between
nodes.

## BPEL processes

In a BPEL process, the nodes
are called activities.  There are a small number of incoming
events and they arrive in a predictable order.  In the following example,
a request is passed to the process, the process calls out to another
service, waits for a response, and then sends a response back to the
caller.  Scattered throughout the process are a few activities that
use web services to calculate some data.

<!-- image -->

## Business state machines

In a business state
machine, the nodes are called states, and they tend to be organized
in a "spaghetti-like" manner.  As control moves from one state to
another in the diagram, web services are invoked automatically when
they enter, exit, or move between states. When a service is in a particular
state, processing stops and waits for an appropriate incoming event.
Events typically arrive in larger numbers, and in an unpredictable
order. In the following example, a request is passed to the business
state machine, it does something, and then it waits for another request.
 The run path in a business state machine is not necessarily a direct
one, and the business logic can cycle back on itself.

<!-- image -->

## In conclusion

Think of a BPEL process as
a series of sequential actions, and the business state machine as
a series of loosely related stages that are acted upon. If your application
is very linear, then use a BPEL process; if it is primarily event-driven
or contains cyclical patterns, then use a business state machine.
Both editors, and the languages they model, are equally valid, and
it is up to you to determine which one best suits your application
design.