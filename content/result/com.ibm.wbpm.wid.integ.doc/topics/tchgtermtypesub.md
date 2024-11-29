<!-- image -->

# Changing the input or output message type in a subflow

When you open a mediation subflow in the Mediation Subflow editor,
you are working with the mediation flow implementation. You
need to use the Quick fix action to propagate any change that you
make to the externals of the subflow in the Mediation Subflow editor.

Within a mediation flow, you are working with the subflow instance.
You can have many instances of a subflow implementation in the same
mediation flow. Changes that you make to the properties of a subflow
instance within the Mediation Flow editor apply only to that subflow
instance.

## Changing the type within a subflow instance

- When you wire a mediation subflow instance in a mediation flow,
an undefined terminal takes the type of the terminal to which it is
wired.
- You can also change the terminal type explicitly by followingthese steps:
    1. Click the subflow to select it.
    2. Switch to the Properties view.
    3. Switch to the Terminal tab.
    4. Expand the terminal tree, and click the terminal whose type you
want to change.
    5. In the Message Type field, click the Change button.
    6. Choose a type from the list of available message types and click OK.

## Changing the type within a subflow implementation

When you change the message type of an input or output of a subflow
in the Subflow editor, you are changing the subflow implementation.
You need to propagate the change to all subflow instances that use
the subflow.

1. Click the node to select it.
2. Switch to the Properties view.
3. Switch to the Terminal tab.
4. Expand the terminal tree, and select in or out terminal, depending
on the node that you are changing. Note: 
The in node
has an out  terminal that propagates the message
to the next primitive or node in the subflow. The out node
has an in terminal that receives the message
and sends it to the next primitive or node outside the subflow.
5. In the Message Type field, click the Change button.
6. Choose a type from the list of available message types and click OK.
7. Press Ctrls-S to save your changes.
8. Synchronize all the subflow instances by using the Quick fix action
in the Problems view. For more information, see Synchronizing a subflow instance and implementation.

## Related concepts

- Mediation subflows
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