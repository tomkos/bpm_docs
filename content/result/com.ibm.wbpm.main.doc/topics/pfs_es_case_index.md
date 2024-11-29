# How case instances are stored in the federated data repository

- GET http://my.elasticsearchOrOpensearch.host:port/myIndex/\_search?q=document.subtype:instance

- GET http://my.elasticsearchOrOpensearch.host:port/myIndex/\_doc/PI\_1234

- bd.parameterName.string for a string
- bd.parameterName.boolean for a Boolean
- bd.parameterName.date for a date
- bd.parameterName.long for a long
- bd.parameterName.double for a double

- Instance document fields for case instances
- For more information

## Instance document fields for case instances

| Field name                            | Type     | Definition                                                                                                             |
|---------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------|
| case.instance.folderowner.key         | String   | Case instance folder owner.                                                                                            |
| case.instance.health.key              | String   | Case health status.                                                                                                    |
| case.instance.identifier.key          | String   | Case identifier.                                                                                                       |
| case.instance.lastmodifier.key        | String   | Case instance last modifier.                                                                                           |
| case.instance.owners.key              | String   | Case instance owners.                                                                                                  |
| case.instance.quicktaskassignnees.key | String   | Case instance quick task assignees.                                                                                    |
| case.instance.stage.status.key        | String   | Case instance stage status                                                                                             |
| case.instance.teammembers.key         | String   | Case instance team members                                                                                             |
| document.subtype                      | String   | Subtype of the document (set to "instance" for a case document).                                                       |
| instance.creationtime.date            | DateTime | Case instance creation date.                                                                                           |
| instance.lastmodification.date        | DateTime | Case instance last modified date.                                                                                      |
| instance.piid.key                     | String   | Case ID or case GUID.                                                                                                  |
| instance.processinstancename.string   | String   | Case title or case title property name.                                                                                |
| instance.starterid.key                | String   | Case instance creator                                                                                                  |
| instance.status.key                   | String   | Status of the case instance. For a case instance, the status values are: New, Working, Initializing, Complete, Failed. |
| process.processappacronym.string      | String   | Solution prefix, or acronym of the solution process application.                                                       |
| process.processtemplateid.key         | String   | Case type identifier.                                                                                                  |
| process.processtemplatename.key       | String   | Case type name.                                                                                                        |
| process.processappname.string         | String   | Solution name, or name of the solution process application.                                                            |
| process.processappid.key              | String   | Identifier of the process application that defines the BPD or BPMN process.                                            |

## For more information