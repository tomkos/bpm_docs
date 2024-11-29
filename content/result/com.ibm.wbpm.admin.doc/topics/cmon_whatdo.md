# What do you monitor?

Regardless of the type of monitoring you intend to perform
on your
service components (problem determination, performance tuning, or
process monitoring), you monitor a certain point that is reached during
processing.
 This point is referred to as an event point, and it
is these points that you select to be monitored. Each event point
encapsulates the service component kind tag, an optional element kind
(which are specific functions of a service component type), and the nature of
the event. All these factors determine the type of event generated
by monitoring.

Event natures describe the situations required
to generate events
during the processing of service components. These natures are key
points in the logic structure of a service component that you select
to be monitored. The most common natures for service component events
are ENTRY, EXIT, and FAILURE, but there are many other natures depending
on the particular component and element. Whenever an application containing
the specified service component is later invoked, an event is fired
every time the processing of a service component crosses the points
corresponding to the event nature.

As an example of how events
are defined for a service component
kind, the MAP service component kind can directly fire events with
natures of ENTRY, EXIT, and FAILURE. It also includes an element kind,
called Transformation, which defines a specific type of functionality
within the MAP component kind. This element also fires events with
ENTRY, EXIT, and FAILURE natures. Consequently, the MAP service component
kind can fire up to six different events depending on the combination
of elements and natures that you specify. The list of all service
components, their elements, and their event natures is contained in
the event catalog.

Monitoring is a separate layer of functionality
that lies atop
the processing of your applications, and does not interfere with the
processing of your service components.  Monitoring is concerned with
service component processing only insofar as it detects activity at
a specified event point. When activity is detected, an event is fired
by monitoring, which determines where the event is sent, and what
data is contained in that event, based on the type of monitoring you
are performing:

- A counter for each EXIT event nature - counts successful computations.
- A counter for each FAILURE event nature - counts failed computations
- The processing duration calculated between corresponding ENTRY
and EXIT events (synchronous computations only).