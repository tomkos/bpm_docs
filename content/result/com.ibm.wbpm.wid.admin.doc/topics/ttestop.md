<!-- image -->

# Testing interface operations

## About this task

- Opening the integration test client.
- Selecting an operation to test.
- Specifying values for the operation.
- Invoking the operation.
- Deploying the module.
- Specifying values for any manual emulation.
- Reinvoking the operation to perform additional tests.
- Creating an Invoke event to test a different operation.
- Saving the test trace.

The following topics provide detailed information about
testing interface operations.

- Opening the integration test client

Depending on whether you want to test an entire module, a set of components, or a single component, you can open the integration test client from either the Business Integration view or the assembly editor.
- Selecting operations for testing

To perform any testing in the integration test client, you need to ensure that the correct operation is selected that you want to test. Although an operation is always selected by default when you open the integration test client, the exact operation that is selected is dependent on whether you are testing a module, a set of components, or an individual component.
- Specifying operation values

In the integration test client, you should specify some initial request parameter values for your selected operation before you invoke it.
- Referencing environment variables in the test client

In the test client, you can reference environment variables in the value editor.
- Defining environment variable values in the test client

In the integration test client, you can define values for proprietary environment variables that you have referenced in either the test client or the test suite editor.
- Defining environment variable values in the administrative console

Although you can define proprietary environment variables in the test client, Component Test Explorer, or by using command-line invocation, you can only define WebSphere Application Server environment variables and JVM property environment variables in the IBM Process Server administrative console.
- Using data pools

In the integration test client, you can use one or more data pools. You can save values to the data pools, edit values in the data pool editor, and reuse values from the data pools. This enables you to more easily manage the input values for your operations and output values for your manual emulations.
- Invoking operations

In the integration test client, you initiate a test by invoking an operation.
- Deploying modules from the integration test client

When you start an operation, the integration test client detects whether your module must be deployed to the server. If the module is not deployed, the integration test client automatically opens the Deployment Location wizard to enable you to easily deploy the module and start the server (if it is not already started).
- Changing deployment properties

If you earlier chose a default deployment location for a module, you can change one or more of its properties or select another default deployment location. You can also choose to have no default deployment location, which means that whenever you open the integration test client and invoke an operation for the same module in the same test configuration, the Deployment Location wizard will open.
- Specifying emulation values in the integration test client

If a manual emulator is encountered during a test, the test pauses at an Emulate event and you need to either specify some output parameter values or select an exception to throw. Specifying output parameter values for an emulation is accomplished in exactly the same way as specifying initial request parameter values for an operation, as described in the topic "Specifying operation values". However, throwing exceptions is unique to manual emulations.
- Specifying human task emulation values in the integration test client

If a human task emulator is encountered during a test, the test pauses at a Claim event and you need to either specify some output parameter values or select an exception to throw. Specifying output parameter values for a human task emulation is accomplished in exactly the same way as specifying initial request parameter values for an operation, as described in the topic "Specifying operation values".
- Reinvoking operations

In the integration test client, you can reinvoke an operation and repeat a test that you ran earlier using the same set of invocation values. However, if your earlier test resulted in a manual Emulate event, you can choose to use the same set of manual emulation values or you can specify a different set of values.
- Generating Invoke events in the integration test client

If you want to invoke and test an operation in the integration test client, an Invoke event must first be generated. An Invoke event is automatically generated whenever you open the integration test client to perform an initial test. However, you can manually generate an Invoke event at any time to perform subsequent tests.
- Filtering events

In the Events page of the integration test client, you can choose to filter out the events that you are not interested in viewing. Any events that you filter out in your current instance of the test client will not be filtered out in any other instances of the test client that you choose to open.
- Stopping server connections in the integration test client

In the integration test client, you can immediately stop a server connection. This detaches the integration test client from the server. All running operations that are waiting on user input from the test client are terminated. All other running applications will continue until they terminate, but no status will reported in the test client.
- Removing events in the integration test client

In the Events page of the integration test client, you can remove one or more selected Invoke or Attach events or you can remove all events. Removing events that are no longer used enables you to more easily manage new events.