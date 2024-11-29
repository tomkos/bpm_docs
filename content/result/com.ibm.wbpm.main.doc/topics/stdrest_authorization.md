# Authorization for Workflow REST APIs

## Authorization roles

## Retrieve and delete user
data

The following actions facilitate compliance with the EU's General Data Protection Regulation.

| Action                                                                                                                    | Eligible roles                             |
|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| Retrieve a list of personal information about a user (GET)GET https://host:port/ops/std/bpm/users/{user\_id}/personal\_data | Business Automation Workflow administrator |
| Delete personal information about a user (DELETE)DELETE https://host:port/ops/std/bpm/users/{user\_id}/personal\_data       | Business Automation Workflow administrator |

## Process APIs

| Action                                                                           | Eligible roles                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Retrieve a list of processes that the user is allowed to see (GET)/bpm/processes | Business Automation Workflow administrator Process application administrator                                                                                                                                                   |
| Start a new instance of a process (POST)/bpm/processes/{process-id}              | Members of teams assigned to the Expose to start option for the process                                                                                                                                                        |
| Retrieve the details of a process instance (GET)/bpm/processes/{process-id}      | Business Automation Workflow administrator Process application administrator Instance owner Follower of the instance Tagged in the instance Members of teams assigned to the Expose Performance Metrics option for the process |
| Delete a process instance (DELETE)/bpm/processes/{process-id}                    | Business Automation Workflow administrator Process application administrator Instance owner                                                                                                                                    |

## User tasks APIs

| Action                                                                        | Eligible roles                                                                                                                                             |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Retrieve a list of tasks that the user is allowed to see (GET)/bpm/user-tasks | Business Automation Workflow administrator Task owner Potential task owner for unclaimed tasks                                                             |
| Retrieve task details (GET)/bpm/user-tasks/{task-id}                          | Business Automation Workflow administrator Process application administrator Instance owner Task team manager Task owner Potential task owner Collaborator |
| Claim a task (PUT)/bpm/user-tasks/{task-id}/claim                             | Business Automation Workflow administrator Process application administrator Potential task owner if an owner is not assigned                              |
| Complete a task (PUT)/bpm/user-tasks/{task-id}/complete                       | Business Automation Workflow administrator Process application administrator Instance owner  Task owner                                                    |