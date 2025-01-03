# Widgets

The default pages in Case Client include
widgets that are already wired together. You can wire other widgets
together, including widgets from other vendors, to create a customized
application.

For example, if you want to create an application for a bank loan
department, you can configure the application so that bank clerks
can initiate loan applications, and managers can approve or deny those
applications. To create this application, you create a Solution space
for the bank by copying the default Solution space. The default Solution
space contains both Work page and Cases page.
The Work page includes the Toolbar and In-baskets
widgets. The Cases page includes the Toolbar,
Search, Case List, and Case Information widgets.

There are two additional spaces, Case Pages space and Step Pages
space, that also include various pre-wired widgets.

After creating space and pages, you can modify the location of
widgets on the pages, add widgets onto pages, and configure the widgets.

- Attachments widget

You use the Attachments widget to display a list of the documents that are attached to a work item. The documents are stored on the Content Platform Engine server. In addition, you can configure a case type so that the Attachments widget can display documents from external repositories.
- Calendar widget

You can use the Calendar widget to display events for one or more cases. By default, the Calendar widget displays due dates for quick tasks and target end dates for case stages. You can also configure the Calendar widget to display events from an internet calendar that uses the iCalendar file format, such as Google Calendar or Apple Calendar.
- Case Information widget

You use the Case Information widget to display an overview of a case to case workers. The Case Information widget can display up to four views: summary, documents, activities, and history.
- Case List widget

You use the Case List widget to display the cases that are returned by a search. Case workers can select a case to view from the list.
- Case Stages widget

You use the Case Stages widget to display a visual representation of the stages that a case passes through. The widget shows case workers which stages are complete, which stage is the current stage, and which stages are yet to come.
- Case Toolbar widget

You use the Case Toolbar widget to specify the actions that case workers can take for cases. These actions can be implemented as buttons or menu buttons in the toolbar.
- Chart widget

You can use the Chart widget to display one of the IBM Case Monitor Dashboard charts on a page. These charts provide various views of case-related and task-related statistics for the solution to which a case belongs.
- Content List widget

You use the Content List widget to display a list of documents that are retrieved from the Content Platform Engine server. Users can use this list to view the documents and their properties, to create document versions, and to download documents.
- Form widget (deprecated)

You can use the Form widget instead of the Properties widget to enable workers to view and edit the property values for a case or for a step (work item) by using a form. The form that is used in the Form widget provides a customizable interface and automation features that are not provided by the Properties widget, such as custom field validation and a calculation engine.
- In-baskets widget

You use the In-baskets widget to enable users to view   and work with work items.
- Instruction widget

You can use the Instruction widget to display instructions for completing a work item that is associated with a custom activity.
- Markup widget

You can use the Markup widget to including custom HTML and JavaScript output on a page in Case Client. For example, you might use this widget to include a personalized message to the case worker who is viewing the page. You might also use this widget to display status information that is generated outside of IBM Business Automation Workflow.
- Original Case Properties widget

You use the Original Case Properties widget to display property values for a case that is being split to create a new case. A case worker can compare the values in this widget to the values that are displayed in the Split Case Properties widget for the new case.
- Page Container widget

You use the Page Container widget as a holder of all the case widgets that you add to your case page.
- Process History widget

You can use the Process History widget to display the status of the milestones that are defined for the workflow with which a work item is associated.
- Properties widget

You use the Properties widget to enable case workers to view and edit the property values for a case or a work item.
- Script Adapter widget

The Script Adapter widget is used to insert logic between widgets during event communication. It transforms data that is published by one widget into a format understood by another widget. For example, you might use the Script Adapter widget to transform the data that is published by the Properties widget into a format that is understood by a custom widget on a Case Details page. You can also use the Script Adapter widget to insert logic between widget event communication. For example, you might use the Script Adapter to perform custom validation on data that is published by the Properties widget. Because you can configure the Script Adapter widget to display event data at runtime, you can also use the widget to help debug your solution.
- Search widget

You use the Search widget to provide caseworker with a way to search for cases based on selected property values.
- Select Case Documents widget

You use the Select Case Documents widget to select the documents from an existing case that are also to be associated with a new split case.
- Split Case Properties widget

You can use the Split Case Properties widget to enable case workers to create a new case that reuses property values from an existing case.
- Task Toolbar widget

You use the Task Toolbar widget to display the header information about a process task instance. The widget has a dependency on the Website Viewer widget to display the task UI content.
- Timeline Visualizer widget

The Timeline Visualizer widget provides a visual representation of the extended history for a case. These representations show the progression of events, tasks, and work items over time for the case.
- To-Do List widget

You use the To-Do List widget to display checklists of to-do items to case workers. To-do items are based on to-do tasks and quick, which do not have an associated workflow. You can define to-do tasks as discretionary if you want to allow case workers to add to-do items at run time. You can enable quick tasks to allow users to create their own to-do tasks.
- Toolbar widget

You use the Toolbar widget to enable a case worker to open a web page, add cases, manage roles, or perform a custom action.
- Viewer widget

You use the Viewer widget to display to case workers documents that are stored in FileNet® P8 object stores.
- Website Viewer widget

You use the Website Viewer widget to display the website that is associated with a specified URL. For example, you might use this widget to display your company’s internal website to case workers. Case workers can browse the website in the Website Viewer widget by clicking the links in the site in the same way that they use a web browser.
- Work Item Toolbar widget

You use the Work Item Toolbar widget to enable responding to work items or adding new activities.