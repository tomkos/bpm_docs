# Monitoring events for a Box collaboration
folder

## About this task

The IBM Business Automation
Workflow
Box Event Listener uses Java event handlers to
define the actions that are to be performed for events. You can use the Box document copy event handler that is provided by
IBM Business Automation
Workflow
Box Event Listener. The event handler copies a
Box document and file that document in a case.
You can then configure a case activity to launch automatically when the Box document is filed in the case. This event handler
displays a dialog box from which a user selects the document class that is used to copy the Box document to the FileNet® P8 object store. The user also can choose whether to
file the document in the case as part of the copy.

Alternatively, you can define a custom event handler plug-in that is a subclass of the
com.ibm.casemgmt.api.handlers.BaseHandler class.