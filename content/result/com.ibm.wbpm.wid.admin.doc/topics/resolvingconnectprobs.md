# Resolving connection problems in Integration Designer

## About this task

The following topics describe some connection problems
in Integration Designer and explain how to resolve them:

- Resolving communication problems with remote UTE servers

If you are having problems communicating with a UTE remote server, such as problems in publishing to the remote server or obtaining the status of the server, it is possible that the server settings or system settings on the remote machine are not correctly set up.
- Creation of a process application server causes a prompt for credentials

When you create a process application server in IBM Integration Designer, such as a Workflow Center server or a Workflow Server on Workflow Center, you might be queried for administrative user ID and password credentials. This is because the user credentials that you are using to log into the Workflow Center are different that the administrative credentials that are required to log into a process application server. To correct the problem, see your system administrator for the required administrative credentials and specify them when you are prompted.
- Your LDAP account is locked after the password is changed

Your LDAP account is locked because IBM Integration Designer is making repeated attempts to connect to IBM Workflow Center.
- Integration Designer prompts for connection information whenever a process application is imported

When a process application is imported into an Integration Designer workspace, an administrative connection to the Process Center server is created. If the Process Center is running on a network deployment environment, then the administrative connection is created for the IBM BPM deployment manager. If the user name and password for the Process Center is the same as for the administrative connection for the deployment manager, then the Process Center server is automatically created. Otherwise, a dialog box opens and prompts you to specify the user name and password for the deployment manager. The dialog box can open many times, which can be intrusive if you are unable to obtain the user name and password.
- Web browser is blank in Process Center perspective of Integration Designer

When you connect to Process Center in Integration Designer and then open the Process Center perspective, it is possible that the web browser will be blank and simply display a white background. There is a simple fix for this problem.