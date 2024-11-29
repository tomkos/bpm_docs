# How process instances are stored in the federated data repository

- GET http://my.elasticsearchOrOpensearch.host:port/myIndex/\_search?q=document.subtype:instance

- GET http://my.elasticsearchOrOpensearch.host:port/myIndex/\_doc/PI\_1234

- bd.parameterName.string for a string
- bd.parameterName.boolean for a Boolean
- bd.parameterName.date for a date
- bd.parameterName.long for a long
- bd.parameterName.double for a double

- Instance document fields for BPD or BPMN process instances
- For more information

## Instance document fields for BPD or BPMN process instances

| Field name                          | Type   | Definition                                                                                                                                                                                                                                                                         |
|-------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| document.subtype                    | String | Subtype of the document (set to "instance" for an instance document).                                                                                                                                                                                                              |
| instance.piid.key                   | String | Identifier of the process instance.                                                                                                                                                                                                                                                |
| instance.processinstancename.string | String | Name of the process instance.                                                                                                                                                                                                                                                      |
| instance.snapshotid.key             | String | Identifier of the process instance snapshot.                                                                                                                                                                                                                                       |
| instance.snapshotname.string        | String | Name of the process instance snapshot                                                                                                                                                                                                                                              |
| instance.status.key                 | String | Status of the process instance.For a BPD or BPMN process instance, valid values are: Active, Completed, Failed, Terminated, Did\_not\_Start and Suspended.                                                                                                                           |
| instance.parentcaseid.key           | String | Case identifier of the process. This parameter is set only for BPD or BPMN processes that are started by Case.                                                                                                                                                                     |
| instance.parentactivityid.key       | String | Case activity identifier of the process. This parameter is set only for BPD or BPMN processes that are started by Case.                                                                                                                                                            |
| instance.workflowapplication.key    | String | Case solution prefix of the process. This parameter is set only for BPD or BPMN processes that are started by Case.                                                                                                                                                                |
| process.processappacronym.string    | String | Acronym of the process application.                                                                                                                                                                                                                                                |
| process.processtemplateid.key       | String | For BPD or BPMN process instances: identifier of the BPD in which the process is modeled, prefixed with 25.                                                                                                                                                                        |
| process.processtemplatename.key     | String | For BPD or BPMN process instances: name of the process itself.                                                                                                                                                                                                                     |
| process.processappname.string       | String | For BPD or BPMN process instances: name of the process application.                                                                                                                                                                                                                |
| process.processappid.key            | String | Identifier of the process application that defines the BPD or BPMN process.                                                                                                                                                                                                        |
| instance.ownergroupid.key           | String | Identifier of the group of users that is the process instance owner. This value matches groups identifiers that are returned by the User Details BPD REST API from a request on the includeInternalMemberships=true, parts=membership, or includeMembershipsAsIDs=true parameters. |

## For more information