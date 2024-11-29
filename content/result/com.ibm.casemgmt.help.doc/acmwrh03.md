# Attachments widget

For FileNet® P8 documents,
the Attachments widget lists attachments by the document title that
is assigned when the attachment was added to the widget. This title
is automatically updated when the document title is updated in the
repository.

- Upload local files to a repository
- Attach documents by browsing and selecting them from a repository
- Attach documents by dragging them from your
file system to the Attachment widget
- Check out, check in, cancel checkout, and view properties of documents;
download attachments; remove attachments
- Add documents from external repositories as work item attachments
- Share documents and folders with external users by using the external
Share feature in IBM® Content
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

- Specify whether attachment content will be displayed in the Viewer
widget or in a separate browser window
- Specify whether to display a list of all document classes or only the list of document classes
that are defined for the current solution when a user adds a document from the local computer as an
attachment.
- Open a specified document when the page containing
the Attachments widget is opened.

## IBM Business Automation
Workflow pages that include this
widget by default

- Add Activity page
- Add Activity Form page
- Work Details page
- Work Details Form page

- Configuring where attachment content is displayed

By default, attachment content is displayed in the Viewer widget that is on the same page as the Attachments widget. Optionally, you can configure the Attachments widget to display content in a separate browser window.
- Configuring entry templates for adding and checking in documents

You can add controls in the Attachments and Case Information widgets to add and check in   documents by using entry templates.
- Attachments widget events

The Attachments widget uses events to process the list of documents that are attached to a work item.