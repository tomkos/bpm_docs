<!-- image -->

# Copying part of a mediation flow into a subflow

## About this task

## Procedure

1. Open the mediation flow in the mediation flow editor.
2. Select the mediation primitives that you want to extract.
3. Right click > Copy into New Mediation Subflow
4. In the New Mediation Subflow wizard, choose the module
or library that will contain the subflow. If you want to share the
subflow with other modules, put it in a library.
5. In the New Mediation Subflow wizard, enter a name for the
subflow.
6. Click Finish
7. Wire the in and out terminals of the subflow, and complete
the wiring.

## Example

- Nodes cannot be copied into subflows. If the selection includes
nodes that reference operations (such as Input, InputResponse, Callout)
the copy action will proceed but these nodes will not be copied. If
the selection contains only these primitive, the copy option will
not be available.
- In and Out nodes of a subflow may be copied to another subflow,
but not to a mediation flow.

## What to do next

## Related concepts

- Mediation subflows
- Mediation subflow limitations

## Related tasks

- Creating a new mediation subflow
- Editing a mediation subflow
- Adding a mediation subflow in a mediation flow
- Using Service Invoke in a subflow
- Synchronizing a subflow instance and implementation

## Related information

- Promoting properties in a subflow
- Changing the input or output message type in a subflow