# Case Folder

- When you open a coach that contains a Case Folder instance, the instance displays the contents
of its case root folder as specified by the configuration options. This root folder is named
Documents. However, the Case Folder displays this name in a breadcrumb trail when you are browsing
one of its subfolders. The root folder for a Case Folder instance is specific to that instance. The
root folder for the Case Folder is specified directly by binding the input variables caseId and
tosName to the respective configuration options.

When Case Folder view is used in the context of the process user task page, the view configures
itself based on the parent case, without specifying the Case identifier and target object store name
in the view’s configuration.

## Configuration properties

| Property                    | Description                                                                                              | Data type   |
|-----------------------------|----------------------------------------------------------------------------------------------------------|-------------|
| Case Identifier             | The Case Identifier is a mandatory option that needs to be bound to the input variable caseId.           | String      |
| Target Object Store Name    | The target object store name is a mandatory option that needs to be bound to the input variable tosName. | String      |
| Edit title                  | Allows to edit the title of this view.                                                                   | Any         |
| Hide title                  | Allows to hide the title as an option.                                                                   | Any         |
| Get Repository Name Service | Service to retrieve the repository name that is associated to the case instance.                         | String      |

## Events

The Case Folder view has an event handler On Document Clicked, which is
prefilled with an event action to help in previewing the documents if the document can be viewed in
a browser. Otherwise, it would allow the document content to be downloaded.

- To view documents in the Document Explorer view for upgraded solution by using custom view,
update the On custom view event of the Document Explorer view with the following
script:

```
var isCaseClient = ${GetIsCaseClient}.getValue();

if(isCaseClient == true) {
	// This would open the document in Navigator viewer only for Case Client.
	var docObject = {};
	var frameURL= null;
	var CaseClientTabID = null;
	if(doc.id.includes("idd\_")){
		docObject.id = doc.id.split("\_")[1];
	}
	frameURL=window.location.href;
	if(frameURL.includes('tw.local.caseDetailsClientTabID')){
		windowURL= frameURL.split('&tw.local.caseDetailsClientTabID=');
		caseClientTabID= windowURL[1].split('&');
		docObject.pageId = caseClientTabID[0];
	}
	docObject.caseAction = "documentClicked";
	this.context.broadcastMessage (docObject);
}
else {
	// This would open the document in native browser for browser supported mime types
	window.open(doc.url, '\_blank')
}
```

- If a process page containing Document explorer view is accessed from Case Client, then the
following script needs to be updated to the On custom view event:

```
var docObject = {};
    var frameURL= null;
    var zTaskId = null;
    if(doc.id.includes("idd\_")){
        docObject.id = doc.id.split("\_")[1];
    }
    frameURL=window.location.href;
    if(frameURL.includes('zTaskId')){
        windowURL= frameURL.split('&zTaskId=');
        zTaskId= windowURL[1].split('&');
        docObject.taskId = zTaskId[0];
    }
    docObject.taskAction = "documentClicked";
    this.context.broadcastMessage (docObject);
```

- If a process page containing Document explorer view is accessed from Workplace, then the
following script needs to be updated to the On custom view event:

```
window.open(doc.url, '\_blank');
```

Document management security has been enhanced so that only documents of specified MIME types are
allowed to be uploaded. To know the default MIME types supported and to add more MIME types, see
Configuring document management security.