# GET method for the case comments resource

## URI

/CASEREST/v1/case/{case folder
id}/comments

| Name             | Type   | Description                                                                                 |
|------------------|--------|---------------------------------------------------------------------------------------------|
| {case folder id} | String | The GUID that identifies the root folder of the case for which comments are to be returned. |

| Name              | Type   | Required?   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------|--------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TargetObjectStore | String | Yes         | The symbolic name of the object store that contains the case.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| CommentType       | String | Yes         | One of the following values to indicate the type of comments to be returned: Activity Case Document WorkItem                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ItemId            | String | No          | The identifier that indicates the specific document or activity or work item for which comments are to be returned. For a document, specify the version series ID. For an activity or a work item, specify the GUID for the activity.You must specify this parameter if you set the CommentType parameter to Activity, Document, or WorkItem. Do not specify this parameter if you set the CommentType parameter to Case.                                                                                                                                                    |
| WorkflowNumber    | String | No          | The workflow number that indicates the specific work item for which comments are to be returned.This parameter is optional if the CommentType parameter is set to WorkItem. If you do not specify this parameter, the GET method returns all work item comments for the matching activity. Work items are always associated with an activity. Tip: After a work item completes, it no longer exists. Access to the work item is not possible. However, if you have the workflow number for the work item, you can still retrieve the individual comments for that work item. |

## Request content

The request for this method
contains no JSON content.

## Response content

- The name of the person who created the comment
- The date the comment was created
- The comment text
- The comment context that indicates the action, such as adding
a case or a document, that was being taken when the comment was created

| Code                      | Description                                                                                                            |
|---------------------------|------------------------------------------------------------------------------------------------------------------------|
| 201 Created               | The method completed successfully and returned the requested case comments.                                            |
| 400 Bad Request           | The required TargetObjectStore parameter or CommentType parameter was not specified, or a parameter value was invalid. |
| 404 Not Found             | The case folder that was specified in the request URI was not found.                                                   |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response.            |

## Example: GET method request

```
GET http://example.com:9080/CaseManager/CASEREST/v1/case
/9E45A997-0E42-406E-AAC4-EE55D8BCF2ED/comments?
TargetObjectStore=MyExampleObjectStore&CommentType=Case HTTP 1.1
Host: www.example.net
```

## Example: GET method

```
{
  "Comments":
  [
    { 
      "Id": "{5E42A997-0F47-446E-AFC4-EE55D8BCF5PP}",
      "Creator": "Bob",
      "CommentContext": 101,
      "DateCreated": "2010-04-07T14:30Z",
      "CommentText": "New request from Bob at GimmeCars.com" 
    },
    { 
      "Id": "{9E45A997-0E42-406E-AAC4-EE55D8BCF2EA}",
      "Creator": "Mary",
      "CommentContext": 102,
      "DateCreated": "2010-04-07T15:30Z",
      "CommentText": "Fast-track Bob's request – very good customer" 
    }
  ]
}
```