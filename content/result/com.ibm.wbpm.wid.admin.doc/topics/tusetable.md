<!-- image -->

# Specifying variable values

## Before you begin

## About this task

## Procedure

1. In the test suite editor, click the Test Cases tab
to open the Test Cases page.
2. In the Test Cases area, select the test case for which
you want to specify variable values.
3. At the bottom of the test suite editor, click the Test
Data Table tab. The Test Data table view opens.
4. Click the Default tab to open the
default test variation pane or click the tab of another test variation
to open its pane. The test data table is displayed in the pane. It
is similar to the value editor in the test client, but it has an In column
and an Expected column rather than a Value
column. The In column is where you specify input or request values
and the Expected column is where you specify output or response values.
5 In the test data table, you can simply type some valuesfor a selected variable by completing the following steps:
    1. In the In column or the Expected column,
click the field cell where you want to specify a new value. Note: If
you specify a value for a variable that is not used in any of the
steps defined in the test case (such as an Invocation, Wait for Time,
Wait On, Verify Event, or Emulator Definition step), the variable
will not be initialized when the test case is run and a value of null
will be returned for the variable.
    2. Press the Enter key or simply being typing some
characters. A text box automatically opens, as shown in the following
figure:
    3. In the text box, type the new value that you want to
assign to the variable. If the format of the value is Java
Expression, then content assist is available. (Specifying
a reference to another element in the table can only be accomplished
in the Java expression format.) You can press Alt+Enter at
any time to add additional input lines. (If you decide that you do
not want to retain the new value that you are specifying in the text
box, you can press the Esc key to discard the new value.) Additional
information about Java expressions is found in the topic Java expressions.
    4. Press Enter or simply click another cell to save
your new value. For example, in the following figure, the value Tools has
been typed in as the value for the first description attribute:
6. If you want to specify values for arrays, right-click the
name of each array field in the Name column
and select Add Elements to open the Add Element
window, then specify a value for the selected field in the Enter
the number of new elements to add field and click OK.
For example, in the figure, the items array
field was right-clicked and Add Elements was
selected, then values were specified for the individual fields under
the items[0] element (such as the value 5 that
is specified for the quantity attribute).

## Example