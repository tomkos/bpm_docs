<!-- image -->

# Unit testing

Use the integration test client to test any of the following items:

- An individual module
- A set of interacting modules, including modules
that are part of a process application or toolkit
- An individual component
- A set of interacting components
- A set of 6.0.2-format event definition (to ensure that they are
emitting common base events correctly)

The integration test client is fully integrated into the workbench
so that you can navigate through the Business Integration view and
other views while you are using the test client. It is also closely
integrated with the assembly editor. You can open the test client
from the assembly editor and you can open the assembly editor from
the test client. Although the assembly editor is considered the primary
launch point for the integration test client, you can also open the
test client from the Business Integration view. Regardless of whether
you open the integration test client from the assembly editor or the
Business Integration view, you can open multiple instances of the
test client and use them to perform simultaneous testing.

When you begin a test by invoking an operation or emitting a 6.0.2-format
common base event, the integration test client automatically detects
the deployment state of the modules to be tested. If any of the modules
have not yet been deployed, the Deployment Location wizard is automatically
opened so that you can select the servers where you want to deploy
the modules. If the servers are not already running, they are started
automatically.

- Test configurations
- Emulators
- Human task emulators
- Monitors
- Events

These concepts are discussed in the following sections.

## Test configurations

Test
configurations are used to control your tests. A test configuration
specifies one or more modules to test, each of which may include zero
or more emulators for components or references in the module and zero
or more monitors for the wires in the module. Modules that are contained
in a test configuration are called test configuration modules.

When
you open the integration test client, a default test configuration
is automatically created that you can immediately use for testing.
The default test configuration is often all that you need for testing
your modules and components. However, you can choose to edit and customize
the default test configuration or you can create and edit one or more
new test configurations.

## Emulators

In the integration
test client, you can use emulators to emulate components and references
in your modules. During a test, when control flows to an emulated
component or reference, the integration test client intercepts the
invocation and routes it to the associated emulator. There are two
types of emulators:

- Manual
- Programmatic

A manual emulator is an emulator for which you must specify
response values for an emulated component or reference at run time.
If you are testing an entire module, the default test configuration
contains manual emulators for all unimplemented components and unwired
references. However, if you are testing only a set of components or
an individual component within a module, the default test configuration
contains manual emulators for any other components that were not selected
for testing regardless of whether they are implemented or not. Although
manual emulators are added by default, you can remove the manual emulators
or redefine them as programmatic emulators.

When a manual emulator
is encountered during a test, a manual Emulate event is generated
and the test pauses to enable you to manually specify some output
parameter values or throw an exception for the emulated components
or references. By comparison, when a programmatic emulator is encountered
during a test, a programmatic Emulate event is generated and the output
parameter values or exception are automatically provided by a Java™ program contained in a visual
snippet or Java snippet.

## Human task emulators

In
the integration test client, you can use human task emulators to emulate
inline or stand-alone human tasks in your modules. During a test,
when control flows to an emulated human task, the integration test
client automatically claims the human task and routes it to the associated
emulator. There are two types of human task emulators:

- Manual
- Programmatic

A manual human task emulator is an emulator for which you
must specify response values for an emulated human task at run time.

When
a manual emulator is encountered during a test, a manual Claim event
is generated and the test pauses to enable you to manually specify
some output parameter values or throw an exception for the emulated
human task. By comparison, when a programmatic human task emulator
is encountered during a test, a programmatic Claim event is generated
and the output parameter values or exception are automatically provided
by a Java program contained
in a visual snippet or Java snippet.

## Monitors

When the integration
test client generates a default test configuration or you add a new
test configuration, monitors are automatically added for any component
wires and exports that are found in the modules of the test configuration.
When you invoke an operation and run a test, these monitors listen
for any requests and responses that flow over the wires and exports.
If a request is detected, a Request event is generated. And if a response
is detected, a Response event is generated. These events show parameter
data that flows across the wires and they are added to the test trace
of events that are displayed in the Events area of the integration
test client.

Although monitors are automatically added for
the wires and components of your test configuration modules, you can
edit the monitors and change whether they monitor requests, responses,
or both. You can also remove the monitors or add additional monitors
as required.

## Events

When you run a test by
invoking an operation or emitting a common base event in the integration
test client, several different types of events are generated over
the course of the test. These events are either interactive or informational.
Interactive events require you to manually specify values before the
test can continue. By comparison, informational events are purely
informative and they do not require you to perform any action.

By
default, certain types of events are always generated by the integration
test client, such as Return events. However, you can customize test
configurations to control whether other types of events are generated,
such as monitor Request and Response events.

