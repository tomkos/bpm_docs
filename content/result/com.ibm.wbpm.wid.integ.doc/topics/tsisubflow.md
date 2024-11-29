<!-- image -->

# Using Service Invoke in a subflow

## Before you begin

## About this task

## Procedure

1. In the Mediation Subflow editor, drop a Service Invoke
primitive onto the canvas.
2. Select a reference from the list of available references
in the Select Reference window, and select an operation. Click OK.
You can also click New to create a new reference.
3. Switch to the Details page of the
Properties view. You will see the reference and operation that you
just added. Configure properties in the Details and Retry pages
as required.
4. Switch to the Promotable Properties page,
and promote the properties that you want to make available
to the subflow instance.
5. Switch to the mediation flow editor, and select the subflow
instance.
6. Switch to the Properties view.
7. Click the References tab. 
You will see the reference of the service invoke that
you added in the list of references for the subflow. 
In the list of subflow
references, Name is the name of the property
and Value is the reference. Make sure that
the Value column shows the correct reference.
If necessary, click Edit to select the correct
reference. You will also see an entry for the reference in the Operations
Connections section at the top of the mediation flow editor.

## Related concepts

- Mediation subflows
- Mediation subflow limitations

## Related tasks

- Creating a new mediation subflow
- Editing a mediation subflow
- Copying part of a mediation flow into a subflow
- Adding a mediation subflow in a mediation flow
- Synchronizing a subflow instance and implementation

## Related information

- Promoting properties in a subflow
- Changing the input or output message type in a subflow