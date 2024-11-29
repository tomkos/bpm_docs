# Update of a property that has dependencies

1. The user selects a value for the State property
on which the City property depends.
2. Case Client calls the
POST method of the particular case type resource to submit the value to the
workflow REST protocol. The request payload includes the working property values, including the
value that is selected for the State
property:POST /CaseManager/CASEREST/v1/casetype/DH2\_MyCase
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
3. The workflow REST protocol passes the values to the external data service by calling the
POST method for the particular object type
resource:POST /testservice/ICMEDREST/type/DH2\_MyCase
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
4. The external data service responds with the choice list options
for the City property based on the selected state.
The response also includes an updated value for the external data
identifier:{
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
5. The workflow REST protocol merges the changes from the external data service into the working
values for the case and returns the updated values to the Case Client:{
  "Properties": [
    {
      "SymbolicName": "DH2\_City", 
      "DisplayName": "City", 
      "Value": null, 
      "DisplayMode": "readwrite", 
      "Description": "City where home office is located", 
      "PropertyType": "string", 
      "Cardinality": "single", 
      "Updatability": "readwrite", 
      "Required": true, 
      "Queryable": true, 
      "Orderable": true, 
      "Hidden": false, 
      "Inherited": false, 
      "DefaultValue": null, 
      "MaxLength": 64, 
      "ChoiceList": {
        "DisplayName": "CityChoiceList", 
        "Choices": [
          {
            "ChoiceName": "Los Angeles", 
            "Value": "Los Angeles"
          }, 
          {
            "ChoiceName": "San Diego", 
            "Value": "San Diego"
          }, 
          {
            "ChoiceName": "San Francisco", 
            "Value": "San Francisco"
          }
        ]
      }, 
      "HasDependentProperties": false
    }
  ], 
  "CaseType": "DH2\_MyCase", 
  "ExternalDataIdentifier": "1,0"
}