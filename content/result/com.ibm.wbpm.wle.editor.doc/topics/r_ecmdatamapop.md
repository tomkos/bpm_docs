# Data mapping in Enterprise Content Management (ECM) operations

- Add document to folder
- Add folder to folder
- Cancel check-out document
- Check-in document
- Check-out document
- Copy document
- Create document
- Create folder
- Delete document
- Delete folder
- Get all document versions
- Get children
- Get document
- Get document content
- Get documents in folder
- Get folder
- Get folder by path
- Get folder tree
- Get type definition
- Get type descendants
- Move document
- Move folder
- Remove document from folder
- Remove folder from folder
- Rename document reference
- Rename folder reference
- Search
- Set document content
- Update document properties
- Update
folder properties

## Add document to folder

Input:

- Parent folder ID (ECMID): The identifier
of the BPM managed store folder
for which a child document is to be referenced. For other servers,
an identifier of the folder that will contain the document.
- Document ID (ECMID): For an BPM managed store server,
the identifier of the document in the external ECM system. For other
servers, a unique identifier of a document object.
- Document server name (String): For an BPM managed store server,
the name of the ECM server of the external system. For other servers,
this parameter is not available.
- Reference name (String): (Optional) For
an BPM managed store server,
the name of the referenced document. For other servers, this parameter
is not available.
- Server name (String): The name of the server
that contains the document.

Output:

- No output is returned.

## Add folder to folder

Input:

- Parent folder ID (ECMID): The identifier
of the BPM managed store folder
for which a child folder is to be referenced.
- Folder ID (ECMID): The identifier of the
folder in the external ECM system.
- Folder server name (String): The name of
the ECM server of the external system.
- Reference name (String): (Optional) The
name of the referenced folder.
- Server name (String): The name of the server
that contains the folder.

Output:

- No output is returned.

## Cancel check-out document

Input:

- Private working copy document ID (ECMID):
A unique identifier for the private working copy of the document object.
- Server name (String): The name of the server
containing the original document.

Output:

- No output is returned.

## Check-in document

Input:

- Private working copy document ID (ECMID):
A unique identifier for the private working copy of the document object.
- Major (Boolean): (Optional) An indicator
of the version of the checked-in document. If set to true then the
document is a major version, which is the default.
- Content stream (ECMContentStream): (Optional)
A stream of data containing the content of the document such as a
word processing document or an image. Information about the ECMContentStream
data type is found in the topic Working with document content.
- Check-in comment (String): (Optional) A
comment about the checked-in document.
- Properties (ECMProperty []): (Optional)
A set of named properties that can be in any order.
- Server name (String): The name of the server
to contain the original document.

Output:

- Document ID (ECMID): A unique identifier
of the document object.

## Check-out document

Input:

- Document ID (ECMID): A unique identifier
of a document object.
- Server name (String): The name of the server
containing the document.

Output:

- Private working copy document ID (ECMID):
A unique identifier for a private working copy of the document object.

## Copy document

Input:

- Document ID (ECMID): A unique identifier
of a document.
- Parent folder ID (ECMID): A unique identifier
of the parent folder for the document.
- Name (String): Optional - A new name for
the copied document. When the name is set, it overrides the name in
the ECMProperty list (if specified).
- Versioning state (String) : (Optional) Aname that defines the version of the document. Valid values are:
    - major: (Default) The copied document is a major version. If versioning
is disabled, the major value is not a valid
versioning state and you must use the none value
instead.
    - minor: The copied document is a minor version.
    - checkedout: The copied document has a checked-out state.
    - none: The copied document cannot be versioned.
- Properties (ECMProperty []): (Optional)
A set of named properties that can be in any order.
- Server name (String): The name of the server
for the document.

Output:

- Document ID (ECMID): A unique identifier
of the new document.

## Create document

Input:

- Object type ID (ECMID): This identifier
corresponds to a class name defined on the ECM system that is used
to create a document. For example, the value cmis:document can
be used to define a basic document. Alternatively, a class name can
be used that corresponds to a class derived from cmis:document.
If you select BPM document store as
the server name, the IBM\_BPM\_Document object
type ID is automatically specified and it cannot be changed.
- Folder ID (ECMID): An identifier for the
parent folder of the document. A right slash character (/) specified
as the value denotes the root folder in the target server. Alternatively,
a relative folder name for the root can be specified; for example, /MyFolder.
- Name (String): The name of the document.
- Versioning state (String) : (Optional) Aname that defines the version of the document. Valid values are:
    - major: (Default) The created document is a major version. If versioning
is disabled, the major value is not a valid
versioning state and you must use the none value
instead.
    - minor: The created document is a minor version.
    - checkedout: The created document has a checked-out state.
    - none: The created document cannot be versioned.
- Content stream (ECMContentStream): (Optional)
A stream of data containing the content of the document such as a
word processing document or an image. Information about the ECMContentStream
data type is found in the topic Working with document content.
- Properties (ECMProperty []): (Optional)
A set of named properties that can be in any order.
- Server name (String): The name of the server
for the document.

Output:

