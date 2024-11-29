# Obtaining the status of the BPM document store

## Before you begin

- The command must be run on the deployment manager node.
- One or more application cluster members must be running.
- The command must be run in connected mode. Do not specify the wsadmin
-conntype none option.
- You must connect to the deployment manager with a user ID that
has WebSphere Application Server operator privileges.

Start the wsadmin scripting client from the
profile\_root/bin directory of the deployment manager
profile. The getDocumentStoreStatus command does not write to a log file, but the
wsadmin scripting client always writes a
profile\_root/logs/wsadmin.traceout log file where you will
find exception stack traces and other information.

Before
you attempt to obtain the status of the BPM document store, review Limitations in administering the BPM document store.

## About this task

- The availability of the document store.
- The status of document migration to the document store.
- The status of the access control migration, either in progress
or completed, if you are migrating to IBM® Business Process Manager
Advanced.
- The status of the IBM\_BPM\_DocumentStore application and whether
it is up-to-date in comparison to the authentication alias and the
EAR file version.

For detailed information about the getDocumentStoreStatus command,
see the "getDocumentStoreStatus command" topic.

To obtain the
status of the BPM document store,
complete the following steps:

## Procedure

1. Run the getDocumentStoreStatus command.
The command returns a sample of the command syntax that can be used
as well as the status of any document migration, as shown in the following
example: 
AdminTask.getDocumentStoreStatus('[-deName myDeName]')
CWTDS2018I: The IBM BPM document migration has not yet started. '{0}' documents need to be migrated.
2 If you receive a message that indicates a problem, completeone of the following steps:
    - If the message indicates that the document store is not available, ensure that your system
does not have the limitations described in the topic Limitations in administering the BPM
document store. If your system does not have any of the limitations, check the log
files.
    - If the message indicates that there is a problem with the status of the
IBM\_BPM\_Document\_Store application, try updating the application by following the instructions in
the topic Updating the BPM document store application.
    - If the message indicates that there is a problem with migration, see the instructions in the
topic Migrating document attachments to the BPM document store.