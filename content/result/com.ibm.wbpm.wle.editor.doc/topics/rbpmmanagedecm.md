# Management of folders and documents for ECM systems

Folders and documents are key concepts in ECM systems.
Folders are similar to paper folders. Folders are containers for other
folders, called subfolders, or documents. Folders provide a structure
for the information on an ECM system. A document might be a credit
report document. The credit report document might have a title for
the person who is associated with the credit report. The document
might have sections for a credit report store and a history of transactions
that involve credit for this person. Each time this document was used
for a person's credit information, that document structure would be
followed. Folders and documents must be managed.

- Management of folders and documents with the BPM document store and an external ECM system
- Migrating process instances between the two ways of managing folders and documents

## Management of folders and documents with the BPM document store and an external ECM
system

In the Process editor, you can integrate the content of your existing ECM systems with an
Business Automation Workflow solution. Your
ECM systems are available for integration as you can define the ECM server settings in the process
application settings page. See Adding an Enterprise Content Management server.

In the Folders tab of your process, you define the initial folder
structure of an instance. The structure consists of references to folders in your ECM systems that
is specified by a path. These folder references can be static; for example, references to folders
that contain document templates that are relevant to the solution. By using the values of variables,
they can also be specific to the instance. A link to a folder specific for a claim instance can be
made by including a claimId variable in the path. You can select a
Create automatically checkbox to create this instance-specific folder
automatically. See Selecting IBM Business Automation Workflow or an external ECM system to manage folders.

The Content Integration tools provide a way of working with your folder structure at run time.
Your users see this folder structure when they work with the instance in IBM Process
Portal. See Integrating with an ECM system or a BPM document store

## Migrating process instances between
the two ways of managing folders and documents

When you
install a new snapshot of a process application, you must decide how
to handle the data from the previous snapshot. Specifically, you must
decide how to handle instances that are still running from the previous
snapshot. An instance is an active process.

When do you migrate instances? Suppose you created a process in a previous release such as
IBM BPM 8.5.6, which you created with the Basic
Case Management feature that uses the case editor. Next, you created a snapshot of your process
application, installed the snapshot on a server, activated it, and started your instances.

Now, you switched your content management mode to Business Automation Workflow. See Changing the way enterprise content is accessed. The Business Automation Workflow mode is based on the
BPM document store, whereas the
previous selection is based on the BPM content store. The BPM document store allows complex folder
structures, which means folders can be nested within folders. For more information on different
types of ECM stores, see Enterprise Content Management (ECM) stores in IBM Business Automation
Workflow. Once you made this switch, you continued to develop your processes and took another
snapshot of your process application. You installed your process application on the server and
activated it. Running instances from the previous snapshot can be migrated now to the new snapshot.
See Migrating snapshots by using Workflow Center. You can migrate an instance that has reached its
end state; that is, the instance finished running. However, the content remains unchanged.

- A BPM-managed root folder is created in the BPM document store. The
processIntanceFolderId is updated to the new root folder's ID.
- New folders and folder references that are modeled on the new version of the process are
added.
- A folder reference that references the previous root folder is
created.
- Existing local documents that are associated with the instance are added to the new root folder.
See Local documents.

The reverse situation is not possible. The Basic Case Management feature is no longer in
Business Automation Workflow.

You do not have to migrate process instances. You can leave the instances currently running to
complete with the previously installed snapshot.