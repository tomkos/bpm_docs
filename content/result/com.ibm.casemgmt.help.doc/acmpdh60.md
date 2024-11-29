# completeCurrentCaseStage operation

When this operation completes, it returns a string that contains the name of the next case stage,
which is the new current case stage. If there is no next case stage, the string contains
CmAcmComplete.

| Parameter   | Type   | Description                                                                                                                                                  |
|-------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId      | String | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window. |