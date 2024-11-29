# POST method for deploying case solutions

## URI

/CASEREST/v1/solutions

| Name                     | Type   | Required?   | Description                                                                                                                                                                 |
|--------------------------|--------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| solutionName             | String | Yes         | The name of the case solution.                                                                                                                                              |
| ConnectionDefinitionName | String | Yes         | Operations: The name of the connection definition.Note: The value is optional for development environment.                                                                  |
| IgnoreLocks              | String | Optional    | Value that helps to determine whether the locks in the solution need to be ignored or not. Possible values: True False  The default value is false                          |
| DeployIncrementally      | String | Optional    | Value that helps determine whether only the changed artifacts of solution or complete solution need to be deployed. Possible values: True False  The default value is false |

## POST method request

```
https://example.com:9443/CaseManager/CASEREST/v1/solutions?solutionName=TestSolution&ConnectionDefinitionName=dev\_env\_connection\_definition&IgnoreLocks=false&DeployIncrementally=false
```

## POST method response

```
{
  "Status": "Initiated",
  "Error Info": "NONE",
  "SolutionName": "TestSolution"
}
```