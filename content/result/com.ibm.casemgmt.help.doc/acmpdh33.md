# getCasePropertyValues operation

| Parameter           | Type     | Description                                                                                                                                                              |
|---------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId              | String   | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window.             |
| customPropertyNames | String[] | Use the return value from the getCasePropertyNames operation.                                                                                                            |
| return\_value        | String[] | The CasePropertyValues value is an array of strings, containing the property values of the requested properties. This return value is used by the createCase operations. |