# Copying, duplicating, moving, and reverting library items

## About this task

When you want to copy or move artifacts in Process Designer, these operations can help you improve
productivity. For example, you can copy artifacts or duplicate them instead of creating them from
scratch. Similarly, you can move resources from process applications or case solutions to toolkits
for reuse. Also, you can revert (roll back)
artifacts to older versions from previous snapshots if the current version has problems. And you can open and view snapshots directly in
Process Designer.

The following table describes the differences in these operations:

| Action        | Description                                                                                                                                                                                                                            | Permissions                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| Copy          | Creates a library item that is a copy of the original item. The newly created item is not associated with the original item from which it was copied. You can copy artifacts to the tip of the same project or to a different project. | You must have write access to the target project.            |
| Duplicate     | Creates a duplicate of the library item in the same project.                                                                                                                                                                           | You must have write access to the target project.            |
| Move          | Relocates the library item to a different project.                                                                                                                                                                                     | You must have write access to the source and target project. |
| Open snapshot | Opens a snapshot for viewing.                                                                                                                                                                                                          | You must have read or write access to the target project.    |
| Revert        | Replaces the current version of the library item in the tip with the selected snapshot version.                                                                                                                                        | You must have write access to the target project.            |

Before you proceed with any of these operations, consider how dependencies are affected:

- When you choose one or more items to move, IBM Process
Designer displays all the dependencies for the
selected items. The list of dependencies includes library items that share the same XSD or WSDL file
as the moving item, for example, two unrelated business objects, BO1 and BO2, that are defined in
the same XSD file. If you choose to move BO1, Process Designer includes BO2 in the list of dependencies even
though BO1 and BO2 do not depend on each other.
- Keep in mind, the destination you choose when relocating a library item might break existing
implementations and references in the source project. For example, consider the case of an activity
that is implemented as a nested process. If you move the nested process without moving the process
that contains the activity, the state of the activity's implementation (the reference to the nested
process) will depend on where you move the nested process. The following table describes the state
of the reference in different destinations:
Table 2. State of the reference to the nested process in different destinations

If you move the nested process to
State of the reference

A new or existing toolkit on which a dependency did not exist
The reference remains intact because Process Designer automatically creates a dependency on the
toolkit.

A toolkit on which the source project is dependent
The reference remains intact if the destination toolkit has not changed since
the most recent snapshot was created. Process Designer automatically creates a snapshot of the toolkit and updates the existing toolkit dependency to
the new snapshot.The reference breaks if the destination toolkit has changed since the most
recent snapshot was created. You can fix the reference by updating the existing toolkit dependency
to the new snapshot of the toolkit that Process Designer automatically creates.

A new or existing project
The reference breaks because projects can't depend on each other. When you
move library items to projects, be sure to move all related items to avoid broken references.
Business Automation Workflow automatically resolves broken
references when related items are not moved simultaneously.
- By default, Process Designer moves all related
items. If you analyze dependent items and choose to move only some of them, ensure that you
understand all the relationships before you complete an operation. To ensure you moved or copied all
items that are required for a particular implementation, check both the source and destination
project for validation errors.

## Procedure

From the Process Designer library,
select a category. In the artifacts list, click
 to toggle between single-selection and multi-selection modes to work with a single item or
multiple items. Depending on the mode you are in, select one or more items and the action from
the context menu.

- Dependent items are the artifacts that the selected library item uses and are moved with the
library item. The list of dependent items to be moved includes items that are dependent because of
the underlying implementation file. You cannot remove these items from the list of items to be
moved.
- Artifacts with dependencies are the items that use the selected artifact. Note: Leaving
artifacts with dependencies out of a move operation can cause errors in the source project because
services, teams, or other items that are required for their implementation are being moved. When
references are moved to a toolkit, you can update them and resolve the errors. However, when
references are moved to a process application or case solution, the references are no longer valid
because you can't have dependencies on process applications or case solutions.

## Results