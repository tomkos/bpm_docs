<!-- image -->

# Compensation handling in long-running BPEL processes

In BPEL processes, compensation is triggered by fault handlers
of a scope or the process, or by the compensation handler of a scope
or an invoke activity.

In BPMN processes,
compensation can be triggered from outside compensation and fault
handlers via the compensate activity. This support is available for
generalized flow activities and collaboration scopes, where compensation
can be triggered from within the flow or scope. In this case, the
compensate activity triggers the compensation of all the activities
in the current scope that completed successfully before the compensate
activity started. When all of these activities are compensated, the
compensate activity completes and the navigation of the process continues.
If the compensation of a completed activity fails, the compensate
activity continues to trigger the compensation of the remaining activities.
When the compensation of these activities finishes, the compensate
activity passes the fault from the failed compensation to the enclosing
scope

## Compensation of child processes

A long-running
process can also compensate child processes that have successfully
completed. A child process is called by an invoke activity. This invoke
activity can have a compensation handler associated with it. If a
compensation handler is defined, its logic determines whether compensation
for the child process is triggered by the compensate activity. If
the compensation handler does not use the compensate activity, compensation
for the child process does not occur. If the invoke activity does
not have a compensation handler, then compensation for the child process
is triggered automatically.

For long-running child processes,
compensation is run for all of the successfully completed, directly
nested scopes on the process level in the reverse order of their completion.
For microflow child processes, compensation runs the undo actions
of all of the invocations in the reverse order of the forward execution
of the invocations.

- Compensate everything that is enclosed in the scopeThe compensation
of activities that started a child processes is integrated into the
sequence of compensating the other activities in the scope. Compensation
of everything in the scope is activated by the default compensation
handler of the current scope, or by a compensate activity that does
not specify a target.
For example, the activities A, B, and
C are enclosed in a scope. Activity B is the invoke activity for a
child process, and activities A and C are scope activities. All of
the activities complete successfully in sequence. When the parent
process is compensated, these activities are compensated in the reverse
order in which they completed: activity C, activity B, and then activity
A.
- Compensate specific activities in the scopeCompensation is
activated by compensate activities that target a scope or an activity.
An invoke activity that started a child process can be the target
of a compensate activity, even if the invoke activity does not have
a compensation handler defined.