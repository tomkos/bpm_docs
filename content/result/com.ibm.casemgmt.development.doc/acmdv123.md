# GET method for the status of particular case resource

## URI

/CASEREST/v1/case/{case folder
id}/status

| Name             | Type   | Description                                                                              |
|------------------|--------|------------------------------------------------------------------------------------------|
| {case folder id} | String | The GUID that identifies the root folder of the case for which status is to be returned. |

| Name              | Type   | Required?   | Description                                                                                                                                           |
|-------------------|--------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| TargetObjectStore | String | Yes         | The symbolic name of the object store that contains the case type.A symbolic name is called a unique identifier in IBM® Business Automation Workflow. |

## Request content

The request for this method
contains no JSON content.

## Response content

| Value        | Description                                                                                                                   |
|--------------|-------------------------------------------------------------------------------------------------------------------------------|
| Complete     | All activities that are associated with the case are completed.                                                               |
| Failed       | The case was not created. The response might still include a case ID and a case creation date if the case folder was created. |
| Initializing | The case is being created, but is not yet ready to be worked on.                                                              |
| New          | The process of creating the case started.                                                                                     |
| Working      | The case was created and is ready to be worked on.                                                                            |

| Code                      | Description                                                                                                                   |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully. The response that is returned by the GET method includes the status of the specified case. |
| 400 Bad Request           | The required TargetObjectStore parameter was missing, or the parameter value was invalid.                                     |
| 404 Not Found             | The case specified in the request was not found.                                                                              |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response.                   |

## Example: GET method request

```
#Request 
GET /CASEREST/v1/case/9E45A997-0E42-406E-AAC4-EE55D8BCF2ED/status
?TargetObjectStore=MyExampleObjectStore
 HTTP/1.1
Host: www.CaseMgmtExample.net
```

## Example: GET method

```
#Response
  HTTP/1.1 200 OK
  Content-Type: application/json;charset-UTF-8
{
    "Status": "Working",
    "CaseIdentifier":"MY\_Case\_000000100105",
    "DateCreated":" 2010-07-16T21:50:36Z",
    "DateLastModified":"2010-07-16T21:50:36Z"
}
```