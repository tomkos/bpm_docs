<!-- image -->

# Business graph use models

Delta support is the capability enabled by the SDO 1.0, where changes to a business object
graph are captured in a special header called the change summary.

An after image is a business graph that captures the current state of business data in an
EIS system, typically as a result of a change to that data in the EIS. An after image enables
changes in EIS systems to be captured and published to the runtime.

- Templated business graph is a business graph that is typed specifically for a type of
business object graph that it wraps.
- Change summary is provided to capture implicit changes, explicit changes, for both Delta,
as well as After Image use models.
- Explicit change summary support is provided by the business graph programming interfaces
enabling BPM component, such as adapters, mediators, maps, and relationships to explicitly modify
the Change Summary header.
- Event summary is provided to support capturing instance-based annotations about data in
the business object graph, and specifically, to contain object event identifiers
- Verb support is provided by the business graph enabling the components in the runtime to
key off the event type to perform value added function.
- Supported verbs is the notion of constraining and extending the set of allowable verbs
that can be specified for a business graph.
- Object event identifiers are supported by the business graph enabling all the objects in
a graph to be uniquely identified. This capability is required by some of the components that
provide value added features.