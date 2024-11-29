# PUT method for the particular case instance resource

The property values that are submitted in the PUT method
request are validated by Content Platform Engine.
If you use an external data service for the case type, the property
values in the request are also validated by the service. The service
validates the values against any property attributes that are set
by the service, which include the minimum value, maximum value, and
choice list.

When the case is saved, the value that was specified
for a property in Case Client is
persisted for the case if the value meets the constraints set by the
external data service. If a value is not specified for a property
in Case Client, the external
data service can set a value that is persisted for the case.

## URI

/CASEREST/v1/case/{case folder
id}

| Name             | Type   | Description                                                                                                 |
|------------------|--------|-------------------------------------------------------------------------------------------------------------|
| {case folder id} | String | The GUID that identifies the root folder of the case for which the PUT method is to update property values. |

## Request content

```
{
    "TargetObjectStore": "<target object store name>",
    "ExternalDataIdentifier" : "<string set by external data service>",
    "ReturnUpdates": <true or false>
    "Properties" :
    [ // the array of case property values can be empty
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
}
```

| Name                     | Type    | Required?   | Description                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------|---------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TargetObjectStore        | String  | Yes         | The symbolic name of the object store that is to contain the new case.A symbolic name is called a unique identifier in IBM® Business Automation Workflow.                                                                                                                                                                                                                                                |
| ExternalData  Identifier | String  | No          | A string that indicates the state of the data that was returned by the external data service.Tip: Include this parameter in the request if a value was provided in response to a previous call to get data from the external data service.                                                                                                                                                               |
| ReturnUpdates            | Boolean | No          | A Boolean value that indicates whether the method is to return the updated case property values. Set this parameter to true to force the method to return the case property values.By default, this parameter is set to false.                                                                                                                                                                           |
| Properties               | Array   | No          | An array that contains values for the properties that are defined for the case type. For each property, you specify the symbolic name of the property and the value for the property.Important: The value that is specified for the property must match the data type of the property. You can use the particular case type resource to get a list of the properties that are defined for the case type. |
| ClientContext            | Array   | No          | An array that contains a series of key value pairs that specify contextual information for a specific activity.                                                                                                                                                                                                                                                                                          |

## Response content

| Code                      | Description                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully. The case was updated with the new property values.                       |
| 400 Bad Request           | The required TargetObjectStore parameter was missing, or the parameter value was invalid.                   |
| 404 Not Found             | The specified case folder was not found.                                                                    |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response. |

## Examples: PUT method request

```
PUT
http://localhost:9081/CaseManager/CASEREST/v1/case/
C5AB1E9D-30D1-4D21-ADDF-F248FF1354B7

{
  "TargetObjectStore":"CMTOSSH",

  "Properties":
  [
    {"SymbolicName":"DH2\_State","Value":"NV"},
    {"SymbolicName":"DH2\_PropOne","Value":8},
    {"SymbolicName":"DH2\_City","Value":"Reno"},
    {"SymbolicName":"DH2\_MVInt","Value":[0,101,300,340]},
    {"SymbolicName":"DH2\_MVString","Value":["One","Three","Sixty"]}
  ]
}
```

## Examples: PUT method response

```
HTTP 1.1 200 OK
Content-Type: application/json;charset-UTF-8
{ }
```