# Modifying configuration parameters for the BPM document store

## About this task

| Configuration parameter                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cmisUrl                                          | The cmisURL parameter is used to customize the CMIS URL that is used by the Business Automation Workflow server. By default, the value of the parameter is not set and a local HTTPS connection is used with /fncmis as the context root. For performance reasons, you could replace the cmisUrl with an unencrypted local URL, as shown in the following example: http://local\_Http\_Proxy\_Server\_In\_Secure\_Network\_Zone/fncmis However, the credentials of the technical user will be sent in an HTTP basic authentication header and WS-Security Username Token over this connection. As a result, using an unencrypted URL is discouraged from a security perspective. |
| numberOfParallelDocumentMigrationWorker          | The numberOfParallelDocumentMigrationWorker parameter is used to specify the maximum number of documents that can be migrated in parallel to the document store. By default, the value of this parameter is set to 10.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| accessControlMigrationMaxDocumentsPerTransaction | The accessControlMigrationMaxDocumentsPerTransaction parameter is used to specify the maximum number of document instances that are migrated in a single transaction during access control migration. By default, the value of this parameter is set to 400. This parameter is only supported if you have Business Automation Workflow with the Basic Case Management feature installed.                                                                                                                                                                                                                                                                                  |
| accessControlMigrationMaxObjectsPerTransaction   | The accessControlMigrationMaxObjectsPerTransaction parameter is used to specify the maximum number of access control objects that are to be changed or created in a single transaction during access control migration. By default, the value of this parameter is set to 500. The value for this configuration parameter must be higher than the value for the accessControlMigrationMaxDocumentsPerTransaction parameter because a document can have one or more access control objects. This parameter is only supported if you have Business Automation Workflow with the Basic Case Management feature installed.                                                    |
| caseHistoryEnabled                               | The caseHistoryEnabled parameter is used to specify whether historic information about a case is saved with the case folder. It is only supported if you have Business Automation Workflow with the Basic Case Management feature installed. By default, the value of this parameter is set to true. When this property is temporarily set to false and later set to true again, the runtime will not restore the events that occurred while the case history was disabled. These events are permanently lost.                                                                                                                                                            |

## Example

The following examples show how to read and modify the
configuration parameters for the BPM document store using
wsadmin scripting:

```
// List all BPM document stores. If there is only one deployment environment, then there is only one document store.
docStores = AdminUtilities.convertToList(AdminConfig.list("BPMDocumentStore"))

// Read the first BPM document store
docStore = docStores[0]

// Show one specific attribute of the BPM document store
AdminConfig.showAttribute(docStore, "cmisUrl")
AdminConfig.showAttribute(docStore, "numberOfParallelDocumentMigrationWorker")
AdminConfig.showAttribute(docStore, "accessControlMigrationMaxDocumentsPerTransaction")
AdminConfig.showAttribute(docStore, "accessControlMigrationMaxObjectsPerTransaction")
AdminConfig.showAttribute(docStore, "caseHistoryEnabled")

// Update one specific attribute of the BPM document store
AdminConfig.modify(docStore, [["cmisUrl", "new value"]])
AdminConfig.modify(docStore, [["numberOfParallelDocumentMigrationWorker", 5]])
AdminConfig.modify(docStore, [["accessControlMigrationMaxDocumentsPerTransaction", 200]])
AdminConfig.modify(docStore, [["accessControlMigrationMaxObjectsPerTransaction", 300]])
AdminConfig.modify(docStore, [["caseHistoryEnabled", false]])

// Save the configuration
AdminConfig.save()
```