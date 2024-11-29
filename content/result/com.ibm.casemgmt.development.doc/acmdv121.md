# POST method for the particular case instance resource

## URI

```
/CASEREST/v1/case/{case folder id}
```

| Name             | Type   | Description                                                               |
|------------------|--------|---------------------------------------------------------------------------|
| {case folder id} | String | The GUID that identifies the root folder of the case that is to be split. |

## Request content for creating a split case

```
{
    "CaseType": "case type symbolic name",
    "TargetObjectStore": "target object store name",
    "OperationDescription": "operation description,
    "Operation": "split",
    "ExternalDataIdentifier": "string set by the external data service",
    "Properties" :
    [ // the array of case property values may be empty
        {
        "SymbolicName": "symbolic name of case property",
        "Value" : "property value"
        },
        ...
    ],
    "DocumentFiling":
    [ // the array of folders to have documents filed in
        {
        "FolderName": "path to case subfolder, or just ‘/’",
        "DocumentId": "vsid for P8 document or PID for CM8 document" 
        },
        ...
    ]
}
```

No data from the original case is used when creating
the new split case. You must pass in the property values you want
to set on the new split case by using the properties attribute.

## Request content for getting case data

```
{
    "TargetObjectStore": "<target object store name>",
    "Operation": "fetchProperties",
    "ClientContext":
    {
        "key": "value",
        // More key value pairs
    }
}
```

## Request content for adding a case relationship

```
{
    "TargetObjectStore": "target object store name",
    "Operation": "relate",
    "CaseFolderId": "GUID of target case",
    "OperationDescription": "operation description - this parameter is optional",
    "RelationshipCategory": "category name - this parameter is optional",
    "TwoWayRelationship": "true/false defaults to true - this parameter is optional"
}
```

## Request content for removing a case relationship

```
{
    "TargetObjectStore": "target object store name",
    "Operation": "unrelate",
    "RelationshipId": "GUID of relationship to delete",
    "OperationDescription": "operation description - this parameter is optional"
}
```

## Request parameters

| Name                     | Type   | Required?   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------|--------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CaseType                 | String | Yes         | The symbolic name that is assigned to the case type of the case that is to be created by the POST method. The CaseType parameter is not required for the relate operation, and it is not required for the unrelate operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| TargetObjectStore        | String | Yes         | The symbolic name of the object store that is to contain the new case.A symbolic name is called a unique identifier in IBM® Business Automation Workflow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Operation  Description   | String | No          | Text that describes the action that is indicated by the POST method.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Operation                | String | Yes         | One of the following operations that the POST method is to run: split Specify this option to reuse data from the current case to create a case. fetchProperties Specify this option to return data for the current case.   relate Specify this option to relate another case to the current case.   unrelate Specify this option to remove the relationship between this case and a related case.                                                                                                                                                                                                                                                                                                                                                                                               |
| ExternalData  Identifier | String | No          | A string that indicates the state of the data that was returned by the external data service. The external identifier is set by the external data service when the properties are fetched for the first time. This identifier is passed back to the external data service for splitting a case or creating a case. The value of this property is set by the service and is not modified by the client.Tip: If you are using an external data service and the Operation parameter is set to split, you can include the ExternalDataIdentifier parameter in the request, since the identifier was set when the properties were fetched. This parameter is not required if the Operation parameter is set to fetchProperties because the identifier might not be set by the external data service. |
| Properties               | Array  | No          | An array that contains values for the properties that are defined for the case type. For each property, you specify the symbolic name of the property and the value for the property.Important: The value must match the data type of the property. You can use the particular case type resource to get a list of the properties that are defined for the case type.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DocumentFiling           | Array  | No          | An array that identifies any documents to be attached to the new case and the folder in which the documents are to be filed. Use the version ID to identify a document. Use a slash (/) to indicate the root folder. Use a slash and the folder name to indicate a subfolder under the root folder, for example, /folder1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ClientContext            | Array  | No          | An array that contains a series of key value pairs that specify contextual information for a specific work item. This parameter is used to send information to an external data service when a caseworker opens the work item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| RelationshipId           | String | No          | The GUID of the related case you want to remove the relationship from.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RelationshipCategory     | String | No          | An optional string that describes the category of the relationship.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| TwoWayRelationship       | String | No          | Indicates whether the related case also has a relationship with the current case. The value of the parameter must be true or false. The default value is true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## Response content

The content of the response
that is returned by the POST method depends on
the operation that you are running. If you are running the split operation,
the method returns the identifier of the new case that was created
by reusing data from an existing case. If you are running the fetchProperties operation,
the method returns the case properties.

| Code                      | Description                                                                                                                                                              |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully, and the case was created. The response that is returned by the POST method contains the case folder ID for the new case.              |
| 201 OK                    | The method completed successfully, and the case relationship was created. The response that is returned by the POST method contains the ID of the new case relationship. |
| 400 Bad Request           | A required parameter was missing, or a parameter value was invalid.                                                                                                      |
| 404 Not Found             | The case folder that was specified in the request was not found.                                                                                                         |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response.                                                              |

## POST method request for splitting
a case

```
# Request
POST / CASEREST / v1 / case  / 9E45A997 - 0E42 - 406E-AAC4 - EE55D8BCF2ED
HTTP / 1.1
Host:
www.CaseMgmtExample.net
Content - Type: application / json;
charset - UTF - 8 {
    "CaseType": "My\_casetype",
    "TargetObjectStore": "myTargetOS",
    "OperationDescription": "splitting case1 to case2",
    "Operation": "split",
    "Properties":
    [{
            "SymbolicName": "AUTO\_ClaimDate",
            "Value": "2010-07-16T21:50:36Z"
        }, {
            "SymbolicName": "AUTO\_PersonsBO",
            "Value": [{
                    "Properties": [{
                            "SymbolicName": "AUTO\_Age",
                            "Value": "45"
                        }, {
                            "SymbolicName": "AUTO\_FirstName",
                            "Value": "John"
                        }, {
                            "SymbolicName": "AUTO\_LastName",
                            "Value": "Doe"
                        }
                    ]
                }, {
                    "Properties": [{
                            "SymbolicName": "AUTO\_Age",
                            "Value": "45"
                        }, {
                            "SymbolicName": "AUTO\_FirstName",
                            "Value": "Jane"
                        }, {
                            "SymbolicName": "AUTO\_LastName",
                            "Value": "Doe"
                        }
                    ]
                }
            ]
        }
    ],
    "DocumentFiling":
    [// the array of folders to have documents filed in
        {
            "FolderName": "/CaseSubFolder1",
            "DocumentId": "12345678-0000-0000-0000-aabbccddeeff"
        }
    ]
}
```

## POST method response for splitting
a case

```
HTTP 1.1 201 OK Created
Content-Type: application/json;charset-UTF-8
{
    "CaseFolderId": "{12345678-1234-1234-1234-aabbccddeeff}"
}
```

## POST method request for relating
a case

```
#Request 
POST /CASEREST/v1/case/9E45A997-0E42-406E-AAC4-EE55D8BCF2ED
 HTTP/1.1
Host: www.CaseMgmtExample.net
Content-Type: application/json;charset-UTF-8
{
  "CaseType": "My\_casetype",
  "TargetObjectStore": "myTargetOS",
  "Operation": "relate",
  "CaseFolderId": "{12345678-1234-1234-1234-aabbccddeeff}",
  "OperationDescription": "description of operation",
  "RelationshipCategory": "category name",
  "TwoWayRelationship": "true"
}
```

## POST method response for create
operation

```
HTTP 1.1 201 OK Created
Content-Type: application/json;charset-UTF-8
{
    "RelationshipId": "{12345678-1234-1234-1234-aabbccddeeff}"
}
```