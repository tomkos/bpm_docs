# Creation of the new case

1. The case worker finishes updating the case properties and clicks Add.
2. Case Client submits the
working property values to the workflow REST protocol by calling the POST method
of the cases resource:POST /CaseManager/CASEREST/v1/cases
{
  "TargetObjectStore": "CMTOSDH", 
  "CaseType": "DH2\_MyCase", 
  "ExternalDataIdentifier": "1,1", 
  "Properties": [

    // Non-external data related properties

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
      "Value": 7
    }, 
    {
      "SymbolicName": "DH2\_City", 
      "Value": "San Diego"
    }, 
    {
      "SymbolicName": "DH2\_MVInt", 
      "Value": [
        0, 
        101, 
        200, 
        210
      ]
    }, 
    {
      "SymbolicName": "DH2\_MVString", 
      "Value": [
        "One", 
        "Three", 
        "Thirty"
      ]
    }
  ]
}
3. The workflow REST protocol submits the property values to the external data service by calling
the POST method of the particular object type
resource:POST /testservice/ICMEDREST/type/DH2\_MyCase
{
  "repositoryId": "CMTOSDH", 
  "requestMode": "finalNewObject", 
  "externalDataIdentifier": "1,1", 
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
      "value": 7
    }, 
    {
      "symbolicName": "DH2\_MVInt", 
      "value": [
        0, 
        101, 
        200, 
        210
      ]
    }, 
    {
      "symbolicName": "DH2\_MVString", 
      "value": [
        "One", 
        "Three", 
        "Thirty"
      ]
    }, 
    {
      "symbolicName": "DH2\_City", 
      "value": "San Diego"
    }
  ]
}
4. The external data service responds with values for the properties
that it manages:{
  "externalDataIdentifier": "1,1", 
  "properties": [
    {
      "symbolicName": "DH2\_State", 
      "required": true, 
      "maxLength": 2, 
      "hasDependentProperties": true, 
      "choiceList": {
        "displayName": "StateChoiceList", 
        "choices": [
          {
            "displayName": "New York", 
            "value": "NY"
          }, 
          {
            "displayName": "California", 
            "value": "CA"
          }, 
          {
            "displayName": "Nevada", 
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
        "displayName": "MVStringChoiceList", 
        "choices": [
          {
            "displayName": "One", 
            "value": "One"
          }, 
          {
            "displayName": "Two", 
            "value": "Two"
          }, 
          {
            "displayName": "Three", 
            "value": "Three"
          }, 
          {
            "displayName": "Twenty", 
            "value": "Twenty"
          }, 
          {
            "displayName": "Thirty", 
            "value": "Thirty"
          }, 
          {
            "displayName": "Fourty", 
            "value": "Fourty"
          }
        ]
      }
    }, 
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
5. The workflow REST protocol validates the values that are submitted by the Case Client with the final external data
constraints. If no errors occur, the protocol creates the case and returns details for the new
case:{
  "CaseTitle": "DH2\_MyCase\_000000100602", 
  "CaseIdentifier": "DH2\_MyCase\_000000100602", 
  "CaseFolderId": "{7F390468-7FAD-43EB-B373-675D2255BB61}"
}