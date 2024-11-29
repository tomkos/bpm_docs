# Roster permissions

| Permission   | Access rights                                                                                                                                                                                                      |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Query        | View the roster summary of the work item. Users can also view the work item itself if they have read access to the queue containing the work item. If no user or group is assigned, any user can query the roster. |
| Create       | Launch a workflow. If no user or group is assigned, any user can launch a workflow.                                                                                                                                |

- A new case is created. Any automatic activities that have no preconditions, or where the
preconditions are already met, are launched when the case is created. The user who created the
activity must have Create rights on the roster.
- A document is created and added to the case. If there is a precondition that causes an activity
to move to the Working state because a document is added to the case, the user who adds the document
must have Create rights on the roster.
- A case property is updated. If there is a precondition that causes an activity to move to the
Working state because of a property value update, the user who updates the property must have Create
rights on the roster.
- A manual activity is started. When the user manually starts an activity, the workflow is
launched. The user who starts the activity must have Create rights on the roster.
- A new activity is created. Any user who creates new user-defined or discretionary activities
must have Create rights on the roster.