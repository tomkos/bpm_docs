<!-- image -->

# Creating component test cases from unit tests

## Before you begin

## About this task

To create test cases from unit tests, perform the following
steps.

## Procedure

1. Open the integration test client and perform a unit test
by invoking an operation.
2. In the Events area, right-click the Invoke event
that was used to initiate the unit test and then click Create
test case. The New Component Test Case wizard opens.
3. In the Test project field, select
the component test project that contains the test suite where you
want to create the new test case.
4. In the Test suite field, select
the test suite where you want to create the new test case.
5 From the Testpattern type area, select the type of component test patternyou want to use for the new component test case.
    - Operation-level test cases: This option creates a separate
test case for each operation included in the test.
    - Scenario-level test case: This option creates a single test
case for all selected operations.
6. If you are creating
a scenario-level test case, enter a name for the test case in the Test
case name field.
7 Determine whether you wantto create a basic test case or whether you want to customize the testcase by selecting specific events to include and the order in whichthe resulting steps occur.

- To create a basic test case, click Finish.
The test suite editor opens and displays the new test case or cases,
depending on whether you chose operation-level or scenario-level testing.
This task is now complete.
- To customize the test case, click Next,
and then continue to the next step in this procedure.
8. From the Add Steps
to the Test Case page, select those events you want to include in
the test case. By default, all Invoke, Return, and Exception
events are selected.Tip: To quickly add or remove all
events of a particular type, click the Select Types button.
In the Select Event Types window that opens, select the event
type or types you want to include or exclude.
9. Click Next.
The wizard creates a step for each selected event and
displays a summary of the test case in the Test Case Summary page.
10. Verify that the test case
contains the appropriate steps and, if necessary, adjust the order
of the steps using the arrow icons on the page.
11. Click Finish. The
test suite editor opens and displays the new test case or cases, depending
on whether you chose operation-level or scenario-level testing.
12. Optional: If you want to save your changes
in the test suite editor, press Ctrl-S. The
new test case is displayed under the associated test suite in the
Business Integration view.