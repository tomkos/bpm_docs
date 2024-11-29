# GET method for the related cases for a particular case resource

## URI

/CASEREST/v1/case/{case folder
id}/cases

| Name             | Type   | Description                                                                                      |
|------------------|--------|--------------------------------------------------------------------------------------------------|
| {case folder id} | String | The GUID that identifies the root folder of the case for which related cases are to be returned. |

| Name                 | Type   | Required?   | Description                                                                                                                                                                                                                                     |
|----------------------|--------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TargetObjectStore    | String | Yes         | The symbolic name of the object store that contains the case.A symbolic name is called a unique identifier in IBM® Business Automation Workflow.                                                                                                |
| RelationshipType     | String | No          | The type of relationship between the case that is returned and the case that is initiating the request. Use this parameter to filter the results by the type of relationship.                                                                   |
| RelationshipCategory | String | No          | The category of the relationship between the case that is returned and the case that is initiating the request. Use this parameter to filter the results by the category of relationship. Use this parameter only if RelationType is "Related". |

## Request content

The request for this method
contains no JSON content.

## Response content

- Status
- Case title
- Case identifier
- Date created
- Creator
- Relationship type
- Relationship ID
- Relationship category

| Code                      | Description                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------|
| 201 Created               | The method completed successfully and returned the requested case comments.                                 |
| 400 Bad Request           | The required TargetObjectStore parameter was not specified, or the parameter value was invalid.             |
| 404 Not Found             | The case folder that was specified in the request URI was not found.                                        |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response. |

## Example: GET method request

```
#Request 
GET /CASEREST/v1/case/9E45A997-0E42-406E-AAC4-EE55D8BCF2ED/cases
?TargetObjectStore=MyExampleObjectStore
 HTTP/1.1
Host: www.CaseMgmtExample.net
```

## Example: GET method response

```
#Response
   HTTP/1.1 200 OK
   Content-Type: application/json;charset-UTF-8
[
{
    "Status": "Working",
    "CaseTitle": "MY\_Case\_000000100105",
    "CaseIdentifier":"MY\_Case\_000000100105",
    "CaseFolderId":"1D56A997-0E42-406E-AAC4-EE55D8BCF2ED",
    "DateCreated":" 2010-07-16T21:50:36Z",
    "Creator": "Admin",
    "RelationshipType": "split source",
    "RelationshipId": "{12345678-1234-1234-1234-aabbccddeeff}"
},
{
    "Status": "Working",
    "CaseTitle": "MyCaseTitle",
    "CaseIdentifier":"MY\_Case\_000000100106",
    "CaseFolderId":"2E67A997-0E42-406E-AAC4-EE55D8BCF2ED",
    "DateCreated":" 2010-07-16T21:50:36Z",
    "Creator": "Admin",
    "RelationshipType": "split target",
    "RelationshipID": "{22345678-1234-1234-1234-aabbccddeeff"}
},
{
    "Status": "Working",
    "CaseTitle": "MY\_Case\_000000100107",
    "CaseIdentifier":"MY\_Case\_000000100107",
    "CaseFolderId":"3F47B997-0E42-406E-AAC4-EE55D8BCF2ED",
    "DateCreated":" 2010-07-16T21:50:36Z",
    "Creator": "Admin",
    "RelationshipType": "split target"
    "RelationshipID": "{32345678-1234-1234-1234-aabbccddeeff"}
},
{
    "Status": "Working",
    "CaseTitle": "MY\_Case\_000000100107",
    "CaseIdentifier": "MY\_Case\_000000100107",
    "CaseFolderId": "3F47B997-0E42-406E-AAC4-EE55D8BCF2ED",
    "DateCreated": "2010-07-16T21:50:36Z",
    "Creator": "Admin",
    "RelationshipType”: "Related",
    "RelationshipId": "{42345678-1234-1234-1234-aabbccddeeff}",
    "RelationshipCategory": "user profile"
}]
```