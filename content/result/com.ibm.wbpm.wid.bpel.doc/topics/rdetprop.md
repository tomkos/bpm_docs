<!-- image -->

# Propagation tab: Human Task editor

- All - All authorization roles are propagated. Each subtask is
given both the default authorization roles and those of the calling
task. The important consequence of this choice is that owners of the
subtasks will be able to see the results of other subtasks.
- Administrator - The administrator role definition is propagated
to the subtasks. Hence the administrator role for the subtasks becomes
the sum of the default administrator role (that the subtask is given
by default) and the administrator role of the main task. This ensures
that anyone who has administrative privileges over the main task also
has them over the subtasks. Individual subtask owners will not be
able to view the results of other subtasks.
- None - None of the authorization roles are propagated from the
main task to the subtasks and the subtasks have only the default authorization
roles. This choice means that no-one can view individual results of
the subtasks.