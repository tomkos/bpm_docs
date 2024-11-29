<!-- image -->

# Changing the implementation type of a component

You can change the implementation type of components even if their
implementations already exist. An exception is that you cannot change the
implementation type of a mediation flow component.

## About this task

When changing implementation type, you need to remain aware of
the limitations of the various implementations. For example, only untyped
and Java™ type
components and selectors can support Java interfaces, so you cannot change a
component with a Java interface to any other type. As well, an interface
in a human task component can only have one operation.

Follow these
instructions to change the component's implementation type:

## Procedure

1. In the assembly editor, click the component so that it is selected
on the canvas.
2. Right-click to select Change Type and the
new implementation type. If the component had an implementation before the
change, it will no longer have the old implementation associated with it but
it still has its interfaces and partner references.

## Related tasks

- Creating an implementation for a component
- Opening an implementation
- Replacing an implementation

## Related information

- Synchronizing the interfaces and references between components and implementations