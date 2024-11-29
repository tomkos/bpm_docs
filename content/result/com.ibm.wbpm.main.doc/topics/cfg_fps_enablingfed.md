# Enabling indexing on a federated system

## About this task

You enable
indexing by creating change log tables on each of the federated systems and then configuring the
systems to update the tables. You can then configure the indexing service for a federated system
through entries in the server.xml configuration file on Process Federation Server.

- Enabling indexing of BPD-related data in a federated environment

When a business process definition (BPD) runs on a Business Automation Workflow or IBM® BPM system, BPD-related data is written to the Workflow Server or IBM Process Server database (BPMDB).
- Enabling indexing of BPEL-related data in a federated environment

When a BPEL process runs on an Business Automation Workflow or IBM BPM system, BPEL process and task-related data is written to the Business Process Choreographer database. This database is the Shared database and defaults to CMNDB. For this data to be included in the Process Federation Server index, you must create change log tables on the Business Automation Workflow or IBM BPM server, and enable BPEL indexing on Process Federation Server.
- Enabling indexing of Case-related data in a federated environment

The Case management tools provide support for indexing Case instances in a federated data repository index, without having to declare an indexer in the IBM Process Federation Server configuration file.
- Identifying and removing inactive change log consumers

When working on tasks and process instances, the federated business process management system populates the following change logs in the database: PFS\_BPD\_CHANGE\_LOG table for BPD federated systems, and PFS\_BPEL\_CHANGE\_LOG for the BPEL federated systems. Process Federation Server acts as a consumer of this change log to identify which tasks or process instances have been updated on the federated system and then perform corresponding updates to the federated data repository.  If you updated the federated system index name more than 5 times, you may face a degraded performance. A good practice is to remove the inactive consumer columns before you start the Process Federation Server cluster