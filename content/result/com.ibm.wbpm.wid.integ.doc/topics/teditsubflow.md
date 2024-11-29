<!-- image -->

# Editing a mediation subflow

## About this task

To edit a mediation subflow, open it in the Mediation
Subflow editor, either by double-clicking the subflow or by using
the Open with action in the Business Integration
view. You can perform these tasks in the Mediation Subflow editor.

## Procedure

- A mediation subflow can have one or more inputs and oneor more outputs. To add inputs or outputs to the subflow, expand the MediationSubflow folder in the palette.
    - To add an input, drop the In icon  onto the subflow canvas. The In node
represents the input terminal of the subflow instance.
    - To add an output, drop the Out icon  onto the subflow canvas. The Out node
represents the input terminal of the subflow instance,
    - To add a subflow, drop the Subflow icon  onto the subflow canvas.
- The inputs and outputs of a subflow are of undefined type
by default. You might need to change the message type in the subflow,
for example, if you need to do transformation in subflow. To change
the message type of inputs or outputs, see Changing the message type of input or output terminals in a mediation primitive.
- To add primitives to the subflow, expand a folder in the
subflow palette, and drop the required primitive onto the canvas.
- To configure properties of a primitive, click the primitive
on the canvas and work in the Properties view.
- To make a property available to the subflow instance in
the mediation flow, promote the property by switching to the Properties
view and click the Promotable Properties tab.
For more information, see Promoting properties in a subflow.
- To invoke an intermediate service, see Using Service Invoke in a subflow.
- If the change you made in the Mediation Subflow editor
affects the externals of the subflow, such as changes to in and out
nodes, promoted properties, or references, you need to
synchronize the subflow implementation and the subflow instances in
the parent mediation flows. After you save your changes in the subflow
implementation, you will see an error in the subflow instance in the
parent mediation flow indicating that the subflow mediation does not
match the implementation. Use the Quick fix action
in the Problems view to synchronize all the subflow instances and
the subflow implementation. For more information, see Synchronizing a subflow instance and implementation.

## Related concepts

- Mediation subflows
- Mediation subflow limitations

## Related tasks

- Creating a new mediation subflow
- Copying part of a mediation flow into a subflow
- Adding a mediation subflow in a mediation flow
- Using Service Invoke in a subflow
- Synchronizing a subflow instance and implementation

## Related information

- Promoting properties in a subflow
- Changing the input or output message type in a subflow