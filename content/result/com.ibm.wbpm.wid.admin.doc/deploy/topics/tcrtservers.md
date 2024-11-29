<!-- image -->

# Working with process application servers

## About this task

By default, a process application server is installed, configured, and run in a Network
Deployment (ND) environment.

There
are two types of process application servers that you can create in Integration Designer to
work with process applications and toolkits:

- Workflow Center server
(also known as a playback server)
- IBM Workflow
Server on Workflow Center (also
known as an online server)

When you have finished developing and testing a process application or toolkit on Workflow Center, you need to install a snapshot of the
process application on an external workflow server that resides outside the authoring environment of
the Workflow Center. This external workflow
server is called a Workflow Server on Workflow Center, which is required for the integration
test client to be able test the modules in the process application or toolkit. The server can be a
development server, test server, staging server, or production server environment.

If you already have a Workflow Center server
in the Servers view of Integration Designer, you can
connect to a workflow server to quickly and easily create an IBM Workflow
Server on Workflow Center in the Servers view.

Information
about creating or connecting to process application servers is found
in the following topics:

- Creating an IBM Workflow Center server

An IBM Workflow Center server (also known as a playback server) can be used to test integration modules that are contained in a process application or toolkit on Workflow Center. The server can also be used to display the current status of the process application or toolkit on Workflow Center, such as whether the process application or toolkit is deployed and started. When you import a process application or toolkit into IBM Integration Designer from the Workflow Center, a Workflow Center server is created automatically in the Servers view.
- Creating an IBM Workflow Server on IBM Workflow Center

An IBM Workflow Server on IBM Workflow Center (also known as an online server) is required for the integration test client to be able to test integration modules in a process application or toolkit that has been deployed to a connected Workflow Server. The server is also required to display the status of the process application or toolkit on the Workflow Server, such as whether the process application or toolkit is deployed and started. The server can be a development server, test server, staging server, or production server.
- Connecting to an IBM Workflow Server on IBM Workflow Center

If you have an IBM Workflow Center server in the Servers view of IBM Integration Designer, you can connect to a process server to quickly and easily create an IBM Workflow Server on Workflow Center (also known as an online server) in the Servers view. A Workflow Server on Workflow Center is required for the integration test client to test integration modules in a process application or toolkit that has been deployed to a connected Workflow Server. The server is also required to display the status of the process application or toolkit on the Workflow Server, such as whether the process application or toolkit is deployed and started. The server can be a development server, test server, staging server, or production server.