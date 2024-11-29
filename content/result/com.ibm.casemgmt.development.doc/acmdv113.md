# GET method for the list of case types resource

## URI

/CASEREST/v1/solution/{solution
name}/casetypes

| Name            | Type   | Description                                                                  |
|-----------------|--------|------------------------------------------------------------------------------|
| {solution name} | String | The name of the solution for which the list of case types is to be returned. |

| Name              | Type   | Required?   | Description                                                        |
|-------------------|--------|-------------|--------------------------------------------------------------------|
| TargetObjectStore | String | Yes         | The symbolic name of the object store that contains the case type. |

## Request content

The request for this method
contains no JSON content.

## Response content

These permissions are set when
you configure security by using IBM® Administration Console for
Content Platform Engine or by
using IBM Business Automation
Workflow
Case administration client. Permission to create a case is set by
selecting the Create instance right for the specific case type. Permission to
create a subfolder is set by selecting the Create subfolder right for the
case type folder.

These permissions are set when you configure security by using IBM Administration Console for
Content Platform Engine or by using IBM Business Automation
Workflow administration client.
Permission to create a case by splitting an existing case is set by
selecting the File in folder/Annotate right
for the case type folder.

| Code                      | Description                                                                                                                                                                                    |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully. The requested list of case types was returned.                                                                                                              |
| 400 Bad Request           | The required TargetObjectStore parameter was not specified or a parameter value was invalid.                                                                                                   |
| 404 Not Found             | Either the solution specified in the request URI was not found or no case types were found for the specified solution. For more information, see the userMessage element in the JSON response. |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response.                                                                                    |

## Example: GET method request

```
GET http://example.com:9080/CaseManager/CASEREST/v1/solution/Auto+Claims
/casetypes?TargetObjectStore=MyTOS HTTP/1.1
Host: www.example.net
```

## Example: GET method

```
HTTP/1.1 200 OK
Content-Type: application/json;charset-UTF-8
{
  "CaseTypes":
  [
    {
      "CaseType": "AUTO\_CollisionClaim",
      "DisplayName": "Collision Claim",
      "Description": "process a collision claim"
      "HasInstanceCreationRights": true,
      "HasAnnotationRights": true
    },
    {
      "CaseType": "AUTO\_LiabilityClaim",
      "DisplayName" : "Liability Claim",
      "Description": "process a liability claim"
      "HasInstanceCreationRights": true,
      "HasAnnotationRights": true
    },
    ...
  ]
}
```