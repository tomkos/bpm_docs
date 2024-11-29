# Case Details pages

The following default Case Details pages are provided:

- Case Details Adapter
- Case Details Adapter  (deprecated)
- Case Details

## Case Details Adapter page

A new Case Details Adapter page is automatically added to all case
solutions. The page has a new default layout. You can use this page by any new custom client-side
human services Case Details view. You can copy the page and modify it in Page Designer to create
your own custom page.

The default page contains the default widgets that are laid out as shown in the following
illustration, but you can add additional case widgets in Page Designer if desired:

<!-- image -->

The following widgets are supported in the Case Details Adapter page:

- Calendar
- Case Information
- Case List
- Case Stages
- Case ToolbarNote: Case Toolbar is a required widget that acts as a controller on the page,
passing the correct client-side human service URL to the Client-Side Human Service Viewer when the
page is opened. It is also used to display any case level actions that are not yet available
directly as client-side human service views.
- Chart
- Content List
- In-baskets
- Search
- Script Adapter
- Timeline Visualizer
- To-Do List
- Toolbar
- Viewer
- Website Viewer or Client-Side Human Service ViewerNote: When the Website Viewer widget is used
in default Adapter pages that incorporate client-side human services, it is renamed to Client-Side
Human Service Viewer.  The Client-Side Human Service widget is required because this is where the
human service case details are rendered.

## Case Details Adapter page (deprecated)

The Case Details Adapter page is automatically added to all new case
solutions. This page was default for custom client-side human services page layouts that did not
have case header information or a close button as part of the custom client-side human services.

The default page contains the default widgets that are laid out as shown in the following
illustration, but you can add additional case widgets in Page Designer if desired:

<!-- image -->

The following widgets are supported in the Case Details Adapter page:

- Calendar
- Case Information
- Case List
- Case Stages
- Case Toolbar
- Chart
- Content List
- In-baskets
- Search
- Script Adapter
- Timeline Visualizer
- To-Do List
- Toolbar
- Viewer
- Website Viewer
Note: When the Website Viewer widget is used in default Adapter pages that incorporate client-side
human services, it is renamed to Client-Side Human Service Viewer.

## Case Details page

The Case Details page is used for viewing or updating case data. The page
uses case widgets only, it does not use the newer client-side human service case page layouts.

<!-- image -->

- The Case Toolbar widget includes the following buttons: Add Custom
Activity, Add Activity, Close,
Comments, Create Package, Save,
and Split Case. The Add Custom Activity button opens a
menu that includes two options: New and Copy Existing Custom
Task.Restriction: The Create Package button is
included by default only for solutions that are created with version 5.2.1 Fix Pack 4 or
later.
- The Case Information widget displays the following tabbed views:
Documents, History, and
Activities.