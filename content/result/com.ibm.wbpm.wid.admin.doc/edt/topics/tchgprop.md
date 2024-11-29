<!-- image -->

# Changing property values in event definitions

In the event definition editor, all values associated with
event definition properties are displayed in the Properties view.
You can use the Properties view to set or change the values of properties.

## About this task

## Procedure

1. In the event definition, select the property for which
you want to set or change values.
2. Click the Properties tab to open
the Properties view.
3. Click the General tab to open the
General page. As shown in the figure, the name and XPath of the property
are displayed. However, the name and path cannot be changed on this
page.
4. Click the Details tab to open the
Details page.
5. If you want the property to be required, select the Required check
box. Note that if you are overriding a property from a parent event
definition and the property has been specified as required in
the parent, the Required check box will already
be selected and you should not clear the check box.
6. If you want to specify a default value for the property,
position your cursor in the Default value field
and type in a string value. The default value represents the
value that should be used during content completion for an event that
is missing a required property. If you are overriding a property from
a parent event definition and you do not specify a default value,
the default value will be inherited from the parent event definition.
7. If you want to specify minimum and maximum permitted values
for the property, select the radio button to the left of the Minimum
value field and then type in string values in the Minimum
value and Maximum value fields.
If the event definition allows a range of values for a property, these
fields define the lower and upper bounds of that range. If you specify
only a minimum value, the permitted range has no upper bound. Similarly,
if you specify only a maximum value, the permitted range has no lower
bound. These fields are optional and cannot be specified if permitted
values are specified. Note that if you are overriding a property from
a parent event definition, you should consult the inheritance rules
at the bottom of this topic before specifying any minimum and maximum
values.
8 If you want to specify one or more permitted values forthe property, complete the following steps:
    1. Select Permitted values.
    2. Beside the Permitted values list
box, click the Add button to add a default
value to the Permitted values list box.
    3. In the Permitted values list
box, highlight the default value (as shown in the figure) and then
type in the actual string value that you want to use.
    4. Repeat the previous two steps for each permitted value
that you want to add. Permitted values are optional and
they cannot be specified if minimum and maximum values are specified.
Note that if you are overriding a property from a parent event definition,
you should consult the inheritance rules at the bottom of this topic
before specifying any permitted values.

## Example

If you are overriding a property from a parent event definition,
the following inheritance rules apply to minimum and maximum values and permitted
values:

- If the parent event definition defines minimum and maximum values
but the child event definition defines permitted values, the minimum
and maximum values defined by the parent are ignored.
- If the parent event definition defines permitted values but the
child event definition defines minimum and maximum values, the permitted
values defined by the parent are ignored.
- If the parent event definition defines only a maximum value but
the child event definition defines only a minimum value, the child
inherits the maximum value defined by the parent.
- If the child event definition does not specify either minimum
and maximum values or permitted values, the minimum and maximum values
or the permitted values specified by the parent are inherited.