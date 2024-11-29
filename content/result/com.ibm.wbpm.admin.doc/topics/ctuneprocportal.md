# Tuning Process Portal searches

When you set configuration property values in .xml files, the rules that are
described in The 100Custom.xml file and configuration apply.

## Saved search count performance optimization

If you expect more
than 500 results entries for a search, for example, if you are using the TWSearch function or saved
search APIs, or if your Process Portal users
usually have more than 500 tasks, you can increase this number.

1. Insert the following section into the 100custom.xml file:
<properties>
    <server merge="mergeChildren">
  <process-search-engine-count-optimization merge="replace">500</process-search-engine-count-optimization>
       </server>
</properties>
2. Adjust the 500 value to meet your needs. The larger the value, the more memory and time are
needed to retrieve the entries.
3. Save the changes to the 100custom.xml file, and restart the server.

## Optimize saved searches with business data variables

You
can optimize your process searches by using the saved search acceleration
tools.

For systems with a large amount of business data that is used in searches (for example 10+), the
Process Portal tasks and instance queries might
operate slower than expected. When you use the saved search acceleration tools to optimize your
process searches, Process Portal searches that
filter on business data are faster.

- SchemaGenerator tool - This tool generates two new tables: LSW\_BPD\_INSTANCE\_VAR\_NAMES (variables
table), and LSW\_BPD\_INSTANCE\_VARS\_PIVOT (pivot table). It also generates the schema for each
table.
- DataLoad tool - This tool populates the variables table with data from the BPD instances that
are currently in progress.

- The pivot table
    - Instance ID
    - Every searchable business data variable that is defined in all currently deployed BPDs
    - Every business data variable that is defined in LSW\_BPD\_INSTANCE\_VARIABLES
- The variables table

- Variable name
- Column name
- Data type

- Enabling an optimization
- Disabling an optimization
- Enabling an optimization again

- See Saved search acceleration tools.

To disable optimization, complete the following steps:

1. Shut down the server.
2. Remove the pivot and variables tables from your database.
3. Restart the server.

1. Deploy all BPD updates.
2. Stop the server.
3. Remove the pivot and variables tables from your database.
4. Rerun the SchemaGenerator and DataLoad tools.
5. Restart the server.

The following requirements and restrictions apply:

- You use this process only for production deployments, or for systems
that simulate production deployments.
- When using a pivot table, you must ensure that you do not use more than 1000 searchable
variables. If you need to exceed this limit, you must drop the pivot table and use the default
search function instead. This will result in performance that is inferior to that of a pivot table.
(The default search function searches the variable values using the LSW\_BPD\_INSTANCE\_VARIABLES
table.)
- If you have deployed a new snapshot that contains changes to business data variable definitionsin BPDs (such as adding new variables, renaming any existing variable, or modifying the type of anyexisting variable) or business data alias changes, you must rerun the tools to rebuild the pivottable.Note: Define business data by selecting the Visible in Process Portal option to make the corresponding variable available on the BPD property sheet. See Making business data available in searches and views . Attention: If youdo not rerun the optimization tools when changes to business data occur, your process searches mightgenerate failures. For example, if you changed the type of business data and do not rerun theoptimization tools, the old business data type persists in the pivot table, which results inpotential SQL exceptions. Similarly, if you added or changed a business data alias and do not rerunthe optimization tools to regenerate the pivot table, SQL exceptions might also occur. Restriction: DB2 The following restrictions apply to a DB2 database. Oracle The following restrictions apply to an Oracle database. All The following restriction applies to the databases of all database products.
    - The copies of all string values in the pivot table are truncated if they exceed 128 bytes.
    - The sizes of all unique business data variables, when added together, must be less than 32767
bytes. This means that if all your business data variables were strings, you would be limited to
32767/128 = 255. This restriction applies to all unique business data variables that are defined
across all your deployed BPDs. For example, if you had three BPDs deployed that each had six
business data variables, but one of them was defined in exactly the same way in all three BPDs, then
you would have a total of 16 unique business data variables.
    - When you query business data by using the DB-based search, the search is typically accessed
through the JavaScript API and several REST APIs. If you pass a decimal value or an empty string
value to a process and the value is stored in a variable that is exposed to searches, the APIs might
return a search result for Oracle that differs from the search result that is returned for other
database products. Generally, this behavior causes a problem only if you are using both Oracle and
another database product, such as DB2.
    - If you pass a decimal value that has zeros as fractions to a process and the decimal value is
stored in a variable that is exposed to searches (such as the Visible in Process
Portal variable), then the APIs return the value as it is formatted by the database. For
example, if you pass a value of 150.00 to the process, the APIs would
return a result of 150 for Oracle and a result of
150.00 for DB2. Any problems that result from this discrepancy can
generally be fixed at the application level. For example, in a Java application, you can use the
 java.text.NumberFormator
java.text.DecimalFormat class to help resolve the problems.
    - If you pass an empty string to a process and the empty string is stored in a variable that is
exposed to searches (such as the Visible in Process Portal variable), then
the APIs return a result of null for Oracle and a result of empty string for DB2.
    - The string values for business data are truncated to 512 characters.

## Improve performance of the process search engine

When you run a DB2 query for process instances by using Process Inspector in the
Process Admin Console, the query might fail and return the SQLCODE=-129 (too many tablename
in query) error message in the browser if a large number of process instances is returned.
If this error occurs, set the use-concatenation-optimization property to
false for the query to succeed.

## Control task visibility in dashboards

With the enable-group-constraint-for-claimed-tasks property, you can control
how tasks are visible in Process Portal dashboards.
By default, this property is set to false so that users can see only the tasks that
they are working on or which they can start. The tasks that other users of the same user group have
claimed are not listed. To allow all users in a user group to see all the claimed tasks for the
users in the group, set this property to true.

## Make search on user names case-sensitive

The case-insensitive-security-cache configuration property gives you control
over case sensitivity for searches on user names. By default, this property is set to
true. This setting means that you can find task assignees by their name in the
database regardless of how you capitalize the user name in the search string. If you want the search
to be case-sensitive, you can set this property to false in the
60Database.xml file. For more information, see Configuring IBM Business Automation Workflow to handle white space and letter case variations in the LDAP server.

## Show or hide unexposed processes

In saved searches, you can configure how the Process Definition filter shows business processes.
By default, the process-definition-search-all-bpds property is set to
false and shows only exposed processes. To show both exposed and unexposed
processes, set the property to true.

- Saved search acceleration tools

In nonfederated Business Automation Workflow environments, you can use the SchemaGenerator and DataLoad tools to optimize saved searches.
- Prioritizing work

To increase your efficiency working on tasks in Process Portal and Workplace, you can activate the Intelligent Task Prioritization function that sorts and filters your task list based on expertise and task completion time. To activate Intelligent Task Prioritization, you must enable the task filter service.