- Document ID (ECMID): The value of this
field identifies a variable that will be used by the service to store
a unique identifier for the new document. For example, if an output
variable named outputDocumentId is defined,
the selector button of the field can be used to set the value to tw.local.outputDocumentId.
After the Create document operation is successfully
run, a unique identifier for the new document is generated by the
system and assigned to the variable.

## Create folder

Input:

- Object type ID (ECMID): The ID of the object's
type. It's base type must be a folder.
- Parent folder ID (ECMID): The identifier
of the parent folder.
- Name (String): The name of the folder.
- Properties (ECMProperty []): (Optional)
A set of named properties that can be in any order.
- Server name (String): The name of the server
for the folder.

Output:

- Folder ID (ECMID): A unique identifier
of the new folder.

## Delete document

Input:

- Document ID (ECMID): A unique identifier
of a document object.
- All versions (Boolean): (Optional) States
whether all versions of the document are to be deleted. The default
is true.
- Server name (String): The name of the server
containing the document.

Output:

- No output is returned.

## Delete folder

Input:

- Folder ID (ECMID): A unique identifier
of a folder object.
- Server name (String): The name of the server
containing the folder.

Output:

- No output is returned.

## Get all document versions

Input:

- Version series ID (ECMID): The version
series identifier that is stored in the cmis:versionSeriesId property.
- Server name (String): The name of the server
containing the document.

Output:

- Documents (ECMDocument []): All versions
of the document.

## Get children

Input:

- Folder ID (ECMID): The folder identifier
that references the children, which can be documents and folders.
- Max items (Integer): (Optional) This value does not override the maximum
value configured at the repository level, for example, defaultMaxItems.
- Skip count (Integer): (Optional) The number
of potential results that the repository must skip over or page over
before results are returned. Defaults to 0.
- Order by (String): (Optional) A comma-separated
list of query names and the ascending modifier, ASC, or the descending
modifier, DESC, for each query name.
- Filter (String): (Optional) A comma-delimited
list of property definition query names. The operation returns only
the properties in the matched object if they exist on the matched
object type definition and in the filter.
- Include allowable actions (Boolean): (Optional)
An indicator that retrieves the available actions for the objects
that are returned in the query. The default is false.
- Server name (String): The name of the server
that contains the folder.

Output:

- Search result (ECMSearchResult): A list
of documents and folders that match the input criteria.

## Get document

Input:

- Document ID (ECMID): A unique identifier
of the document.
- Server name (String): The name of the server
containing the document.
- Max items (Integer): This value does not override the maximum value
configured at the repository level, for example, defaultMaxItems.

Output:

- Document (ECMDocument): The document object.

## Get document content

Input:

- Document ID (ECMID): A unique identifier
of a document.
- Server name (String): The name of the server
containing the document.

Output:

- Content stream (ECMContentStream): The
stream of data containing the content of the document. Information
about the ECMContentStream data type is found in the topic Working with document content.

## Get documents in folder

The number of documents returned depends on the configured value of the repository. The default
is typically 25 and can be changed with defaultMaxItems within Content Management
Interoperability Services (CMIS).

Input:

- Folder ID (ECMID): A unique identifier
of the folder containing the documents.
- Server name (String): The name of the server
containing the folder.

Output:

- Documents (ECMDocument []): The documents
contained in the folder.

## Get folder

Input:

- Folder ID (ECMID): A unique identifier
of a folder.
- Server name (String): The name of the server
containing the folder.

Output:

- Folder (ECMFolder): The folder object.

## Get folder by path

Input:

- Path (String): The path to the folder.
A "/" represents a root folder.
- Server name (String): The name of the server
containing the folder.

Output:

- Folder (ECMFolder): The folder object.

## Get folder tree

Input:

- Folder ID (ECMID): A unique identifier
of a folder. It indicates the top level of the tree structure.
- Depth (Integer): (Optional) The number
of levels of folders to return. The default, -1, returns all descendant
folders.
- Server name (String): The name of the server
containing the folder.

Output:

- Folders (ECMFolder []): The folder objects
contained within the specified folder and its level of descendants.

## Get type definition

Input:

- Object type ID (ECMID): The ID of an Object-Type.
- Server name (String): The name of the server
containing the object type.

Output:

- Object type definition (ECMObjectTypeDefinition):
The definition of the type. The ECMObjectTypeDefinition object contains
the type metadata.

## Get type descendants

Input:

- Object type ID (ECMID): (Optional) An ID
of an Object-Type. If not specified, all root object types are returned.
- Depth (Integer): (Optional) The number
of levels of the type hierarchy to return. the default, -1, returns
all descendant types.
- Include property definitions (Boolean):
(Optional) An indicator that specifies whether type properties are
to be returned. The default, false, means that the properties of the
type are not to be included.
- Server name (String): The name of the server
containing the object type.

Output:

- Object type definitions (ECMObjectTypeDefinition []):
An array of type definitions. The ECMObjectTypeDefinition object contains
the type metadata.

## Move document

Input:

- Document ID (ECMID): A unique identifier
of a document.
- Target folder ID (ECMID): A unique identifier
of the new folder for the document.
- Source folder ID (ECMID): A unique identifier
of the present folder for the document.
- Server name (String): The name of the server
containing the document and folders.

