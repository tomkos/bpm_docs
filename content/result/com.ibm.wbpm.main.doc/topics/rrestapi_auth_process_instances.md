# REST API authorization for process instances

For all APIs that support action policies, you can change the default association with the
tw\_admins group to another group as explained in Configuration properties for action policies. For more information about roles, see Authorization roles.

## Process Instance Variable Resource (PUT)

Action policy:
ACTION\_UPDATE\_INSTANCE\_VARIABLE

| Eligible roles                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Enabled for task states   | Preconditions   | API Documentation                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| Business Automation Workflow administrator Process application administrator  If a team is not defined for process application administrators, you can authorize more users by assigning one or more groups to the ACTION\_UPDATE\_INSTANCE\_VARIABLE action policy. If a team is defined for process application administrators, the action policy is ignored. If the user set up a such a team, the only way to authorize more users is to add them to that team. | Any                       | None            | For more information about the API to update a variable value in a BPD instance, see Process Instance Variable Resource (PUT). |

## Process Instance Resource (GET)

| Eligible roles                                                                                                                                                                                                       | Enabled for task states   | Preconditions   | API documentation                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------|------------------------------------------------------------------------------------------------------------------------|
| Business Automation Workflow administrator Process application administrator Instance owner Performance metrics user For any task within the process: Task team manager Task owner Task potential owner Collaborator | Any                       | None            | For more information about the API to retrieve the details of a process instance, see Process Instance Resource (GET). |

## Process Resource - POST (start)

| Eligible roles                                                                                                                                                                                                                                                               | Enabled for task states   | Preconditions                                     | API documentation                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|---------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Business Automation Workflow administrator Process application administrator Process instance owner For any task within the process: Task team manager Task owner Task potential owner (if the task owner is not set) Collaborator   Process starters (any exposed to start) | Any                       | The snapshot is not archived and not deactivated. | For more information about the API to start a BPD instance, see Process Resource - POST (start). |

## Process Resource - POST (sendMessage)

Action policy:
ACTION\_SEND\_MESSAGE

| Eligible roles                                                                    | Enabled for task states   | Preconditions   | API documentation                                                                                                     |
|-----------------------------------------------------------------------------------|---------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------|
| By default, any role is eligible. Restricted by action policy ACTION\_SEND\_MESSAGE | Any                       | None            | For more information about the API to send a message to the event manager, see Process Resource - POST (sendMessage). |

## Process Instance Resource - PUT (evaluate a JavaScript
expression)

| Eligible roles                                | Enabled for task states   | Preconditions                                                                                               | API documentation                                                                                                                              |
|-----------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Any authenticated user (see the precondition) | Any                       | In the 99Local.xml file, the <enable-javascript-execution> must be set to true. Its default value is false. | For more information about the API to running a JavaScript expression, see Process Instance Resource - PUT (evaluate a JavaScript expression). |

## Process Instance Resource - PUT (suspend)

Action
policy: ACTION\_SUSPEND\_INSTANCE

| Eligible roles                                                                                                                                                                                                                          | Enabled for task states   | Preconditions   | API documentation                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Business Automation Workflow administrator Process application administrator Any authenticated user, except if the role is restricted by action policy ACTION\_SUSPEND\_INSTANCE. By default, users with the tw\_admins role are eligible. | Active                    | None            | For more information about the API to suspend a process instance, see Process Instance Resource - PUT (suspend, resume, terminate, or retry). |

## Process Instance Resource - PUT (resume)

Action
policy: ACTION\_RESUME\_INSTANCE

| Eligible roles                                                                                                                                                                                                                         | Enabled for task states   | Preconditions   | API documentation                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Business Automation Workflow administrator Process application administrator Any authenticated user, except if the role is restricted by action policy ACTION\_RESUME\_INSTANCE. By default, users with the tw\_admins role are eligible. | Suspended                 | None            | For more information about the API to resume a process instance, see Process Instance Resource - PUT (suspend, resume, terminate, or retry). |

## Process Instance Resource - PUT (retry)

Action
policy: ACTION\_RETRY\_INSTANCE

| Eligible roles                                                                                                                                                                                                                        | Enabled for task states   | Preconditions   | API documentation                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Business Automation Workflow administrator Process application administrator Any authenticated user, except if the role is restricted by action policy ACTION\_RETRY\_INSTANCE. By default, users with the tw\_admins role are eligible. | Failed                    | None            | For more information about the API to retry a process instance, see Process Instance Resource - PUT (suspend, resume, terminate, or retry). |

## Process Instance Resource - PUT (terminate)

Action
policy: ACTION\_ABORT\_INSTANCE

| Eligible roles                                                                                                                                                                                                                        | Enabled for task states          | Preconditions   | API documentation                                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Business Automation Workflow administrator Process application administrator Any authenticated user, except if the role is restricted by action policy ACTION\_ABORT\_INSTANCE. By default, users with the tw\_admins role are eligible. | Suspended, Failed, or Terminated | None            | For more information about the API to terminate a process instance, see Process Instance Resource - PUT (suspend, resume, terminate, or retry). |

## Process Instance Resource - PUT (delete)

Action
policy: ACTION\_DELETE\_INSTANCE

