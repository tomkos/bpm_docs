# GET method for the create new activity resource

## URI

/CASEREST/v1/case/{case folder
id}/tasktype/{symbolic task name}

| Name                 | Type   | Description                                                                                |
|----------------------|--------|--------------------------------------------------------------------------------------------|
| {case folder id}     | String | The GUID that identifies the root folder of the case to which the activity is to be added. |
| {symbolic task name} | String | The symbolic name of the activity type to be used for the new activity.                    |

| Name              | Type   | Required?   | Description                                                   |
|-------------------|--------|-------------|---------------------------------------------------------------|
| TargetObjectStore | String | Yes         | The symbolic name of the object store that contains the case. |

## Request content

The request for this method
contains no JSON content.

## Response content

- Attachments
- System properties
- Workflow groups
- Data fields
- Step processor

| Code                      | Description                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully. The requested activity type information was returned.                    |
| 400 Bad Request           | The required TargetObjectStore parameter was not specified or a parameter value was invalid.                |
| 404 Not Found             | The case folder ID or the symbolic activity name specified in the request URI was not found.                |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response. |

## Example: GET method request

```
GET http://example.com:9080/CaseManager/CASEREST/v1/case
/12345678-abcd-dcba-4321-12345678/tasktype/
AUTO\_ContactCustomer?TargetObjectStore=MyTOS HTTP/1.1
Host: www.example.net
```

## Example: GET method response

```
HTTP/1.1 200 OK
Content-Type: application/json;charset-UTF-8
{
  "attachments": {},
  "systemProperties":
  {
    "responses": ["yes", "no"],
    "mapName": "Workflow",
    "stepId": 0,
    "stepName": "LaunchStep",
    "caseFolderId": "{8CA37883-9BA1-4513-AF94-120EA4255A2B}",
    "workflowName": "ETE\_ETECase3\_ETECase3Task1",
    "selectedResponse": "",
    "workObjectNumber": "D931E58C31E1DE44BDF519E88565614F",
    "subject": "ETE\_ETECase3\_ETECase3Task1",
    "authoredMapName": "Workflow",
    "instruction": ""
  },
  "workflowGroups":
  {
    "F\_Trackers":
    {
      "value" : [],
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
      "isArray":false
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
      "desc": "",
      "mode": 3,
      "modified": false,
      "type": 16,
      "name": "ETEProperty5",
      "isArray":false
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
```