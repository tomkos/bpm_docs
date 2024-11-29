# Alternative administration modes for BPEL processes

The set of users that
can administer or monitor process, activity, and scope instances is
not changed by this administration mode. However, if the process or
any of its activities have replacement variables that reference the
modeled administration task, the people query for the task cannot
be resolved, and the default people assignments apply.

If you do not specify an administration mode, instance-based authorization
applies to actions on processes, activities, and scopes. In addition,
administration tasks are created as defined in the process template.
If the process template does not have any administration tasks, a
default administration task is created at run time when a process
instance is started.

If you change the administration mode, the new mode applies to
all new process instances. For existing instances, the administration
mode that is used depends on the position of the process navigation
when the administration mode was changed. Activities before the current
position are subject to the administration mode that applied when
the instances were created. For all other activities, the new administration
mode applies. Take care to avoid any disruption to people or automated
processes that perform administrative actions using user IDs that
are not in the appropriate role.

## Additional information on restricting process administration
to system administrators

This process administration mode
is the most restrictive. A different set of rules applies to what
happens when a new process instance is started and which user IDs
are allowed to view, monitor, or perform administrative actions on
process instance, scope instances, and activity instances.

- Your BPEL process relies on actions that are associated with modeled
administration tasks, for example, escalations.
- If adding the users that need to perform the modeled administration
tasks to the BPESystemAdministrator role, grants these users more
rights than they need.

<!-- image -->