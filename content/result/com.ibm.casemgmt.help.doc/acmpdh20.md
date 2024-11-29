# Adding case operations to a 
FileNet

process

## Before you begin

Define the activity in Case Builder.

## About this task

To add case operations, you open the activity in IBM®
FileNet Process Designer. You then add a component step to the workflow with
which you associate the case operations. You can associate more than one operation to a component
step. For example, you can configure case operations to create a case and add a comment with a
single component step.

- Create a case by using a specified case type.
- Add a comment to the current case.
- Create a discretionary activity in a case.
- File attachments to a case into a subfolder
- Relate the current case to another case.

## Procedure

To add case operations to a workflow step:

1. In a stand-alone IBM
FileNet Process Designer, open the solution
for editing the FileNet P8 activity workflow, which you want to add the case operation.
2. In IBM
FileNet Process Designer, drag the
Component icon to drop at the place in the activity that you want the
operation to be performed.
3. On the Component tab, click the Add
icon.
4. From the Component list, select
ICM\_Operations.
5. Select the operation that you want to insert and then click
OK.
6 In the Operation Parameters area, enter an expression for each operationparameter:
    1. Click in the Expression field for the parameter.
    2. From the Expression list, select Build
Expression.
    3. For the caseID parameter, in the Business Object
Fields list, you must select F\_CaseFolder and click
Insert.
    4. For the taskID parameter, in the Business Object
Fields list, you must select F\_CaseTask and click
Insert.
    5. Use other case properties for the expression. In the Business Object
Fields list, select F\_CaseFolder, then select the case property
and click Insert.

 If the expression contains a hardcoded string, enclose the string in double quotation marks.

- addCaseOwners operation

Assigns users to a case team as owners of the current case.
- addCaseRoleMembers operation

Assigns users to the case team as members of a role in the current case.
- addCommentToCurrentCase operation

Adds a comment to the current case. You can specify the comment or use Expression Builder to assign a string case property as the comment.
- addCommentToCurrentDocument operation

Adds a new comment to the specified case document or attachment. To add a comment, the document or attachment must be filed in the current case.
- addCommentToCurrentTask operation

Adds a comment to the current task. You can specify the comment or use Expression Builder to assign a string case property as the comment.
- addDependentObject operation

This operation adds a new object at the specified location in a list of dependent objects for a case property of type Business Object.
- completeCurrentCaseStage operation

Completes the current case stage and advances to the next case stage if there is a next case stage.
- createCasePackage operation

Creates a package that contains the case artifacts that are specified by the parameters for this operation and stores the package in the case folder.
- createCaseUsingSameCaseType operation

Creates a new instance of case using the same case type.
- createCaseUsingSpecifiedCaseType operation

Creates a new instance of a case for the specified case type.
- createDefaultCasePackage operation

Creates a package that contains all case-related artifacts and stores the package in the case folder.
- createDiscretionaryTaskInCurrentCase operation

Creates a new activity instance of a discretionary activity type. The discretionary activity must be defined in the same solution.
- createDiscretionaryTaskInCurrentCaseWithWorkflowParams operation

Creates a new activity instance of a discretionary activity type with the specified workflow parameters.
- createDiscretionaryTaskWithProps operation

Creates a new activity instance of a discretionary activity type with the specified properties.
- createNewDependentObject operation

Creates a pending instance of the specified dependent object class to use as the starting value for a new case property. If you want, you can then use addDependentObject operation to add more values. You assign the collected values as the value of a business object property when you create a case.
- createSubfolderUnderCurrentCase operation

Creates a subfolder under the current case folder.
- disableSpecifiedCaseStage operation

Disables a specified stage from the list of existing case stages.
- enableSpecifiedCaseStage operation

Enables a specified case stage back to the list of existing case stages.
- fileAttachmentsToCurrentCase operation

Files attachments to a specified subfolder under the current case folder. Attachments can originate in the case management object stores or in other repositories that are configured for the case management environment.
- findDependentObjects operation

Finds the indexes of objects that match the specified criteria in a list of dependent objects for a case property of type Business Object.
- getCasePropertyNames operation

Returns a list of the names of the properties in a case. This operation is a prerequisite for the createCase operations.
- getCasePropertyValues operation

Returns a list of the property values of a specified case. This operation is a prerequisite for the createCase operations.
- getCaseStructure operation

Returns the case structure for a given case. The structure is returned as a list of folder names and document series IDs, but excludes any empty folders. Typically, this operation is called to obtain the case structure prior to calling the createCase operations.
- getTaskPropertyNames operation

Returns the custom property names of a task.
- getTaskPropertyValues operation

Returns task property values for a given list of task properties.
- placeCurrentCaseStageOnHold operation

Puts the current case stage on hold.
- relateCurrentCase operation

Creates a relationship between the current working case and the targeted case.
- releaseCurrentOnHoldCaseStage operation

Releases the hold on the current case stage.
- removeCaseOwners operation

Removes users as owners of the current case.
- removeCaseRoleMembers operation

Removes users as members of a role in the current case.
- removeDependentObject operation

Removes the object at the specified index from a list of dependent objects for a case property of type Business Object.
- replaceCaseOwners operation

Replaces the users currently assigned as owners of the current case with a new set of users.
- replaceCaseRoleMembers operation

Replaces the users currently assigned as members of a role in the current case with a new set of users.
- restartPreviousCaseStage operation

Restarts the previous case stage.
- searchTasks operation

Searches for tasks in a particular case by using the provided conditions.
- setCasePropertyValues operation

Sets the values for the specified properties in a case.
- setDependentObjectProperties operation

Updates the property values for the object at the specified index in the list of dependent objects for a case property of type Business Object.
- setTaskPropertyValues operation

Sets the task property values for a particular task. This method typically applies when updating the task properties on a task other than the current one. For the current task, you can use step parameters to set the task properties.
- terminateTasksInCurrentCase operation

Terminates all workflows (tasks) in the current case. Tasks are terminated only if they have not completed and have not failed. Tasks that are in Waiting state will not be terminated.
- unfileAttachmentFromCurrentCase operation

Unfiles an attachment from a case folder.
- unfileDocAttachmentFromCurrentCase operation

Unfiles the specified document attachment from the folder or subfolder of the specified case. Upon successful completion of this method, the document is no longer filed in the folder.
- unrelateCurrentCase operation

Removes the specified relationship to the current case.