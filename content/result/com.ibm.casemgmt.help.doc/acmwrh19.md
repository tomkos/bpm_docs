# Classic pages

The page title and layout can be modified using the Page Options tool on the Page Editor screen.
The flow of events is achieved either by widgets that broadcast events or by widgets that are wired
to other widgets on the page. You might configure your application so that each case activity has
its own page. For example, you might require that a loan officer must create and submit loan
requests and notify customers when a decision is reached. So you add a page to create and submit
loan requests. You then create a separate page with work items to contact customers with the status
of their loan requests. In addition, you might configure the application so that different roles use
different pages.

An HTML template defines the layout and widget configuration for a page. A JavaScript file
contains the Dojo classes and workflow JavaScript classes that handle the processing that is
required for the page. A JSON file contains the definitions for wired events and any disabled
broadcast events.

- Adapter pages

The adapter pages enable the creation of UI views that incorporate client-side human services in addition to displaying supported case widgets.
- Solution pages

Solution pages provide case workers with access to cases and work items that are in a solution. The solution pages include the Work page, with the In-baskets and Toolbar widgets, and the Cases page, with the Case Search-related widgets.
- Case Details pages

The Case Details pages include pages that case workers use to interact with specific cases.
- Add Case pages

The Add Case pages includes pages that caseworker use to create cases of specific case types.
- Split Case pages

The Split Case pages include pages that case workers use to create new cases that are based on existing cases. One default Split Case page is provided.
- Add Activity pages

The Add Activity pages include the step pages that display when a caseworker adds a discretionary activity to a case.
- Task Details pages

The Task Details pages includes step pages that display when a case worker opens a work item. Case workers use the step pages to complete the work items that are assigned to them.
- Custom Activity Details pages

The Custom Activity Details pages include the step page that displays when a case worker opens a work item that was defined for a custom activity. One default Custom Activity Details page is provided.