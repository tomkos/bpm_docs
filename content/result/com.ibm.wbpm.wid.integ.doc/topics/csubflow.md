<!-- image -->

# Mediation subflows

Use mediation subflows to reuse common patterns in mediation flows,
and also as a way to group primitives in the Mediation Flow editor.

A mediation subflow can be created in a module, mediation module,
or library. A mediation subflow must be used within a mediation flow.
It is good practice to store subflows in libraries so that they can
be easily shared between mediation flows in different modules.

A mediation subflow has one or more in nodes, one or more
mediation primitives, and one more out nodes. Unlike mediation
flows, the inputs and outputs of a subflow are not tied to specific
interfaces. Instead, the in and out nodes
represent the inputs and outputs of the subflow. In a wired mediation
flow, these nodes have message types associated with them. The message
types on these nodes are not defined when the subflow is created;
they can be changed later. The subflow implementation is defined in
the Subflow Editor.

- The Details page lists the properties that
have been promoted in the subflow editor. Here, you can change the
value of a property.
- The References page lists the properties
of Service Invoke primitives in the subflow.
- The Promotable Properties page lists the
properties that have been promoted in the subflow. You can further
promote these properties in the mediation flow.

You can create a Mediation Subflow from the File menu, or from
the Mediation Flow editor. See topic "Creating Mediation Subflows"
in related tasks for more information.

## Related concepts

- Mediation subflow limitations

## Related tasks

- Creating a new mediation subflow
- Editing a mediation subflow
- Copying part of a mediation flow into a subflow
- Adding a mediation subflow in a mediation flow
- Using Service Invoke in a subflow
- Synchronizing a subflow instance and implementation

## Related information

- Promoting properties in a subflow
- Changing the input or output message type in a subflow