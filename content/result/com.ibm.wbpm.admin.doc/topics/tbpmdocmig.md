# Migrating document attachments to the BPM document store

## Before you begin

Before you attempt to migrate your document attachments
to the BPM document store,
review the following topic to ensure that your system meets the requirements
for document migration: Limitations in administering the BPM document store.

When document attachments are being migrated to the BPM document store, they are temporarily stored twice in the
Process database. For this reason, you should ensure that the database has sufficient storage to
accommodate the twice-stored documents before you start the document migration.

The document store restricts document size to 1 gigabyte or less. If the content of any document
attachment in the Process database exceeds 1 gigabyte, you cannot migrate the document attachment to
the BPM document store. The document attachment will
remain in the database and a reference to the document attachment will be created in the document
store. You can access the content of the document attachment through APIs and Enterprise Content
Management operations as if the document had been completely migrated.

If you
are migrating documents from a pre-8.5.0.0 version to the current
version, use the startDocumentStoreMigration command
for your migration.

The startDocumentStoreMigration and getDocumentStoreStatus commands
are used to perform many of the tasks in this topic. The commands
are run using the AdminTask object of the wsadmin scripting client.
To run the commands, the following conditions must be met:

- The commands must be run on the deployment manager node.
- One or more application cluster members must be running.
- Run the commands in connected mode. Do not specify the wsadmin
-conntype none option.
- You must connect to the deployment manager with a user ID that
has WebSphere Application Server operator privileges.

Start the wsadmin scripting client from the
profile\_root/bin directory of the deployment manager
profile. The commands do not write to a log file, but the wsadmin scripting client always writes a
profile\_root/logs/wsadmin.traceout log file where you will
find exception stack traces and other information.

## About this task

To migrate document attachments to the BPM document store, complete
the following steps:

## Procedure

1. Run the getDocumentStoreStatus command.
This wsadmin command returns the command syntax that can be used as
well as the status of any document migration, as shown in the following
sample: 
AdminTask.getDocumentStoreStatus('[-deName myDeName]')
CWTDS2018I: The IBM BPM document migration has not yet started. '{0}' documents need to be migrated.

To pass more parameters for the command, you can use the following
syntax:install\_root wsadmin -user my\_user\_name -password my\_password -lang jython -c "print AdminTask.getDocumentStoreStatus('[-deName myDeName]')"
For
example:C:\8500PC\STANDARD\deploy2\AppServer\profiles\DmgrProfile\bin>wsadmin -user tw\_admin -password tw\_admin -lang jython -c "print AdminTask.getDocumentStoreStatus('[-deName De1]')"
For detailed information about the getDocumentStoreStatus command, see the
getDocumentStoreStatus command topic.
2. Run the startDocumentStoreMigration command.
This wsadmin command returns the command syntax that can be used,
as shown in the following sample: 
AdminTask.startDocumentStoreMigration('[-deName myDeName]')To specify other parameters for the command, you can use the following
syntax:profile\_root\bin\wsadmin -user my\_user\_name -password my\_password -lang jython -c "print AdminTask.startDocumentStoreMigration('[-deName myDeName]')"
For example:
C:\8500PC\STANDARD\deploy2\AppServer\profiles\DmgrProfile\bin>wsadmin -user tw\_admin -password tw\_admin -lang jython -c "print AdminTask.startDocumentStoreMigration('[-deName De1]')"
For detailed information about the startDocumentStoreMigration command, see the
startDocumentStoreMigration command topic.
3. Run the getDocumentStoreStatus command
again to check the status of the document migration. If the migration
is proceeding successfully or has completed successfully, the command
will return one of the following messages: 
CWTDS2019I: The BPM document migration is running. '{0}' of '{1}' documents are already migrated.

CWTDS2020I: The BPM document migration is running. '{0}' of '{1}' documents are already migrated. A cleanup is currently in progress.

CWTDS2021I: The BPM document migration has finished. '{0}' documents were migrated.

If one or more documents fail to migrate successfully, the
getDocumentStoreStatus command may return one of the following
messages:CWTDS2022I: The BPM document migration has stopped with an error. '{0}' of '{1}' documents are already migrated. For '{2}' documents, the migration failed.

CWTDS2023I: The migration failed for document '{0}'. Details: '{1}'.
4 If a message indicates that one or more of the documentshas failed to migrate successfully, complete one of the followingsteps:
    - If all of the documents failed to migrate successfully, check the migration configuration
and the logs for a general problem, such as a problem with the database connection.
    - If the logs indicate an OutOfMemoryError condition, try increasing
the heap size of the JVM for the period of time in which the migration
will take place. Alternatively, try reducing the maximum number of
documents that can be migrated in parallel to the BPM document store. For
more information, see Modifying configuration parameters.
    - If the logs indicate transaction timeouts, there may be very large documents that failed to
migrate within one transaction. Try raising the transaction timeout temporarily by following the
instructions in the Transaction service settings topic. Alternatively, you can run the
startDocumentStoreMigration command with the
-keepFailedDocuments option as described in the next bullet.
    - If some of the documents failed to migrate successfully, you can choose to retain the
content of these documents in the database and only create references for the documents in the
document store. The legacy document APIs and ECM operations will continue to work with the documents
in the database. To retain the content of the documents in the database and only create references
for the documents in the document store, run the startDocumentStoreMigration
command with the -keepFailedDocuments option, as shown in the following
example:AdminTask.startDocumentStoreMigration('[-deName myDeName -keepFailedDocuments]')

## What to do next