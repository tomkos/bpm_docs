<!-- image -->

# Promoting properties in a subflow

You might want to set the value of the property in the mediation
flow at development time. Or, if you reuse the same subflow in multiple
places in a flow, you might not want to use the same alias name for
the property depending on the behavior you want.

To promote a property in the subflow implementation, complete the
following steps:

1. Open the subflow in the Mediation Subflow editor.
2. Click a primitive to select it, and switch to the Properties view.
3. Click the Promotable Properties tab to
view the properties that are available for promotion.
4. Select the check box in the Promoted  column
for the property that you want to promote.
5. Change the Alias and Alias value of
the property. In the subflow instance in the parent mediation flow,
the Alias becomes the name of the property, and the alias value becomes
the default value of the property.
6. Press Ctrl-S to save your changes. The property is now available
in all the mediation flows that use this subflow.
7. In the Mediation Flow editor, open a mediation flow that uses
the subflow.
8. Select the subflow and switch to the Properties view.
9. Click the Promotable Properties tab.
10. Select the check box in the Promoted  column
for the property that you want to promote.
11. Optional: Change the Alias or Alias
value.

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

- Changing the input or output message type in a subflow