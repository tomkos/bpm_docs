# unfileAttachmentFromCurrentCase operation

| Parameter     | Type   | Description                                                                                                                                                  |
|---------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId        | String | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window. |
| subfolderPath | String | The path to the subfolder.                                                                                                                                   |
| documentTitle | String | The name of the document to be unfiled. You can use the CE\_Operations getStringProperty operation on the document to use for this value.                     |