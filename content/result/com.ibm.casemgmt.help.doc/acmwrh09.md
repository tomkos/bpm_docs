# Creating a custom page with widgets

## About this task

By creating custom pages, you can tailor the Case Client user interface to meet
specific requirements. For example, you might want two versions of the Case
Details page, one for managers and one for caseworker. In the version that is, intended
for managers, you include the Timeline Visualizer widget to display the extended case history. In
the version that is intended for caseworker, you do not include the Timeline Visualizer widget.

You create and test new pages in your development environment. When you deploy your solution to a
production environment, the new pages are automatically copied to that environment.

## Procedure

To create a page:

1. Open the solution in Case Builder.
2. On the Pages tab, add a page of one of the following page types:

Solution
Creates a blank page.
Case Details
Creates a page that is based on the Case Details page.
Add Case
Creates a page that is based on the Add Case page.
Split Case
Creates a page that is based on the Split Case page.
Add Activity
Creates a page that is based on the Add Activity page.
Work Details
Creates a page that is based on the Work Details page.
Custom Activity Details
Creates a page that is based on the Custom Activity Details page.

To create a page that is based on one of the other workflow pages or on a custom page, click the
Copy icon for that page.
3. Click the page name to design and configure the page layout.
4 In Page Designer, design the page layout:
    1. On the toolbar, click the Page Options icon to open the Page
Options window, where you can select and configure the page layout. Click
OK.

You can choose a layout that has a set configuration of rows, columns, or both. Certain layouts
also have collapsible sections, which can be configured as collapsed by default to change how the
page is displayed initially to the user. Alternatively, you can choose the Free
Form layout. With this layout, you use the Column and
Tab containers to configure the page exactly as you need.
    2. If you selected the Free Form layout, drag containers onto the
page. 
Restriction: If you add separate properties widgets to different tabs in a tab container
of a Free Form layout, the erroneous properties might not be visible. This
behavior occurs when an invalid value is present in properties of the properties widget of a
background tab.
    3. Drag widgets into the appropriate containers on the page.

Restriction: The solution pages do not monitor for unsaved changes in the widgets that
are on the page. To avoid potential loss of user input, do not put the Properties widget, Form
widget, or Viewer widget on these pages.
    4. Edit the settings for the widgets.
    5. Edit the wiring for the page and the widgets, if that is needed.
5 Associate the page with the role, work item, or case type: Component Action Case type Specify the default page layouts that you want to use for your case type: To override the Default layout for Case Details page selection for aspecific role, click Add Role . Select the page or client-side human servicethat you want to associate with the role. Role Specify the new page layout as a Solution page for a role: Work item Specify the new page layout as the default Work Details page for a stepin any FileNet® P8 process activity:

| Component   | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Case type   | Specify the default page layouts that you want to use for your case type: On the Case Types tab, open the case type. In the Default layout for Add Case page drop-down list, select one of the following page or client-side human service options: Add Case Add Case Form Add Case Default (Human Service) Add\_Case\_Custom\_name (Human Service) (if any)   In the Default layout for Split Case page drop-down list, select the following page option: Split Case   In the Default layout for Case Details page drop-down list, select one of the following page or client-side human service options: Case Details Case Details Form Case Details Default (Human Service) Case\_Details\_Custom\_name (Human Service) (if any)    To override the Default layout for Case Details page selection for a specific role, click Add Role. Select the page or client-side human service that you want to associate with the role. |
| Role        | Specify the new page layout as a Solution page for a role: On the Roles tab, open the role. On the Pages tab for the role, click Assign Page and select the page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Work item   | Specify the new page layout as the default Work Details page for a step in any FileNet® P8 process activity: On the Case Types tab, open the case type. On the Activities page, open the FileNet P8 activity that contains the step. Open the activity in Step Designer and select the step. In the Step Properties area, select the page from the Page Layout list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

- Classic pages

A page contains the widgets that are required to complete an activity. For example, the widgets that you use to create a loan request are grouped on a page.
- Widgets

Widgets are portable, reusable components that are used in pages to manage content and process work items.
- Action events

Some of the Case Client actions publish outgoing events. As with widgets, you can wire these events to the incoming events of widgets.