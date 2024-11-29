<!-- image -->

# Creating and managing test cases

## About this task

Think of a test case as a container for multiple operations
that you have selected for testing. Test cases enable you to automate
and simultaneously test the operations in the integration test client.

Test cases can have Invoke, Return, Exception, Request,
Response, Fine-Grained Trace, and Emulate events. Each event you include
becomes a step in the test case. A basic test case automatically includes
all Invoke, Return, and Exception events.

- An emulator definition step allows you to define a series of rules
to emulate a component, reference, or human task in a test case. You
can use the test data table to specify expected input data and output
response data for the components, references, inline human tasks,
and stand-alone human tasks that you want to emulate.
- A Verify Event step enables you to verify request, response, or
exception data that is passed over a monitor wire between source and
target components. It also enables you to verify fine-grained trace
data that is returned from a test run. Note that Verify Event steps
can only monitor the events that can be displayed in the test client.

- Adding test cases from the Business Integration view

If necessary, you can create a new test case and add it to an existing test suite. Alternatively, you can create a new test case and simultaneously create a new test suite to contain it.
- Managing test data

The Test Data Table view enables you to manage your test data in numerous ways. For example, you can add variables and choose from a wide selection of variable values.
- Managing test variations

A test variation is a specific set of variable values for a test case. Although each test case is automatically assigned a default test variation, you can create multiple test variations for a test case that each contain a different set of variable values. When a test case is run, all of the test variations for the test case are run.
- Managing invocations

In the test suite editor, you can create and manage synchronous and asynchronous invocations, which are used to invoke components and operations.
- Managing Wait On steps

A Wait On step is used to wait for an asynchronous operation to complete.
- Managing Wait for Time steps

A Wait for Time step enables a test case to pause for a specified amount of time before continuing execution. This helps synchronize multiple asynchronous calls in a single test case. It also enables you to test more complex scenarios, such as those involving a long-running process that requires multiple interactions.
- Managing Verify Event steps

A Verify Event step enables you to verify request, response, or exception data that is passed over a monitor wire between source and target components. It also enables you to verify fine-grained trace data that is returned from a test run. Note that Verify Event steps can only monitor the events that can be displayed in the test client. There are situations where the SCA run time does not contain enough information for the test client to generate events for some SCA wires. In these cases, a Verify Event steps cannot be used.
- Managing emulator definition steps

In the test suite editor, you have the choice of adding an emulator that applies to all test cases in a test suite or adding emulator definition steps that apply to specific test cases in a test suite. An emulator definition step allows you to define a series of rules to emulate a component, reference, or human task in a test case. You can use the test data table to specify expected input data and output response data for the components, references, inline human tasks, and stand-alone human tasks that you want to emulate. Also, emulator definition steps enable you to automatically claim and complete your human tasks without using BPC Explorer or Business Space.
- Removing test cases

You can remove any test cases that are listed in the Test Cases area of the test suite editor. This enables you to more easily manage the remaining test cases.