| Event type                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Invoke event (manual)        | An interactive event that is generated when you start the integration test client or when you click the Invoke icon in the integration test client. During this event, you can select a test configuration, module, interface, and operation. You can also specify input parameter values to pass to the operation and invoke the operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Invoke started event         | An informational event that indicates that a test has started.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Invoke event                 | An informational event that confirms when an operation has been successfully invoked on the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Request event                | An informational event that indicates that a request has passed across a monitored wire. The event contains return values or exceptions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Response event               | An informational event that indicates that a response has passed across a monitored wire. The event contains return values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Response event (exception)   | An informational event that indicates that a response has passed across a monitored wire. The event contains an exception. If the exception contains user-specified Web Services Description Language (WSDL) fault data that does not include a string type object, the test client displays both the fault data and the module, component, interface, and operation that contributed to the exception. However, if the fault data includes a string type object, the test client displays the associated exception class, exception message, and trace. Similarly, if the exception is a Java exception or it contains a Java exception, the test client displays the exception class, exception message, and trace.                                                                              |
| Emulate event (manual)       | An interactive event that indicates that a component or reference was encountered that is being emulated by a manual emulator. When a manual emulator is encountered during a test, the invocation of the operation pauses so that you can specify some output parameter values or select an exception to throw. The list of exceptions is populated based on either the throws clause of the J-type interface or the faults section of the W-type interface.                                                                                                                                                                                                                                                                                                                                      |
| Emulate event (programmatic) | An informational event that indicates that a component or reference was encountered that is being emulated with a programmatic emulator. Programmatic emulators use scripts to automatically pass output parameter values or throw exceptions, which means that you do not need to specify values or throw exceptions yourself.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Return event                 | An informational event that indicates that a response has been received from the invocation of an operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Exception event              | An informational event that indicates that an exception has occurred. The exception can be an unmonitored exception that occurred during the invocation of an operation or it can be an exception that you deliberately selected and threw. If the exception contains user-specified WSDL fault data that does not include a string type object, the test client displays both the fault data and the module, component, interface, and operation that contributed to the exception. However, if the fault data includes a string type object, the test client displays the associated exception class, exception message, and trace. Similarly, if the exception is a Java exception or it contains a Java exception, the test client displays the exception class, exception message, and trace. |
| Invoke returned event        | An informational event that indicates that an operation has automatically completed or has been manually stopped. An Invoke returned event does not necessarily mean that all activities are complete as the result of an invocation. It simply means that the original invocation was returned. Events could still be displayed within the Invoke started or Invoke returned events if the original invocation was one way or some resultant invocations were asynchronous.                                                                                                                                                                                                                                                                                                                       |
| Attach event                 | An interactive event that is generated by right-clicking a module in the Business Integration view and selecting Test > Attach or by selecting Attach in the integration test client. During this event, you can attach the integration test client directly to a test configuration module and then use a JMS message, web service, JSP, or some other mechanism to invoke an operation rather than using the invocation mechanism provided by the test client.                                                                                                                                                                                                                                                                                                                                   |
| Emit event                   | An interactive event that is generated when you start the integration test client using the Test > Test Event Definition menu item or when you select Emit in the integration test client. During this event, you can select an event definition for testing. It also enables you to specify values for the event definition and then emit a 6.0.2-format common base event that is defined by the event definition.                                                                                                                                                                                                                                                                                                                                                                               |
| Emitted event                | An informational event that indicates when a 6.0.2-format common base event has been emitted for a selected event definition.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Succeeded event              | An informational event that indicates that an emitted 6.0.2-format common base event was correctly emitted for the selected event definition.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Binding event                | An informational event that indicates when an export has been invoked through a supported binding type in the integration test client. The test client supports web services and SCA binding types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Claim event (manual)         | An interactive event that indicates that a human task was encountered that is being emulated by a manual emulator. When a manual emulator is encountered during a test, the invocation of the operation pauses so that you can specify some output parameter values or select an exception to throw. The manual Claim event is similar to the manual Emulate event.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Claim event (programmatic)   | An informational event that indicates that a human task was encountered that is being emulated with a programmatic emulator. The programmatic Claim event is similar to the programmatic Emulate event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Fine-Grained Trace           | An informational event that indicates that fine-grained trace was used in the testing of a supported component.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

- Integration test client

In IBM Integration Designer, the integration test client is the designated tool for testing modules and components. In the test client, you can manage and precisely control your tests.
- Setting preferences for the integration test client

By default, the user-definable preferences for the integration test client are already optimized for testing modules. However, in the course of your testing activities, you may find that you want to change some preferences.
- Getting started with the integration test client

The integration test client is the designated IBM Integration Designer tool for testing modules and components. When you open the integration test client, a default test configuration is automatically generated. This default test configuration is often all you need to perform your test activities.
- Running unit tests in the test client

In the integration test client, you can rapidly test your modules and components using the default test configuration. This enables you to run a wide variety of tests without adding and editing a new test configuration.
- Running tests with fine-grained trace

When you are testing business processes, state machines, or mediation flows in the integration test client, you can choose to run your tests either with or without fine-grained trace. If you run your tests with fine-grained trace, the Events area of the test client is populated with additional events that correspond to the elements encountered in the execution path of the component being tested. If the associated component editor is open, the execution path is traced and highlighted in the component editor to enable you to easily see the specific path that was run and tested.
- Running component tests in the test client

In the integration test client, you can initiate and run a component test that enables you to sequentially test multiple operations as a group in the integration test client.
- Managing test configurations

In the integration test client, test configurations are used to customize and control your tests. You can edit and customize any existing test configuration or you can add and customize new test configurations for specific tests.
- Logging out of server security login sessions in the integration test client

If security is enabled for your integration test client server and you have logged in using a user ID, you can choose to manually log out at any time.
- Limitations for the integration test client

From time to time, you may encounter some limitations in using the integration test client. In most situations, you can successfully work around these limitations.