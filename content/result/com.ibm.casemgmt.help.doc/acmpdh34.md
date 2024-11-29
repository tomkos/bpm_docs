# getCaseStructure operation

| Parameter    | Type     | Description                                                                                                                                                  |
|--------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId       | String   | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window. |
| return\_value | String[] | The CaseStructure value is an array of strings, containing the case structure as strings of the form folder\_path/=doc\_version\_series\_ID.                     |