# Troubleshooting Case Client

- Instance user interface fails to open for a solution in Case Client

If you create a solution in IBM® Business Automation Workflow V18.0.0.1 or IBM Case Manager V5.3.3 and then upgrade to IBM Business Automation Workflow V19.0.0.1 or later, the View Process action and View Process Inspector action are not configured in Case Builder by default. You must configure the View Process action and View Process Inspector action in Case Builder to enable the instance user interface to open for the solution in Case Client.
- Cannot open Workplace

You cannot open  Workplace if you did not accept the self-signed certificate from the workflow server. In addition, you cannot open Workplace if the workflow desktop URL does not use the HTTPS protocol.
- A case cannot be created if the initiating document title contains a vertical bar (|)

Some cases are created automatically when you add a specific type of document. However, if the title of an initiating document contains a vertical bar (|), Case Client cannot create the case.
- Activities cannot communicate with a workflow process

You might encounter problems in which an activity fails to communicate with a workflow process that it starts.
- Reducing the time needed for advanced searches

When you search over large numbers of items, you might need to create an index on any custom user properties that are used in a WHERE condition. If you do not create an index, the search can take a long time because it performs a table scan.
- Changing the screen display resolution for Case Client and Case Builder

The default screen size for Case Client and Case Builder can be too large for small computer monitors with low resolution (for example, 768x1080).
- A search returns too many results

If you do not specify the criteria correctly in the Advanced Search dialog box, an   unexpectedly large number of results can be returned.
- Prompt to stop the script is displayed when searching for cases

If a search for cases takes a long time, your web browser displays a dialog box that asks if you want to stop the script.
- Sending a link to a case in an email opens an empty tab in the Firefox browser

If you use Mozilla Firefox as your browser, a blank tab might be left open if you select the Send Link to Case in the Case List widget menu or Send Link to Case by Email in the Case Toolbar widget.
- Incrementing float values in number spinner property fields

Case Client users may encounter issues with number spinner controls when the value in the field is a float type.
- Errors in Case Client property settings

In Case Client, you can recover from some errors in property fields.
- Filtering the in-basket with an (is-like) filter returns only exact matches

When you use an (is-like) filter for your in-basket, you see only exact matches returned.
- Cannot add values to multi value properties

It is not possible to add values to multi value properties because the OK button on the data entry window is not visible.
- Some automatically completed activities show extra states in the case history

Some automatically completed activities show extra states in the case history.
- Document Modified events do not display in the histogram

Changes to a document in a case do not display in the histogram of the Case History Visualizer.
- Reserved words cannot be used in solution names

Content Platform Engine reserved words cannot be used in workflow solution names.
- Cannot open a view that contains a datetime property with an invalid mask or pattern

If you define an invalid mask or pattern for a datetime property in Properties View Designer and then you save and close the view, you cannot reopen that view in Properties View Designer. If you deploy a solution and try to open a work item in Case Client, the view does not load.
- The time mask pattern K does not work in Case Client

In Properties View Designer, you can specify the pattern of date and time fields by using standard date and time mask patterns. Choosing the K pattern for the time mask, however, can lead to validation errors.
- Some property values are empty for cases that are returned by a search that uses the icm.util.SearchPayload class

If you write a custom search that uses the icm.util.SearchPayload class and your solution contains multiple case types, property values in the returned cases might be empty.
- You cannot use the number grouping characters in integer or float values in IBM Business Automation Workflow

You cannot use the number grouping characters for your locale as separators in IBM Business Automation Workflow numeric fields.
- Some property containers are not displayed in Internet Explorer 9

If you run Case Client in Internet Explorer 9, some containers might not be displayed if the property view contains a scroll bar for a horizontal list of radio buttons.
- The Browse button is disabled after you cancel from the Run Content Navigator File Tracker window

When you add a document to a case, if you click Cancel from the Run Content Navigator File Tracker window, you can no longer browse for a document to add.
- Unexpected viewer behavior in Case Client when you open documents for which the MIME types are not configured

When the viewer for Case Client is not configured for the relevant document MIME type, the viewer prevents you from viewing a document a second time.
- Some search documents do not behave as expected when added to specific widgets

Some search documents that are created in IBM Content Navigator do not behave as expected when they are added to specific widgets.
- Changes in activity property events are not shown in the Timeline Visualizer widget

Changes in activity property events are not captured in the case history unless you correctly configure the TimeToLive JVM parameter on your Content Platform Engine server.
- A completed CmAcmCaseState property does not reset back to Working even when new activity instances are launched for a completed case

When the caseState (CmAcmCaseState) property is set to Completed (3), its value does not change back to Working (2) if a disabled activity is enabled or if the re-enabled activity is launched. Once a case is marked as completed, the caseState does not change.
- Different browsers can display workflow group fields differently in Case Client

Depending on the browser that you use, fields that include workflow groups in a system-generated view can display in different orders in Case Client.
- Some container types in the Properties View Designer are incompatible with certain locales

Using some container types in Properties View Designer in some locales can cause the view to become corrupted.
- Cannot cancel the check-out of documents in Case Client that were added from an Alfresco CMIS repository

You can add documents from an Alfresco CMIS repository as case documents or as attachments.
- Inconsistent user interface behavior with bidirectional locales in IBM Business Automation Workflow

When you run IBM Business Automation Workflow on a browser that uses a bidirectional locale, some aspects of the user interface do not display consistently.
- Documents from external repositories cannot be removed or unfiled from a case folder if Content Platform Engine uses a database other than Db2

Normally, you can remove or unfile a document from a case folder by using Case Client. However, if the document is from a non-case management (external) repository and if Content Platform Engine uses a database other than Db2®, you cannot remove or unfile the document. If you attempt to remove or unfile the document, you encounter an error.
- Favorites and sync features are not supported for IBM Business Automation Workflow documents from repositories other than IBM FileNet P8

You cannot use the favorites and sync features on case documents that are stored in external repositories such as IBM Content Manager and CMIS repositories.
- Box actions are not displayed in the Documents view for existing solutions

The Box actions are not displayed in the Documents view for existing solutions.
- Case packaging action is not displayed on Case Details or Cases page for existing solutions

The case packaging action is not displayed on the Case Details or Cases page for existing solutions.
- Text in case package PDF file is not displayed correctly

In the PDF file that is included in a case package, some text is not displayed correctly.
- Unicode names are incorrect in case package for documents with non-English characters in the file name

When a case document has non-English characters in the file name, the resulting case package .zip file contains the correct file name with non-English characters. However, if you use a third-party utility to extract this document from the case package .zip file, the document name might be garbled. When you view the case package PDF document, the file name might be garbled in the tooltip for the link to the case document. In addition, the file name in any security warning dialog box that is displayed when you click on the link to the case document.
- The file does not open when you click a link to a .zip file in a case package

If you create a case package for a case that includes a .zip file as a case document, the case package PDF contains a link to that .zip file. However, you click on the link in the case package PDF file, the .zip file does not open.
- Restarting a workflow activity that fails to start

When a workflow activity fails to start, you must change the activity state manually and restart the activity.
- Box Collaboration action fails in a distributed environment when the date/time is not synchronized

In a distributed or cluster environment, an attempt to perform a Box collaboration action in Case Client fails if system time is not synchronized with the internet time.
- Content security policy directive frame-ancestors self errors in the Case Client

When you set Content Security Policy (CSP) on IBM Content Navigator on Case Client, it refuses to frame xxx because ancestor violates the CSP directive and shows "frame-ancestors 'self'" errors.