# Heritage Document List control (deprecated)

For information about how to map deprecated functions to UI functions, see the topic Mapping deprecated functions to UI functions.

## Restrictions and limitations

None

## Data binding

| Binding description                                     | Data type              |
|---------------------------------------------------------|------------------------|
| Each ECMDocumentInfo contains the URL for the document. | ECMDocumentInfo (List) |

## Configuration properties

| Configuration property    | Nested configuration property    | Description                                                                                                                                                                                                                                                                                                                                                                                                                      | Data type                                                                                                                                                           |
|---------------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Allow create              |                                  | Select this option if the user can add a document to the Enterprise Content Management document repository. The default value is false.                                                                                                                                                                                                                                                                                          | Boolean                                                                                                                                                             |
| Allow update              |                                  | Select this option to allow the user to update document content and properties. The default value is false.                                                                                                                                                                                                                                                                                                                      | Boolean                                                                                                                                                             |
| Open in new window        |                                  | Select this option to open the document in a new browser window. The default value is false.                                                                                                                                                                                                                                                                                                                                     | Boolean                                                                                                                                                             |
| Refresh trigger           |                                  | Enables the contents of the view to be refreshed. Bind this property to the private variable that is used by Refresh Controller, Refresh Button, or both.When the value of the bound variable changes to true, the view is refreshed. After the view is refreshed, the value of the variable returns to false. If this configuration is bound to a variable, the Refresh button provided by the Document List control is hidden. | refreshTrigger (Boolean)Default: False (no refresh pending)                                                                                                         |
| Number of results to show |                                  | Set the maximum number of documents in a search result that the user can see in the list at any one time. The default value is 10.                                                                                                                                                                                                                                                                                               | Integer                                                                                                                                                             |
| Show all content          |                                  | Select this option to show all documents. The Number of results to show sets the maximum number of documents in the list.Clear this option to show the documents in a series of pages if the search result returns more than Number of results to show documents. The default value is false.                                                                                                                                    | Boolean                                                                                                                                                             |
| Configure for use with    |                                  | You can accept the default selection ECM Documents or select BPM Documents. Depending on whether you select BPM Documents or ECM Documents, you can set the options in the BPM document options group or the ECM document options group. .                                                                                                                                                                                       | DocumentSelection                                                                                                                                                   |
| BPM document options      |                                  | If you selected BPM Documents in the Configure for use with drop-down list, you can specify the options in the BPM document options group. (The ECM document options group is ignored.)                                                                                                                                                                                                                                          | BPMDocumentOptions                                                                                                                                                  |
|                           | Display options                  | The display options are used to filter the documents that are displayed in the document list.                                                                                                                                                                                                                                                                                                                                    | BPMDocumentDisplayOptions                                                                                                                                           |
|                           | Associated with process instance | If not selected, shows all documents that meet the criteria. If selected, shows only those documents that were created during the run of the BPD. The HS needs to be in a task activity implementation within a BPD and run from there. The default value is false.                                                                                                                                                              | Boolean                                                                                                                                                             |
|                           | Display match rule               | The Display match rule configuration option is used to search for documents based on properties that match in the documents. There are three values:None - Displays a list of all documents regardless of the matching properties that are specified. Any - Displays a list of those documents that match any of the specified properties. All - Displays a list of those documents that match all of the specified properties.  | BPMDocumentMatchRule                                                                                                                                                |
|                           | Display properties               | The name/value pairs that are associated with the documents for which you are searching.                                                                                                                                                                                                                                                                                                                                         | NameValuePair (List)                                                                                                                                                |
|                           | Name                             | Define a name for a display property.                                                                                                                                                                                                                                                                                                                                                                                            | String                                                                                                                                                              |
|                           | Value                            | Define a value for the display property.                                                                                                                                                                                                                                                                                                                                                                                         | String                                                                                                                                                              |
|                           | Upload options                   | The upload options are used to specify an upload name for a document and to specify the properties that you want to associate with the uploaded document. These options are only applicable when Allow create is also selected. The fully qualified path should start with a slash (/), which signifies the root of the Enterprise Content Management system.                                                                    | BPMDocumentUploadOptions                                                                                                                                            |
|                           | Default upload name              | The default name of the document that you want to create.                                                                                                                                                                                                                                                                                                                                                                        | String                                                                                                                                                              |
|                           | User editable                    | Select this to edit the name of the document in the Create Document dialog box. The default value is false.                                                                                                                                                                                                                                                                                                                      | Boolean                                                                                                                                                             |
|                           | Add properties                   | Select this to add the properties specified in the Upload Properties table to the document. The default value is false.                                                                                                                                                                                                                                                                                                          | Boolean                                                                                                                                                             |
|                           | Upload properties                | Specify the properties that you want to associate with the document (if you have selected the Add Properties check box).                                                                                                                                                                                                                                                                                                         | NameValuePair(List)                                                                                                                                                 |
|                           | Name                             | Define a name for the upload property.                                                                                                                                                                                                                                                                                                                                                                                           | String                                                                                                                                                              |
|                           | Value                            | Define a value for the upload property.                                                                                                                                                                                                                                                                                                                                                                                          | String                                                                                                                                                              |
|                           | Hide In Portal                   | Prevents the document from being displayed in the document list. The default value is false.                                                                                                                                                                                                                                                                                                                                     | Boolean                                                                                                                                                             |
| ECM document options      |                                  | If you selected ECM Documents in the Configure for use with drop-down list, you can the options in the ECM document options group are used and the options in the BPM document options group are ignored.                                                                                                                                                                                                                        | CMISDocumentOptions                                                                                                                                                 |
|                           | Parent folder path               | Sets the fully qualified path to the parent folder in the ECM system where users create or upload documents. This option is only applicable when Allow create is also selected. The fully qualified path should start with a slash (/), which signifies the root of the Enterprise Content Management system.                                                                                                                    | String                                                                                                                                                              |
|                           | CMIS query                       | A string of text containing the Content Management Interoperability Services (CMIS) query. For additional information about CMIS queries, see the "Query" section of the CMIS specification. If a query is specified, it is passed to the associated search service where it can be used in the data mapping.                                                                                                                    | String                                                                                                                                                              |
| Search                    |                                  | Specify the service used to search for documents in the Enterprise Content Management document repository.Important: If the Configure for use with option is set to ECM documents, you must provide a service. Use the Default ECM Search Service Ajax service provided in the Content Management (SYSCM) toolkit as a template. The default service shows an example of the expected input and output definition.               | ServiceInput:  maxItems(Integer) skipCount(Integer) searchAllVersions(Boolean) cmisQuery (String) useBPMDocuments (String)    Output: searchResult(ECMSearchResult) |
| Get all document versions |                                  | Specify the service used to get all versions of a specific document in the Enterprise Content Management document repository.                                                                                                                                                                                                                                                                                                    | ServiceInput:  versionSeriesId(ECMID) serverName(String)   Output: documents(ECMDocument)(List)                                                                     |
| Get document              |                                  | Specify the service used to get a specific document in the Enterprise Content Management document repository.                                                                                                                                                                                                                                                                                                                    | ServiceInput:  documentId(ECMID) serverName(String)   Output: documents(ECMDocument)                                                                                |
| Get type definition       |                                  | Specify the service used to get the type metadata of a document or folder in the Enterprise Content Management document repository.                                                                                                                                                                                                                                                                                              | ServiceInput:  objectTypeId(ECMID) serverName(String)   Output: typeDefinition(ECMObjectTypeDefinition)                                                             |
| Get type descendants      |                                  | Specify the service used to get the descendants of a type in the Enterprise Content Management document repository.                                                                                                                                                                                                                                                                                                              | ServiceInput:  objectTypeId(ECMID) serverName(String) depth(Integer) includePropertyDefinitions(Boolean)   Output: typeDefinitions(ECMObjectTypeDefinition)         |