<!-- image -->

# Specifying parents for child event definitions in the event
definition editor

All event definitions inherit directly or indirectly from
a root event definition named WBI.MonitoringEvent. When you create
a new event definition in the event definition editor, it is automatically
defined as a child of the root event definition. However, if you do
not want the root event definition to be the parent of your new event
definition, you can specify a different event definition as the parent.

## Before you begin

## About this task

## Procedure

1. Beside the Parent field of the child
event definition that you want to specify a parent for, click the Browse
Parent Event icon . The Select Event Definition
window opens.
2. In the Select an event to open field,
begin typing the name of the parent event definition. The Matching
Events list is automatically updated to show one or more
event definition names that match the characters that you have typed.
Note: The
event definitions listed in the Matching Events list
all reside in the same project scope as your child event definition.
You cannot select your child event definition as a parent of itself.
Similarly, you cannot select a parent that has your child event definition
as its parent.
3. In the Matching Events list, ensure
that the correct parent event definition is selected.
4. In the Files list, ensure that the
correct event definition file is selected that contains the parent
event definition.
5. Click Finish. The name of the selected
parent event definition is displayed in the Parent field
of the child event definition.