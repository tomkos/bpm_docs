# POST method for the case comments resource

## URI

/CASEREST/v1/case/{case folder
id}/comments

| Name             | Type   | Description                                                                               |
|------------------|--------|-------------------------------------------------------------------------------------------|
| {case folder id} | String | The GUID that identifies the root folder of the case to which the comment is to be added. |

| Name              | Type   | Required?   | Description                                                   |
|-------------------|--------|-------------|---------------------------------------------------------------|
| TargetObjectStore | String | Yes         | The symbolic name of the object store that contains the case. |

## Request content

| Request element   | Comment types                       | Description                                                                                                                                                                                                                                       |
|-------------------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CommentType       | Case, document, activity, work item | One of the following values that indicates the type of comments to be returned: Activity Case Document WorkItem                                                                                                                                   |
| CommentContext    | Case, document, activity, work item | A number that indicates the action, such as adding a document or case, that was being taken when this comment was created. This value is based on the choice list that is defined in the CmAcmActionChoiceList object in the target object store. |
| CommentText       | Case, document, activity, work item | A string that contains the text for the comment.                                                                                                                                                                                                  |
| ItemId            | Document, activity, work item       | The identifier that indicates the specific document, activity, or work item for which the comment is to be added. For a document, specify the version series ID. For an activity or a work item, specify the GUID for the activity.               |
| DocumentTitle     | Document                            | The title that is assigned to the document in Content Platform Engine.                                                                                                                                                                            |
| WorkClassName     | Work item                           | The name of the work class that describes the attributes of the work item, such as data fields, a security configuration, and event logging options. In most cases, a work class corresponds to a workflow roster.                                |
| StepName          | Work item                           | The name of the step that contains the work item.                                                                                                                                                                                                 |
| WorkflowNumber    | Work item                           | The work object number that indicates the specific work item for which comments are to be returned.                                                                                                                                               |
| Response          | Work item                           | The response that was used to process the work item.                                                                                                                                                                                              |

## Response content

- The comment context, which indicates the action that was being
taken when this comment was created
- The date the comment was created
- The comment identifier
- The text of the comment
- The creator of the comment

| Code                      | Description                                                                                                                                                                                             |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully. The new comment was added to the case. The response header includes the URI for the comment.                                                                         |
| 400 Bad Request           | One of the required parameters was not specified, or a parameter value was invalid. For information about the error, see the userMessage element in the JSON response that was returned by this method. |
| 404 Not Found             | The case folder that was specified in the request URI was not found.                                                                                                                                    |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response that was returned by this method.                                                            |

## Example: POST method request

```
POST http://example.com:9080/CaseManager/CASEREST/v1/case/
9E45A997-0E42-406E-AAC4-EE55D8BCF2ED/comments?
TargetObjectStore=MyExampleObjectStore HTTP 1.1
Host: www.example.net
{
  "CommentType" : "Document",
  "CommentContext" : 402,
  "CommentText" : "this is a sample comment for a document in a case",
  "ItemId" : "B9BA42F3-CD30-4C93-BE8B-BDE0BC85AA4F",
  "DocumentTitle" : "Sample Document for My Case" 
}
```

## Example: POST method response

```
201 Created
{
  "CommentContext":402,
  "DateCreated":"2010-07-21T23:15:40Z",
  "Id":"{C1D63E6A-0CEC-433E-A6B9-C0EA0FDEFB53}",
  "CommentText":"This is a sample comment for a document in a case",
  "Creator":"P8Admin"
}
```

## Example: JSON payload for an activity comment

```
{
  "CommentType" : "Activity",
  "CommentContext" : 202,
  "CommentText" : "This is a sample comment for an activity in a case",
  "ItemId" : "B4DD9C04-46B4-4295-8EA0-1C0DB95C6C74" 
}
```

## Example: JSON payload for a work item comment

```
{
  "CommentType" : "WorkItem",
  "CommentContext" : 301,
  "CommentText" : "This is a sample comment for a work item in a case",
  "ItemId" : "B4DD9C04-46B4-4295-8EA0-1C0DB95C6C74",
  "WorkClassName" : "\_work\_class\_name",
  "StepName" : "test\_step\_name",
  "Response" : "test\_response",
  "WorkflowNumber" : "78FE3D3856F047408B29ECA140EE90B7"
}
```