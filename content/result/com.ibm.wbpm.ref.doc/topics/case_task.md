# Case Tasks List

You can create a quick task using the New Quick Task button.  You can start a
discretionary To-do task using the Add-To-do button.

When the Case Tasks List view is used in the context of the process user task page, the view is
configured based on the parent case, without specifying the case identifier and target object store
name in the view’s configuration.

## Configuration properties

| Property                    | Description                                                                        | Data type   |
|-----------------------------|------------------------------------------------------------------------------------|-------------|
| Case Identifier             | The required case identifier of the case instance.                                 | String      |
| Target Object Store Name    | The repository name that the view needs to connect to.                             | String      |
| Edit title                  | Allows to customize the title.                                                     | String      |
| Hide title                  | Hides the title.                                                                   | Boolean     |
| Hide Quick Task             | Hides quick tasks from the table.                                                  | Boolean     |
| Hide To-dos                 | Hides To-do tasks from the table.                                                  | Boolean     |
| Hide Process Tasks          | Hides the process tasks from the table.                                            | Boolean     |
| Hide External Process Tasks | Hides the external process tasks from the table.                                   | Boolean     |
| Hide Add To-do Button       | Hides the Add-To-Do button. Users cannot create discretionary to-do task.          | Boolean     |
| Hide Add Quick Task Button  | Hides the New Quick Task button. Users cannot create quick tasks.                  | Boolean     |
| Get Repository Name Service | Service to retrieve the repository name that is associated with the case instance. | String      |
| Hide modify task            | Hides the Modify Task action icon against a process.                               | Boolean     |
| Hide open workflow          | Hides the Open Workflow action icon against a process.                             | Boolean     |
| Hide modify workflow        | Hides the Modify Workflow action icon against a process.                           | Boolean     |
| Hide audit history          | Hides the Audit History action icon against a process.                             | Boolean     |
| Hide view progress diagram  | Hides the View Process Diagram action icon against a process.                      | Boolean     |
| Hide reassign back          | Hides the Reassign Back action icon against a process.                             | Boolean     |

- Quick tasks

You can enable caseworkers to create quick tasks for a case type by enabling the case type option Enable caseworker to create quick tasks, while you design a case type in a case solution.
- To-do tasks

You can use Case tasks list view to work on to-do tasks that are part of a case instance.
- Process tasks

You can use the Case tasks list view to work on process user tasks that are part of a case instance.