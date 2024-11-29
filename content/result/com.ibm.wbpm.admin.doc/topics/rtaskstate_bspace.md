<!-- image -->

# How task states in Business Process Choreographer relate to
the task status in Business Space

The following table shows how the task states that are
available in Business Process Choreographer map to the task status
that is shown in Business Space.

| Task state in Business Process Choreographer   | Task type                                                               | Task status in Business Space   |
|------------------------------------------------|-------------------------------------------------------------------------|---------------------------------|
| Inactive                                       | All task types                                                          | Not active                      |
| Ready                                          | Collaboration and to-do tasks                                           | Available                       |
| Running                                        | Invocation tasks, collaboration and to-do tasks with parallel ownership | In progress                     |
| Finished                                       | All task types                                                          | Successful                      |
| Failed                                         | All task types                                                          | Failed                          |
| Terminated                                     | All task types                                                          | Canceled                        |
| Claimed                                        | Collaboration and to-do tasks with single ownership                     | In progress                     |
| Terminating                                    | All task types                                                          | Canceled                        |
| Failing                                        | All task types                                                          | Failed                          |
| Expired                                        | All task types                                                          | Expired                         |
| Forwarded                                      | Collaboration and to-do tasks  with single ownership                    | Forwarded                       |
| Skipped                                        | Inline invocation and to-do tasks                                       | Skipped                         |
| Stopped                                        | All types of inline tasks                                               | Stopped                         |