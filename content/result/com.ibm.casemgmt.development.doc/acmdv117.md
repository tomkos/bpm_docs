# POST method for the particular case type resource

When you get the properties to create a case, call
the POST method instead of the GET method
if you need to pass contextual information to an external data service.
The POST method includes the clientContext parameter
that contains an array of key value pairs that specify the contextual
information for a specific task.

An external data service
can specify that a property has dependent properties. The values of
the dependent properties are determined by the value of that property.
You can call the POST method when the property
value is modified so that it can return updated values for the dependent
properties. For example, you might use an external data service to
populate a choice list with cities from a state that a case worker
selects. When a case worker selects California as the state, you call
the POST method to populate the choice list with
the appropriate California cities.

## URI

/CASEREST/v1/casetype/{case
type name}

| Name             | Type   | Description                    |
|------------------|--------|--------------------------------|
| {case type name} | String | The symbolic name of case type |

## Request content for retrieving data for a new case

```
{
  "TargetObjectStore" : "<target object store name>",
  "RequestMode":"<request mode>",
  "ClientContext":
  {
    "<key>":"<value>",
    // More key value pairs"
  }
}
```

## Request content for retrieving updates for dependent
properties

```
{
  "TargetObjectStore" : "<target object store name>",
  "RequestMode":"<request mode>",
  "ExternalDataIdentifier":"<string set by the external data service>",
  "Properties",
  [
   {
     "symbolicName" : "<property name>",
     "value"        : "<current value>",
   }
   {
     // More properties
   }
  ],
  "ClientContext":
  {
    "<key>":"<value>",
    // More key value pairs
  }
}
```

## Request parameters

| Name                     | Type        | Required?                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------|-------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TargetObjectStore        | String      | Yes                                                                          | The symbolic name of the object store that contains the case type.A symbolic name is called a unique identifier in IBM® Business Automation Workflow.                                                                                                                                                                                                                                      |
| RequestMode              | String      | No                                                                           | One of the following request modes that indicates the reason that the POST method is being called: initialNewObject Use this value if you are calling the POST method to get the properties for a new case. inProgressChanges Use this value if you are calling the POST method to update the values of dependent properties.  The default value for the RequestMode is inProgressChanges. |
| ExternalData  Identifier | String      | Yes, if using an external data service to get values of dependent properties | A string that indicates the state of the data that was returned by the external data service. The value of this property is set by the service and is not modified by the client.                                                                                                                                                                                                          |
| Properties               | Array       | Yes                                                                          | An array that contains values for the properties that are defined for the case type. For each property, you specify the symbolic name of the property and the value for the property.Important: The value must match the data type of the property.                                                                                                                                        |
| ClientContext            | JSON object | No                                                                           | An array that contains a series of key value pairs that specify contextual information for a specific work item. This parameter is used to send information to an external data service when a case worker opens the work item.                                                                                                                                                            |

## Response content

The content of the response
that is returned by the POST method depends on
the setting of the RequestMode property. If this
property is set to initialNewObject, the response contains all the
properties that are defined for the specified case type. If the property
is set to inProgressChanges, the response contains only those properties
that were updated by an external data service based on a change to
another property value.

| Code                      | Description                                                                                                                                |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully. The response that is returned by the POST method includes the information for the specified case types. |
| 400 Bad Request           | One of the required parameters was missing, or a parameter value was invalid.                                                              |
| 404 Not Found             | The case type that was specified in the request was not found.                                                                             |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response.                                |

## Example: POST method
request

```
POST /CaseManager/CASEREST/v1/casetype/DH2\_MyCase
{
  "TargetObjectStore": "CMTOSDH", 
  "ExternalDataIdentifier": "-1,0", 
  "Properties": [

    // Properties not related to external data

    {
      "SymbolicName": "CmAcmCaseIdentifier", 
      "Value": null
    }, 
    {
      "SymbolicName": "CmAcmCaseState", 
      "Value": 0
    }, 

    // ...

    {
      "SymbolicName": "DH2\_State", 
      "Value": "CA"
    }, 
    {
      "SymbolicName": "DH2\_PropOne", 
      "Value": null
    }, 
    {
      "SymbolicName": "DH2\_City", 
      "Value": null
    }, 
    {
      "SymbolicName": "DH2\_MVInt", 
      "Value": [
        0, 
        100
      ]
    }, 
    {
      "SymbolicName": "DH2\_MVString", 
      "Value": [ ]
    }
  ]
}
```

## Example: POST method
response

```
#Response
HTTP/1.1 200 OK
Content-Type: application/json;charset-UTF-8
{
  "externalDataIdentifier": "1,0", 
  "properties": [
    {
      "symbolicName": "DH2\_City", 
      "hidden": false, 
      "required": true, 
      "hasDependentProperties": false, 
      "choiceList": {
        "displayName": "CityChoiceList", 
        "choices": [
          {
            "displayName": "Los Angeles", 
            "value": "Los Angeles"
          }, 
          {
            "displayName": "San Diego", 
            "value": "San Diego"
          }, 
          {
            "displayName": "San Francisco", 
            "value": "San Francisco"
          }
        ]
      }
    }
  ]
}
```