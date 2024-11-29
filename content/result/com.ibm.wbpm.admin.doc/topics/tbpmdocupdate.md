# Updating the BPM document store application

## Before you begin

The updateDocumentStoreApplication command
is run using the AdminTask object of the wsadmin scripting client.
To run the command, the following conditions must be met:

- The command must be run on the deployment manager node.
- Run the command in either local or connected mode.
- When running the command in connected mode, you must specify a
user ID that has WebSphere Application Server operator and deployer
privileges.

## About this task

Start the wsadmin scripting client from the deployment\_manager\_profile/bin directory
on either Workflow Server or Workflow Center. The updateDocumentStoreApplication command
does not write to a log file, but the wsadmin scripting client always
writes a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

For detailed information about the updateDocumentStoreApplication command
syntax, see the "updateDocumentStoreApplication command" topic.