| Eligible roles                                                                                                                                                                                                                         | Enabled for task states          | Preconditions   | API documentation                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Business Automation Workflow administrator Process application administrator Any authenticated user, except if the role is restricted by action policy ACTION\_DELETE\_INSTANCE. By default, users with the tw\_admins role are eligible. | Suspended, Failed, or Terminated | None            | For more information about the API to delete a process instance, see Process Instance Resource - PUT (suspend, resume, terminate, or retry). |

## Process Instance Resource - PUT (update document)

Action policy: ACTION\_UPDATE\_DOCUMENT

| Eligible roles                                                                                                                                                                                                                                                                                                                                                          | Enabled for BPD instance execution status                                                                                                                                               | Preconditions   | API documentation                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| Instance owner Owner of any task in the instance A member of the group that is assigned to the task, or a manager of the task team, or a collaborator of the task The user that follows the instance The user that is tagged in the instance Process application administrator The user is a member of the team to which the BPD is exposed through Performance Metrics | BPD instance is active, failed or suspended or Allow content operations for the completed process has been checked in BPD in the designer when the instance is completed or terminated. | None            | For more information about the API to update a process instance, see Process Instance Resource - PUT (update document). |

## Process Instance Resource - PUT (update due date)

Action
policy: ACTION\_CHANGE\_INSTANCE\_DUEDATE

| Eligible roles                                                                                                                                                                                                                                                | Enabled for task states   | Preconditions   | API documentation                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| Business Automation Workflow administrator Process application administrator Instance owner Any authenticated user, except if the role is restricted by action policy ACTION\_CHANGE\_INSTANCE\_DUEDATE. By default, users with the tw\_admins role are eligible. | Active or Suspended       | None            | For more information about the API to update a process instance, see Process Instance Resource - PUT (update due date). |

## Process Instance Resource - POST (add document)

Action policy: ACTION\_ADD\_DOCUMENT

| Eligible roles                                                                                                                                                                                                                                                                                                                                                          | Enabled for BPD instance execution status                                                                                                                                               | Preconditions                                                                       | API documentation                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Instance owner Owner of any task in the instance A member of the group that is assigned to the task, or a manager of the task team, or a collaborator of the task The user that follows the instance The user that is tagged in the instance Process application administrator The user is a member of the team to which the BPD is exposed through Performance Metrics | BPD instance is active, failed or suspended or Allow content operations for the completed process has been checked in BPD in the designer when the instance is completed or terminated. | Allow locally managed documents is enabled if the instance uses BPM managed folders | For more information about the API to update a process instance, see Process Instance Resource - POST (add document). |

## Process Instance Resource - POST (comment)

Action
policy: ACTION\_ADD\_COMMENT

| Eligible roles                                                                                                                  | Enabled for task states   | Preconditions   | API documentation                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------|----------------------------------------------------------------------------------------------------------------------------|
| Any authenticated user, except if the role is restricted by action policy ACTION\_ADD\_COMMENT. By default, any user is eligible. | Any                       | None            | For more information about the API to add a comment to a process instance, see Process Instance Resource - POST (comment). |

## Process Instance Resource - POST (fire timer)

Action
policy: ACTION\_FIRE\_TIMER

| Eligible roles                                                                                                                                                                                           | Enabled for task states   | Preconditions   | API documentation                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------|
| Business Automation Workflow administrator Process application administrator Users who are enabled by action policy ACTION\_FIRE\_TIMER and authorized to retrieve instance details. By default, any user. | Active                    | None            | For more information about the API to trigger a timer manually, see Process Instance Resource - POST (fire timer). |

## Process Instance Resource - POST (delete token)

Action
policy: ACTION\_DELETE\_TOKEN

| Eligible roles                                                                                                                                                                                             | Enabled for task states   | Preconditions   | API documentation                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------|------------------------------------------------------------------------------------------------------------|
| Business Automation Workflow administrator Process application administrator Users who are enabled by action policy ACTION\_DELETE\_TOKEN and authorized to retrieve instance details. By default, any user. | Any                       | None            | For more information about the API to delete a token, see Process Instance Resource - POST (delete token). |

## Process Instance Task Summary
Resource

| Eligible roles                                                                                                                                                                            | Enabled for task states   | Preconditions   | API documentation                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------|----------------------------------------------------------------------------------------------------------------|
| Business Automation Workflow administrator Process application administrator Instance owner Task team manager Task owner Task potential owner (if the task owner is not set) Collaborator | Any                       | None            | For more information about the API to list process instance tasks, see Process Instance Task Summary Resource. |

## Process Resource - GET (bulk instance details)

| Eligible roles                                                                                                                                                                                             | Enabled for task states   | Preconditions   | API documentation                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Business Automation Workflow administrator Process application administrator Instance owner Performance team Task team manager Task owner Task potential owner (if the task owner is not set) Collaborator | Any                       | None            | For more information about the API to retrieve information about process instances, see Process Resource - GET (bulk instance details). |

## Process Actions Resource - GET

| Eligible roles         | Enabled for task states   | Preconditions   | API documentation                                                                                                 |
|------------------------|---------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------|
| Any authenticated user | Any                       | None            | For more information about the API to retrieve actions for process instances, see Process Actions Resource - GET. |