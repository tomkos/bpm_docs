# GET method for the list of discretionary activity types resource

## URI

/CASEREST/v1/casetype/{case type name}/discretionarytasktypes

| Name             | Type   | Description                                                                                         |
|------------------|--------|-----------------------------------------------------------------------------------------------------|
| {case type name} | String | The symbolic name of the case type for which the list of user-created activities is to be returned. |

| Name              | Type   | Required?   | Description                                                        |
|-------------------|--------|-------------|--------------------------------------------------------------------|
| TargetObjectStore | String | Yes         | The symbolic name of the object store that contains the case type. |

## Request content

The request for this method
contains no JSON content.

## Response content

| Property                  | Description                                                                                                                                                                                                                                                                                  |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description               | The description that is defined for the activity.                                                                                                                                                                                                                                            |
| HasInstanceCreationRights | A Boolean value that is set to true if the current user can create an instance of this activity type.                                                                                                                                                                                        |
| RequiresLaunchInfo        | A Boolean value that is set to true if the GET method for the create new activity resource must be called to obtain launch step information for the activity.If this property is set to true, the StepElement property is required for the POST method for the create new activity resource. |
| TaskClassId               | The GUID for the Task class.                                                                                                                                                                                                                                                                 |
| TaskDisplayName           | The name of the activity that is displayed in Case Client.                                                                                                                                                                                                                                   |
| TaskName                  | The symbolic name of the activity.                                                                                                                                                                                                                                                           |
| IsHidden                  | A Boolean value that is set to true if the activity is hidden from the user at run time.                                                                                                                                                                                                     |
| IsContainer               | A Boolean value that is set to true if the activity is a container activity.                                                                                                                                                                                                                 |

| Code                      | Description                                                                                                      |
|---------------------------|------------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully. The requested list of activity types was returned.                            |
| 400 Bad Request           | The required TargetObjectStore parameter was not specified or a parameter value was invalid.                     |
| 404 Not Found             | The case type specified in the request URI was not found.                                                        |
| 500 Internal Server Error | A server error occurred. For information about the error, refer to the userMessage element in the JSON response. |

## Example: GET method request

```
GET http://example.com:9080/CaseManager/CASEREST/v1/casetype
/AUTO\_CollisionClaim/discretionarytasktypes
?TargetObjectStore=MyTOS HTTP/1.1
Host: www.example.net
```

## Example: GET method response

```
#Response
HTTP/1.1 200 OK
Content-Type: application/json;charset-UTF-8
{
   "DiscretionaryTaskTypes":
   [
      {
         "TaskName": "AUTO\_ContactCustomer",
         "TaskDisplayName": "Contact Customer",
         "Description": "phone, email or write to the customer",
         "TaskClassId": "{76DE6D7A-FC7D-4AD0-A109-DB9B9E63E7AE}",
         "HasInstanceCreationRights": true,
         "RequiresLaunchInfo": true,
					"IsHidden": false,
					"IsContainer": false
      },
      {
         "TaskName": "AUTO\_ReadCollisionReport",
         "TaskDisplayName": "Read Collision Report",
         "Description": "read the collision report and police report",
         "TaskClassId": "{070AF241-C4FC-4E0A-86ED-BE017B68913F}",
         "HasInstanceCreationRights": true,
         "RequiresLaunchInfo":false,
					"IsHidden": false,
					"IsContainer": false
      }
      ...
   ]
}
```