# GET method for the particular solution resource

## URI

/CASEREST/v1/solution/{SolutionName}

| Name           | Type   | Description                                                       |
|----------------|--------|-------------------------------------------------------------------|
| {SolutionName} | String | The name of the solution for which information is to be returned. |

| Name              | Type   | Required   | Description                                                       |
|-------------------|--------|------------|-------------------------------------------------------------------|
| TargetObjectStore | String | Yes        | The symbolic name of the object store that contains the solution. |

## Request content

The request for this method
contains no JSON content.

## Response content

For each case type, the
method returns a list of the properties and a detailed description
of the views.

| Code                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully. The response that is returned by the GET method includes the information for the specified solution.                                                                                                                                                                                                                                                                                                                              |
| 400 Bad Request           | One of the required parameters was missing or a parameter value was invalid.                                                                                                                                                                                                                                                                                                                                                                                         |
| 404 Not Found             | The solution that was specified in the request was not found.If a request is received for an object type that the external data service does not manage any data for, it must return status code 404: Not Found. The integration tier layer of IBM® Business Automation Workflow treats this return status as if the particular object type did not have any external data associated with it.  No error is returned to the IBM Business Automation Workflow caller. |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response.                                                                                                                                                                                                                                                                                                                                                          |

## Example: GET method request

```
GET /CASEREST/v1/solution/Auto+Loan+Solution
?TargetObjectStore=MyTargetObjectStore HTTP/1.1
Host: "www.example.net"
```

## Example: GET method

```
#Response
HTTP/1.1 200 OK
Content-Type: application/json;charset-UTF-8
{
"CaseTypes" : [
{
"CaseType" : "AUTO\_CollisionClaimCase1",
"DisplayName" : "Collision Claim Case",
"Description" : "Case to process a collision claim",
"CaseTitleProperty": "CmAcmCaseIdentifier",
"Views":
{
  "CaseDataView": 
  {
    "Fields": 
    [
      { "FieldType": "property", "Name": "caseName" },
      { "FieldType": "property", "Name": "accountNumber" },
      { "FieldType": "group", "Label": "Home Address", 
        "OpenState": false,
        "Fields": 
        [ 
          {"FieldType": "property", "Name": "StreetAddressLine1"},
          {"FieldType": "property", "Name": "StreetAddressLine2"},
          {"FieldType": "property", "Name": "City"},
          {"FieldType": "property", "Name": "State"},
          {"FieldType": "property", "Name": "ZIPCode"},
        ] 
      }
    ]
  },
  "CaseSummaryView": 
  {
    "Fields": 
    [
      { "FieldType": "property", "Name": "caseName" },      
      { "FieldType": "property", "Name": "customerName" },
      { "FieldType": "property", "Name": "requestedLoanAmount" },
      { "FieldType": "property", "Name": "percentageDown" },
      { "FieldType": "property", "Name": "FicoScore" }
    ]
  },
  "CaseSearchView": 
  {
    "Fields": 
    [
      { "FieldType": "property", "Name": "caseName" },      
      { "FieldType": "property", "Name": "customerName" },
      { "FieldType": "property", "Name": "accountNumber" },
      { "FieldType": "property", "Name": "requestedLoanAmount" }
    ]     
}
}
},
{
"CaseType" : "AUTO\_CollisionClaimCase2",
"CaseTiTleProperty": "CmAcmCaseIdentifier",
"Views": …
}
],
"SolutionProperties":
[
{
      "SymbolicName": "AUTO\_City", 
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
  }
}
]
}
```