<!-- image -->

# Order-by clause

You can specify a list of columns from the views by which the result
is sorted. These columns must be fully qualified by the name of the
view and the column.

The order-by clause syntax is similar to the syntax of an SQL order-by
clause; use commas to separate each part of the clause. You can also
specify ASC to sort the columns in ascending
order, and DESC to sort the columns in descending
order. If you do not want to sort the query result set, you must specify null for
the order-by clause.

Sort criteria are applied on the server, that is, the locale of
the server is used for sorting. If you specify more than one column,
the query result set is ordered by the values of the first column,
then by the values of the second column, and so on. You cannot specify
the columns in the order-by clause by position as you can with an
SQL query.

## Examples of order-by clauses

- PROCESS\_TEMPLATE.NAME: Sorts the query result alphabetically by the
process-template name.
- PROCESS\_INSTANCE.CREATED, PROCESS\_INSTANCE.NAME DESC: Sorts the query result by
the creation date and, for a specific date, sorts the results alphabetically by the process-instance
name in reverse order.
- ACTIVITY.OWNER, ACTIVITY.TEMPLATE\_NAME, ACTIVITY.STATE: Sorts the query result
by the activity owner, then the activity-template name, and then the state of the activity.