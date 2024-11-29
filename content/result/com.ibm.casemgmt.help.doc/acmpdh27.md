# fileAttachmentsToCurrentCase operation

You can use this operation only to file attachments to an existing subfolder. To file an
attachment in a new subfolder, you must first call the createSubfolderUnderCurrentCase operation to
create the subfolder.

If a case type is configured so that users can attach documents from repositories other than the
case management target object store, you can use this operation to file attachments from an external
repository. For an attachment from an external repository, this operation files the external
document reference object in the case along with the information that is required to reference the
external document.

If a case type does not support external repositories, you can use the
FileAttachmentsToCurrentCase operation only to file attachments that are in the same target object
store as the current case.

If an attachment cannot be found, the system stops execution of the current work item and returns
an error.

| Parameter     | Type           | Description                                                                                                                                                               |
|---------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId        | String         | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window.              |
| attachments   | VWAttachment[] | An array of VWAttachment objects, which are the attachments for the filing document. Attachments can originate from the case management repository or other repositories. |
| subfolderPath | String         | Path to the subfolder, relative to the Case folder. If the documents to be filed are in the root of the case folder, this path can be the empty string or "/".            |
| return\_value  | VWAttachment   | The subfolder, which is returned as a VWAttachment object.                                                                                                                |