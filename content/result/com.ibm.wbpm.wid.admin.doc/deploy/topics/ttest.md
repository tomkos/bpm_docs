<!-- image -->

# Testing authentication using the integration test client

## About this task

To
test authentication:

## Procedure

1. In the Business Integration view,
right-click the module that contains your import and select Test
> Test Module. The integration test client opens. In
the Events area of the integration test client, an Invoke event is
automatically generated whenever the test client is started. (An Invoke
event is an interactive event, which means that you must manually
select an operation to test and specify some initial request parameters
values for the operation before the test can continue.)
2 In the Detailed Properties areaof the integration test client, complete the following steps:
    1. In the Component field, ensure
that the selected component is the component that you want to debug.
For example, if you were working with the sample application that
serves as a running example in these topics on implementing basic
authentication, you would select sendWebServiceCallToServer.
    2. In the Interface field, ensure
that the component interface is selected that contains the operation
that you want to invoke.
    3. In the Operation field, ensure
that the interface operation is selected that you want to invoke.
3. In the Initial request parameters value
editor, specify the input values for the selected operation in the Value column,
as shown in the figure below:
4. Click Continue. The Deployment Location
wizard opens.
5. Ensure that the correct deployment location is selected
in the Deployment Location wizard.
6. In the Mode drop-down list, ensure
that Run is selected and then click Finish to
automatically deploy the module to the server and to invoke the selected
operation. If your test is successful, the integration test client
returns the result of your test.

## What to do next