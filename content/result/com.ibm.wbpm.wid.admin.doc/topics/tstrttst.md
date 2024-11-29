<!-- image -->

# Opening the integration test client

## Procedure

1 If you want to test an entire module, choose one of the following options: The integration test client opens. Any unimplemented components or unwired references inthe module will be emulated.
    - In the Business Integration view, right-click your module and select Test >  Test Modules on a Local Server.
    - In the Business Integration view, expand your module and then right-click the assembly
diagram and select Test  > Test Modules on a Local Server.
    - Open your module in the assembly editor (and ensure that you press Ctrl-S to save any
changes that you made), then right-click an empty portion of the assembly editor canvas and select Test  > Test Modules on a Local Server.
    - To test a module on a Workflow Center
Server, right-click the module, then select Test > Test Modules. When you select this option, the test configuration contains the process application
or toolkit, and the test is performed on the target Workflow Center Server. All the modules that are part of the
process application or toolkit will be tested.
2. If you want to test a process application
or a toolkit, including all modules that are part of the process application
or toolkit, right-click the process application or toolkit name in
the Business Integration view and select Test > Test Process Application or Test > Test Toolkit.
3 If you want to test a set of components or an individual component rather than an entiremodule, open your module in the assembly editor (and ensure that you press Ctrl-S to save anychanges that you make), then choose one of the following options: The integration test client opens. You may experience a failure to connect to theserver. This connection failure occurs when you have the integration test client runtime on your owncomputer or you have created a proxy server. The following two steps show you how to correct theconnection problem if the integration test client runtime is on your own computer, then for a proxyserver.

- If you want to test a subset of components in your module and have any unselected components
emulated, click one of the components in the set of components that you want to test and use the
Ctrl key to select the remaining components in the set. Then right-click one of the selected
components and select Test Components in Isolation. Any components that you
did not select in the module will automatically be emulated regardless of whether they are
implemented or not.
- If you want to test a single component in your module and have other components emulated,
right-click the component and select Test Component in Isolation. Other
components will automatically be emulated regardless of whether they are implemented or
not.
- If you want to test a single component in your module and not have other implemented
components emulated, right-click the component and select Test
Component.

The integration test client opens.

4 To correct the connection problem if the integration test client runtime is on your owncomputer, go through the following steps:

1. Navigate to <IID\_install\_dir>\SPDShared\plugins and locate the
com.ibm.wbit.comptest.core\_8.5.*.jar file. 

Note: you can find the Integration Designer shared plug-ins location by opening IBM Installation
Manager, selecting File  > View Installed Packages, selecting IBM Integration Designer, and then checking the value next to
Shared Resources Directory.
2. From that JAR file, extract the TestController70.ear file and save it to
a temporary location.
3. Log in to the administrative console and navigate to WebSphere enterprise
applications. Locate TestController70, and uninstall it. If the file is not there,
proceed to the next step.
4. Install the TestController70.ear file that you saved in a previous step.
You can install using all the default values. If you are not using a single node environment, it may
help to synchronize nodes after installing to ensure the application is propagated to all nodes.
Start TestController70 and wait for the application to show as started.
5 To correct the connection problem if you have created a proxy server, go through the followingsteps:

1. If you do not have the TestController70.ear file installed, install it as
described in the previous step. If you have the TestController70.ear file
installed, stop it first by using the administrative console.
2. Navigate to Websphere enterprise applications > TestController70. Under the configuration of TestController70, click Web Module Properties > Virtual hosts.
3. Select the proxy host, for example, De1.proxy\_host. Click
OK and click Save.
4. Restart the TestController70 application.
5. Return to the workspace and run the integration test client component again.

## Example

## What to do next