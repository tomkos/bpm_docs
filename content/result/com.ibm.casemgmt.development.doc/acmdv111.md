# GET method for the list of document classes resource

## URI

/CASEREST/v1/solution/{solution
name}/documenttypes

| Name            | Type   | Required?   | Description                                                                        |
|-----------------|--------|-------------|------------------------------------------------------------------------------------|
| {solution name} | String | No          | The name of the solution for which the list of document classes is to be returned. |

| Name              | Type   | Required?   | Description                                                        |
|-------------------|--------|-------------|--------------------------------------------------------------------|
| TargetObjectStore | String | Yes         | The symbolic name of the object store that contains the case type. |

## Request content

The request for this method
contains no JSON content.

## Response content

- The name of the document class or item type.
- The identifier of the item type. No identifier is returned for a document class.
- The name that is displayed for the document class or item type.
- The description of the document class or item type.
- A Boolean value that is set to true if the case worker has permission to create a document of
this document class or item type. This value is always set to true for an item type.

| Code                      | Description                                                                                                                                                                |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully. The requested list of document classes was returned.                                                                                    |
| 400 Bad Request           | The required TargetObjectStore parameter was not specified or a parameter value was invalid.                                                                               |
| 404 Not Found             | No document classes were found for the solution or the specified solution was not found.For information about the error, see the userMessage element in the JSON response. |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response.                                                                |

## Example: GET method request

This sample code requests a list of all document classes that are defined for the Auto Claims
solution:

```
#Request to get the document classes of a deployed solution
GET /CASEREST/v1/solution/Auto+Claims/documenttypes
?TargetObjectStore=MyTOS HTTP/1.1
Host: www.example.net
```

## Example: GET method response for
a Content Platform Engine object store

```
#Response
HTTP/1.1 200 OK
Content-Type: application/json;charset-UTF-8
{
    "DocumentTypes":
    [
        {
            "DocumentType": "AUTO\_CollisionClaim",
            "DisplayName": "Collision Claim",
            "Description": "collision claim",
            "HasInstanceCreationRights": true
        },
        {
            "DocumentType": "Correspondence",
            "DisplayName": "Correspondence",
            "Description": "client correspondence",
            "HasInstanceCreationRights": true
        },
        ...
    ]
}
```