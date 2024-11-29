# GET method for the list of activity instances resource

## URI

/CASEREST/v1/case/{case folder
id}/tasks

| Name             | Type   | Description                                                                                   |
|------------------|--------|-----------------------------------------------------------------------------------------------|
| {case folder id} | String | The GUID that identifies the root folder of the case for which activities are to be returned. |

| Name              | Type   | Required?   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------|--------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TargetObjectStore | String | Yes         | The symbolic name of the object store that contains the case.A symbolic name is called a unique identifier in IBM® Business Automation Workflow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Grouping          | String | Yes         | The identifier that indicates grouping for the activities. You must set this parameter to ROD, which represents the following groups: Required This group includes activities for which the RequiredState property is set to REQUIRED\_BY\_USER or REQUIRED\_BY\_INCLUSIVE. Optional This group includes activities that are enabled and for which the RequiredState property is set to OPTIONAL. Disabled This group includes activities that are disabled and for which the DisabledState property is set to DISABLED\_BY\_USER, DISABLED\_BY\_EXCLUSIVE, or DISABLED\_BY\_ABORTED.  The GET method does not return groups that are empty. The groups can be returned in any order. Within each group, the activities are ordered first by the activity state and then by the activity name. |

## Request content

The request for this method
contains no JSON content.

## Response content

- The required state of the activity
- The disabled state of the activity
- The launch mode state of the activity
- The date the activity was created
- The activity identifier
- The activity name
- The activity symbolic name
- The activity number
- The date the activity was last modified
- Whether the activity is hidden
- Whether the activity is a container
- The process instance ID
- The date the activity was last restarted
- The restart count
- The roster name

| Code                      | Description                                                                                                         |
|---------------------------|---------------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully and returned the requested list of activities.                                    |
| 400 Bad Request           | The required TargetObjectStore parameter or Grouping parameter was not specified, or a parameter value was invalid. |
| 404 Not Found             | The case folder that was specified in the request URI was not found.                                                |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response.         |

## Example: GET method request

```
GET http://example.com:9080/CaseManager/CASEREST/v1/case
/9E45A997-0E42-406E-AAC4-EE55D8BCF2ED/tasks
?TargetObjectStore=MyExampleObjectStore&Grouping=ROD
HTTP/1.1
Host: www.CaseMgmtExample.net
```

## Example: GET method response

```
#Response
HTTP/1.1 200 OK
Content-Type: application/json;charset-UTF-8
{
  "Optional":
  [
    {
      "RequiredState": 0, "TaskState": 3, "DisabledState": 0,
      "LaunchMode": 0, "DateCreated": "2010-07-16T21:50:36Z",
      "TaskId": "{3B5C8E64-43FE-4188-AC72-457A4B8E374C}",
      "TaskName": "ETECase2 Task number 2",
      "DateLastModified": "2010-07-16T21:50:36Z",
      "IsHidden": false,
      "IsContainer": false,
      "ProcessInstanceId": "0907E35E7DC03B4FA03F6B6767633FB2",
      "LastRestartDate": "2010-07-16T21:50:36Z",
      "RestartCount": "1",
      "RosterName": "MySolution1"
    }
  ],
  "Required":
  [
    {
      "RequiredState": 1, "TaskState": 1, "DisabledState": 0,
      "LaunchMode": 4, "DateCreated":"2010-07-16T21:50:36Z",
      "TaskId": "{CB3F1916-8D03-44C8-9598-23589D9ED78F}",
      "TaskName": "ETECase2 Task number 1",
      "DateLastModified": "2010-07-16T21:50:36Z"
      "IsHidden": false,
      "IsContainer": false,
      "ProcessInstanceId": "0907E35E7DC03B4FA03F6B6767633FB1",
      "LastRestartDate": null,
      "RestartCount": "0",
      "RosterName": "MySolution1"
    }
  ]
}
```