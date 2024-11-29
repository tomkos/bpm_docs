# disableSpecifiedCaseStage operation

When the operation completes, it returns a string value that contains the symbolic name of the
next case stage. If the stage cannot be disabled, an empty string is returned. If there is no next
stage after the disabled stage, it returns an empty string.

| Parameter   | Type   | Description                                                                                                                                                  |
|-------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId      | String | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window. |
| stageName   | String | Symbolic name of a case stage.                                                                                                                               |