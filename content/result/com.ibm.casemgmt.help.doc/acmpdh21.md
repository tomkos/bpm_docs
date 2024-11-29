# addCommentToCurrentCase operation

| Parameter    | Type   | Description                                                                                                                                                  |
|--------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId       | String | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window. |
| comment      | String | The comment that is to be added to the case.The comment must be 64 KB or less in size.                                                                       |
| return\_value | String | GUID of the new comment.To set the return value, click in the Expression field and select <Create return value>.                                             |