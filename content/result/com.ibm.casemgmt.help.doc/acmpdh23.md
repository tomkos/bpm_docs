# createCaseUsingSameCaseType operation

Before you use the createCaseUsingSameCaseType operation, use the getCasePropertyNames,
getCasePropertyValues, and getCaseStructure operations to get the appropriate return values. Use
these returned values for customPropertyNames,
customPropertyValues, and caseStructure parameters in the
createCaseUsingSameCaseType operation.

| Parameter            | Type      | Description                                                                                                                                                                                         |
|----------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId               | String    | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window.                                        |
| customPropertyNames  | String[ ] | An array of strings that contains the names of the case properties that are to be set for the new case. You can use the values returned from the getCasePropertyNames operation for this parameter. |
| customPropertyValues | String[ ] | An array of strings that contains the values they are returned from the getCasePropertyValues operation.                                                                                            |
| caseStructure        | String[ ] | The case structure value returned from the getCaseStructure operation, passed as an array of strings in the form folder\_path/=doc\_version\_series\_ID.                                                |
| return\_value         | String    | The GUID of the new case.                                                                                                                                                                           |