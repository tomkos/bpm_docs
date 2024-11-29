# POST method for importing legacy solutions

## URI

/CASEREST/v1/solution/import

| Name                   | Type   | Required   | Description                                                                      |
|------------------------|--------|------------|----------------------------------------------------------------------------------|
| zipFile                | File   | Yes        | The compressed file, which contains the solution package that is to be imported. |
| projectAreaName        | String | Yes        | Name of the project area where the solution needs to be imported.                |
| overwrite              | String | Optional   | Value to indicate whether the solution needs to be overwritten or not.           |
| serviceDataMapFile     | File   | Optional   | The service datamap XML file.                                                    |
| principalDataMapFile   | File   | Optional   | The principal datamap XML file.                                                  |
| objectStoreDataMapFile | File   | Optional   | The object store datamap XML file.                                               |

## POST curl method request

```
curl -X 'POST' --user <username>:<password> 'https://example.com:9443/CaseManager/CASEREST/v1/solution/import' -H 'accept: application/json' -H 'Content-Type:
 multipart/form-data' -F 'zipFile=@C:\SolutionCB1\_solution.zip;type=application/x-zip-compressed' -F 'projectAreaName=dev\_env\_connection\_definition' --insecure
```

## POST method response

```
{"result":"success","SolutionPrefix":"SCB1","SolutionName":"SolutionCB1"}
```