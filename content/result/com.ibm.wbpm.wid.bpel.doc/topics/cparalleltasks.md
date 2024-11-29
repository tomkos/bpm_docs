<!-- image -->

# To-do tasks and collaboration tasks with parallel ownership

When a task with parallel ownership is started, a subtask for each
potential owner is created and started, and the parent task goes into
the running state. The potential owners can be individuals or groups.
If a subtask is created for a group, any member of this group can
claim the task. The input message and all other relevant information
for the parent task are copied to each subtask. The subtasks are always
collaboration tasks.

After the subtasks are started they go into either the ready state
or, if automatic claim is specified for the parent task and the potential
owner has an individual work item, the claimed state. When the subtasks
are created, the parent task goes into the waiting-for-subtask substate.
The subtasks then go through the normal lifecycle of a collaboration
task; the parent task remains in the waiting-for-subtask substate
until all of its subtasks reach an end state. If the completion condition
for the parent task becomes true, all of the subtasks, which are not
yet in an end state, are terminated.

Because parent tasks do not have an owner, you cannot use the API
operations, such as claim or cancelClaim on
them. If the parent task is modeled so that its subtasks are claimed
automatically, the subtasks are automatically assigned to each of
the potential owners.

## Authorization considerations

- The administrator of the task with parallel ownership becomes
the administrator of each of the subtasks
- The person who starts the task with parallel ownership becomes
the originator of each of the subtasks
- One potential owner

## Completion conditions

```
tel:getCountOfFinishedSubtasks() div tel:getCountOfSubtasks() > 0.5
```

If one of the completion conditions
applies, the task with parallel ownership finishes and the aggregated
result for all of the subtasks is constructed. If subtasks exist that
are not yet finished, they are automatically terminated.

## Result construction

- The field in the output message of each of the subtasks that is
the source for result aggregation
- The field in the output message of the task with parallel ownership
that is the target for the result of the aggregation

## Example of a TEL definition of a task with parallel
ownership

```
<tel:result>               
   <tel:aggregate location="/reviewresult" function="tel:and()"/>               
   <tel:aggregate location="/reviewcomments"                              
                  condition="/reviewresult=true()"                               
                  function="tel:concatWithDelimiter('|')"/>             
</tel:result>
```

In this example, result aggregation
is specified for the reviewresult and reviewcomments fields
in the output message. The location /reviewcomments specifies
that the corresponding field in the output message of the subtask
is used as the source for aggregation. The XPath indicator "/" denotes
the root of the output message definition. The /reviewresult=true() condition
specifies that a subtask is considered only if the value of the reviewresult field
in its output message is set to true. The aggregation function specifies
that the values of the qualifying output messages are concatenated
into an aggregate String using the specified delimiter.

- XPath extension functions for human tasks with parallel ownership

For human tasks with parallel ownership, you can use XPath extension functions to control how individual responses are combined to produce a result.

## Related concepts

- Types of human task
- Inline and stand-alone human tasks
- Task templates
- Task instances
- Human task clients
- Human task user interfaces
- Versioning of human tasks
- Lifecycle of a human task

## Related tasks

- Setting human task preferences
- Improving performance when using human task list widgets