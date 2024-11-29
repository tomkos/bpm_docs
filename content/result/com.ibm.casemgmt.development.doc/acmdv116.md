# GET method for the particular case type resource

If you are using an external data service,
the GET method incorporates information from that
service into property information that the method returns.

To create a case that reuses data from an existing case,
you can specify the optional SourceCaseFolderId parameter
to identify the source case. The IBM® Business Automation
Workflow REST protocol reuses
the property values that are not null or empty from the source case
for any matching properties in the new case.

## URI

/CASEREST/v1/casetype/{case
type name}

| Name             | Type   | Description                    |
|------------------|--------|--------------------------------|
| {case type name} | String | The symbolic name of case type |

| Name               | Type   | Required?   | Description                                                                                                                                          |
|--------------------|--------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| TargetObjectStore  | String | Yes         | The symbolic name of the object store that contains the case type.A symbolic name is called a unique identifier in IBM Business Automation Workflow. |
| SourceCaseFolderId | String | No          | The GUID that identifies the root folder of an existing case from which data is to be reused in creating the case.                                   |

## Request content

The request for this method
contains no JSON content.

## Response content

GET method
returns the properties that are defined for the specified case type.

| Code                      | Description                                                                                                                               |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully. The response that is returned by the GET method includes the information for the specified case types. |
| 400 Bad Request           | The required TargetObjectStore parameter was missing or the parameter value was invalid.                                                  |
| 404 Not Found             | The case type specified in the request was not found.                                                                                     |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response.                               |

## Example: GET method request

```
#Request to properties for case type DH2\_MyCase
GET /CaseManager/CASEREST/v1/casetype/DH2\_MyCase?TargetObjectStore=MyTOS
 HTTP/1.1
Host: www.example.net
```

## Example: GET method

```
#Response
HTTP/1.1 200 OK
Content-Type: application/json;charset-UTF-8
{
  "externalDataIdentifier": "-1,0", 
  "properties": [
    {
      "symbolicName": "DH2\_State", 
      "required": true, 
      "maxLength": 2, 
      "hasDependentProperties": true, 
      "choiceList": {
        "ChoiceName": "StateChoiceList", 
        "choices": [
          {
            "ChoiceName": "New York",
            "value": "NY"
          }, 
          {
            "ChoiceName": "California", 
            "value": "CA"
          }, 
          {
            "ChoiceName": "Nevada", 
            "value": "NV"
          }
        ]
      }
    }, 
    {
      "symbolicName": "DH2\_PropOne", 
      "maxValue": 10, 
      "minValue": 1, 
      "hasDependentProperties": false
    }, 
    {
      "symbolicName": "DH2\_MVInt", 
      "value": [
        0, 
        100
      ], 
      "maxValue": 1000, 
      "minValue": 0, 
      "hasDependentProperties": true
    }, 
    {
      "symbolicName": "DH2\_MVString", 
      "required": true, 
      "maxLength": 24, 
      "hasDependentProperties": false, 
      "choiceList": {
        "ChoiceName": "MVStringChoiceList", 
        "choices": [
          {
            "ChoiceName": "One", 
            "value": "One"
          }, 
          {
            "ChoiceName": "Two", 
            "value": "Two"
          }, 
          {
            "ChoiceName": "Three", 
            "value": "Three"
          }, 
          {
            "ChoiceName": "Ten", 
            "value": "Ten"
          }, 
          {
            "ChoiceName": "Eleven", 
            "value": "Eleven"
          }, 
          {
            "ChoiceName": "Twelve", 
            "value": "Twelve"
          }
        ]
      }
    }, 
    {
      "symbolicName": "DH2\_City", 
      "value": null, 
      "displayMode": "readonly", 
      "hidden": true, 
      "required": true, 
      "hasDependentProperties": false
    }
  ]
}
```