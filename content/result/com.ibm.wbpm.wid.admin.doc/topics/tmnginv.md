<!-- image -->

# Managing invocations

## About this task

- Adding invocations

In the test suite editor, you can add an invocation to a test case at any time.
- Selecting operations for testing

To perform any component testing in the integration test client, you need to ensure that the correct operation is selected that you want to test. Selecting an operation for testing in the test suite editor is similar to selecting an operation for testing in the integration test client.
- Defining invocations as asynchronous

By default, invocations are assumed to be synchronous. However, you can choose to define an invocation as asynchronous.
- Ignoring exception errors for an invocation

By default, exception errors in the invocation cause the test case to fail. However, you can choose to ignore exception errors for a specific invocation so that the test passes.
- Specifying request, response, and exception variables

In the Test Cases page of the test suite editor, you can specify a request, response, or exception variable for an invocation selected in the Test Cases area. The value that is used for a request, response, or exception variable is whatever value is specified for the variable in the test data table.
- Refreshing invocations

If the test suite editor is open and you make changes to a referenced operation in your workspace without refactoring the changes, the invocation that references the operation will be flagged with an error symbol in the test suite editor. However, you can refresh the invocation in the test suite editor to pick up your changes to the operation and the error symbol will disappear.
- Removing invocations

You can remove any invocations that are listed in the Test Cases area of the test suite editor. This enables you to more easily manage the remaining invocations.