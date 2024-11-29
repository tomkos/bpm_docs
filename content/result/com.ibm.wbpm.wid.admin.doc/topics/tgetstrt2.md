<!-- image -->

# Getting started: Top-down testing of test cases

## About this task

To perform
top-down testing of test cases:

## Procedure

1. In
the Business Integration perspective, select File >
New > Component Test Project. The New Component Test
Project wizard opens.
2. In the Project name field, type
the name that you want to assign to the new component test project.
3. If you are testing a module that is part
of a Process Application, the next window allows you to select a process
application or toolkit that will be associated with the new component
test project.
4. Click Finish. The new component
test project appears in the Business Integration view.
5. In the Business Integration view, right-click the component
test project and select New > Component Test Suite.
The New Component Test Suite wizard opens.
6. In the Name field, type the name
that you want to assign to the new test suite.
7. Click Next. The Select a Test Pattern
page opens.
8. In the Available test patterns list
box, select Operation-level testing.
9. Click Next. The Select the Operations
to be Tested page opens.
10. In the Select the Operations to be Tested page, select
the specific operations that you want to test, as shown in the following
figure:
11. Click Finish. The new test suite
is added to the component test project in the Business Integration
view. The test suite contains one component test case for each operation
that was selected in the New Component Test Suite wizard. The
test suite editor automatically opens to the Overview page for the
new test suite that you created.
12. In the test suite editor, click the Test Cases tab.
The Test Cases page opens and displays the properties for the first
test case that is selected in the test suite, as shown in the following
figure:  Below the Test Cases page, the Test Data Table
view is displayed for the test case that is selected in the Test Cases
page.
13. In the Test Cases area of the Test Cases page, select the
first invocation under the first test case, as shown in the following
figure:  The Test Cases page changes to display the properties
for the selected invocation, as shown in the following figure:
14. In the lower right corner of the Test Cases page, ensure
that the Request tab is selected.
15. Under the Request tab, select New from
the Item list. The New Data Table Variable
window opens.
16. In the Name field, type the name
that you want to assign to the new data table variable.
17. In the Type system section of the
wizard, select either Java or XSD.
18. Beside the Type field, click Browse and
select the data type.
19. In the Add field, select either Before or After to
indicate the position where you want the new variable to appear in
the data type table in relation to the variable listed in the unlabeled
field to the right of the Add field.
20. In the unlabeled field to the right of the Add field,
select the existing variable that you want to position the new variable
either before or after.
21. In the Variable intent section,
select Input parameter or Expected
result. (This example assumes that Input parameter is
selected.)
22. Click Finish to add the new variable
to the test data table. In the following figure, a new variable named Item2 has
been added to the test data table:
23. In the Set column of the test data
table, specify input values for the request by clicking a cell
and typing a value and then pressing Enter.
Or you can use the pop-up menu to set a value.
24. In the Expected column of the test
data table, specify return values for the response by clicking
a cell and typing a value and then pressing Enter.
Or you can use the pop-up menu to set a value. The
following figure shows some values that have been set in the test
data table:
25. In the Test Cases area of the Test Cases page, select the
next test case or an invocation under the next test case.
The test data table view changes to reflect the variables and
attributes for the operation associated with the selected test case.
26. In the test data table, right-click the items array
and select Add Elements. The Add Element window
opens.
27. In the Enter the number of new elements to add field,
type the number of elements that you want to add and click OK.
28. In the test data table, specify some values, as shown in
the following figure:
29. Press Ctrl-S to save your changes.
30. In the Business Integration view, right-click your test
suite and select Run Test Cases. The integration
test client opens, as shown in the following figure:
31. In the Events area, click the Continue icon.
Depending on the current deployment state of your module, the Deployment
Location wizard may open, as shown in the following figure:
32. If the Deployment Location wizard opens, select the server
where you want to deploy your module and click Finish.
33. If the User Login window opens, type your administrative
user ID and password into the User ID and Password fields.
The test runs and completes, as shown in the following figure: