<!-- image -->

# Working with servers

In IBM® Integration
Designer, you can work with
both unit test environment (UTE) servers and process application servers. A set of server tools is
provided that enables you to accomplish multiple tasks, such as creating servers, deploying
applications, and starting or stopping servers.

Recent versions of IBM Business Automation
Workflow use the SSL
communication protocol TLSv1.2 and later versions. The default protocol for Integration Designer 22.0.2 changed to
TLSv1.2. To set a different TLS protocol, follow the instructions in Connecting Integration Designer to a server by using a protocol other than TLSv1.2.

## About this task

If you have modules that are contained in
a process application or toolkit, you have two deployment options:

- You can deploy the individual modules in the process application
or toolkit to a UTE server for preliminary testing.
- You can deploy the process application or toolkit to a process
application server, which enables you to test all of the modules in
the context of the process application or toolkit that contains them.

You cannot deploy entire process applications or toolkits
to a UTE server. And you cannot deploy modules to a process application
server from the Servers view unless they are contained in a process
application or toolkit.

The following topics explain how to
work with UTE servers and process application servers in Integration Designer:

- Connecting Integration Designer to a server by using a protocol other than TLSv1.2

IBM Business Automation Workflow 22.0.x uses the Transport Layer Security (TLS) SSL communication protocols v1.2 and v1.3. In 22.0.2,  the default protocol for IBM Integration Designer changed to TLSv1.2. To connect to Workflow Center or the unit test environment (UTE) by using a different TLS protocol, you must set options in the <IID install root>\eclipse.ini file.
- Working with UTE servers

In IBM Integration Designer, you can work with unit test environment (UTE) servers. For example, you can create a new UTE server and then deploy your integration modules or mediation modules to the server for testing. The server can only run in a non-ND environment.
- Working with process application servers

In IBM Integration Designer, you can work with process application servers. For example, you can create a new process application server and then deploy your process applications or toolkits to the server. This enables you to test the process application modules or toolkit modules in the context of the process application or toolkit that contains them, and to also see the status of the process application or toolkit in the Servers view. However, before a Workflow Center server can be automatically or manually created, you will need to obtain the relevant administrative connection information from your system administrator, including the administrative user name and password.
- Viewing the state and status of modules or servers

You can view the state of a module that you have added to a test environment server, or the state of a server that is connected to your workspace, using the Servers view.