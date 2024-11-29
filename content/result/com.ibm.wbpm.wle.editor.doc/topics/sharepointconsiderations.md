# Integration considerations for Microsoft
SharePoint

For information about specifying the context path, see Accessing the SharePoint CMIS provider from IBM Business Automation Workflow. You can
contact your Microsoft SharePoint administrator for
complete connection information.

Other integration considerations for Microsoft
SharePoint are described in the following sections:

- Setup
- CMIS capabilities
- Deviations from the CMIS standard
- Document name
- Compatibility with folders in processes
- Time zone of DateTime property values
- Reference

## Setup

Your Microsoft SharePoint installation may use a URL
convention for the CMIS web service endpoint that is not expected by the workflow system. For
information on how to establish the addressability of the CMIS web service, see Accessing the SharePoint CMIS provider from IBM Business Automation Workflow.

## CMIS capabilities

Microsoft SharePoint supports the optional CMIS
capabilities that are described in the following table:

| CMIS capability           | Microsoft SharePoint   | Workflow considerations                                                   |
|---------------------------|------------------------|---------------------------------------------------------------------------|
| ACL                       | manage                 | Not applicable                                                            |
| AllVersionsSearchable     | false                  | A search will only be applied to the latest (major) version of a document |
| Changes                   | objectidsonly          | Not applicable                                                            |
| ContentStreamUpdatability | anytime                |                                                                           |
| GetDescendants            | false                  | Not applicable                                                            |
| GetFolderTree             | true                   |                                                                           |
| Join                      | none                   | Queries cannot include any JOIN clauses                                   |
| Multifiling               | false                  | Documents can only reside in one folder                                   |
| PWCSearchable             | true                   |                                                                           |
| PWCUpdatable              | true                   |                                                                           |
| Query                     | bothseparate           |                                                                           |
| Renditions                | none                   | Not applicable                                                            |
| Unfiling                  | false                  | Documents are always filed in a folder                                    |
| VersionSpecificFiling     | false                  |                                                                           |

## Deviations from the CMIS standard

Microsoft SharePoint deviates from the OASIS CMIS
standard in the following ways:

- When a document is being created, the content of the document must be provided.
- The IN and LIKE operators are not supported for WHERE clauses in queries.

## Document name

Microsoft SharePoint does not allow you to store a separate document name and file name for its
content. When you create a document, Microsoft SharePoint automatically takes your provided document
name and adds the file extension from the content file name. This concatenated name is then used as
the document name. For example, if your content has a file name Claim.pdf and your
value for the document name is Claim 2016-123, then Microsoft SharePoint stores the
document by using the Claim 2016-123.pdf name.

When you check in a document that uses a Content Integration step in a service, you cannot
provide both a new name and a file name for the content. A request with both names fails. Instead,
either set the file name on the content or the document name.

When you create or update a document that uses the Document Explorer, Document List or Heritage
Document List coach views, the document name is automatically calculated based on the previous
description.

## Compatibility with folders in processes

Microsoft SharePoint does not allow you to perform
queries with the cmis:objectId and cmis:versionSeriesId in the
WHERE clause. Documents and folders referenced from these systems are not returned with accurate
information in a Get children operation against the BPM managed store. See References to external ECM systems from a BPM folder.

## Time zone of DateTime property values

The CMIS responses from Microsoft SharePoint contain
DateTime values that are specified in coordinated universal time (UTC), but without any time zone
information. By default, these values will be interpreted using the workflow system's own default
time zone. This can lead to incorrect values, such as when using content integration tasks in a
service flow or when using the Document Explorer and Document List views in a human service. To
correct this behavior, you can add or update the ecm-server-default-timezone
setting in the 100Custom.xml files. For example, when a CMIS response contains
DateTime values without any time zone, you can use the setting to configure the workflow system to
assume the UTC time zone. For more information about using the
ecm-server-default-timezone setting, see the topic Setting default time zones for ECM servers.

## Reference

For information about the Microsoft SharePoint
implementation of the OASIS CMIS standard, see the Microsoft topic Content Management Interoperability Services (CMIS) connector overview (SharePoint Server
2010).

- Accessing the SharePoint CMIS provider

The Content Management Interoperability Services (CMIS) standard is used to provide integration with Enterprise Content Management (ECM) systems like Microsoft SharePoint. The CMIS functionality is composed of nine separate web service endpoints.