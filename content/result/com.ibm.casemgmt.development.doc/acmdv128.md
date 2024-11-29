# PUT method for the particular activity instance resource

To avoid unnecessary Content Platform Engine errors, the
PUT method ensures that the activity is in the correct state before the activity
is updated. If a case worker requests to disable an activity, the PUT method
ensures that the activity is not in a working or complete state. If the activity is in a working or
complete state, the method ignores the request. If a case worker requests to start an activity, the
PUT method ensures that the activity is in a ready state.

Because multiple case workers might decide an activity must be enabled, the
PUT method does not return an error when a request is made to enable an activity
that is already enabled. Instead, the method always returns an updated version of the activity.

## URI

/CASEREST/v1/task/{taskId}

| Name     | Type   | Description                                               |
|----------|--------|-----------------------------------------------------------|
| {taskId} | String | The GUID for the activity instance that is to be updated. |

| Name              | Type   | Required?   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------|--------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TargetObjectStore | String | Yes         | The symbolic name of the object store that contains the activity.A symbolic name is called a unique identifier in IBM® Business Automation Workflow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Grouping          | String | Yes         | The identifier that indicates grouping for the activities. You must set this parameter to ROD, which represents the following groups: Required This group includes activities for which the RequiredState property is set to REQUIRED\_BY\_USER or REQUIRED\_BY\_INCLUSIVE. Optional This group includes activities that are enabled and for which the RequiredState property is set to OPTIONAL. Disabled This group includes activities that are disabled and for which the DisabledState property is set to DISABLED\_BY\_USER, DISABLED\_BY\_EXCLUSIVE, or DISABLED\_BY\_ABORTED.  The PUT method does not return groups that are empty. |

## Request content

```
{
  "action": "<start or enable or disable or stop or restart>"     
}
```

## Response content

- The required state of the activity
- The disabled state of the activity
- The launch mode state of the activity
- The date the activity was created
- The activity identifier
- The activity name
- The activity number
- The date the activity was last modified

| Code                      | Description                                                                                                    |
|---------------------------|----------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully. No content is returned.                                                     |
| 400 Bad Request           | The TargetObjectStore parameter or the Grouping parameter was not specified, or a parameter value was invalid. |
| 404 Not Found             | The activity specified in the request URI was not found.                                                       |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response.    |

## Example: PUT method

```
PUT http://example.com:9080/CaseManager/CASEREST/v1/task
/7A75A997-0E42-406E-AZC4-EE55D7DER9PF?TargetObjectStore=MyExampleObjectStore
&Grouping=ROD HTTP 1.1
Host: www.example.net
{
  "Action": "disable"
}
```

```
#Response
HTTP/1.1 200 OK
Content-Type: application/json;charset-UTF-8
{
  "Required":
  [
    {
      "RequiredState": 1,
      "TaskState": 1,
      "DisabledState": 0,
      "LaunchMode": 4,
      "DateCreated": "2010-07-16T21:50:36Z",
      "TaskId": "{CB3F1916-8D03-44C8-9598-23589D9ED78F}",
      "TaskName": "ETECase2 Task number 1",
      "DateLastModified": "2010-07-16T21:50:36Z"
    }
  ]
}
```