<!-- image -->

# Implementations

The component's implementation executes the logic.

Service components are the main building blocks of a module. You
can implement your services using a variety of programming paradigms,
from process-flow style BPEL processes, to state machine-style event
management, to declarative business rules style. The style of implementation
you select will be determined both by your comfort level with a given
paradigm and the nature of the problem.

- Business processes
- State machines
- Human tasks
- Java™
- Rule groups
- Selectors
- Interface maps
- Mediation flows

You can create implementations using a variety of visual construction
tools. You can find detailed information about working with each of
the implementations in other sections of the documentation.

<!-- image -->

If the component's implementation does not exist, the component
will have an exclamation mark in the lower left corner, as shown in
the Component1 component. If the implementation already exists, then
there is no exclamation mark, as shown in the following image of the
CustomerQuery component:

Components that do not have an implementation type specified have
the untyped icon, , as shown in the following image of the CustomerQuery
component:

In bottom-up development, you can drag one of the implementations
(for example, a human task) from the same module onto the canvas of
the assembly editor and the component will be created for you. The
component will show its implementation type with no exclamation mark
to indicate that the implementation exists.

Also, you can set qualifiers on the component's implementation.
The qualifiers provide "quality of service" support (such as transaction
support, event sequencing, or security) required from the hosting
container.