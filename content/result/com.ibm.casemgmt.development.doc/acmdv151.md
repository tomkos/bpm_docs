# GET method for the list of case folder resources

## URI

/CASEREST/v1/case/{case folder id}/casedocumentslist

The URI for the GET method includes the following path element:

| Name             | Type   | Description                                                                                                                           |
|------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------|
| {CaseInstanceId} | String | The ID that identifies the root folder of the case that is used to retrieve the list of case folders, sub-folders and case documents. |

| Name              | Type   | Required?   | Description                                                   |
|-------------------|--------|-------------|---------------------------------------------------------------|
| TargetObjectStore | String | Yes         | The symbolic name of the object store that contains the case. |

## GET method request

The request for this method
contains no JSON content.

## GET method response

- A nested list of the case folders, sub-folders, case documents
- A list of the case folder or document properties

| Code                      | Description                                                                                                   |
|---------------------------|---------------------------------------------------------------------------------------------------------------|
| 200 OK                    | The method completed successfully and returned the requested list of case folders, sub-folders and documents. |
| 400 Bad Request           | The required TargetObjectStore parameter was not specified, or a parameter value was invalid.                 |
| 404 Not Found             | The specified case folder was not found.                                                                      |
| 500 Internal Server Error | A server error occurred. For information about the error, see the userMessage element in the JSON response.   |

## Example: GET method request

```
GET
http://localhost:9081/CaseManager/CASEREST/v1/case/
C5AB1E9D-30D1-4D21-ADDF-F248FF1354B7/casedocumentslist
?TargetObjectStore=CMTOSDH
```

## Example: GET method response

```
#Response
HTTP/1.1 200 OK
Content-Type: application/json;charset-UTF-8
{
   "docList":[
      {
         "template":"CmAcmCaseSubfolder",
         "LastModifier":"deadmin",
         "children":[
            {
               "template":"CmAcmCaseSubfolder",
               "LastModifier":"deadmin",
               "children":[
                  {
                     "template":"CmAcmCaseSubfolder",
                     "LastModifier":"deadmin",
                     "children":[
                        {
                           "template":"Document",
                           "LastModifier":"deadmin",
                           "parentFolderPath":"Test Folder\/Test Sub-Folder",
                           "DateCreated":"05\/12\/2021, 07:18 AM",
                           "VersionSeriesId":"{60F16079-0000-C712-A54F-A6066B38CDC9}",
                           "Creator":"deadmin",
                           "isExternalP8Doc":false,
                           "externalDocId":null,
                           "Name":"Test Document.txt",
                           "DateLastModified":"05\/12\/2021, 07:18 AM",
                           "MajorVersionNumber":1,
                           "mimetype":"text\/plain",
                           "Id":"{60F16079-0000-C411-8387-ACD1E37F2B0F}",
                           "MinorVersionNumber":0,
                           "ContainmentName":"Test Document.txt"
                        }
                     ],
                     "mimetype":"folder",
                     "Id":"{30F06079-0000-C811-A242-62DD34D2F9C0}",
                     "Creator":"deadmin",
                     "Name":"Test Sub-Folder",
                     "DateLastModified":"05\/12\/2021, 07:17 AM"
                  }
               ],
               "mimetype":"folder",
               "Id":"{E0EF6079-0000-CE16-A9D7-0322F12DBF21}",
               "Creator":"deadmin",
               "Name":"Test Folder",
               "DateLastModified":"05\/12\/2021, 07:16 AM"
            }
         ],
         "mimetype":"folder",
         "Id":"{D0EE6079-0000-CD2C-A9C8-6174154F2576}",
         "Creator":"deadmin",
         "Name":"000000110001",
         "DateLastModified":"05\/12\/2021, 07:20 AM"
      }
   ],
   "\_isDocumentPresent":true
}
```