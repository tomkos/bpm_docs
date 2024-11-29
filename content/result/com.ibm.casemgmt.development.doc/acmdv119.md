# POST method for the cases resource

The property values that are submitted in
the POST method request are validated by Content Platform Engine. If you use an external
data service for the case type, the property values in the request
are also validated by the IBM® Business Automation
Workflow REST
protocol against the values that are returned by the service. The
protocol validates the values against any property attributes that
are set by the service, such as the minimum value, maximum value,
and choice list.

When the case is saved, the value
that was specified for a property in Case Client is persisted for the
case if the value meets the constraints that are set by the external
data service. If a value is not specified for a property in Case Client, the external data service
can set a value that is persisted for the case.

## URI

/CASEREST/v1/cases

## Request content

```
{
  "CaseType": "<case type symbolic name>",
  "TargetObjectStore": "<target object store name>",
  "ReturnUpdates": <true or false>,
  "ExternalDataIdentifier" : "<string set by external data service">,
  "Properties" :
  [ // the array of case property values may be empty
    {
      "SymbolicName": "<symbolic name of case property>",
      "Value" : <property value>
    },
    ...
  ]
  "ClientContext":
  {
    "<key>":"<value>",
    // More key value pairs
  }
}}
```

| Name                     | Type    | Required?   | Description                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------|---------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CaseType                 | String  | Yes         | The symbolic name that is assigned to the case type.                                                                                                                                                                                                                                                                                                                                                     |
| TargetObjectStore        | String  | Yes         | The symbolic name of the object store that contains the case.A symbolic name is called a unique identifier in IBM Business Automation Workflow.                                                                                                                                                                                                                                                          |
| ReturnUpdates            | Boolean | No          | A Boolean value that indicates whether the method is to return the property values after the case is created. Set this parameter to true to force the method to return the case property values.By default, this parameter is set to false.                                                                                                                                                              |
| ExternalData  Identifier | String  | No          | A string that indicates the state of the data that was returned by the external data service.Tip: Include this parameter in the request if a value was provided in response to a previous call to get data from the external data service.                                                                                                                                                               |
| Properties               | Array   | No          | An array that contains values for the properties that are defined for the case type. For each property, you specify the symbolic name of the property and the value for the property.Important: The value that is specified for the property must match the data type of the property. You can use the particular case type resource to get a list of the properties that are defined for the case type. |
| ClientContext            | Array   | No          | An array that contains a series of key value pairs that specify contextual information for a specific work item. This parameter is used to send information to an external data service when a case worker opens the work item.                                                                                                                                                                          |

## Response content

| Code                      | Description                                                                                                        |
|---------------------------|--------------------------------------------------------------------------------------------------------------------|
| 201 Created               | The method completed successfully. The POST method returns the identifier that is assigned to the new case folder. |
| 400 Bad Request           | One of the required parameters was missing, or a parameter value was invalid.                                      |
| 404 Not Found             | The case type that was specified in the request was not found.                                                     |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response.        |

## Example: POST method request

This sample code requests a case of the AUTO\_CollisionClaim case type, which includes a
AUTO\_PersonsBO business object property that to be created and the property values that to be
returned after the case is created.

```
POST http: //example.com:9080/CaseManager/CASEREST/v1/cases
HTTP / 1.1
Host: www.CaseMgmtExample.net
Content - Type: charset.json;
charset - UTF - 8{
    "CaseType": "AUTO\_CollisionClaim",
    "TargetObjectStore": "ATOSME",
    "ReturnUpdates": false,
    "Properties":
    [{
            "SymbolicName": "AUTO\_ClaimDate",
            "Value": "2010-07-16T21:50:36Z",
        }, {
            "SymbolicName": "AUTO\_PersonsBO",
            "Value": [{
                    "Properties": [{
                            "SymbolicName": "AUTO\_Age",
                            "Value": "45",
                        }, {
                            "SymbolicName": "AUTO\_FirstName",
                            "Value": "John",
                        }, {
                            "SymbolicName": "AUTO\_LastName",
                            "Value": "Doe",
                        }
                    ]
                }, {
                    "Properties": [{
                            "SymbolicName": "AUTO\_Age",
                            "Value": "45",
                        }, {
                            "SymbolicName": "AUTO\_FirstName",
                            "Value": "Jane",
                        }, {
                            "SymbolicName": "AUTO\_LastName",
                            "Value": "Doe",
                        }
                    ]
                }
            ]
        }
    ]
}
```

## Example: POST method response

```
HTTP 1.1 201 OK Created
Content-Type: application/json;charset-UTF-8
{
  "CaseTitle": "DH2\_MyCase\_000000100402", 
  "CaseIdentifier": "DH2\_MyCase\_000000100402", 
  "CaseFolderId": "{A42BE8EB-848F-4CBD-B2F7-64FAF2CE7081}"
}
```