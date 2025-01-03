# GET method for the particular case instance resource

## URI

/CASEREST/v1/case/{case folder
id}

| Name             | Type   | Description                                                                                        |
|------------------|--------|----------------------------------------------------------------------------------------------------|
| {case folder id} | String | The GUID that identifies the root folder of the case for which the method is to return properties. |

| Name              | Type   | Required?   | Description                                                   |
|-------------------|--------|-------------|---------------------------------------------------------------|
| TargetObjectStore | String | Yes         | The symbolic name of the object store that contains the case. |

## Request content

The request for this method
contains no JSON content.

## Response content

- The symbolic name of the case that is represented by the case
folder
- A list of the case properties and their current values

If you are using an external data service to populate
the case properties, the GET method includes information
from the external service in the response. Typically, the values provided
by the external data service are the same as the current property
values for the case. However, if the values for a property are different,
the Value attribute for the property differs
from the OriginalValue attribute.

| Code                      | Description                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully, and the list of properties for the specified case was returned.          |
| 400 Bad Request           | A required parameter was missing, or the parameter value was invalid.                                       |
| 404 Not Found             | The specified case folder was not found.                                                                    |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response. |

## Example: GET method request

```
GET
http://localhost:9081/CaseManager/CASEREST/v1/case/
C5AB1E9D-30D1-4D21-ADDF-F248FF1354B7
?TargetObjectStore=CMTOSDH
```

## Example: GET method response

```
#Response
HTTP/1.1 200 OK
Content-Type: application/json;charset-UTF-8
{
  "Properties": [

    {
      "SymbolicName": "DateCreated", 
      "DisplayName": "Date Created", 
      "Value": "2011-04-28T18:49:55Z", 
      "OriginalValue": "2011-04-28T18:49:55Z", 
      "DisplayMode": "readwrite", 
      "Description": "The date and time this object was created.", 
      "PropertyType": "datetime", 
      "Cardinality": "single", 
      "Updatability": "readonly", 
      "Required": false, 
      "Queryable": true, 
      "Orderable": true, 
      "Hidden": false, 
      "Inherited": true, 
      "DefaultValue": null, 
      "MaxValue": "9999-12-31T23:59:59Z", 
      "MinValue": "1753-01-01T00:00:00Z", 
      "HasDependentProperties": false
    }, 

    // Additional properties omitted

    {
      "SymbolicName": "CmAcmCaseIdentifier", 
      "DisplayName": "Case Identifier", 
      "Value": "DH2\_MyCase\_000000100602", 
      "OriginalValue": "DH2\_MyCase\_000000100602", 
      "DisplayMode": "readwrite", 
      "Description": "A specially formatted identifier for 
        Case Folder instances, consists of Case Folder subclass 
        symbolic class name, \"\_\" and then a  12 digit sequence
        number with leading zeros.", 
      "PropertyType": "string", 
      "Cardinality": "single", 
      "Updatability": "readwrite", 
      "Required": false, 
      "Queryable": true, 
      "Orderable": true, 
      "Hidden": false, 
      "Inherited": true, 
      "DefaultValue": null, 
      "MaxLength": 85, 
      "HasDependentProperties": false
    }, 
    {
      "SymbolicName": "CmAcmCaseState", 
      "DisplayName": "Case State", 
      "Value": 2, 
      "OriginalValue": 2, 
      "DisplayMode": "readwrite", 
      "Description": "An integer choice property that defines the possible
        the possible states of Case Folder instance.", 
      "PropertyType": "integer", 
      "Cardinality": "single", 
      "Updatability": "readwrite", 
      "Required": true, 
      "Queryable": true, 
      "Orderable": true, 
      "Hidden": false, 
      "Inherited": true, 
      "DefaultValue": 0, 
      "MaxValue": null, 
      "MinValue": null, 
      "ChoiceList": {
        "DisplayName": "CmAcmCaseStateChoiceList", 
        "Choices": [
         {
          "ChoiceName": "New", 
          "Value": 0
         }, 
         {
          "ChoiceName": "Initializing", 
          "Value": 1
         }, 
         {
          "ChoiceName": "Working", 
          "Value": 2
         }, 
         {
          "ChoiceName": "Complete", 
          "Value": 3
         }, 
         {
          "ChoiceName": "Failed", 
          "Value": 4
         }
        ]
      }, 
      "HasDependentProperties": false
    }, 
    {
      "SymbolicName": "DH2\_State", 
      "DisplayName": "State", 
      "Value": "CA", 
      "OriginalValue": "CA", 
      "DisplayMode": "readwrite", 
      "Description": "State where home office is located", 
      "PropertyType": "string", 
      "Cardinality": "single", 
      "Updatability": "readwrite", 
      "Required": true, 
      "Queryable": true, 
      "Orderable": true, 
      "Hidden": false, 
      "Inherited": false, 
      "DefaultValue": null, 
      "MaxLength": 2, 
      "ChoiceList": {
        "DisplayName": "StateChoiceList", 
        "Choices": [
        {
          "ChoiceName": "New York", 
          "Value": "NY"
        }, 
        {
          "ChoiceName": "California", 
          "Value": "CA"
        }, 
        {
          "ChoiceName": "Nevada", 
          "Value": "NV"
        }
        ]
      }, 
      "HasDependentProperties": true
    }, 

    // Additional properties omitted

  ]
}
```