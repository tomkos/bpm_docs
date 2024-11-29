<!-- image -->

# Task kinds and instance-based authorization roles

| Role                       | To-do tasks   | Invocation tasks   | Collaboration tasks   | Administration tasks   | Comments                                        |
|----------------------------|---------------|--------------------|-----------------------|------------------------|-------------------------------------------------|
| Potential instance creator | X             | X                  | X                     |                        | People who are allowed to create task instances |
| Originator                 | X             | X                  | X                     |                        | The person who created the task                 |
| Potential owner            | X             |                    | X                     |                        | People who can claim and work with tasks        |
| Owner                      | X             |                    | X                     |                        | The person who claimed the task                 |
| Potential starter          |               | X                  |                       |                        | People who are allowed to start the task        |
| Starter                    |               | X                  |                       |                        | The person who started the task                 |
| Administrator              | X             | X                  | X                     | X1                     | People who are allowed to administer a task     |
| Editor                     | X             |                    | X                     |                        | People who are allowed to edit task data        |
| Reader                     | X             | X                  | X                     | X2                     | People who are allowed to see task data         |
| Escalation receiver        | X3            | X3                 | X3                    | X3                     | People who receive an escalation                |

1. This role also has authorization for administrative actions on
the administered process, scope, or activity
2. This role also has authorization for read operations on the administered
process, scope, or activity
3. This role has authorization for read operations on the corresponding
task