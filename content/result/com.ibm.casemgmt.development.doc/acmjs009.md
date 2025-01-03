# icm.action

A workflow action works for a specific type of object such as a case or a work item. The object
is indicated by the subpackage within the icm.action package. One exception is
the icm.action.util package, which contains actions that are not performed for
specific case management objects.

An action also requires a specific context within which the action works. The context identifies
the objects that the action requires. The context also determines on which toolbars and menus the
action is available. For example, the action that is represented by the
icm.action.case.AddCustomTask class requires either an
icm.model.Case object or an icm.model.WorkItem object. This
action is available on the toolbar for editing a case or opening a work item. The action is not
available on the toolbar for adding a case or work item.

| Syntax                                                      | Description                                                                                                             |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| ['Case', 'WorkItem']                                        | The action requires either a case object or a work item object.                                                         |
| [['NewCase', 'Coordination']]                               | The action requires a new case object and a coordination object.                                                        |
| [['CasePage', 'Coordination'], ['NewCase', 'Coordination']] | The action requires either a case page object and a coordination object or a new case object and a coordination object. |

## icm.action.attachment package

The icm.action.attachment package
defines a single class, Remove, for the attachment context.
A Remove object is used to remove a document from
an attachment.

## icm.action.case package

| Class                     | Context                                                     | Description                                                                                                                          |
|---------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| AddCaseAndClosePage       | [['NewCase', 'Coordination']]                               | Saves the case that is being added, and then closes the current Add Case page or Split Case page.                                    |
| AddCustomTask             | ['Case', 'WorkItem']                                        | Opens the Custom Activity Editor window so that the user can add a custom activity to a case.                                        |
| AddCustomTaskFromExisting | ['Case', 'WorkItem']                                        | Opens a copy of the selected activity in the Custom Activity Editor window so that the user can add a new custom activity to a case. |
| CloseCasePage             | [['CasePage', 'Coordination'], ['NewCase', 'Coordination']] | Closes the current Add Case page, Case Details page, or Split Case page without saving any changes.                                  |
| OpenAddPredefinedTaskPage | ['Case', 'WorkItem']                                        | Adds a discretionary activity to the case.                                                                                           |
| OpenCasePage              | ['CaseReference']                                           | Opens the selected case in the Case Details page.                                                                                    |
| OpenSplitCasePage         | [['Solution', 'Case']]                                      | Opens the Split Case page so that the user can reuse properties from an existing case to create a new case.                          |
| SaveCaseOnPage            | [['CasePage', 'Coordination'], ['NewCase', 'Coordination']] | Saves the case that is being edited or added without closing the page.                                                               |
| SendLink                  | ['Case']                                                    | Sends an email that contains the URL to open the selected case in the Case Details page.                                             |
| ShowLink                  | ['Case']                                                    | Displays the URL to open the selected case in the Case Details page.                                                                 |

## icm.action.comment package

| Class              | Context                | Description                                                                                    |
|--------------------|------------------------|------------------------------------------------------------------------------------------------|
| AddCaseComment     | ['Case']               | Opens the Comments window so that the user can add a comment or view comments for a case.      |
| AddDocumentComment | [['Case', 'Document']] | Opens the Comments window so that the user can add a comment or view comments for a document.  |
| AddTaskComment     | ['WorkItem', 'Task']   | Opens the Comments window so that the user can add a comment or view comments for an activity. |
| AddWorkItemComment | ['WorkItem']           | Opens the Comments window so that the user can add a comment or view comments for a work item. |

## icm.action.contentitem package

| Class   | Context                | Description                                  |
|---------|------------------------|----------------------------------------------|
| Cut     | ['Document']           | Removes the selected document from the case. |
| Open    | ['Folder', 'Document'] | Opens the selected document or folder.       |
| Paste   | ['CurrentFolder']      | Pastes a document into the case.             |

## icm.action.document package

| Class                | Context           | Description                                                                                                                                                                                                                                     |
|----------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AddDocumentFromLocal | ['CurrentFolder'] | Adds a document to a case or a case folder.When Allow documents and attachments from repositories other than the case management object stores is selected, documents can be saved directly to a case without selecting a repository or folder. |
| Open                 | ['Document']      | Opens the selected document.                                                                                                                                                                                                                    |
| Refresh              | ['Document']      | Refreshes the document.                                                                                                                                                                                                                         |

## icm.action.folder package

| Class     | Context           | Description                                         |
|-----------|-------------------|-----------------------------------------------------|
| AddFolder | ['CurrentFolder'] | Adds a folder to the case.                          |
| Open      | ['Folder']        | Opens the selected folder and displays its content. |

## icm.action.solution package

| Class                  | Context      | Description                                                                                   |
|------------------------|--------------|-----------------------------------------------------------------------------------------------|
| EditProcessPreferences | ['Solution'] | Opens the Preference window so that the user can edit notification preferences for processes. |
| ManageRoles            | ['Solution'] | Opens the Manage Roles window so that the user can assign users to roles in a solution.       |
| OpenAddCasePage        | ['Solution'] | Opens the Add Case page so that the user can create a case of the selected case type.         |

## icm.action.task package

| Class               | Context                       | Description                                                                      |
|---------------------|-------------------------------|----------------------------------------------------------------------------------|
| AddTaskAndClosePage | [['NewTask', 'Coordination']] | Starts the new activity and closes the current Add Activity page.                |
| CancelAddTaskPage   | [['NewTask', 'Coordination']] | Cancels the addition of a new activity and closes the current Add Activity page. |

## icm.action.utility package

| Class        | Context   | Description                                                                |
|--------------|-----------|----------------------------------------------------------------------------|
| EventAction  | None      | Creates a button or menu item that publishes or broadcasts a custom event. |
| OpenWebPage  | None      | Opens the specified website in a separate window.                          |
| ScriptAction | None      | Creates a button or menu item that runs a custom script.                   |

## icm.action.workitem package

| Class                        | Context                            | Description                                                                                                                                 |
|------------------------------|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| CloseWorkItemPage            | [['WorkItemPage', 'Coordination']] | Closes the current Work Details page without saving any changes.                                                                            |
| DispatchWorkItemAndClosePage | [['WorkItemPage', 'Coordination']] | Dispatches the current work item. If the next work item is not opened automatically, this action also closes the current Work Details page. |
| MoveToInbox                  | [['WorkItem', 'Solution']]         | Moves the selected work item to the user's personal in-basket.                                                                              |
| OpenNextWorkItemInPage       | [['WorkItemPage', 'Coordination']] | Opens the next available work item in the same page when the user dispatches the current work item.                                         |
| OpenWorkItemPage             | ['WorkItemReference']              | Opens the selected work item in the Work Details page.                                                                                      |
| Reassign                     | [['WorkItem', 'Solution', 'Role']] | Reassigns the selected work item to another user. If the work item is open, this action first closes the work item.                         |
| ReturnToSender               | [['WorkItem', 'Solution']]         | Returns a work item to the in-basket it was most recently in. If the work item is open, this action first closes the work item.             |
| SaveWorkItemOnPage           | [['WorkItemPage', 'Coordination']] | Saves the work item that the user is editing without closing the Work Details page.                                                         |

- Action contexts

The context for an action corresponds to one or more Business Automation Workflow or IBM® Content Navigator model classes.

## Related reference

- icm.model
- icm.base
- icm.dialog
- icm.pgwidget
- icm.util
- icm.widget.menu