<!-- image -->

# Loading invocation records into the integration test client

## Before you begin

## About this task

## Procedure

1. Ensure that the modules and libraries that are associated
with the invocation records are resident in the workbench.
2. Click the Server Logs tab to open
the Server Logs view.
3. In the Server Logs view, click the tab of the server console
or server log that contains the invocation records that you want to
load into the integration test client.
4. Ensure that the tab is filtered to display invocation records
in hierarchical format. (Invocation records are displayed in hierarchical
format by default. Detailed information about displaying invocation
records is found in the topics "Filtering server console and log records
in the Server Logs view" and "Overview of cross-component tracing.")
5. In the tab, select the check box beside the top invocation
record, which is typically a Start invoke record.
This will automatically select the check boxes of all records within
the invocation.
6. Click the Load into Test Client icon . The test client opens and
displays the events that correspond to the invocation records.
If you encountered an ServiceRuntimeException
when running a test that involved asynchronous invocations from a
mediation flow, the exception is expected and can be ignored. It is
thrown when the mediation flow polls for results but the invocation
response is not yet available.