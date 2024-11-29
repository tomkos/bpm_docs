# getCasePropertyNames operation

| Parameter    | Type     | Description                                                                                                                                                                                    |
|--------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId       | String   | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window.                                   |
| caseType     | String   | The case type to be used.                                                                                                                                                                      |
| return\_value | String[] | The CasePropertyNames value is an array of strings, containing the property names of the case. This return value is used by the createCase operations and the getCasePropertyValues operation. |