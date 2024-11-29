<!-- image -->

# Running test projects, suites, and cases in the Component Test
Explorer

## Before you begin

## About this task

To run a component test project, test suite, or test case,
complete the following steps:

## Procedure

1. In the Component Test Explorer menu bar, click Test
Cases. The Test Cases page opens.
2. In the explorer area, select a component test project,
test suite, or test case.
3 If you have referenced some proprietary environment variablesin the test suite editor for the selected component test project,test suite, or test case, and you now want to define the environmentvariables, complete the following steps:
    1. Scroll down to the Environment Variables table
and click Add. The Select Environment Variables
page opens.
    2. In the Select Environment Variables page, select the
check boxes beside the proprietary environment variables that are
referenced in the test suite editor and then click Finish.
The names of the environment variables are displayed in the Name column
of the Environment Variables table and they are all assigned an initial
value of empty string (" ").
    3. In the Value column of the Environment
Variables table, type in a value for each environment
variable that you do not want to have assigned a value of empty string
during the test. Note: If you defined a default value for
an environment variable in the test suite editor and you want to use
the default value in the test, you must ensure that the environment
variable does not appear in the Environment Variables table.
If it appears in the table, you can remove it by clicking Remove.
4. Click the Run icon . An entry appears in the Log table
and the Result column of the table displays
a result state of running. (The Log table
shows a history of all of the tests that have been run for the component
test project, test suite, or test case that is selected in the explorer
area.)
5. Click the Refresh icon  to refresh the state of the log entry.
A test case run is complete when the Result column
displays one of the following result states:

pass
The test passed.
fail
The test failed. Either an assertion failed or an unexpected error
occurred.
error
An error occurred when Component Test Explorer attempted to load
and run a test.

The result state information includes the number
of test cases that are in the result state, for example pass 2.
 If multiple test cases run, then the states of all of the test cases
will be shown in the final state. For example, pass 2; fail 3 means
that you ran five test cases; two which passed and three which failed,
as shown in the following figure:
6. To open additional results information, click the result
state in the Result column. The summary for
each  test case and variation is displayed, as shown in the following
figure: