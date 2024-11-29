<!-- image -->

# Testing event definitions

## Before you begin

Testing an event definition is similar in many respects to testing an interface operation. If you
have not worked with the test client before, you should read Testing interface operations and
its subtopics before testing either an event definition or an interface operation.

## About this task

To test an event definition:

## Procedure

1 Complete one of the following steps:
    - If the integration test client is not open, right-click your module in the Business
Integration view and select Test > Test Event Definition. The integration
test client opens and an Emit event is displayed in the Events area.
    - If the integration test client is already open for your module, click the down arrow beside
the Invoke icon  and select Emit. An Emit
event is displayed in the Events area.
2. In the Configuration field, ensure that the correct test
configuration is selected. A default test configuration is automatically created whenever you open
the integration test client. If you did not open the integration test client by loading a test
configuration that you saved earlier, the default test configuration will already be selected in the
Configuration field.
3. In the Module field, ensure that the correct module is
selected.
4. In the Event definition field, select the event definition that
you want to test. The test client will list all event definitions found in the selected module or in
any libraries or projects that are referenced by the module.
5. In the value editor, specify values for the properties and extended data elements of your
event definition. Information about using the value editor and data pool editor to specify values
for event definitions is found in the test client topic Value and data pool
editors.
6. Click the Continue icon . If the Deployment Location
wizard opens, select the server where you want to deploy your selected module, as described in the
test client topic "Deploying modules." The Events area displays a Started event and an Emitted
event. If the test is successful, a Succeeded event and a Stopped event are also displayed.
If the test is not successful, an Exception event and a Stopped event are
displayed.