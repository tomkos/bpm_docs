<!-- image -->

# Managing Wait On steps

## About this task

- Adding Wait On steps

In the test suite editor, you can add a Wait On step that will wait for an asynchronous invocation to complete.
- Selecting asynchronous invocations for Wait On steps

You can select any asynchronous invocation that you want an existing Wait On step to wait on.
- Specifying timeout values for Wait On steps

When you specify a timeout value for a Wait On step, the Wait On step will wait for an asynchronous invocation to complete up to and including the amount of time specified in the timeout value. If the asynchronous invocation completes within the specified amount of time, the Wait On step will assign any response or exception variables specified for the asynchronous invocation. If the asynchronous invocation does not complete within the specified amount of time, an exception will be thrown and the test case will fail.
- Removing Wait On steps

You can remove any Wait On steps that are listed in the Test Cases area of the test suite editor. This enables you to more easily manage the remaining Wait On steps.