# Get method for associated object stores

## URI

/CaseManager/CASEREST/v1/solution/{solutionAcronym}/associatedobjectstores

| Name            | Type   | Required   | Description                       |
|-----------------|--------|------------|-----------------------------------|
| solutionAcronym | String | Yes        | The acronym of the case solution. |

## GET method request

```
https://example.com:9443/CaseManager/CASEREST/v1/solution/TS/associatedobjectstores
```

## GET method response

```
{
  "DesignObjectStore": "dos",
  "TargetObjectStore": [
    "tos"
  ]
}
```