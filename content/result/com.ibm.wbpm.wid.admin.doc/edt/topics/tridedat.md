<!-- image -->

# Overriding extended data elements of parent event definitions

A child event definition automatically inherits the extended
data elements of its parent event definition. However, in the event
definition editor, you can choose to have your child event definition
override one or more extended data elements of its immediate parent
or any higher-level parents in the same inheritance hierarchy.

## About this task

## Procedure

1. Open your child event definition in the event definition
editor.
2. In the event definition editor, click the Add
Extended Data from Parent icon . The Select
Contents window opens. By default, the window
box shows the name of the immediate parent event definition and all
of its extended data elements that are not currently overridden in
the child event definition.
3. If you want to show the names of all parent event
definitions in the same inheritance hierarchy as well as all of their
extended data elements that are not currently overridden in the child
event definition, select the Show all parent events check
box.
4. In the Select the contents to add list,
select one or more extended data elements of one or more parent event
definitions that you want to override in your child event definition. If you
are overriding an extended data element that contains nested child
extended data elements, you can only select the parent extended data
element in the Select Contents window. Although both the parent
and its child extended data elements will be added to your event definition,
you can later remove any of the child extended data elements that
you do not want and they will be transparently inherited from the
parent event definition.
5. Click Finish. The overridden extended
data elements are added to the child event definition. The overridden
extended data elements are flagged with the This extended
data is inherited from the parent event definition symbol .

## What to do next