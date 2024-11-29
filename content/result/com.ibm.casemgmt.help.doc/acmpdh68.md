# enableSpecifiedCaseStage operation

Enables the specified case stage back to the list of existing case stages. The specified stage
must be disabled earlier. If the case stage is enabled successfully, it returns the name of the
enabled case stage. If the stage cannot be enabled, it returns an empty string.

| Parameter   | Type   | Description                                                                                                                                                  |
|-------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId      | String | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window. |
| stageName   | String | Symbolic name of a case stage.                                                                                                                               |