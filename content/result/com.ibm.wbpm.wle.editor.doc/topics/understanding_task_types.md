# Task types

The following task types are supported.

| Task type        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User Task        | User tasks are completed by a person. By default, user tasks are associated with client-side human services. If you want a user to start a service but no additional user involvement is required, you can associate a service with a user task, such as an Integration service. In this way, the required user implementation is automatically created when you drag process components onto a diagram. You can also choose User Task and an associated service for an activity implementation, as described in Implementing activities in a process. |
| Inline User Task | Inline user tasks are extensions of user tasks. You do not need to attach a human service to an inline user task because a human service is already provided by default.                                                                                                                                                                                                                                                                                                                                                                               |
| System Task      | System tasks must be completed by an automated system or service and are automatically run without a need for user initiation regardless of the type of lane in which they are defined in a process diagram. System tasks that you place in a non-system lane are also run by the system by the first-configured system lane user. You can also choose System Task and an associated service for an activity implementation, as described in Implementing activities in a process.                                                                     |
| Script           | A script uses JavaScript to access and manipulate data. For information, see JavaScript API. For information about adding global JavaScript functions as managed server files, see Managing external files.                                                                                                                                                                                                                                                                                                                                            |
| Decision Task    | Decision tasks are useful when you want a decision or condition in a business rule to determine which process implementation is started. When you drag a Decision service from the library to a process diagram, an activity with a Decision task is automatically created. You can also choose Decision Task and an associated Decision service for an activity implementation, as described in Implementing activities in a process.Note: Decision tasks are equivalent to BPMN 2.0 Business Rule Tasks.                                             |