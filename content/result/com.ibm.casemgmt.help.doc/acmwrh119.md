# Task Details pages

- Process Task Details Adapter, to display task-related information.
- Process Instance Details Adapter, to display instance-related
information.
- Work Details, to work on a work item.
- Work Details Form, to work on a work item by using a form.
- Form Attachment Work Details, to work on a form-based work item.

## Process Task Details Adapter page

<!-- image -->

- The Task Toolbar widget displays header information about a process task. The widget displays
the task name, parent case title (ID), and task due date by default, but you can edit the settings
to also display the process instance name. Information about editing the settings is found in the
topic Task Toolbar widget.
- The Client-Side Human Service Viewer displays the content of the process task. This is
accomplished by the Task Toolbar widget, which broadcasts a DisplayURL
event that is handled by the Client-Side Human Service Viewer. As this is a broadcast event, any
other widgets that handle this event will also be affected.

## Process Instance Details Adapter page

<!-- image -->

- The Task Toolbar widget displays header information about a process instance. The widget
displays the instance name, parent case title (ID), and instance due date by default, but you can
edit the settings to also display the process task name. Information about editing the settings is
found in the topic Task Toolbar widget.
- The Client-Side Human Service Viewer displays the content of the process instance. This is
accomplished by the Task Toolbar widget, which broadcasts a DisplayURL
event that is handled by the Client-Side Human Service Viewer As this is a broadcast event, any
other widgets that handle this event will also be affected.

## Work Details page

<!-- image -->

- The Work Item Toolbar widget includes the following buttons: Close,
Comments, Complete, and
Save.
- The Case Information widget displays the following tabbed views:
Documents, Activities, and
History.

## Form Attachment Work Details page

<!-- image -->

The information that a case worker enters in the Form widget on this page is saved in a form
document. The form document is then attached to the work item.

By default, when included on the Form Attachment Work Details page the Work
Item Toolbar widget includes the following buttons: Close,
Comments, Complete, and
Save.

## Work Details Form page

<!-- image -->

The information that a case worker enters in the Form widget on this page is saved as property
values for the case.

- The Work Item Toolbar widget includes the following buttons: Close,
Comments, Complete, and
Save.
- The Case Information widget displays the following tabbed views:
Documents, Activities, and
History.