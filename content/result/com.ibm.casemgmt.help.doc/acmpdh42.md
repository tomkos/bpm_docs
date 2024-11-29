# unfileDocAttachmentFromCurrentCase operation

If a case type is configured so that users can attach documents from repositories other than the
case management target object store, you can use this operation to unfile attachments from an
external repository. To unfile an attachment from an external repository, the attachment must be
filed in the current case along with the information that is needed to reference the external
document.

| Parameter      | Type       | Description                                                                                                                                                  |
|----------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId         | String     | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window. |
| subfolderPath  | String     | Path to the subfolder, relative to the Case folder. If the document to be unfiled is in the root of the case folder, this can be the empty string or "/".    |
| sourceDocument | Attachment | An Attachment object for the document attachment to unfile.                                                                                                  |
| return\_value   | Attachment | The folder or subfolder from which the attachment was unfiled, or an empty attachment if the attachment was not unfiled.                                     |