Output:

- No output is returned.

## Move folder

Input:

- Folder ID (ECMID): The identifier of the
folder.
- Target folder ID (ECMID): The identifier
of the new parent folder.
- Source folder ID (ECMID): The identifier
of the old parent folder.
- Server name (String): The name of the ECM
server that identifies the corresponding ECM repository.

Output:

- No output is returned.

## Remove document from folder

Input:

- Parent folder ID (ECMID): The identifier
of the BPM managed store folder
for which a child document is to be unreferenced. For other servers,
an optional identifier of the parent folder of the document; and,
if not specified, the document is removed from all folders.
- Document ID (ECMID): For an BPM managed store server,
the identifier of the document in the external ECM system. For other
servers, a unique identifier of a document.
- Document server name (String): For an BPM managed store server,
the name of the ECM server of the external system. For other servers,
this parameter is not available.
- Server name (String): The name of the server
containing the document.

Output:

- No output is returned.

## Remove folder from folder

Input:

- Parent folder ID (ECMID): The identifier
of the BPM managed store folder
for which a child folder is to be unreferenced.
- Folder ID (ECMID): The identifier of the
folder in the external ECM system.
- Folder server name (String): The name of
the ECM server of the external system.
- Server name (String): The name of the server
containing the folder.

Output:

- No output is returned.

## Rename document reference

Input:

- Parent folder ID (ECMID): The identifier
of the BPM managed store folder
for which a child document is referenced.
- Document ID (ECMID): For an BPM managed store server,
the identifier of the document in the external ECM system.
- Document server name (String): For an BPM managed store server,
the name of the ECM server of the external system.
- Reference name (String): For an BPM managed store server,
the new name of the referenced document.
- Server name (String): The name of the server
that contains the folder. The server name must be  ECMServerNames.IBM\_BPM\_MANAGED\_STORE
when using data mapping.

Output:

- No output is returned.

## Rename folder reference

Input:

- Parent folder ID (ECMID): The identifier
of the BPM managed store folder
for which a child folder is referenced.
- Folder ID (ECMID): The identifier of the
folder in the external ECM system.
- Folder server name (String): The name of
the ECM server of the external system.
- Reference name (String): The new name of
the referenced folder.
- Server name (String): The name of the server
that contains the folder. The server name must be  ECMServerNames.IBM\_BPM\_MANAGED\_STORE
when using data mapping.

Output:

- No output is returned.

## Search

Input:

- CMIS query (String): Text containing a
Content Management Interoperability Services (CMIS) query. See Building a query for an Enterprise Content Management search operation.
- Return type (String) : (Optional) An indicatorthat determines the type of items returned by the search result. Thefollowing types can be specified:
    - ECMSearchResultRow: (Default) An ECMSearchResultRow contains an
array of values. The name is the query name of the Content Management
Interoperability Service (CMIS) property used in the SELECT clause
of the query or the name can be determined by introspection of the
metadata.
    - Business object name: When the name of a business object type
is specified then an instance of that type is returned. The properties
returned by the search are mapped to the properties of the business
object if their names match.
- Search all versions (Boolean): (Optional)
An indicator that specifies which document versions are to be considered.
If true then it considers the latest and older versions of the document
or documents in the search. If false, which is the default, then only
the latest version is returned.
- Max items (Integer): (Optional) This value does not override the maximum
value configured at the repository level, for example, defaultMaxItems.
- Skip count (Integer): (Optional) An indicator
that specifies the number of potential items to be skipped over before
returning any items. The default is 0.
- Include allowable actions (Boolean): (Optional)
An indicator that retrieves the available actions for the objects
returned in the query. This parameter is only offered with the BPM content store.
The default is false.
- Server name (String): The name of the server
containing the documents and folders.

Output:

- Search result (ECMSearchResult): An object
containing a set of qualifying items. The content is different based
on the value of the Return type input parameter. The default is an
object of type ECMSearchResultRow.

## Set document content

Input:

- Document ID (ECMID): A unique identifier
of a document.
- Content stream (ECMContentStream): The
stream of data containing the content for the document such as a word
processing document or an image. Information about the ECMContentStream
data type is found in the topic Working with document content.
- Server name (String): The name of the server
containing the document.

Output:

- Document ID (ECMID): The unique identifier
of a document.

The Set document content operation
can only be used after running the Check-out document operation
and before running the Check-in document operation.

## Update document properties

Input:

- Document ID (ECMID): An identifier of a
document object.
- Name (String): (Optional) A new name for
the document.
- Properties (ECMProperty []): (Optional)
A set of named properties that can be in any order.
- Server name (String): The name of the server
containing the document.

Output:

- Document ID (ECMID): The unique identifier
of the document.

## Update folder properties

Input:

- Folder ID (ECMID): An identifier of a folder
object.
- Name (String): (Optional) A new name for
the folder.
- Properties (ECMProperty []): (Optional)
A set of named properties that can be in any order.
- Server name (String): The name of the server
containing the folder.

Output:

- Folder ID (ECMID): The unique identifier
of the folder.