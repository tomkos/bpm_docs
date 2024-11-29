<!-- image -->

# Compensation handling in BPEL microflows

Typically, undo actions are specified in the process model for
activities that cannot be reversed by rolling back the transaction.
When a process instance runs, undo actions for compensable activities
are registered with the enclosing unit of work. Depending on the outcome
of the rollback or commit, compensation starts.

If the microflow is a child of a compensable, long-running process,
the undo actions of the microflow are made available to the parent
process when the microflow completes. It can, therefore, potentially
participate in the compensation of the parent process. For these types
of microflows, specify undo actions for all of the activities in the
process when you define your process model.

If a fault occurs during compensation processing, the compensation
action requires manual resolution to overcome the fault. You can use
Business Process Choreographer Explorer to repair these compensation
actions.