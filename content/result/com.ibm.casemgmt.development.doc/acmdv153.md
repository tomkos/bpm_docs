# POST method for save and apply Security manifest

## URI

| Name                    | Type   | Parameter/Value                                                               | Description                                                                                                                      |
|-------------------------|--------|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| DesignObjectStore       | String | Mandatory parameter                                                           | The symbolic name of the Design Object Store.                                                                                    |
| SolutionName            | String | Mandatory parameter                                                           | Name of the solution, where security manifest needs to be created or applied.                                                    |
| ManifestName            | String | Mandatory parameter                                                           | Name of the manifest, which needs to be created and applied.                                                                     |
| TargetEnvironmentName   | String | Mandatory parameter for production environment if manifest action is "apply". | Name of Target Environment or Project Area.                                                                                      |
| ApplyRoleMembership     | String | Default parameter value is false.                                             | This option applies the role membership configuration to the solution. The previously configured role membership is overwritten. |
| applyDiscretionaryTasks | String | Default parameter value is false.                                             | This option applies discretionary activities in addition to the security configuration.                                          |
| manifestAction          | String | Default parameter value is "save".                                            | If you want to create or edit and apply the security manifest, use "apply", else save to create or edit the manifest.            |

| Name                   | Description                                                                                                                                                                                                                            |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| manifestName           | Name of the manifest, which needs to be created and applied.                                                                                                                                                                           |
| allCaseTypes           | Keep it empty array if there is no common privilege for all the case types. If there is common privilege for all the case types, make the entry like "allCaseTypes":[{"roleName":"role1","rolePrivileges":["view","update","manage"]}] |
| caseTypes              | Define the privilege per case type.                                                                                                                                                                                                    |
| solutionRoles          | Define the solution roles with the participants.                                                                                                                                                                                       |
| securityAdministrators | Define security administrators array with their role privileges.                                                                                                                                                                       |

## POST

```
POST https://example.com:9443/CaseManager/CASEREST/v1/saveSolutionSecurityManifest?DesignObjectStore=dos&SolutionName=testSol&ManifestName=test\_security\_manifest&ApplyRoleMembership=true&AapplyDiscretionaryTasks=true&manifestAction=apply
```

```
{
    "manifestName": "test\_security\_manifest",
    "allCaseTypes": [],
    "caseTypes": [{
        "caseTypeName": "TS\_caseType",
        "caseTypeRoles": [{
            "roleName": "role\_name",
            "rolePrivileges": ["create", "view", "update", "manage"]
        }]
    }],
    "solutionRoles": [{
        "roleName": "role\_name",
        "participants": []
    }],
    "securityAdministrators": [{
        "SHORT\_NAME": "deadmin",
        "adminName": "deadmin",
        "principalType": "User",
        "rolePrivileges": ["fullcontrol"]
    }]
}
```