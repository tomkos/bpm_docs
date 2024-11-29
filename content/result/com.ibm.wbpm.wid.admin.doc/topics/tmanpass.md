<!-- image -->

# Running unit tests in the test client

## About this task

The following topics provide detailed information about
all of the tasks involved in running a unit test of your modules and
components.

- Testing interface operations

The most common use for the integration test client is to test interface operations in components. The test client provides a wide variety of tools that enable you to rapidly select the operation that you want to test and then invoke it for testing.
- Testing exports

If an export has a binding type that is supported by the integration test client, you can invoke and test the export directly through its binding and the value editor will be populated with values that are based on the binding type. Currently, the test client supports web services binding types and SCA binding types. If you have an export that does not have a supported binding type or does not have any binding at all, you can still use the test client to test the export. However, the test client will invoke the component that is wired to the export rather than invoking the export directly through a binding.
- Testing web service exports with SOAP messages

In the integration test client, you can interactively send sample SOAP messages with or without attachments to a web services export and view the SOAP response.
- Testing a web service gateway

A web service gateway uses a generic interface that defines generic one-way and request-response operations, which means that the way you test a service gateway is slightly different than the way you test other modules.
- Testing XML maps

To test completed XML maps without editing them, you can use the integration test client. The maps will not be deployed to a server and do not need to be associated with a mapping primitive.
- Testing business graphs

If an interface operation has a business graph as its parameter, you can use the integration test client to test the business graph in much the same way that you can test other operation parameters. You can select specific business graph properties to manage as attributes in the value editor, which enables you to pass or return values for the business graph attributes. This test capability is especially useful for testing business graph implementations that are used by IBM adapters that connect to EIS systems.
- Testing event definitions

In addition to testing interface operations in the integration test client, you can also test event definitions. Event definitions are files that enable you to define additional content like business metrics in emitted events. In the test client, you can specify values for an event definition and then use the event definition to emit a common base event, which enables you to ensure that the event definition is defining the emitted event correctly. Note, however, that you can only test event definitions that are based on 6.0.2-format events.
- Creating component test cases from unit tests

When you have finished running a unit test, you can create a component test case that populates its input and expected output values from those values specified in the unit test. Test cases can be created at the operation level or the scenario level, and you have the option of defining the individual steps for the test case (including steps for creating emulators and event verifications).
- Managing test traces

When you test your modules and components in the integration test client, a chain of events occurs and these events are recorded in a test trace. You can save your test trace at any time and later reload it into the integration test client so that you can repeat the same chain of events in another test.
- Managing test configuration module attachments

If you want to use the integration test client for testing but you would rather use your own mechanism to invoke operations, you can attach the integration test client directly to one or more test configuration modules. You can also detach the integration test client from a test configuration module or synchronize an Attach event with an updated test configuration.