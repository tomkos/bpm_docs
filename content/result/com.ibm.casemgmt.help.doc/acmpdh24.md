# createCaseUsingSpecifiedCaseType operation

| Parameter            | Type      | Description                                                                                                                                                  |
|----------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseType             | String    | The case type name in symbolic form.                                                                                                                         |
| customPropertyNames  | String[ ] | Values that are returned from the getCasePropertyNames operation.                                                                                            |
| customPropertyValues | String[ ] | Values that are returned from the getCasePropertyValues operation.                                                                                           |
| caseStructure        | String[ ] | The case structure value that is returned from the getCaseStructure operation, passed as an array of strings of the form folder\_path/=doc\_version\_series\_ID. |
| return\_value         | String    | The GUID of the new case.                                                                                                                                    |