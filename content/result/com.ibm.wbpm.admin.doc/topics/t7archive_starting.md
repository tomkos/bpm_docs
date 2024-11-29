<!-- image -->

# Starting Business Process Archive Explorer

## Before you begin

- BPArchiveMgr\_scope
- TaskArchiveMgr\_scope
- BPCArchiveExplorer\_scope

## About this task

To start Business Process Archive Explorer, complete the
following steps.

## Procedure

1. Direct your web browser to the Business Process Archive
Explorer URL. The value of the URL depends on how the
virtual host and context root were configured for your installation.
The URL takes the following form.https://application\_server\_host:port\_number/context\_rootImportant: Any attempts to access the Business
Process Archive Explorer using the HTTP protocol are redirected to
use HTTPS.

In addition, you can extend
the URL to go directly to the details of a process or task.https://application\_server\_host:port\_number/context\_root?oid\_type=oid
Where:
application\_server\_host
The network name for the host of the Business Process Archive
Explorer instance with which you want to work.
port\_number
The port number used by Business Process Archive Explorer. The
port number depends on your system configuration. The default port
number is 9443.
context\_root
The root directory for the Business Process Archive Explorer application
on the application server. The default is bpcarchive.
oid\_type
Optional. The type of object that you want to display. This parameter
can take one of the following values:
aiid
Activity instance ID
piid
Process instance ID
ptid
Process template ID
tkiid
Task instance ID
tktid
Task template ID

oid
Optional. The value of the object ID.
2. If security is enabled, you must enter a user ID and password,
then click Login.

## Results

<!-- image -->