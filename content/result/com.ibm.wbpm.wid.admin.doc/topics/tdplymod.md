<!-- image -->

# Deploying modules from the integration test client

## Before you begin

## About this task

In the Deployment Location wizard, IBM® Workflow
Server always
appears as a selectable deployment location. If your module contains
only Java components or it contains Java 2 Platform Enterprise Edition
components that are all unimplemented, Eclipse JVM will
appear as a selectable deployment location. If
you are testing a module that is deployed as part of a process application
or a toolkit, IBM Workflow
Center Server appears
as a selectable deployment location.

To deploy your module:

## Procedure

1 If you have selected more than one module for testing oryou have more than one module in your test configuration, the SelectDeployment Location for Each Module page of the Deployment Locationwizard opens and you should complete one of the following steps:
    - If you want to use the default deployment location specified
for each module listed in the wizard, click Finish to
immediately deploy the modules. (If administrative security is enabled
for one or more of the servers, you will first need to specify a user
ID and password as described in the final step of this topic.)
    - If you want to change the default deployment location specified
for one or more modules, select the check box beside each module for
which you want to specify a different deployment location and then
click Select Location. The Select Deployment
Location page of the Deployment wizard opens and you can work with
it by completing the following steps.
2 In the Select Deployment Location page of the DeploymentLocation wizard, choose one of the following options:

- If your module contains at least one component that is not
a Java™ component or if you want to test a set
of interacting modules, ensure that IBM Workflow
Server is
selected in the Deployment location list box.
(This is the designated server for running SCA applications, BPEL
business processes, human tasks, transition tables, business rules,
selectors, and other resources. You can also use this server for running
mediation flows contained in mediation modules.)
- If your module is deployed as part of a process
application or a toolkit, ensure that IBM Workflow
Center Server is
selected as the deployment location. If there are multiple modules
in the process application or toolkit, all the modules will be tested.
- If your module is a mediation module, ensure that IBM Workflow
Server is
selected as the deployment location. )
- If your module only contains Java components
and you do not want to test a set of interacting modules, or if your
module contains Java 2 Platform Enterprise Edition resources but none
of the components are implemented, you can select Eclipse
JVM. (The main advantage to choosing the Eclipse JVM is
that it starts more quickly than IBM Workflow
Server.
However, once started, both runtimes provide similar test performance.)
3. In the Mode drop-down list, select
either Run or Debug to
start the server in Run or Debug mode. (If the server is already running
in one of these modes, the Mode drop-down list
will show the current server mode and it will be disabled.)
4. If you want to use the selected server or JVM as your default
deployment location for future testing, select the Use
this as the default and do not ask again check box. The
next time that you open the test client to start an operation for
the same module in the same test configuration, your module will automatically
be deployed to the default deployment location without the Deployment
Location wizard opening. (If you later want to select a different
deployment location for the same module in the same test configuration,
follow the instructions in the topic Changing deployment properties).
5 Click Finish . If you selected aserver as your deployment location and administrative security isenabled for that server, a User Login window is displayed (if youare not already logged in) and you must log in by completing the followingsteps: Note that each login session is associated with a single testconfiguration that is identified in the title bar of the User Loginwindow. The login session endures until you manually log out by clickingthe Logout button on the Configurations pageof the test client or until you are automatically logged out whenyou stop or close the test client.Note: If an exception is receivedthat states that the server must be running in development mode, youcan enable development mode for the server by following the instructionsin the topic Enabling development mode for stand-alone test environment servers .

1. In the User ID field, type an
administrative security user ID.
2. In the Password field, type the
password for the user ID.
3. Click OK. The module is deployed
to your selected deployment location and the invocation of your operation
continues.

## What to do next