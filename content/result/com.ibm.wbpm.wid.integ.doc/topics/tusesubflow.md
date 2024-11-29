<!-- image -->

# Adding a mediation subflow in a mediation flow

## Before you begin

## About this task

## Procedure

- Add the mediation subflow to the canvas of the mediationflow editor in one of the following ways:
    - From the project tree in the Business Integration view:
        1. In the project that contains the subflow, expand the category Integration
Logic > Mediation Subflows.
        2. Locate the subflow that you want to use, and drag it onto the
Mediation Flow editor canvas.
- From the mediation flow editor palette:
    1. In the mediation flow editor, expand the Mediation Subflow category
in the palette.
    2. Drag the Mediation Subflow icon  onto the canvas.
    3. In the Subflow Selection window, choose the subflow that you want
to add and click OK to add the subflow to the
canvas.
- Wire the subflow instance. By default, a subflow has untyped
in and out terminals. If you create a wire to an untyped input terminal,
the terminal's type will change to match the type of the terminal
to which it is connected. The same behavior occurs for an untyped
output terminal. If the terminal type does not match, you will need
to add a primitive to transform the message.
- Configure properties of the subflow instance in the Propertiesview:

    - The Details tab
lists the properties that have been promoted in the subflow implementation.
To set the value of a property, select it in the list and clicking Edit.
    - The References tab lists the references
of the Service Invoke primitive in the subflow.
    - The Promotable Properties tab lists the
properties that have been promoted in the subflow implementation.
Use this view to set the alias name or value of a property, or to
if you want to change the property at run time. For more information,
see Promoting properties in a subflow
- Click the subflow instance to open the subflow implementation
in the Subflow Editor.

## Related concepts

- Mediation subflows
- Mediation subflow limitations

## Related tasks

- Creating a new mediation subflow
- Editing a mediation subflow
- Copying part of a mediation flow into a subflow
- Using Service Invoke in a subflow
- Synchronizing a subflow instance and implementation

## Related information

- Promoting properties in a subflow
- Changing the input or output message type in a subflow