<!-- image -->

# Troubleshooting Business Process Choreographer Explorer or
Business Process Archive Explorer

## About this task

Use the following information to solve problems relating
to accessing or using Business Process Choreographer Explorer or Business
Process Archive Explorer.

- Use the administrative console to make sure that the web client
application BPCExplorer\_scope or BPCArchiveExplorer\_scopeis
deployed and running on the server.
- In the administrative console, on the page for the application, under View Deployment
Descriptor, verify that the context root is the one you used when setting up the
Business Process Choreographer Explorer or Business Process Archive Explorer.
- Make sure that your virtual host configuration is correct. By
default, the web modules of the Business Process Choreographer applications
are configured for the default\_host virtual host.
 Make sure that the host names and ports that you use to access the
Business Process Choreographer Explorer or Business Process Archive
Explorer are associated with the host alias.

This starts
a search for the error code on the IBM® technical
support site. This site only provides information in English. Copy
the error message code that is shown on the Business Process Choreographer
Explorer or Business Process Archive Explorer Error page to the clipboard.
The error code has the format CWWBcnnnnc, where each c is
a character and nnnn is a 4-digit number. Go to the technical
support page.
Paste the error code into the Additional search terms field,
and click Go.

- Use the administrative console to ensure that WebSphere administrative
security is enabled.
- Check that you are logged onto Business Process Choreographer
Explorer or Business Process Archive Explorer using the correct identity.
Depending on the authorization granted to your user ID, the administrative
views and options are might be not visible or not enabled.
- Use IBM Integration
Designer to
check or modify the authorization settings defined in the BPEL process.

This error can indicate that the process container or human task container has been
stopped, and the client could not connect to the server. Verify that the process container and the
human task container are running and accessible. The nested exception might contain further details
about the problem.

This error is thrown if users attempt to log in while the
process container or Business Process Archive Manager is not running. Verify that the application
BPEContainer\_InstallScope or
BPArchiveMgr\_InstallScope is running, where
InstallScope is either the cluster\_name or
nodename\_servername.