# POST method for import manifest

## URI

/CaseManager/CASEREST/v1/solution/importManifest

| Name     | Type   | Required   | Description                               |
|----------|--------|------------|-------------------------------------------|
| manifest | File   | Yes        | The manifest file that is to be imported. |

## POST curl request

```
curl -v -X 'POST' --user <username>:<password> 'https://<hostname>:<port>/CaseManager/CASEREST/v1/solution/importManifest' -H 'Content-Type: multipart/form-data' -F 'manifest=@C:\Solution\_securityManifest.zip;type=application/x-zip-compressed'
```

## POST method response

```
{
  "Status": "The manifest was imported successfully."
}
```