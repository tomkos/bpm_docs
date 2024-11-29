# GET method for the case page resource

## URI

/CASEREST/v1/casetype/{case
type name}/page

| Name             | Type   | Description                         |
|------------------|--------|-------------------------------------|
| {case type name} | String | The symbolic name of the case type. |

| Name              | Type   | Required?   | Description                                                                                                                                                                                                                                                                                                                    |
|-------------------|--------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TargetObjectStore | String | Yes         | The symbolic name of the object store that contains the case type.                                                                                                                                                                                                                                                             |
| PageType          | String | Yes         | One of the following values that indicates the page for which the ID is to be returned: CaseCreationPage Returns the ID for the Add Case page. CasePage Returns the ID for the Case Details page. CaseSplitPage Returns the ID for the Split Case page.                                                                        |
| Role              | String | No          | The name of the role for which the Case Details page ID is to be returned.Specify this parameter when the PageType parameter is set to CasePage to return the ID of the Case Details page that is used for a specific role. This parameter is not valid if the PageType parameter is set to CaseCreationPage or CaseSplitPage. |

## Request content

The request for this method
contains no JSON content.

## Response content

The method returns the
page ID of the specified page type for the case type.

| Code                      | Description                                                                                                         |
|---------------------------|---------------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully and returned the requested page ID.                                               |
| 400 Bad Request           | The required TargetObjectStore parameter or PageType parameter was not specified, or a parameter value was invalid. |
| 404 Not Found             | The case folder that was specified in the request URI was not found.                                                |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response.         |

## Example: GET method request

```
GET http://example.com:9080/CaseManager/CASEREST/v1/casetype
/AUTO\_CollisionClaim/page?TargetObjectStore=MyTOS
&PageType=CasePage&Role=caseWorker HTTP/1.1
Host: www.example.net
```

## Example: GET method response

```
HTTP/1.1 200 OK
Content-Type: application/json;charset-UTF-8
{
  "PhysicalPageId": "e134f49999c112399a"
}
```