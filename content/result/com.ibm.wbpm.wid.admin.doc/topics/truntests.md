<!-- image -->

# Running test suites

## About this task

## Procedure

1. In the Business Integration view, use the Ctrl key
to select the component test artifacts that you want to run and test,
such as component test projects, test suites, or test cases.
2. Right-click one of the selected artifacts and select Run
Test. The integration test client opens and displays the
selected test suite. To test a component
test project that is part of a process application or toolkit, right-click
the test case name and select Run Test Case.
The integration test client opens
3. In the Events area, click the Continue icon.
Depending on the current deployment state of your module, the Deployment
Location wizard may open, as shown in the following figure:
4. If the Deployment Location wizard opens, select the server
where you want to deploy your module and click Finish.
If you are testing a component test project
that is part of a process application or a toolkit, you can select
the unit test environment (UTE) server or the Workflow Center Server
as the deployment location.
5. If the User Login window opens, type your administrative
user ID and password into the User ID and Password fields.
The test runs and completes. If you select a Run
Test or Test Suite event in the
Events area, the Detailed Properties section displays an overall Pass,
Fail, or Error verdict and progress bars that indicate how many test
cases passed, failed, or were in error (as shown in the previous figure).
If you select a Test Case or Test
Variation event, the Detailed Properties section will
display a Pass, Fail, or Error verdict for the selected test case
or test variation. Additionally, selecting a Test Variation event
will reveal the nature of any failure or error that was encountered
during the test.