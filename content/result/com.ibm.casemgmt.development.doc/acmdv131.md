# GET method for the case history resource

To make it easier to display the entries, the GET method
always returns a string value for the PropertyValue element,
regardless of the type of the property. Therefore, you do not convert
integer, float, or datetime properties for display.

## URI

/CASEREST/v1/case/{case folder
id}/history

| Name             | Type   | Description                                                                               |
|------------------|--------|-------------------------------------------------------------------------------------------|
| {case folder id} | String | The GUID that identifies the root folder of the case for which history is to be returned. |

```
&ObjectTypes=Document+CmAcmCaseFolder+CmAcmCaseSubfolder&EventTypes=Creation
```

| Name                 | Type    | Required?   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------|---------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TargetObjectStore    | String  | Yes         | The symbolic name of the object store that contains the case.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| BatchSize            | Integer | No          | The maximum number of entries to be returned. If you do not set this parameter, the method returns a maximum of 200 audit entries.Tip: For best results, set the BatchSize parameter to no more than 200.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ContinuationToken    | String  | No          | The value of the Continuation element that is returned in the JSON response for the previous call to the GET method. Omit this parameter from the request to retrieve the first batch of entries. Specify this parameter in the next request to retrieve the next batch of entries. Enter the value as follows (without quotation marks):ContinuationToken=34832908d930ddkdj390di3kj If the Continuation element that is returned in the JSON response contains a null string, there are no more entries to be returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ObjectTypes          | String  | No          | The object types for which entries are to be returned. Enter one or more object types by using spaces to separate multiple types. The following list identifies the symbolic names of Content Platform Engine objects that you might need: CmAcmCaseComment Return entries for comments on the case. CmAcmCaseFolder Return entries for case folders. CmAcmCaseSubfolder Return entries for case subfolders. CmAcmCaseTask Return entries for activities. CmAcmVersionSeriesComment Return entries for comments on a document. CmAcmWorkItemComment Return entries for comments on work items. Document Return entries for documents that are associated with the case.   When appropriate, the GET method returns entries for subclasses of the selected object types. For example, the GET method returns entries for subclasses of the Document object type automatically. You do not specify each subclass by name. If you do not specify the ObjectTypes parameter, the method returns entries for all object types. |
| EventTypes           | String  | No          | The type of event for which entries are to be returned. Enter one or more event types by using spaces to separate multiple types. You can query any subclass of the Content Platform Engine ObjectChangeEvent class.  If you do not specify the EventTypes parameter, the method returns entries for all event types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| AdditionalProperties | String  | No          | A list of the symbolic names of the properties to include in the "AdditionalProperties" JSON element in the returned payload. Enter one or more property names. Use spaces to separate multiple names. Note: Multi-value properties are supported from 24.0.0.0 release but Business Object is not supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| AdditionalFilter     | String  | No          | The property expression to be included in the WHERE clause of the case history query. This expression is a UTF-8 encoded URL, and must comply with Content Platform Engine SQL syntax.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Request content

The request for this method
contains no JSON content.

## Response content

| Code                      | Description                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully and returned the requested entries.                                       |
| 400 Bad Request           | The required TargetObjectStore parameter was not specified, or a parameter value was invalid.               |
| 404 Not Found             | The case folder that was specified in the request URI was not found.                                        |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response. |

## Retrieving batches of case history entries

The
first time that you call the GET method, you can
set the BatchSize parameter to specify the number
of entries. However, you do not set the ContinuationToken parameter.
The GET method returns the specified number of
entries in reverse chronological order, beginning with the newest
entry in the log. If there are more entries in the case history, the
method also returns a continuation token. You must include the continuation
token in the query parameters to retrieve the next batch of entries.

To
retrieve the next batch of entries, you make a second call to GET method
by using the same values for all parameters except the ContinuationToken parameter.
You set the ContinuationToken parameter to the
continuation token that is returned by the preceding method call.
The method then returns the next set of entries.

You can continue
to call the GET method by using the continuation
token to return all entries for the case. When there are no more entries,
the method does not return a continuation token.

