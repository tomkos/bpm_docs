# Case toolkit

- A JavaScript file that provides the behavior of the
view.
- Image files to represent the view on the palette and on the canvas.
- A preview JavaScript file that shows a preliminary image of the view.

When these case views are used in the context of the process user task
page, the views configure themselves automatically based on the parent case, without the need to
specify the Case identifier and Target Object Store
name in the view’s configuration. Also, on these pages, the Case Content objects under
caseProperties variable can be used without need of Case Properties view. This is
due to the process instance itself acting as the controller and passing in the case instance content
object as referential input variable. The case data is managed along with the other process
variables and synchronized with the case instance automatically.

If these case views are
added to other client-side human service pages that are not directly associated with a parent case,
you can directly specify a Case identifier and Target Object Store
name in the optional configuration.

Configuring Case views in custom case
client-side human service

If any Case views are added to any custom case client-side human
service, which are created through Case Type > Views > Case Layouts, the
view's Case identifier and Target Object Store name
configuration must be mapped to the input variables (caseId and
tosName). In case of the Case Properties view, the binding
to the view must be set to the caseProperties private variable. These settings
are configured for the case views on any case client-side human service pages that are created from
the default case pages by using Case Type > Views > Case Layouts > Add Layout > Case Page
Layout.

<!-- image -->

- Add Activities

You can add new discretionary activities for workflow process activities.
- Add Case

You can use the Add Case view to create new case instances for specific case types.
- Case Activities

Use the Case Activities view to display the activities of the case.
- Case Calendar

Use the Case Calendar view to display events. By default, the view displays due dates for quick tasks and target end dates for case stages.
- Case Comments

Use the Case Comments view to display and add comments in the case.
- Case Folder

The Case Folder view displays documents and folders that are pertaining to the case instance in the target object store. If you are authorized, then you can search, create, delete, and rename folders. You can also upload, view, check out, and remove documents.
- Case Folder Tree

You can use the Case Folder Tree view to display the folder tree of the case.
- Case History

You can use the Case History view to display the history of the case.
- Case List

Use the Case List view to display a list of cases. When used in conjunction with the Case Search view, the Case List view lists the case results that are returned from the case searches.
- Case Search

Use the Case Search view to search for cases. Use this view in conjunction with the Case List view, which displays the list of cases that are returned from the case searches.
- Case Stages

Use the Case Stages view to display the stages of the case.
- Case Tasks List

Use the Case Tasks List view to display a list of case tasks for Quick Tasks, To-do and Process user tasks associated to a case instance.
- Case Visualizer

The Case Visualizer view provides historical information to a case in client-side human services. The information representation shows the progression of events, tasks, and work items over time for the case and might use significant computing resource, specifically database server storage, and CPU. Attention to the solution design, capacity planning, monitoring, and system (database) maintenance are essential to use the feature effectively.
- Create Package

Use the Case Package view to share the details about a case with external stakeholders who do not have access to the case management system. For example, if a case needs to be sent to a legal advisor for review, the caseworker can create its case package. That is from the Case Details or Cases page, they can select properties, documents, related cases, and other case information such as case comments and history, and package them into a single compressed file that gets saved in the case folder. The case package contains the selected case documents and a PDF file that lists the selected case information.
- Manage Roles

To access a solution, a user must be a member of a role that is associated with that solution. You can use the Manage Roles view to add users and groups to a role.
- Manage Team

Use the Manage Team view to control the access to case instances.
- Related Cases

Use the Related Cases view to define relationships between cases.
- Create Case service

The Create Case service is used to create a case by using a service call.
- Get Case Calendar Events service

Retrieves case-related calendar events for Case Stages or quick task due dates.
- Get Case Instance Object service

The Get Case Instance Object Service is used to fetch the case instance metadata by using a service call. This service is used internally by the Case views and in the custom client-side human services for Case Details.
- Get Repository Name service

The Get Repository Name service is used to fetch the target object store name using a service call. This service is used internally in the Case views, to fetch the target object store name, when configured to work in the context of a case orchestrated process user task pages.
- Initialize Case Content Objects service

The Initialize Case Content Objects service is used in the custom client-side human services for Case Details to load the caseProperties content object by using a service call. Any view that binds to the caseProperties content object uses this loaded data.
- Save Case Properties service

The Save Case Properties service is used in the custom client-side human services for Case Details to save the changes that are done to the caseProperties content object by using a service call.
- Split Case service

The Split Case service is used in the custom client-side human services to split an existing case and create a new case by using a service call. The custom client-side human service provides a user interface that displays the properties and documents from the parent case. You can either modify the properties or retain the existing values from the parent case before the Split Case service is initiated. The documents attached to the new case depend on whether you choose a subset of documents or all the documents from the parent case.
- Split Case

You can use the Split case view to reuse properties and documents from an existing case to create a new one.