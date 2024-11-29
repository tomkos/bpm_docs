# Using decision tables in the Process Designer

## Before you begin

## Procedure

The following steps illustrate how to add a simple decision
table to an existing Decision task.

1. Click the Decisions tab to open
the decision editor.
2. Select your Decision task, for example, Approval.
The editor opens with a basic template for a simple rule,
with one condition (if) and one action (then). Click
the X on the right side to delete that action
rule.
3 Add a decision table.
    1. Click Add a decision table.
A default decision table is shown that contains a condition
column (C0), an action column (A0), and twenty rows.
    2. Change the labels of the columns by double clicking
the column header and entering the new name. For example,
change C0 to Amount, C2 to Rating,
and A0 to Approval.
    3. Save your work by pressing Ctrl+S.
4 Define the rules for the decision table. Forexample,

- If the amount is between 0 and 10000 and the rating is at least
100, set Approval to approve.
- If the amount is between 10001 and 100000 and the rating is at
least 200, set Approval to approve.
- If the amount is between 100001 and 1000000 and the rating is
at least 300, set Approval to approve.

1 Define the conditions for the columns.
    1. Right-click the Amount column header and choose Define
column. An editor window for defining conditions opens.
    2. Click in the window and press the space bar to see the options.
    3. Choose the amount variable and press the space
bar again.
    4. Choose is between min and max and click Define at
the bottom of the editor window. The condition for the first column
is now defined. Check that you see min and max labels
below the Amount column header.
    5. Double-click the first row below the min and max labels
and enter 0 for the min value and 10000 for
the max value.
    6. In the second row, enter 10000 for the
min value and 100000 for the max value. Check
that you get an error for overlapping values. Change the min value
from 10000 to 10001.
    7. In the third row, enter 100001 and 1000000 for
the min and max values.
2 Define the Rating column as rating is atleast <a number> .

1. Right-click the Rating column header and choose Define
column. An editor window for defining conditions opens.
2. Click in the window and press the space bar.
3. Choose the rating variable and press the space
bar again to see the options.
4. Choose the is at least <a number> option
and click Define.
5. Provide the numbers by double-clicking on the rows, and entering 100, 200,
and 300.
3 Define the Approval column as set approvalto approve . The definition of the decision table is complete. Tips:

1. Right-click the Approval column header and choose Define
column. An editor window for defining conditions opens.
2. Click in the window and press the space bar.
3. Choose the set <variable> to <variable value> option.
4. Click <variable> and choose approval.
5. Click <variable value> and choose <string>.
6. Enter approved between the “” and
click Define.

- You can use the keyboard shortcut Ctrl+F to open a search field
that will perform a search on all values that are in the decision
table.
- Move the mouse pointer over the row numbers to see the rules as
if-then rules.
4. Save your work by pressing Ctrl+S.

## Results

## What to do next

The previous example only shows how to define a decision
table, and does not model when a credit approval would be rejected.

```
If 
AMOUNT is between 10001 and 100000 and the RATING is at least 200
then
approve is set to approved.
```

```
If
AMOUNT is between 10001 and 100000 and the RATING is less than 200
then
approve is set to rejected.
```

- Decision tables - except you must double-click a cell to edit it, and
preconditions, optimizing, and row ordering are not supported.
- Rules Embedded capabilities and limitations
- Restricted characters in element names and vocabulary labels