# POST method for the create new activity resource

## URI

/CASEREST/v1/case/{case folder
id}/tasks

| Name             | Type   | Description                                                                                |
|------------------|--------|--------------------------------------------------------------------------------------------|
| {case folder id} | String | The GUID that identifies the root folder of the case to which the activity is to be added. |

## Request content

- A 201 Created response code is returned if the initial POST request was never
received by the server, but the second request was received and successfully processed.
- A 200 OK response code is returned if the initial POST request was received
by the server and successfully processed, but the response was lost. In this situation, the second
request is treated as a duplicate POST request.
- Any other return code indicates that an error occurred.

```
Content-Type: charset.json;charset-UTF-8
{   "TaskTypeName": "<Symbolic activity type name>",
    "TaskName": "<Activity name to create>",
    "StepElement": <JSON object returned by previous GET method>
}
```

| Name         | Type   | Required?   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------|--------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TaskTypeName | String | Yes         | The symbolic name of the activity type.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| TaskName     | String | Yes         | The name of the activity that is being created.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| StepElement  | Object | No          | A JSON object that contains the information that is required to launch the activity.The StepElement parameter is required if the RequiresLaunchInfo property that is returned by the GET method for the list of discretionary activity types resource is set to true.Note: For information about the JSON representation for step elements, see the section "JSON representation for step elements" in the IBM® FileNet® P8 Platform help topic Process Engine REST Service Reference. |

## Response content

| Code                      | Description                                                                                                                                                                                                          |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 201 Created               | The method completed successfully. The workflow that is associated with the activity is started.                                                                                                                     |
| 200 OK                    | A duplicate POST request was detected, so the method does not create an activity or start the workflow. However, the response that is returned is the same as the response that is returned for the initial request. |
| 400 Bad Request           | The required TargetObjectStore parameter was missing, or a parameter value was invalid.                                                                                                                              |
| 404 Not Found             | The case folder specified in the request was not found.                                                                                                                                                              |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response.                                                                                                          |

## Example: POST method request

```
POST http://example.com:9080/CaseManager/CASEREST/v1/case
/9E45A997-0E42-406E-AAC4-EE55D8BCF2ED/tasks?
TargetObjectStore=MyExampleObjectStore HTTP/1.1
Host: www.CaseMgmtExample.net
Content-Type: charset.json;charset-UTF-8
{
  "TaskTypeName": "AUTO\_TakeCustomerToLunch",
  "TaskName": "Take customer to lunch",
  "StepElement":
  {
    "attachments": {},
    "systemProperties":
    {
      "responses": ["yes","no"],
      "mapName": "Workflow",
      "stepId": 0,
      "stepName": "LaunchStep",
      "caseFolderId": "{8CA37883-9BA1-4513-AF94-120EA4255A2B}",
      "workflowName": "ETE\_ETECase3\_ETECase3Task1",
      "selectedResponse": "yes",
      "workObjectNumber": "D931E58C31E1DE44BDF519E88565614F",
      "subject": "ETE\_ETECase3\_ETECase3Task1",
      "authoredMapName": "Workflow",
      "instruction": ""
    },
    "workflowGroups":
    {
      "F\_Trackers":
      {
        "value": [],
        "desc": "",
        "mode": 3,
        "modified": false,
        "type": 64,
        "name": "F\_Trackers",
        "isArray": true
      }
    },
    "dataFields":
    {
      "ETEProperty1":
      {
        "value": true,
        "desc": "", 
        "mode": 3,
        "modified": false,
        "type": 4,
        "name": "ETEProperty1", 
        "isArray": false
      },
      "ETEProperty2":
      {
        "value": 163,
        "desc": "",
        "mode": 3,
        "modified": false,
        "type": 1,
        "name": "ETEProperty2",
        "isArray": false
      },
      "ETEProperty3":
      {
        "value": "TestStringChoice1",
        "desc": "",
        "mode": 3,
        "modified": false,
        "type": 2,
        "name": "ETEProperty3",
        "isArray": false
      },
      "ETEProperty4":
      {
        "value": 3.1415926535,
        "desc": "",
        "mode": 3,
        "modified": false,
        "type": 8,
        "name": "ETEProperty4",
        "isArray": false
      },
      "ETEProperty5":
      {
        "value": "2010-07-05T19:21:24Z",
        "desc":"",
        "mode": 3,
        "modified": false,
        "type": 16,
        "name": "ETEProperty5",
        "isArray": false
      }
    },
    "stepProcessor":
    {
      "width":800,
      "height":600,
      "applicationName":"",
      "appType":32,
      "id":455,
      "name":"ETE\_LaunchPage",
      "processorType":4,
      "locations":{"8":"123456"}
    }
  }
}
```

## Example: POST method response

```
HTTP/1.1 201 Created
Location: http://www.CaseMgmtExample.net/task/{task ID}
Content-Location: http://www.CaseMgmtExample.net/task/{task ID}
Content-Type: application/json;charset-UTF-8
{  
  "TaskId": "{CB3F1916-8D03-44C8-9598-23589D9ED78F}"
}
```