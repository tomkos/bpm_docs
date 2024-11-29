# Integration considerations for IBM®
FileNet Content Manager

You can contact your FileNet Content
Manager administrator
for complete connection information.

The following sections describe other integration considerations for FileNet Content
Manager.

- CMIS capabilities
- Best practices

## CMIS capabilities

FileNet Content
Manager
supports the optional CMIS capabilities that are described in the following table:

| CMIS capability           | IBM FileNet Content Manager   | Workflow considerations                                                                                              |
|---------------------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------|
| ACL                       | none                          | Not applicable                                                                                                       |
| AllVersionsSearchable     | true                          |                                                                                                                      |
| Changes                   | none                          | Not applicable                                                                                                       |
| ContentStreamUpdatability | pwconly                       | Documents must be checked out for updates                                                                            |
| GetDescendants            | true                          |                                                                                                                      |
| GetFolderTree             | true                          |                                                                                                                      |
| Join                      | innerandouter                 |                                                                                                                      |
| Multifiling               | true                          |                                                                                                                      |
| PWCSearchable             | true                          |                                                                                                                      |
| PWCUpdatable              | true                          |                                                                                                                      |
| Query                     | metadataonly or bothcombined  | The CONTAINS() predicate is only supported if IBM Content Search Services is configured for the target object store. |
| Renditions                | none                          | Not applicable                                                                                                       |
| Unfiling                  | true                          |                                                                                                                      |
| VersionSpecificFiling     | false                         |                                                                                                                      |

## Best practices

The cmis:name property of document types

FileNet Content
Manager
document classes have a Name property that is mapped to one of the other properties
of the document class. By default, it is mapped to the DocumentTitle property. The
CMIS implementation maps the Name property to cmis:name, but also
returns the property that it is mapped from when you request an object type definition.

Views, such as Responsive Document Explorer and Responsive Document List, render a user interface
based on the available properties in the object type definition when you create or update a
document. Because of the behavior described previously, it will show both properties. When you enter
different values in them, only one of them will be saved.

- You can configure the mapped property (DocumentTitle by default) as hidden for
the document classes that you use in your FileNet Content
Manager system. These
hidden properties are filtered out by default by the CMIS implementation, and then only the
name property is shown. Note that your CMIS configuration can also be configured to
show hidden properties. See Filter hidden properties (filterHiddenProperties) in the FileNet P8
documentation.
- You can customize the Get type definition AJAX service on your view to filter
out a property in your solution.