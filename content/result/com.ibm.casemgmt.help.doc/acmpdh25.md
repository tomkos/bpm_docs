# createDiscretionaryTaskInCurrentCase operation

| Parameter             | Type   | Description                                                                                                                                                  |
|-----------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId                | String | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window. |
| discretionaryTaskName | String | The symbolic name of the discretionary activity. The name format must be PREFIX\_ActivityName.                                                                |
| return\_value          | String | The GUID of the new activity.                                                                                                                                |