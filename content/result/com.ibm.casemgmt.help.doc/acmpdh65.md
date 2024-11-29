# setCasePropertyValues operation

| Parameter          | Type     | Description                                                                                                                                                  |
|--------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseId             | String   | The identifier of the case. You must set the expression for the caseID parameter to the F\_CaseFolder business object field in the Expression Builder window. |
| casePropertyNames  | String[] | The list of case properties to update.                                                                                                                       |
| casePropertyValues | String[] | The list of property values. The list length must have the same length as casePropertyNames.                                                                 |