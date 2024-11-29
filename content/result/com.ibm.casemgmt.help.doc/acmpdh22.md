# addCommentToCurrentTask operation

| Parameter    | Type   | Description                                                                                                                                                  |
|--------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId       | String | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window. |
| taskId       | String | F\_CaseTask must be used as parameter in Process Designer.                                                                                                    |
| comment      | String | The comment to be addedThe comment must be 64 KB or less in size.                                                                                            |
| return\_value | String | The GUID of the new comment.                                                                                                                                 |