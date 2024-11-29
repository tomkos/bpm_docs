# Enterprise Content Management (ECM) stores in IBM Business Automation
Workflow

The following ECM stores are included in IBM Business Automation
Workflow:

- BPM content store (deprecated)
- BPM document store
- BPM managed store
- BPM target store

These ECM stores are described in the following sections.

## BPM content store (deprecated)

The BPM content store is used for content management in processes that use the deprecated Basic
Case Management feature. The BPM content store supports a subset of the inbound content event types
that are supported by external ECM systems. Event subscriptions for the BPM content store can only
be created by using the IBM\_BPM\_Document type. To author or run a process that uses
the Basic Case Management feature to manage documents and folders in the BPM content store, you need
to have installed the Basic Case Management feature in a previous release. For more information, see
the topic Deprecated: Inbound events for the BPM content store.

## BPM document store

The BPM document store is an embedded document repository that is enabled for Content Management
Interoperability Services (CMIS). It is used to store documents in IBM Business Automation
Workflow. The BPM document store supports most CMIS
operations and a number of inbound events. You can use either coaches or heritage coaches to work
with documents in the BPM document store. For more information, see the topic The BPM document store or the topic Management of folders and documents for ECM systems.

## BPM managed store

When you build a process, the ECM folders and documents are managed by IBM Business Automation
Workflow using the BPM managed
store as a repository. The BPM managed store permits complex folder structures where folders can be
nested within other folders. Creation of documents attachments using the BPM managed store as a
repository is deprecated. For more information, see the topic Management of folders and documents for ECM systems.

## BPM target store

Processes in a business application workflow can interact with cases running in the case
management feature that is included in IBM Business Automation
Workflow.
The BPM target store is the FileNet® P8 target object
store to which cases are deployed. For more information, see the topic Creating a target object store or
the topic Reassigning the BPM document store.