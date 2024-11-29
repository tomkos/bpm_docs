# Views in the Dashboards toolkit

- To customize a view, always clone both the view and its corresponding service, and make your
changes on the copies of the artifacts.
- If you create Process Portal dashboards byusing the views and services in the toolkit, the behavior or visualization of the page might changeif you upgrade to a newer version of the toolkit. If you want to retain the existing behavior of theProcess Portal application, take one of thefollowing actions:
    - Copy the views and services that you need to the new version of the application.
    - Do not upgrade to the newer version of the toolkit.

- Batch Modify Dialog

Use Batch Modify Dialog to display a dialog that allows users to update a batch of process instance values and use the projected path management capabilities.
- Breadcrumb

Use Breadcrumb to add a breadcrumb to the coach view to show the navigation path that the user took to get to the current view.
- Category Selection

Use Category Selection to apply selection categories to a list of objects, for example, to a list of tasks or activities.
- Chart

Use Chart to create pie charts, bar charts, column charts, and line charts that display sets of data.
- Chart with Time Selector

Use Chart with Time Selector to enable users to select the granularity of data displayed.
- Dashboard Layout template

Use this template to create the layout for pages in Process Portal that are exposed as dashboards.
- Data

Use Data to display process or case variables that are defined as being available for search.
- Data Section

Use Data Section to provide a collapsible coach view section that displays the business data for an instance. A configuration property determines whether users can change the values of these variables.
- Dialog

Use Dialog to create a secondary window that contains other controls. The Dialog control can be configured to be modal or nonmodal in the display of the contained controls.
- Default Instance Details template

The ready-to-use Process Portal application that is shipped with IBM® Business Automation Workflow includes a dashboard for displaying details of the process instances. Use this template as the basis for creating a customized default Process Portal dashboard for displaying instance details.
- Floating Layout

Use Floating Layout to create an area in which layout elements are arranged side by side horizontally.
- Follow Button

Use Follow Button to add a button to follow or unfollow a process instance.
- Gantt Chart Instance Details

Use Gantt Chart Instance Details to create a Gantt chart that displays process instance details.
- Gantt Chart Process Overview

Use Gantt Chart Process Overview to create a Gantt chart that displays aggregate process data.
- Icon Button

Use Icon Button to display a clickable button that is rendered as an icon.
- Instance Activities List

Use Instance Activities List to show a list of activities for a process or case instance.
- Instance Activities Section

Use Instance Activities Section to provide a coach view that displays a list of activities for a process or case instance. The list can be filtered according to a category, such as ready activities, or by a text filter that the user enters.
- Instance Details UI Service Template

Use this service to customize the default Details UI for processes and BPDs. The Details UI displays instance details in Process Portal.
- Instance List

Use Instance List to show the list of process instances and case instances for the current user. The list can be filtered according to the instance state and search criteria.
- Instance Summary Section

Use Instance Summary Section to display active summary information and stream events for a specified process or case instance. This information includes the start date, and status information for the instance.
- Instance Tasks List

Use Instance Tasks List to show the list of tasks for an instance of a process or case. From this list, users with the appropriate authorization can work on, modify, and assign or reassign tasks.
- Instance Tasks Section

Use Instance Tasks Section to provide a coach view that displays a list of tasks for a process or case instance that can be filtered according to a category, such as completed tasks.
- Navigation Controller

Use the Navigation Controller to allow users to navigate between dashboards. To enable users to navigate between a standard dashboard, such as the Team Performance dashboard or the Process Performance dashboard, and a custom performance dashboard, a custom copy of the Navigation Controller is required.
- Process Diagram

Use Process Diagram to display process data in a visual diagram that can be annotated with additional information based on configuration options.
- Process Due Date

Use Process Due Date to allow users to edit the due date of a process.
- Process Instances List

Use Process Instances List to show the list of instances for a specified business process definition. Several filters control the actual selection.
- Refresh Button

Use Refresh Button to add a button to a coach view so that users can manually refresh the contents of the view. To respond to a refresh request, the individual coach views must be configured accordingly.
- Refresh Controller

Use Refresh Controller to automatically trigger the refresh of coaches or pages in the view at regular intervals. To respond to a refresh request, the individual views must be configured accordingly.
- Search

Use Search to enable users to perform an enhanced search for specific business data.
- Service Controller

Use Service Controller to consolidate the changes from the bound variables into a single boundary event. The boundary event can be used, for example, to refresh service variables.
- Split-Panes Section

Use Split-Panes Section to create a coach view with two sections: a main content section and a sidebar section. The width of the sidebar is configurable.
- Stream

Use Stream to display activity data for a specified user in a common stream-based format.
- Task List

Use Task List to show the list of existing tasks for the current user. The task list can be filtered according to specified users, teams, dates, and search criteria.
- Tasks Due

Use Tasks Due to create a due date histogram that displays the distribution of the tasks, ordered by due date.
- Team Roster

Use Team Roster to display a list of team members for a specified team and, optionally, displays users with active or selected tasks assigned to them.
- Team Summary

Use Team Summary to display active task summary information for a specified team.
- Text Filter

Use Text Filter to enable users to enter strings in a text box to filter lists of objects, for example, activities or documents.
- Two-Column Section

Use Two-Column Section to create a two-column layout for a coach view. The width of the columns is customizable.
- Zoom

Use Zoom to create a slider that can be used to increase or decrease the zoom level of other controls.