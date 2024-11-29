# createSubfolderUnderCurrentCase operation

| Parameter     | Type         | Description                                                                                                                                                  |
|---------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId        | String       | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window. |
| subfolderPath | String       | The name of the subfolder to be created under the current case folder.                                                                                       |
| return\_value  | VWAttachment | The newly-created subfolder, which is returned as an attachment object.                                                                                      |