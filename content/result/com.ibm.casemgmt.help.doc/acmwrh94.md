# Case Information widget

The case identifier is displayed at the top of the Case Information
widget with a link to open the case in the Case Details page.

## Case Information widget configuration

You can edit the settings for the Case Information widget to select the views that
are to be displayed in the widget. If you configure the widget to display more than one view, each
view is shown on a separate tab. For the Documents view, you can specify whether documents are to
open in a separate browser window and whether only document classes that are defined in the solution
are to be displayed.

You can configure toolbars and menus to provide user actions that are specific to the
Documents view, History view, and
Activities view. In the Documents view, you can perform
multiple actions, such as:

- Configure toolbars and menus for documents and for folders.
- Enable users to add documents and folders to their Favorites and sync content between devices.
Favorites and sync must be enabled in IBM® Content
Navigator before case workers can use the
feature.
- Configure the use of check boxes for the documents in the list. By
default, check boxes are disabled, but you can enable them in the IBM Content
Navigator administration desktop by changing the
Content list checkboxes control to the Show state. For
more information about enabling the check boxes, see the topic Tips for working in IBM Content Navigator.
- Share documents and folders with external users by using the external
Share feature in IBM Content
Navigator. 
Note: The external Share feature must be configured in IBM Content
Navigator before you can share documents and
folders externally. The external Share feature is supported in IBM Business Automation
Workflow with an external IBM Content
Navigator deployed on WebSphere® Application
Server V9.0 and above. The external Share feature is also
supported in Content Platform Engine and IBM Content
Navigator container deployment environments
where the external Share container must be additionally deployed.

You can wire the Case Information widget so that a document is automatically displayed in the
Viewer widget when a user selects the document on the Documents tab. To make documents display
automatically, wire the outgoing Document selected event for the Case Information widget to
the incoming Open document event for the Viewer widget.

## IBM Business Automation
Workflow pages
that include this widget by default

## Case Information widget restrictions

The Case Information widget does not support the following MIME types that are specific to
Workplace and Workplace XT. Because the widget does not display these document classes correctly,
users might encounter errors when they open the documents of these types. To avoid these errors,
store files with the following MIME types in folders that users cannot browse to or that they cannot
search for:

```
application/x-filenet-customobjectentrytemplate
application/x-filenet-declarerecordentrytemplate
application/x-filenet-documententrytemplate
application/x-filenet-entrytemplate
application/x-filenet-folderentrytemplate
```

```
application/x-filenet-rm-electronicrecord
application/x-filenet-rm-emailrecord
application/x-filenet-rm-physicalrecord
```

```
application/x-filenet-search
application/x-filenet-searchtemplate
```

```
application/x-filenet-scenariodefinition
application/x-filenet-workflowdefinition
application/x-filenet-xpdlworkflowdefinition
```

- Activity view for the Case Information widget

You can configure the Case Information widget to provide case workers with a list of the activities that are defined for the case.
- Documents view for the Case Information widget

You can configure the Case Information widget to provide caseworker with a list of the documents that are associated with the case.
- History view for the Case Information widget

You can configure the Case Information widget to provide case workers with a history of events that occurred for the case. The History view displays a list of the events in chronological order with the most recent events first.
- Summary view for the Case Information widget

You can configure the Case Information widget to display a summary of the case properties in Case Builder.
- Case Information widget events

The Case Information widget handles incoming events to display document, history, task, and summary information about a case.