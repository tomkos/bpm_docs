# Working with UTE servers

In IBM® Integration
Designer, you can work with
unit test environment (UTE) servers. For example, you can create a new UTE server and then deploy
your integration modules or mediation modules to the server for testing. The server can only run in
a non-ND environment.

For instructions to upgrade your UTE to V8.6, see Upgrading the IBM
Integration Designer test environment from version 8.5.x to IBM Business Process Manager Process
Server version 8.6. You cannot install a new Business Automation Workflow V8.6 UTE, but you can upgrade an existing
V8.5.x UTE and then reset upgraded UTE profiles or create new UTE profiles, as needed.

## About this task

Information about working with UTE servers is found in
the following topics:

- Creating test environment servers

If you chose to install the  Workflow Server test environment profile when you installed IBM Integration Designer, then you will already have a default unit test environment (UTE) server that was automatically created. However, if you deleted the default server or if you are working with a standalone installation of  Workflow Server, you will need to manually create a test environment server for testing your integration and mediation modules.
- Editing server configurations in the test environment

There may be occasions when you want to edit a server configuration. For example, you may want to open the server administrative console and then edit some properties, such as configuring the behavior of human tasks at run time. Or you may want to open the IBM Integration Designer server configuration editor and then edit some basic settings, such as modifying a port number. Modifying port numbers, for example, avoids creating additional server profiles.
- Enabling development mode for stand-alone test environment servers

When a test environment server is installed as part of the IBM Business Automation Workflow installation, the server is automatically set to run in development mode by default. This is the mode for a test environment server. However, if you install a stand-alone server separately from your IBM Business Automation Workflow installation and you want to use the stand-alone server as a test environment server, you need to manually enable the server to run in development mode.
- Starting servers in the test environment

Before you can create a running instance of a component in IBM Integration Designer, you need to start the server.
- Adding modules to test environment servers

Before you can test your modules on a test environment server, you need to add the modules to the server.
- Publishing modules to test environment servers

In IBM Integration Designer, you will occasionally need to publish modules to a running test environment server. This effectively redeploys the modules and allows the running server to pick up changes that you have made to the components of your modules.
- Publishing changed resources to servers

If changed (new, modified, or deleted) resources exist in your workspace and you click the Update Running Servers button in the Build Activities view, a window will open that enables you to view the resources and choose whether to publish the updates to the servers.
- Removing modules from servers

From time to time, you will want to remove modules from your servers. For example, if you have modules that you no longer need to test, you should consider removing them from the server so that they do not needlessly impact the performance of the server.
- Restarting servers in the test environment

In IBM Integration Designer, you may encounter situations where you need to restart a running test environment server. For example, you will probably need to restart a server if you make changes to the server configuration while the server is running.
- Stopping servers in the test environment

Whenever you finish using a test environment server in IBM Integration Designer, you should stop it. This ensures that the server will not unnecessarily impact the performance of other tools in the workbench or the computer that it is running on.
- Creating or resetting default server profiles

A default  server profile is a test environment server profile that is created when the test environment is installed with IBM Integration Designer. In the Servers view, you can choose to create or reset a default server profile. For example, you might want to create a default server profile that you earlier chose not to have created when you installed the test environment. Or you might need to reset an existing default server profile that is no longer functioning correctly.