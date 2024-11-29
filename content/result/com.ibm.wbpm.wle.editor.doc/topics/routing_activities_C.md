# Assigning a BPD activity to an ad hoc list of users (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

The ad hoc group or list of users is maintained
while the process instance exists on the runtime Workflow Server.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application that contains a BPD.
3. Open the diagram of your BPD and select the activity that
you want to route.
4. Click the Assignments page in the
properties view.
5. From the Assign To list, select List
of Users (Deprecated).
6. In the Binding field, specify the
variable that binds the list to the activity to be assigned. For
example, you can define a new complex variable that is a list (array)
to pass the list of users from the service that generates the list
to the activity to be assigned.