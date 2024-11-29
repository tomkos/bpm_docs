# Troubleshooting overlap and gap warnings in table-based rules

## Symptoms

Orange
icons are displayed in the lower left corners of cells in the table-based
business rule.

## Causes

## Resolving the problem

Because
overlaps and gaps do not prevent a rule from running, you can deploy
a rule that has gap and overlap warnings. However, overlaps and gaps
might produce incorrect results when the rule runs if there are ambiguities
in the rule definition.

By default, rule designer checks for
overlaps and gaps in all columns. If you do not want rule designer
to display gap and overlap warnings for a particular column, right-click
the header cell of the column and clear the Check Gap and Check
Overlap check boxes.

In some cases, empty rows are
considered as gaps and are flagged with warnings. To resolve these
warnings, click the optimize icon in the upper left corner of the
table-based rule to remove any empty rows and arrange the data in
ascending order based on the values in the first column. The optimize
icon is enabled only after you make changes to the table-based rule.

To
resolve gaps in a particular column, you can add a row with the value Otherwise to
define a rule to use in case none of the other values for the condition
in that column are true. To set the value of a cell to Otherwise,
right-click the cell and click Set to Otherwise.