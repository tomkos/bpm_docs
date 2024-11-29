# GET method for the list of view definitions resource

## URI

/CASEREST/v1/casetype/{case
type name}/viewdefinitions

| Name             | Type   | Description                                                                      |
|------------------|--------|----------------------------------------------------------------------------------|
| {case type name} | String | The symbolic name of the case type for which view properties are to be returned. |

| Name              | Type   | Required?   | Description                                                               |
|-------------------|--------|-------------|---------------------------------------------------------------------------|
| TargetObjectStore | String | Yes         | The symbolic name of the target object store that contains the case type. |

## Request content

The request for this method
contains no JSON content.

## Response content

For each view definition,
the GET method returns a list of the properties
that are displayed as fields in the view. To work with these properties,
you can use IBM® CMIS for FileNet® Content Manager to
obtain detailed information such as data types and lengths.

| Code                      | Description                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully and returned the requested view properties.                               |
| 400 Bad Request           | The TargetObjectStore parameter was not specified or the parameter value was invalid.                       |
| 404 Not Found             | The case type that was specified in the request URI was not found.                                          |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response. |

## Example: GET method request

```
GET http://example.com:9080/CaseManager/CASEREST/v1/casetype
/AUTO\_FleetPurchase/viewdefinitions?
TargetObjectStore=MyExampleObjectStore HTTP/1.1
Host: www.CaseMgmtExample.net
```

## Example: GET method response

```
#Response
HTTP/1.1 200 OK
Content-Type: application/json;charset-UTF-8
{
  "CaseTitleProperty": "CmAcmCaseIdentifier",
  "CaseDataView": 
  {
    "Fields": 
    [
      {"FieldType": "property", "Name": "caseName"},
      {"FieldType": "property", "Name": "accountNumber"},
      {"FieldType": "group", "Label": "Home Address",
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
      {"FieldType": "property", "Name": "caseName"},		
      {"FieldType": "property", "Name": "customerName"},
      {"FieldType": "property", "Name": "requestedLoanAmount"},
      {"FieldType": "property", "Name": "percentageDown"},
      {"FieldType": "property", "Name": "FicoScore"}
    ]
  },
  "CaseSearchView": 
  {
    "Fields": 
    [
      {"FieldType": "property", "Name": "caseName"},		
      {"FieldType": "property", "Name": "customerName"},
      {"FieldType": "property", "Name": "accountNumber"},
      {"FieldType": "property", "Name": "requestedLoanAmount"}
    ]     
  }
}
```