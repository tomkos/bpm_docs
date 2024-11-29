<!-- image -->

# Creating test suites with scenario-based test cases

## Before you begin

## About this task

## Procedure

1. In the Business Integration view, right-click the component
test project where you want to create your test suite and then select New
> Component Test Suite. The Create Component Test Suite
wizard opens.
2. In the Name field, type the name
that you want to assign to the new test suite.
3. Click Next. The Select a Test Pattern
page opens.
4. In the Available test patterns list
box, select Scenario-based testing.
5. Click Next. The Define a Test Scenario
page opens.
6. In the Test case name field, type
the name that you want to assign to the test case.
7 Complete the following steps to select operations for thetest scenario:
    1. In the Available components and interfaces list
box, expand a module and then expand one of its components to reveal
the interface that contains one or more operations that you want to
select.
    2. Select the interface that contains the one or more operations
that you want to add to the test scenario. The operations are displayed
in the Testable operations list box.
    3. In the Testable operations list
box, select an operation and click the Add icon.
The name of the operation and its location are displayed in the Test
scenario list box.
    4. Repeat these steps for each operation that you want
to add to the test scenario. The order in which the operations are
listed in the Test scenario list box will determine the sequence in
which they are tested.
8 If you want to remove one or all operations from the Testscenario list box, complete one of the following steps:

- To remove a single operation, select the operation and then
click the Remove icon.
- To remove all operations, click the Remove All icon.
9 If you want to undo or redo the addition or removal ofan operation in the Test scenario list box,complete one of the following steps:

- To undo the addition or removal of an operation, click
the Undo icon.
- To redo the addition or removal of an operation, click
the Redo icon.
10 If you want to move an operation up or down in the listof operations, complete one of the following steps:

- To move an operation up the list, select the operation and
then click the Up icon.
- To move an operation down the list, select the operation and
then click the Down icon.
11. Click Finish. In the Business Integration
view, the new test suite is added to the component test project and
the test suite automatically opens in the test suite editor.