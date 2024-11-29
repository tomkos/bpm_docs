# GET method for deployment status

## URI

/CASEREST/v1/solution/{solutionName}/deploymentstatus

| Name         | Type   | Required   | Description                    |
|--------------|--------|------------|--------------------------------|
| solutionName | String | Yes        | The name of the case solution. |

| Name              | Type   | Required   | Description                                                                                                          |
|-------------------|--------|------------|----------------------------------------------------------------------------------------------------------------------|
| TargetObjectStore | String | Yes        | The name of the object store where the solution is deployed.Note: The value is optional for development environment. |

## GET method request

```
https://example.com:9443/CaseManager/CASEREST/v1/solution/TestSolution/deploymentstatus?TargetObjectStore=tos
```

## GET method response

```
{
  "Status": "Completed",
  "ConnectionDefinitionId": "{4007A18B-0300-CF89-87C7-0BAFACE030D8}",
  "TestUrl": "https://example.com:9443/navigator/?desktop=baw&feature=Cases&tos=tos&solution=TS",
  "Synchronized": true,
  "SolutionId": "{8043A18B-0000-CE25-8CD0-35DB258318CA}",
  "PeConfigId": "{5047018B-0000-CC2B-A34A-BADFD99E54DE}",
  "Name": "TestSolution",
  "DateLastModified": "2023-11-05T20:55:08Z"
}
```