# POST method for apply manifest

## URI

/CASEREST/v1/solution/{solutionAcronym}/applyManifest

| Name            | Type   | Required   | Description                                                              |
|-----------------|--------|------------|--------------------------------------------------------------------------|
| solutionAcronym | String | Yes        | The acronym of the case solution for which manifest needs to be applied. |

| Name                     | Type   | Required   | Description                                              |
|--------------------------|--------|------------|----------------------------------------------------------|
| ConnectionDefinitionName | String | Yes        | Name of the connection definition.                       |
| manifestName             | String | Yes        | The name of the manifest to be applied.                  |
| manifestType             | String | Yes        | The type of manifest. Possible values - Audit, Security. |

## POST curl method request

```
curl -X 'POST' --user <username>:<password> 'https://<hostname>:
<port>/CaseManager/CASEREST/v1/solution/S6O/applyManifest?
ConnectionDefinitionName=dev\_env\_connection\_defintion&manifestName=security1&manifestType=security' -H 'accept: application/json'
```

## POST method response

```
{ "Status": "The security1 security configuration was applied successfully." }
```