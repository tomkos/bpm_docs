# POST method for the particular object type resource

- The default value
- The value persisted for the property in the repository
- The working value that the case worker entered for the property

The response payload that the external data service returns
includes changes to the properties that it manages. The service can
modify attributes of properties in addition to modifying property
values.

The workflow REST protocol then merges these changes into the case data and returns the data to
the Case Client.

## URI syntax

```
/type/{object type name}
```

| Name               | Type   | Description                                                                 |
|--------------------|--------|-----------------------------------------------------------------------------|
| {object type name} | String | The symbolic name of case type that defines the case that is being updated. |

## Request content

```
{
   "repositoryId":"<target object store name>",
   "objectId"   : "<GUID of the case folder>",
   "requestMode" : "<request context>",
   "externalDataIdentifier" : "<identifier for service">,

   "properties":
   [
   {
      "symbolicName" : "<property name>",
      "value"        : <current value>,
   }

   // More properties ...

   ],

   "clientContext":
   {
      "Key1":"Value1",
      "Key2":"Value2"
   }

}
```

| Name                     | Type   | Required?                               | Description                                                                                                                                                                                                                                             |
|--------------------------|--------|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| repositoryId             | String | Yes                                     | The symbolic name of the object store that contains the case type.A symbolic name that is called a unique identifier.                                                                                                                                   |
| objectId                 | String | No                                      | The GUID that identifies the root folder of an existing case. This parameter is not specified when the POST method is called to create a case.                                                                                                          |
| requestMode              | String | Yes                                     | One of the following request modes that indicates the reason that the POST method is being called: initialNewObject initialExistingObject inProgressChanges finalNewObject finalExistingObject                                                          |
| externalData  Identifier | String | Yes, for certainrequest  Mode  settings | A string that indicates the state of the data that was returned by the external data service. The request must include this identifier if the requestMode parameter is set to one of these values: inProgressChanges finalNewObject finalExistingObject |
| properties               | Array  | Yes                                     | An array that contains values for the properties that are defined for the case type. For each property, the request contains the symbolic name and the property value.                                                                                  |
| clientContext            | Array  | No                                      | An array that contains a series of key value pairs that specify contextual information for a specific work item. This parameter is used to send information to an external data service when a case worker opens the work item.                         |

## Response codes

| Code                      | Description                                                                                                                                                                                                                                                                                                    |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully. The response that is returned by the POST method includes the updated information for the case.                                                                                                                                                                             |
| 400 Bad Request           | One of the required parameters was missing or a parameter value was invalid.                                                                                                                                                                                                                                   |
| 404 Not Found             | The case type that was specified in the request was not found. This error does not indicate that the case type is invalid. Instead, it indicates that the external data service does not manage any property values for the case type. The workflow REST protocol does not return an error to the Case Client. |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response.                                                                                                                                                                                                    |

## Example: POST method request

```
POST /testservice/ICMEDREST/type/DH2\_MyCase
{
  "repositoryId": "CMTOSDH", 
  "requestMode": "inProgressChanges", 
  "externalDataIdentifier": "-1,0", 
  "properties": [

    // Non-external data related properties

    {
      "symbolicName": "CmAcmCaseIdentifier", 
      "value": null
    }, 
    {
      "symbolicName": "CmAcmCaseState", 
      "value": 0
    }, 

    // ...

    {
      "symbolicName": "DH2\_State", 
      "value": "CA"
    }, 
    {
      "symbolicName": "DH2\_PropOne", 
      "value": null
    }, 
    {
      "symbolicName": "DH2\_MVInt", 
      "value": [
        0, 
        100
      ]
    }, 
    {
      "symbolicName": "DH2\_MVString", 
      "value": [ ]
    }, 
    {
      "symbolicName": "DH2\_City", 
      "value": null
    }
  ]
}
```

## Example: POST method response

```
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