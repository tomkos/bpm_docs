# Administering the BPM document store

## About this task

- Administering the technical user for the BPM document store

 Traditional: 
 When working with the BPM document store, there are multiple scenarios that require a technical user (system user). The technical user is an identity that the system can use to act on its own. For example, a run-as technical user is required for creating default configurations for the domain, object store, and document class definition. A technical user is also required when IBM Business Automation Workflow connects to the BPM document store using Content Management Interoperability Service (CMIS).
- Obtaining the status of the BPM document store

 Traditional: 
 The getDocumentStoreStatus command is used to obtain the status of the BPM document store and the IBM\_BPM\_DocumentStore application.
- Cleaning up the BPM document store

 Traditional: 
 Freeing up space in the database tables that are used to persist case document and case folder properties allows you to define and add new properties to the case document and case folder classes.
- Migrating document attachments to the BPM document store

 Traditional: 
 After migration, you must migrate your document attachments from the Process database to the BPM document store. The migration of document attachments is a required post-migration task. The original versions of the document attachments will continue to reside in the database until all documents have been migrated. After the migration is complete, you can use either coaches or heritage coaches to work with documents in the BPM document store.
- Managing tracing for the BPM document store

 Traditional: 
 The maintainDocumentStoreTrace command is used to enable or disable tracing for an individual component or all components of the BPM document store.
- Updating the BPM document store application

 Traditional: 
 The updateDocumentStoreApplication command is used to update the installed application IBM\_BPM\_DocumentStore in a deployment target. An update of the application is generally required if an iFix has been installed for the BPM document store or if the role type mapping has changed for the embedded ECMTechnicalUser.
- Modifying configuration parameters for the BPM document store

 Traditional: 
 The BPM document store has some configuration parameters that can be read and modified using wsadmin scripting.
- Using the Administration Console for Content Platform Engine

 Traditional: 
 To administer objects, such as folders and documents, in the embedded content store that is available in Business Automation Workflow, you can use the IBM Administration Console for Content Platform Engine.
- Business Automation Workflow interaction with the Content Platform Engine

 Traditional: 
 When you configure Business Automation Workflow to use an external Enterprise Content Management (ECM) server, the external ECM server can be affected by commands that are run in Business Automation Workflow.
- Limitations in administering the BPM document store

There are some limitations in administering the BPM document store. In most situations, you can successfully work around these limitations.