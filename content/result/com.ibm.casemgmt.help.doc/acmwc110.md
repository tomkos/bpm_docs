# Content List widget incoming events

## Clear content event

| Description   | Clear the content in the Content List widget.   |
|---------------|-------------------------------------------------|
| Event ID      | icm.ClearContent                                |
| Payload       | null                                            |

## Display documents event

| Description   | Display the list of documents that are referenced in the event payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.ReceivedDocumentIDs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Payload       | objectStoreNames An array that contains the IBM® Content Navigator repository IDs of the target object stores. symbolicNames An array that contains the symbolic names for the Document properties. values An array of JSON objects that contains the versions series identifiers for the documents. externalColumns An array of Dojo objects in which each object contains the name and identifier of an external column.  The following example illustrates the payload:payload = { "objectStoreNames" : ["TOS"], "symbolicNames": [...], "values": [...], "externalColumns": [{"symbolicName": "", "name": ""}] }; |

## Search with stored search event

| Description   | Run the stored search that is specified in the payload and display the list of documents that are returned by the search.                                                                                                                                                                                                                                                                                                     |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.ReceivedStoredSearch                                                                                                                                                                                                                                                                                                                                                                                                      |
| Payload       | StoredSearch.objectStoreName  The IBM Content Navigator repository ID of the             target object store or the target object store name.  StoredSearch.vsId The version series identifier of the stored search that is to be run. StoredSearch.version A string that indicates the version of the stored search that is to be run.                       The valid values are current or                       released. |

## Search with values event

| Description   | Use the name and value pairs that are specified in the event payload as the criteria for the configured stored search. Run the search and display the list of documents that is returned.        |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.ReceivedSearchValues                                                                                                                                                                         |
| Payload       | A list of properties each with name and value pair to be used as criteria for the configured stored search. The following example illustrates the payload: [{name:"AT\_companyName",value:"IBM"}] |

## Search with work item event

| Description   | Use the workflow data field values that are specified in the event payload as the criteria for the configured stored search. Run the search and display the list of documents that is returned.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendWorkItem                                                                                                                                                                                  |
| Payload       | workItem An icm.model.WorkItem object that represents the work item for which a list of documents is to be returned.                                                                              |