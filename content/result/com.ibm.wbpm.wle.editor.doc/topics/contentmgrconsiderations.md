# Integration considerations for IBM Content
Manager

The following sections describe other integration
considerations for IBM Content
Manager:

- CMIS capabilities
- Compatibility with folders in processes
- Known limitations

## CMIS capabilities

IBM Content
Manager
supports the optional CMIS capabilities that are described in the following table:

| CMIS Capability           | IBM Content Manager   | Business Automation Workflow Considerations             |
|---------------------------|-----------------------|---------------------------------------------------------|
| ACL                       | none                  | Not applicable                                          |
| AllVersionsSearchable     | true                  |                                                         |
| Changes                   | none                  | Not applicable                                          |
| ContentStreamUpdatability | pwconly               | Documents must be checked out for updates               |
| GetDescendants            | true                  |                                                         |
| GetFolderTree             | true                  |                                                         |
| Join                      | none                  | Queries cannot include any JOIN clauses                 |
| Multifiling               | true                  |                                                         |
| PWCSearchable             | false                 | Private working copies of a document are not searchable |
| PWCUpdatable              | false                 | The private working copy of a document is not updatable |
| Query                     | metadataonly          | The CONTAINS() predicate function is not supported      |
| Renditions                | none                  | Not applicable                                          |
| Unfiling                  | true                  |                                                         |
| VersionSpecificFiling     | false                 |                                                         |

## Compatibility with folders in processes

In a process, you define an initial folder structure with references to folders on external ECM
systems. To identify a folder in an external ECM system, you use its path to identify the folder.
IBM Content
Manager
supports two different path types: unrevised path and fast access path. The path you specify in the
process definition may be either path type, but to use the Create
automatically feature, the path has to be an unrevised path. To use unrevised paths, the
findFolderWithoutFastAccessPath configuration property has to be set to true (which
it is by default) and the sortByNameIdealAttribute configuration property has to be
set correctly.

- fastFolderAccessPaths
- findFolderWithoutFastAccessPath
- sortByNameIdealAttribute

## Known limitations

The known limitations of the IBM CMIS for Content Manager 8.4.3 implementation are described in
the topic IBM CMIS for Content Manager implementation of the OASIS CMIS
specification.

Since IBM Content
Manager 8.5.0, the
CMIS implementation is packaged as part of IBM Content Navigator. This new CMIS implementation
resolves some of the earlier limitations. You can, for example, configure properties to enable
features as discussed in Configuring additional IBM CMIS for Content Manager settings. One important
feature you should enable is sorting by name when retrieving the children of a folder. See sortChildrenByNameAndTitle. You want to enable this feature because by
default it is not enabled and set to NONE, which causes an error when you use the
Responsive Document Explorer.