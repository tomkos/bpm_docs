# Populating a table control using an SQL query in a heritage coach (deprecated)

## Before you begin

Before using a SQL query to populate a Table control, be
aware of the following:

- The Execute SQL option is only used for retrieval of data (insert,
update, and delete operations on data are not allowed).
- The SQL query is run before the heritage coach is displayed, and only if the variable to which
the table is bound has no current value. If you want to refresh the value every time the heritage
coach is rendered, select the Reload option. For example, if the Service
updates the value during the life of the runtime task, you would want to reload this value each time
the heritage coach is rendered.
- The property names of your custom data structure must match the column names in the database
table that you want to query. When executing the SQL query, IBM® Business Automation Workflow uses these labels to match the values from
the columns to the correct rows in your heritage coach table. Note that the names are not
case-sensitive. If the property names do not match the column names, you can use column aliases in
your SQL statement to perform the correct matching. The following
example:SELECT PRICE AS Cost, ITEM\_NAME AS ItemNamereturns the value of
the PRICE column to the Cost property in your custom data structure, displaying it in the column to
which it is bound in the heritage coach. The value of the ITEM\_NAME column is displayed in the Item
Name column.

## About this task

## Procedure

1. Open the service that contains the heritage coach that you want to work with and then click the
Coaches tab.
2. Drag a Table control from the palette onto the design area.
3. While the Table control is selected, click the Presentation
option in the properties.
4. Click the Execute SQL check box
to enable it.
5. In the Data Source text box, type
the data source from where you want to retrieve the data. By default,
the data source is "jdbc/TeamworksDB" , which points
to Business Automation Workflow databases.
When you want to use a data source other than the jdbc/TeamworksDB data
source, ensure that it is an XA data source. If you use a non-XA data
source, or an emulated XA data source, you might receive an error
about a database connection failure.
6. In the SQL text box, enter an SQL
query to select the data that you want from the data source. 
For example, you could select the ID, status, and employee type
from a table named R2H\_PositionType by entering the following text:select id, status, employeeType from R2H\_PositionTypeThe
order of the entries is in the order which the table rows are returned.
Use an ORDER BY clause in your SQL statement to override this behavior.