To allow a
case worker to view the results that were returned in a previous call
to the GET method, you must maintain a string array
that contains the nonnull continuation tokens. You can then use the
array values to retrieve a specific batch of entries.

For example,
assume that you store the continuation tokens in an array named A and
that this array contains X tokens. X is
also the index of the array element in which the next continuation
token are stored. The initial value of X is 0 because
there are no continuation results in the array A.

When
the GET method returns the first batch of entries,
the continuation token in the response is saved in A[0] and
the value of X increases by one to 1 because it starts
from 0. When the GET method returns the second
batch of entries, the continuation token in the response is saved
in A[1] and the value of X increases by
one to 2.

- A[1] to retrieve the third batch of entries
- A[0] to retrieve the second batch of entries
- Null to retrieve the first batch of entries

- If X-1 >= 0, then A[X-1] is the continuation token that is
required to get the next batch of results.
- If X-2 is >= 0, then A[X-2] is the token that is required to
return the last batch of results again.
- A[X-3] is the token that is required to return the batch that
comes before the last batch of results again.

Before you use a continuation token to retrieve a previously
retrieved batch of results, you must decrease X correctly to ensure
that A[X-1] is the continuation token that is required to return the
next batch of results.

## Example: GET method request

```
#Request to get comment history of a particular case
GET http://example.com:9080/CaseManager/CASEREST/v1/case
/19278CB3-C71C-4DE5-95FE-7C7544020A31/history
?TargetObjectStore=ATOSME&BatchSize=5
&ObjectTypes=CmAcmCaseComment+CmAcmWorkItemComment+
CmAcmVersionSeriesComment&EventTypes=CreationEvent
HTTP/1.1
Host: www.example.net
```

## Example: GET method response

