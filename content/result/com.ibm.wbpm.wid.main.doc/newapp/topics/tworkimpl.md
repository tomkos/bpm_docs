<!-- image -->

# Working with implementations

In IBM® Integration
Designer, a component implementation consists of the business logic that
is executed when the component is opened, because it implements the
interfaces and references. When you work with the assembly editor,
you can add new components and use the Generate Implementation action to automatically create implementations and open them for
editing.

## About this task

An implementation provides logic to a component but,
in general, does not recognize other components and other implementations
in the module. The SCA runtime routes events to other components and
their implementations.

The implementation is narrowly focused
only on the logic. The component is more broadly focused in terms
of providing access through wires to other components and their implementations.

- Creating an implementation for a component

The component's implementation provides the business logic for the service.
- Opening an implementation

From the assembly editor, you can open and edit a component's implementation. The component's implementation executes the business logic of the service.
- Replacing an implementation

If you have made changes to components in the assembly diagram, you can replace existing implementations of components with new ones.
- Changing the implementation type of a component

You can change the implementation type of components even if their implementations already exist. An exception is that you cannot change the implementation type of a mediation flow component.
- Synchronizing the interfaces and references between components and implementations

After a component in the assembly diagram has been associated with an implementation, the interfaces and partner references must be kept synchronized. The assembly editor in IBM Integration Designer provides a mechanism that allows you to maintain this synchronization.

## Related concepts

- Workspaces
- Creating modules and libraries

## Related tasks

- Organizing projects using integration solutions
- Creating and wiring components
- Adding notes
- Setting assembly editor preferences
- Finding errors in the assembly diagram

## Related information

- Assembling services: Customer enquiry example