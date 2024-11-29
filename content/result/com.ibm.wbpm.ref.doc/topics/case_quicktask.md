# Quick tasks

- Filter the quick tasks to view only quick tasks in the Case task list.
- Expand the quick task to view the system-level information.
- Open, complete, and delete the quick task. Mark the quick task back as incomplete to rework on
the quick task.
- Do batch operations such as complete and delete a set of quick tasks by selecting more than one
quick task.
- Search or find the case task on name and assignedTo column.

You can view quick tasks in the Case calendar view. You can create a quick task from the
Case calendar view. The task is added in the Case task list in the Case tasks list view.

You can follow these steps to customize the Create quick task action:

1. Open the Case solution in Process Designer.
2. Create a New view (Example: Create quick task modal).
3 Click the Variables tab and create these two configuration options:
    - caseId of type String
    - tosname of type String
4. Add a button (Example: Create Quick Task) along with the Create
quick task modal view to the Layout.
5. Set the Case Identifier  and Target object store name
configuration options of the Create quick task modal view to the configuration
options that you created in Step 3.
6. From the Create quick task modal view, select the
Visibility tab and choose "None".
7. Click the Create quick task button, select the Event
tab and specify this statement on the onclick event:
${<control Id of Create Quick Task Modal view>}.showModal().
Example:
${Create\_Quick\_Task\_Modal}.showModal()
8. Add the newly created Create quick task modal view to the custom CSHS next to
the close button and map the caseId of type String  and
tosname of type String configuration options.