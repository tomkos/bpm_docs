<!-- image -->

# Changing extended data element values in event definitions

## Before you begin

## About this task

## Procedure

1. In the event definition, select the extended data element
for which you want to set or change values.
2. Click the Properties tab to open
the Properties view.
3. If the data type of the extended data element is not an
array, then position your cursor in the Default value field
and type in a default value. This field is optional. The default value
will be used during content completion for an event that is missing
a required extended data element. If you are overriding an extended
data element from a parent event definition and you do not specify
a default value, the default value will be inherited from the parent
event definition.
4 If the data type of the extended data element is anarray, then optionally complete the following steps:
    1. Beside the Default values field,
click the Add button to add a value variable
to the Default values field for the first element
in the array.
    2. In the Default values field,
ensure that the value variable is selected
and then type in the default value that you want to use for the first
element in the array.
    3. Repeat the previous two steps for each element in the
array. The
default values will be used during content completion for an event
that is missing a required extended data element. The Default
values field is optional. If you are overriding an extended
data element from a parent event definition and you do not specify
a default value, the default value will be inherited from the parent
event definition.
5 If the extended data element has a data type of noValue ,you can optionally specify minimum and maximum occurrences by completingone or both of the following steps: If you are overriding an extended data element from the parentevent definition, any values specified in the Minimum occurs or Maximumoccurs fields will override the values specified in theparent event definition.

1. In the Minimum occurs field,
type the minimum number of instances of the extended data element
that must appear. This field is optional. The default value is 1.
2. In the Maximum occurs field,
type the maximum number of instances of the extended data element
that can appear. If you want the maximum number of instances to be
unbounded, you can type unbounded in the field.
This field is optional. The default value is 1.