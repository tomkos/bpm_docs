# Configuring where attachment content is displayed

## About this task

Attachment content is displayed when the Attachments widget loads and when users
double-click attachments or click View from the pop-up menu.

## Procedure

To configure the Attachments widget:

1. Click the Edit Settings icon.
2. Set and save the configuration options: 

Option
Description

Open documents in a separate browser window
Displays the content of the attachment in a separate browser window. Important: If a page does not contain the Viewer widget, you must enable this option so that users can open
documents from the Attachment widget.

Only show document classes that are defined in the solution
Limits the list of document classes that are displayed when the user adds a document from a
local computer as an attachment. When this option is selected, only the document classes that are
defined in the solution are displayed. If this option is not selected, users can select from all the
document classes in the current object store.

Open a document when the Work Details page is opened
Automatically displays the first or only document in the specified attachment set when the
Work Details page or Add Activity page opens. The document is
displayed in the Viewer widget.Important: Be sure to enter a valid, case-sensitive attachment set name in the
Default attachment to display field. If you leave this field blank, provide
an invalid attachment set name, or the specified attachment set name doesn't exist for the current
work item, the Viewer widget isn't loaded.
The attachment set name is configured in the
Case Builder in the Manage Attachments
section in the Step Designer. The attachment set name and the actual attachments are configured in
Process Designer on the workflow attachment property.
Recommendation: Because this widget must work for all case types in this solution, select an attachment
set that exists in most, if not all, steps.
Restriction: The Viewer widget does not display form content.