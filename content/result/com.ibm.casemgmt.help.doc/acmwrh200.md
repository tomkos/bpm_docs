# Content List widget

- Double-click documents to open them
- Right-click in the Content List widget to perform basic operations, such as:
    - Viewing
    - Creating document versions
    - Downloading documents
    - Editing document properties
    - Sharing documents and folders with external users by using the external
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
- Browse through the list of documents

You add the Content List widget to a Work page
and then wire the widget to the In-basket widget. Or, you can add
the widget to a new page along with the Viewer widget, and then edit
the settings for the widget and to specify a stored search URL.

- Specify the default view for the list and whether case workers can switch
                    between views
- Indicate how the widget is to retrieve the list of documents that
are to be displayed
- Configure a pop-up menu for the documents in the Content List
widget

You can also choose to display a check box beside each document in the
list. The check box feature is disabled by default, but you can enable it in the IBM Content
Navigator administration desktop by changing the
Content list checkboxes control to the Show state. For
more information about enabling the check box feature, see the topic Tips for working in IBM Content Navigator.

- Preparing to use the Content List widget

To enable users to use the Content List widget, you must add the widget to a page. You then must edit the settings for the Content List widget to indicate how the list of documents is to be generated and, optionally, to configure a pop-up menu.
- Configuring the list of documents for the Content List widget

You configure the Content List widget to indicate how the widget retrieves the list of documents that are to be displayed.
- Content List widget events

The Content List widget uses events to display a list of documents from which users can access documents, create document versions, and download documents.