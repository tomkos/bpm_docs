<!-- image -->

# Authorization for administering BPEL processes

## Process administration

To define which users
are allowed to perform administrative actions and to read the process
data, you can specify an administration task as part of a long-running
BPEL process. The administrator and reader roles for the administration
task determine who is the process administrator and the process reader.
The process administrator can, for example, terminate the process
instance.

An administration task is associated with every BPEL
process. If an administration task is not modeled for the process,
a default administration task is created at run time. This default
task defines the process starter as the process administrator, and
does not assign any readers to the process.

## Scope administration

You can model an administration
task for the scope that defines scope readers and scope administrators.
A scope reader is allowed to view local variables. Scope administrators
are allowed to repair activity instances in the scope, and to view
and update local variables. If the scope is enclosed in another scope, the scope reader and
administration rights are inherited by the enclosing scope. Scope
readers and administrators also become readers and administrators
of the activities in the scope.

## Activity administration

The administrator
role for an activity administration task determines who is allowed
to administer the corresponding activity. The activity administrator
can, for example, restart the activity. The administration task is
created as soon as administrative actions, that is, restart or complete,
can be performed on the activity instance. Reader and administrator
roles of the process, and reader and administrator roles of the enclosing
scopes are automatically propagated to the activities.

- For each invoke or snippet activity. This administration task
determines who is allowed to administer the activity in addition to
the process administrators.
- A default administration task for activities on the process level
that applies to any activity that does not have an administration
task assigned to it.