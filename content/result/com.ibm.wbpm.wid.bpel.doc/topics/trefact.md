<!-- image -->

# Refactoring and business state machines

## About this task

## Procedure

1. In the Business Integration view,
right-click the state machine.
2. From the drop-down menu, hover over Refactor and
then choose from one of the following three options:

Option
Description

Rename
Use this option to change the name assigned to the state machine.

Move
Use this option to move your state machine to a new folder
or module.

Change Namespace
Use this option to assign a new namespace to your state machine.

## Results

When you rename an interface operation
via the refactor menu, you may notice the following error in the Problems
view if you've created Java™ or
visual snippets that use its inputs or outputs: <variable\_name>
cannot be resolved.

It happens because the state machine
editor creates arbitrary variables to hold the input/output of operations.
These variables can be used in Java or
visual snippets, or in an invoke.  The form of these variables is: <operation\_name>\_<Input/Output>\_<operation\_parameter\_name> For
example, the variable for operation myOperation input parameter input1 is: myOperation\_Input\_input1 
Currently, there is no refactoring support to rename these variables
used in Java or visual snippets.

To
resolve this error, you must manually update all occurrences of the
variable in the Java or visual snippets, according
to the new operation name.

When you rename a
business object attribute via the refactor menu, all visual snippets
that reference this attribute will be automatically updated.

## Related concepts

- Replacement variables and context variables

## Related reference

- Description tab: business state machine editor