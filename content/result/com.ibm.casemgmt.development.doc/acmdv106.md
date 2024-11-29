# Retrieval of initial information for a new case

1. The case worker clicks Add Case and selects
the appropriate case type.
2. Case Client submits a request
to the REST API to obtain a complete list of case properties and their attributes, including their
default values. The request is submitted by calling the GET method of the
particular case type
resource:GET /CaseManager/CASEREST/v1/casetype/DH2\_MyCase
3. The REST API passes the default case data to the external data service by calling the
POST method particular object type
resource:POST /testservice/ICMEDREST/type/DH2\_MyCase
{
  "repositoryId": "CMTOSDH", 
  "requestMode": "initialNewObject", 
  "properties": [

    // Payload may include additional properties 
    // not meaningful to the external data service

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
      "value": null
    }, 
    {
      "symbolicName": "DH2\_PropOne", 
      "value": null
    }, 
    {
      "symbolicName": "DH2\_MVInt", 
      "value": [ ]
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
4. The external data service responds with the changes to the attributes
for the properties that it manages. The response also includes the
initial setting for the external data identifier.{
  "externalDataIdentifier": "-1,0", 
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
            "displayName": "Ten", 
            "value": "Ten"
          }, 
          {
            "displayName": "Eleven", 
            "value": "Eleven"
          }, 
          {
            "displayName": "Twelve", 
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
5. The REST API merges this information with the default case data and returns the updated values
to Case Client:{
  "Properties": [

    // Non-external data related properties

    {
      "SymbolicName": "CmAcmCaseIdentifier", 
      "DisplayName": "Case Identifier", 
      "Value": null, 
      "DisplayMode": "readwrite", 
      "Description": "A specially formatted identifier for Case Folder 
         instances, consists of Case Folder subclass symbolic class name,
         \"\_\" and then a 12 digit sequence number with leading zeros.", 
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
      "Value": 0, 
      "DisplayMode": "readwrite", 
      "Description": "An integer choice property that defines 
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

    // ...

    {
      "SymbolicName": "DH2\_State", 
      "DisplayName": "State", 
      "Value": null, 
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
    {
      "SymbolicName": "DH2\_PropOne", 
      "DisplayName": "Prop One", 
      "Value": null, 
      "DisplayMode": "readwrite", 
      "Description": "An integer property", 
      "PropertyType": "integer", 
      "Cardinality": "single", 
      "Updatability": "readwrite", 
      "Required": false, 
      "Queryable": true, 
      "Orderable": true, 
      "Hidden": false, 
      "Inherited": false, 
      "DefaultValue": null, 
      "MaxValue": 10, 
      "MinValue": 1, 
      "HasDependentProperties": false
    }, 
    {
      "SymbolicName": "DH2\_MVInt", 
      "DisplayName": "MVInt", 
      "Value": [
        0, 
        100
      ], 
      "DisplayMode": "readwrite", 
      "Description": "Multi-value integer property", 
      "PropertyType": "integer", 
      "Cardinality": "multi", 
      "RequiresUniqueElements": false, 
      "Updatability": "readwrite", 
      "Required": false, 
      "Queryable": true, 
      "Orderable": false, 
      "Hidden": false, 
      "Inherited": false, 
      "DefaultValue": null, 
      "MaxValue": 1000, 
      "MinValue": 0, 
      "HasDependentProperties": true
    }, 
    {
      "SymbolicName": "DH2\_MVString", 
      "DisplayName": "MVString", 
      "Value": [ ], 
      "DisplayMode": "readwrite", 
      "Description": "Multi-value string property", 
      "PropertyType": "string", 
      "Cardinality": "multi", 
      "RequiresUniqueElements": false, 
      "Updatability": "readwrite", 
      "Required": true, 
      "Queryable": true, 
      "Orderable": false, 
      "Hidden": false, 
      "Inherited": false, 
      "DefaultValue": null, 
      "MaxLength": 24, 
      "ChoiceList": {
        "DisplayName": "MVStringChoiceList", 
        "Choices": [
          {
            "ChoiceName": "One", 
            "Value": "One"
          }, 
          {
            "ChoiceName": "Two", 
            "Value": "Two"
          }, 
          {
            "ChoiceName": "Three", 
            "Value": "Three"
          }, 
          {
            "ChoiceName": "Ten", 
            "Value": "Ten"
          }, 
          {
            "ChoiceName": "Eleven", 
            "Value": "Eleven"
          }, 
          {
            "ChoiceName": "Twelve", 
            "Value": "Twelve"
          }
        ]
      }, 
      "HasDependentProperties": false
    }, 
    {
      "SymbolicName": "DH2\_City", 
      "DisplayName": "City", 
      "Value": null, 
      "DisplayMode": "readonly", 
      "Description": "City where home office is located", 
      "PropertyType": "string", 
      "Cardinality": "single", 
      "Updatability": "readwrite", 
      "Required": true, 
      "Queryable": true, 
      "Orderable": true, 
      "Hidden": true, 
      "Inherited": false, 
      "DefaultValue": null, 
      "MaxLength": 64, 
      "HasDependentProperties": false
    }
  ], 
  "CaseType": "DH2\_MyCase", 
  "Description": "A simple case type", 
  "CaseTitleProperty": "CmAcmCaseIdentifier", 
  "DisplayName": "My Case", 
  "ExternalDataIdentifier": "-1,0"
}