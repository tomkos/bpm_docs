<!-- image -->

# Viewing the state and status of modules or servers

## About this task

In IBM® Integration
Designer,
you can deploy your modules to one or more servers in the test environment.
The Servers view displays a list of all your servers and projects
that are associated with that server. A project displays under a server
when a project from the workbench is added to the server. You can
use the Servers view to determine the current status and state of
the server; and the projects and modules added to the server, including
process applications or toolkits that contain the modules.

## Procedure

1. In the Business Integration perspective, click the Servers tab
to open the Servers view.
2 The Servers view shows each IBM WorkflowServer or Workflow Center Serverthat is connected to your workspace. The Servers view also displaysthe current state of all connected servers. Informationabout the state and status of the server is displayed next to theserver name.
    - Server stateThe following table lists the possible
states of the server:
Table 1. Description of the server states

Server state
Description

Starting
A connection to the server is being established,
or the actual server is starting.

Started
The server is started. Both the workspace and
the server are ready to run applications on the server.

Stopping
The server is stopping. The workspace is in
the process of connecting to the server and is ending the process
on the server.

Stopped
The server is in a stopped state, or a connection
cannot be established between your workspace and the server.
    - Server statusThe following table lists the possible
server status:
Table 2. Description of the server status

Server status
Description

Synchronized
All the modules in the workspace have been published
to the server. The server and the applications are in sync.

Publishing
Changes to the modules in the workspace are
being published to the server. Files related to the modules are in
the correct location for the server to find and use them.

Republish
At least one module in the workspace has changed.
The module needs to be published to the server.
3 The Servers view also displays the state and status ofmodules. The modules are shown in a hierarchical tree view. If themodules are part of a process application or toolkit, the modulesare displayed under the name of the process application or toolkit. Information about the state and status of a module is displayednext to the module name.

- Module stateThe following table lists the possible
states of a module:
Table 3. Description of the module states

Module state
Description

Started
The module is started on the server, and is
ready to run.

Stopped
The module is stopped on the server, and cannot
run.
- Module statusThe following table lists the possible
module status:
Table 4. Description of the module status

Module status
Description

Synchronized
The module has been published to the server.
There are no pending changes to the module.

Republish
The module has changes which need to be published
to the server. The server needs to be updated.
4 The Servers view also displays the status and version ofa process application or toolkit that contains modules in your workspace. Information about status and version is displayed next to theprocess application or toolkit name.

- Process application or toolkit state
Table 5. Description
of the process application or toolkit states

Module state
Description

Started
All modules in the process application or toolkit
have started.

Stopped
Some or all of the modules in the process application
or toolkit are stopped on the server, and cannot run.
- Process application or toolkit statusThe following
table lists the possible status:
Table 6. Description of the process
application or toolkit status

Module status
Description

Synchronized
All modules contained in the process application
or toolkit have been published to the server. There are no pending
changes.

Republish
At least one module contained in the process
application or toolkit has changes which need to be published to the
server. The server needs to be updated.