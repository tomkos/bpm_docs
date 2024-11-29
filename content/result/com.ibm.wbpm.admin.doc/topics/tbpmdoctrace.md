# Managing tracing for the BPM document store

## Before you begin

The maintainDocumentStoreTrace command
is run using the AdminTask object of the wsadmin scripting client.
To run the command, the following conditions must be met:

- The command must be run on the deployment manager node.
- One or more application cluster members must be running.
- Run the command in connected mode. Do not specify the wsadmin
-conntype none option.
- You must connect to the deployment manager with a user ID that
has WebSphere Application Server operator privileges.

## About this task

Start the wsadmin scripting client from the
profile\_root/bin directory of the deployment manager
profile. The maintainDocumentStoreTrace command does not write to a log file, but
the wsadmin scripting client always writes a
profile\_root/logs/wsadmin.traceout log file where you will
find exception stack traces and other information.

For detailed information about the maintainDocumentStoreTrace command,
see the "maintainDocumentStoreTrace command" topic.