<!-- image -->

# Deploy the modules to the server

## About this task

To deploy the module to the server:

## Procedure

1. If the Business Integration perspective is not open, select Window
> Open Perspective > Business Integration to open it.
This is where you perform most of your development tasks in IBM® Integration
Designer.
2. Click the Servers tab. The Servers view opens, as
shown in the following figure:
3. In the Servers view, right-click IBM Workflow
Server and
select Add and Remove Projects. The Add and Remove Projects
window opens, as shown here:
4. In the Available projects list, select the HelloServiceApp 
application.
5. Click Add. The HelloServiceApp  application
is added to the Configured projects list.
6. Similarly add the HelloWorldMediationApp  application
to the Configured projects list.
7. Click Finish. The HelloServiceApp  application
and the HelloWorldMediationApp application now both appear
under the expanded server in the Servers  view, as shown in
the following figure:
8. If the State column in the Servers view shows
this server is Stopped, right-click the server and click Start.
Wait until the Servers view shows a state of Started. This
may take a few moments.
9. Optional: The Server Logs view shows the
messages emitted by the server. Double-click the Server
Logs tab to give it focus and expand it to full size.
Scroll to the bottom and you will see the logged messages indicating
that the two applications have started, as shown here:
10. Optional: The Build Activities view shows
you the status of your projects, and after the initial association
of a project with a server, it is a good place to do subsequent publishes
after making changes. Click the Build Activities tab and expand Project
status to ensure your projects display a status of Ready to
run, as shown in the following figure:  If you make changes to a module
in your workspace and the same module deployed on the server now displays
a status of Started but requires republishing,
you can click Update Running Servers to publish
the changed module resources to the server. The status of the module
will change to Started and synchronized because
the module resources on the server are now the same as the module
resources in the workspace.

## Results