```
#Response
HTTP/1.1 200 OK
Content-Type: application/json;charset-UTF-8
{
  "ContinuationToken":"1,1118.0",
  "Events":
  [
    {
      "EventType":"CreationEvent",
      "EventObjectType":"CmAcmCaseComment",
      "EventTypeLocalizedName":"Creation Event",
      "EventObjectLocalizedName":"Case Comment",
      "EventUser":"P8Admin",
      "EventDateTime":"2010-08-18T18:04:51Z",
      "CmAcmCommentText":"Here is a comment on this case. 
        Not my first.",
      "AdditionalProperties":{"CmAcmCaseIdentifier":""}
    },
    {
      "EventType":"CreationEvent",
      "EventObjectType":"CmAcmVersionSeriesComment",
      "EventTypeLocalizedName":"Creation Event",
      "EventObjectLocalizedName":"Version Series Comment",
      "EventUser":"P8Admin",
      "EventDateTime":"2010-08-18T18:00:38Z",
      "CmAcmCommentText":
          "Test comment for CmAcmVersionSeriesComment.",
      "CmAcmObjectName":"This is the title of the document",
      "AdditionalProperties":{"CmAcmCaseIdentifier":""}
    },
    {
      "EventType":"CreationEvent",
      "EventObjectType":"CmAcmWorkItemComment",
      "EventTypeLocalizedName":"Creation Event",
      "EventObjectLocalizedName":"Work Item Comment",
      "EventUser":"P8Admin",
      "EventDateTime":"2010-08-18T18:00:16Z",
      "CmAcmCommentText":"This was the right resolution for this 
        work item.",
      "CmAcmTaskName":"ETECase1 Task number 1",
      "CmAcmStepName":"test\_step\_name",
      "AdditionalProperties":{"CmAcmCaseIdentifier":""}
    },
    {
      "EventType":"CmAcmCaseRelatedEvent",
      "EventTypeLocalizedName":"Case Related Event",
      "EventDateTime":"2011-06-10T22:53:59Z",
      "EventUser":"P8Admin",
      "EventObjectType":"CmAcmCaseFolder",
      "EventObjectLocalizedName":"Case Folder",
      "CmAcmCaseFolder":"{B4CD0C8E-8D1D-424A-A84F-1D2F6F4FB773}",
      "CmAcmRelatedCaseFolder":
          "{56872C9A-D84C-4316-BB49-0EB1062D5F34}",
      "CmAcmCaseTitle":"CTLT\_CT1\_000000100209",
      "CmAcmRelatedCaseTitle":"CTLT\_CT1\_000000100212",
      "CmAcmCaseIdentifier":"CTLT\_CT1\_000000100209",
      "CmAcmRelatedCaseIdentifier":"CTLT\_CT1\_000000100212",
      "CmAcmRelationshipType":101,
      "Description":
          "split case from poster - test for multi-value",
      "CmAcmCategoryName":null,
      "CmAcmRelatedCaseClassName":"CTLT\_CT1",
      "RelatedCaseClassLocalizedName":"CT1",
      "CmAcmObjectName":"000000100209",
      "AdditionalProperties":{"CmAcmCaseIdentifier":" 
         CTLT\_CT1\_000000100209"}
    },
    {
      "EventType":"CmAcmCaseRelatedEvent",
     "EventTypeLocalizedName":"Case Related Event",
     "EventDateTime":"2012-04-09T14:41:52Z",
     "EventUser":"P8Admin",
     "EventObjectType":"CmAcmCaseFolder",
     "EventObjectLocalizedName":"Case Folder",
     "CmAcmCaseFolder":"{B4CD0C8E-8D1D-424A-A84F-1D2F6F4FB773}",
     "CmAcmRelatedCaseFolder":
         "{56872C9A-D84C-4316-BB49-0EB1062D5F34}",
     "CmAcmCaseTitle":"CTLT\_CT1\_000000100209",
     "CmAcmRelatedCaseTitle":"CTLT\_CT1\_000000100212",
     "CmAcmCaseIdentifier":"CTLT\_CT1\_000000100209",
     "CmAcmRelatedCaseIdentifier":"CTLT\_CT1\_000000100212",
     "CmAcmRelationshipType":0,
     "Description":
         "relating case 1 to case 2 due to similar victim profile",
     "CmAcmObjectName":"000000100209",
     "CmAcmCategoryName":"victim profile",
     "CmAcmRelatedCaseClassName":"CTLT\_CT1", 
     "RelatedCaseClassLocalizedName":"CT1",
     "AdditionalProperties":
         {"CmAcmCaseIdentifier":" CTLT\_CT1\_000000100209"}
    },
    {
     "EventType":"CmAcmCaseRelatedEvent",
     "EventTypeLocalizedName":"Case Related Event",
     "EventDateTime":"2012-04-09T14:48:29Z",
     "EventUser":"P8Admin",
     "EventObjectType":"CmAcmCaseFolder",
     "EventObjectLocalizedName":"Case Folder",
     "CmAcmCaseFolder":"{B4CD0C8E-8D1D-424A-A84F-1D2F6F4FB773}",
     "CmAcmRelatedCaseFolder":"{56872C9A-D84C-4316-BB49-0EB1062D5F34}",
     "CmAcmCaseTitle":"CTLT\_CT1\_000000100209",
     "CmAcmRelatedCaseTitle":"CTLT\_CT1\_000000100212",
     "CmAcmCaseIdentifier":"CTLT\_CT1\_000000100209",
     "CmAcmRelatedCaseIdentifier":"CTLT\_CT1\_000000100212",
     "CmAcmRelationshipType":1,
     "Description":"unrelating case 1 from case 2",
     "CmAcmObjectName":"000000100209",
     "CmAcmCategoryName":"victim profile",
     "CmAcmRelatedCaseClassName":"CTLT\_CT1", 
     "RelatedCaseClassLocalizedName":"CT1",
     "AdditionalProperties":
         {"CmAcmCaseIdentifier":" CTLT\_CT1\_000000100209"}
    },
    {
     "EventType":"ChangeStateEvent", 
     "EventTypeLocalizedName":"Change State Event", 
     "EventDateTime":"2012-04-14T01:28:52Z", 
     "EventUser":"P8Admin", 
     "EventObjectType":"CmAcmCaseTask", 
     "EventObjectLocalizedName":"Case Task", 
     "CmAcmObjectState":4, 
     "CmAcmLastRestartDate":"", 
     "CmAcmRestartCount":null, 
     "CmAcmDisabledState":0, 
     "CmAcmObjectName":"Case1AutomaticTask2"
    }
    ...
  ]
}
```