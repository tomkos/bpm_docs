# Integration considerations for Alfresco Community

Other integration considerations for Alfresco Community are described in the following
sections:

- CMIS capabilities
- Deviations from the CMIS standard

## Capabilities

Alfresco Community supports the optional CMIS capabilities that are described in the following
table:

| CMIS capability           | Alfresco Community   | Workflow considerations                                 |
|---------------------------|----------------------|---------------------------------------------------------|
| ACL                       | manage               | Not applicable                                          |
| AllVersionsSearchable     | false                |                                                         |
| Changes                   | none                 | Not applicable                                          |
| ContentStreamUpdatability | anytime              |                                                         |
| GetDescendants            | true                 |                                                         |
| GetFolderTree             | true                 |                                                         |
| Join                      | none                 | Queries cannot include any JOIN clauses                 |
| Multifiling               | true                 |                                                         |
| PWCSearchable             | false                | Private working copies of a document are not searchable |
| PWCUpdatable              | true                 |                                                         |
| Query                     | bothcombined         |                                                         |
| Renditions                | read                 | Not applicable                                          |
| Unfiling                  | false                | Documents are always filed in a folder                  |
| VersionSpecificFiling     | false                |                                                         |

## Deviations from the CMIS standard

Alfresco deviates from the OASIS CMIS standard in the following ways:

- The ECM operation Remove Document From Folder (CMIS
removeObjectFromFolder) requires the specification of the Parent
Folder Id (CMIS folderId) parameter even though the CMIS standard
defines it as optional.
- When a new version of a document is being created, Alfresco requires a new unique document name
to be specified.