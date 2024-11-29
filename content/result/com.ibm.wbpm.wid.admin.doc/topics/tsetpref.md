<!-- image -->

# Setting preferences for the integration test client

## About this task

- Disabling warnings about hot code replacement in the integration debugger

Hot code replacement enables you to modify your component without republishing or restarting the server. By default, you receive a warning whenever hot code replacement will not work for a component that you are debugging. For example, hot code replacement does not work for business rule groups. However, you can set an integration debugger preference to disable warnings about hot code replacement.
- Disabling warnings about refactoring in the integration debugger

By default, you receive a refactoring warning whenever your business process breakpoints have been updated as a result of changes you made to your module. The warning cautions you that the updated breakpoints will not take effect until after you have redeployed the module to the server. However, you can set an integration debugger preference to disable these warnings about refactoring.
- Disabling warnings about server synchronization in the integration debugger

By default, you receive a server synchronization warning whenever a component in your workspace is out of synchronization with the version of the component that is running on the server. This most typically occurs when you have made updates to your component in the workspace but you have not yet redeployed the component to the server. As a result, the server is running an older version of the component than is currently found in your workspace. However, you can set an integration debugger preference to disable warnings about server synchronization.
- Disabling warnings about components that cannot currently be debugged in the integration debugger

By default, you receive a warning about any component that cannot be debugged in the integration debugger. For example, business rules may need to be rebuilt before you can debug them. However, you can set an integration debugger preference to disable warnings about components that cannot currently be debugged.
- Enabling prompting when duplicate files are encountered in the integration debugger

When you begin to debug a component that has the same file name as one or more other components in the workbench, you will be prompted to confirm the correct component when the first breakpoint is encountered in the component being debugged. By default, you will only be prompted once and then your selection will be used for all subsequent debugging sessions involving a component of the same file name. However, you can set an integration debugger preference to enable you to be prompted every time you begin to debug a component that has the same file name as one or more other components in the workbench.
- Specifying how invalid breakpoints should be handled in the integration debugger

In business integration components, breakpoints can become invalid over time. For example, breakpoints can become invalid if refactoring occurs and the breakpoints are not updated or removed. However, you can set a preference to specify how you want invalid breakpoints to be handled in the integration debugger during the course of your debugging tasks.
- Enabling all variables to be displayed in the integration debugger

If you have stepped into a Java snippet in the integration debugger, the Variables view displays all of the Java variables in the snippet except for the this variable. However, you can set an integration debugger preference that enables the this variable to be displayed in the Variables view.
- Enabling debug trace logging in the integration debugger

A debug trace log contains problem determination information that is helpful to IBM support personnel. By default, debug trace logging is not enabled when you are working with the integration debugger. However, you can set an integration debugger preference to enable debug trace logging.
- Enabling or disabling the integration debugger

In IBM Integration Designer, the integration debugger is enabled by default. However, you can set a preference that disables or enables the debugger.
- Enabling or disabling debugger tracing on servers

By default, integration debugger tracing is disabled on servers. Although you can set a preference to enable tracing (which will allow debugger trace information to be displayed in server consoles and server logs in the Server Logs view), you should only enable debugger tracing on the advice of IBM Software Support personnel.
- Changing Java breakpoint query timeout values

When a Java breakpoint is encountered while running an application on the server in Debug mode, the integration debugger queries whether a Java snippet is running. If the debugger cannot make the determination before the query times out, the debugger handles the Java breakpoint as though it is not associated with a snippet event. If necessary, you can increase (or reduce) the timeout value for Java breakpoint queries.
- Specifying regular debugging or problem determination debugging

By default, the integration debugger is optimized for regular debugging of application modules and components in IBM Integration Designer. However, if you are experiencing problems with the debugger, you can specify options that enable you to perform problem determination on the debugger under the guidance of IBM support personnel.
- Changing integration debugger thread filters

In IBM Integration Designer, the recommended thread filters are already set by default for use with the integration debugger. However, you can view or change the thread filters if circumstances warrant it.
- Changing integration debugger timeout values

If you are experiencing problems with the integration debugger timing out before you can begin your debugging session, you can change the debugger timeout values to allow the debugger more time to start.
- Enabling modified resources to be saved automatically

If you attempt to start the test client when there are modified files that have not been saved, the test client will not start and you will be prompted to save the files. However, you can select a preference that enables the modified resources to be saved automatically when you start the test client.
- Including other modules for testing that are referenced by integration solutions

When you open the integration test client on a module that is referenced by an integration solution, only the selected module is added to the test configuration for testing. However, you can set a preference so that all other modules referenced by the integration solution are added to the test configuration for testing.
- Specifying automatic publishing before starting the test client

If you invoke the test client from a selected module or project, the default action is for the test client to automatically build, publish, and start the module or project on the server before the integration test client opens. However, you can change the default action if you prefer.
- Disabling prompts to save work when closing test client

By default, you are prompted to save your work whenever you close the integration test client. However, you can set a preference to disable the prompts.
- Specifying the timeout value for the test client

By default, the amount of time that the test client will wait for the server to start before timing out is five minutes. However, you can specify a different timeout value.
- Specifying the default action when publishing to a server

If you are running tests and you manually publish a module to the server, the default action is for a window to open in which you can choose whether to stop or continue. However, you can change the default action if necessary
- Selecting business graph properties to display in the integration test client

In IBM Integration Designer, if you want to test a component that uses a business graph, you can select specific properties to manage as attributes in the value editor of the integration test client. You can then pass or return values for the business graph attributes, which is especially useful if you are working with an enterprise information system (EIS), such as CICS®.
- Specifying the maximum depth of expanded business objects

In the integration test client, nested business objects are automatically expanded to a depth of five levels in the value editor and zero levels in the data pool editor. However, you can change the maximum depth to which you want to automatically expand your nested business objects.
- Specifying the maximum number of previous input values to save

When you close the integration test client, the maximum number of previous input values that are automatically saved from the value editor is five. However, you can set a preference to change the maximum number of previous input values.
- Specifying a default data pool

If you have not specified a default data pool, the most recently used data pool in a test client instance is used as the default data pool in the instance. However, you can specify a default data pool for all instances of the test client.
- Enabling or disabling fine-grained trace

In the integration test client, fine-grained trace is enabled by default for all supported components. However, you can set a preference that controls whether fine-grained trace is enabled or disabled.
- Controlling event path highlighting for fine-grained trace

When fine-grained trace is used for testing in the integration test client, the event path is highlighted in the supported component editors by default. However, you can set preferences that control the specific forms of event highlighting.
- Controlling split-editor mode for fine-grained trace

By default, when you select an event in the test client and fine-grained trace is used for testing, the associated component editor does not open automatically in split-editor mode beside the test client. However, you can set preferences to control split-editor mode and the position of the supported component editors.
- Specifying security settings for server authentication

By default, the administrative security settings are used to authenticate with the server when you are using the integration test client. However, you can set preferences to change the way that you authenticate with the server.
- Customizing keyboard shortcuts

In the integration test client, you can use keyboard shortcuts to perform several actions. If you want, you can customize some of the keyboard shortcuts.