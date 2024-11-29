# GET method for the list of solutions resource

## URI

/CASEREST/v1/solutions

## Request content

The request for this method
contains no JSON content.

## Response content

- Solution name
- Name of the target object store to which the solution is deployed
- Deployment status
- Connection point
- Web application ID

| Code                      | Description                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully. The requested list of solutions was returned.                            |
| 404 Not Found             | No solutions were found.For information about the error, see the userMessage element in the JSON response.  |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response. |

## Example: GET method response

```
GET http://example.com:9080/CaseManager/CASEREST/v1/solutionsHTTP/1.1
Host: www.example.net
```

## Example: GET method response

```
HTTP/1.1 200 OK
Content-Type: application/json;charset-UTF-8
{
  "Solutions":
  [
    {
      "SolutionName": "Automobile Claims",
      "SolutionFolderId": "{659C6566-4A6B-4328-A89A-27D2D08D0A1B}",
      "Description": "Solution for processing automobile claims",
      "TargetOS": "AutomobileClaimsOS",
      "Status": "Completed",
      "PEConnectionPoint": "PECP1",
      "WebAppID": "ABC"
    },
    {
      "SolutionName": "Fire Insurance Claims",
      "SolutionFolderId": "{18389232-FE4D-4400-8215-0FFA5A3F2C88}",
      "Description": "Solution for processing fire damage",
      "TargetOS": "FireInsuranceOS",
      "Status": "Failed",
      "PEConnectionPoint": "PECP1",
      "WebAppID": "8"
    }
  ]
}
```