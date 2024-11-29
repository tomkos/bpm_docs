# Saved search acceleration tools

## Prerequisite

- Use the command line script, but you must stop all the servers.
- Use the Saved Search REST APIs to create and delete the saved search acceleration tools. You do
not need to restart the servers. For more information, see Operations REST APIs.

If you are using containers, you must use the Saved Search REST APIs to create the saved search
acceleration tools.

## Generate a schema

```
./SchemaGenerator.{sh|bat} -profileName PROFILE\_NAME -deName DEPLOYMENT\_ENVIRONMENT -OPTION
```

When you choose the -output or -screen option,
you can first review the changes that the tool will make, and then
make them manually. If you choose anything other than the -execute option,
you must manually run the SQL statement before you proceed. You can
then review the changes that the tool wants to perform, and you can
make any changes that are necessary for your environment before you
execute them, such as providing SQL hints or adding indexes.

- The generated SQL statement might be too long for the SQL command
line processor if the system contains a very large number of searchable
variables. You might see the SP2-0027: Input is too long (>
2499 characters) error. To solve the problem, split the statement
across multiple lines of less than 2500 characters each.
- If you run the SQL statement manually, consult IBM Support before
you change any column names or data types.

## Examples of schema generation

```
>./SchemaGenerator.sh -execute
INFO  SchemaGenerator - SchemaGenerator starting
INFO  SchemaGenerator - dbdriver   : oracle.jdbc.driver.OracleDriver
INFO  SchemaGenerator - dburl      : jdbc:oracle:thin:@utica.lombardiqa.com:1521:uticasid
INFO  SchemaGenerator - dbuser     : adminusr
INFO  SchemaGenerator - Processing BPD ID 784afc31-e47b-4e83-b596-20b3cee2b422
INFO  SchemaGenerator - Processing BPD ID c904b3b1-afc1-4698-bf5a-a20892c20275
INFO  SchemaGenerator - Processing BPD ID e39cc53a-b75c-498c-8c28-43761fb73f2d
INFO  SchemaGenerator - Finished processing BPDs
INFO  SchemaGenerator - Executing Pivot Table DDL
INFO  SchemaGenerator - Executing Variable Names Table DDL
INFO  SchemaGenerator - Executing insert statements for Variable Names Table
INFO  SchemaGenerator - SchemaGenerator completed successfully.
```

```
>./SchemaGenerator.sh -output pivot.sql
INFO  SchemaGenerator - SchemaGenerator starting
INFO  SchemaGenerator - dbdriver   : oracle.jdbc.driver.OracleDriver
INFO  SchemaGenerator - dburl      : jdbc:oracle:thin:@utica.lombardiqa.com:1521:uticasid
INFO  SchemaGenerator - dbuser     : adminusr
INFO  SchemaGenerator - Processing BPD ID 784afc31-e47b-4e83-b596-20b3cee2b422
INFO  SchemaGenerator - Processing BPD ID c904b3b1-afc1-4698-bf5a-a20892c20275
INFO  SchemaGenerator - Processing BPD ID e39cc53a-b75c-498c-8c28-43761fb73f2d
INFO  SchemaGenerator - Finished processing BPDs
INFO  SchemaGenerator - Writing DDL to pivot.sql
INFO  SchemaGenerator - Finished writing DDL to pivot.sql
INFO  SchemaGenerator - SchemaGenerator completed successfully.
```

## Load data

After the
tables are created and all variables are loaded into the variables
table, you must load the LSW\_BPD\_INSTANCE\_VARS\_PIVOT table with data
by using the DataLoad tool. The tool loads all the BPD instances that
are currently on the server. Loading the data allows the search queries
to use the pivot tables and find the data. When new instances are
created, instances are changed, or instances are cleaned up (by the
 BPMProcessInstancesCleanup script), the new data is automatically
loaded to the pivot tables or the pivot tables are cleaned up, too.

```
./DataLoad.{sh|bat} -profileName PROFILE\_NAME -deName DEPLOYMENT\_ENVIRONMENT
```

The
DataLoad tool populates the pivot table with data from every BPD instance
that is currently deployed in your database. This tool provides status
messages to keep you informed of its progress.

## Example of DataLoad output

```
INFO  DataLoad - DataLoad starting
INFO  DataLoad - dbdriver   : oracle.jdbc.driver.OracleDriver
INFO  DataLoad - dburl      : jdbc:oracle:thin:@utica.lombardiqa.com:1521:uticasid
INFO  DataLoad - dbuser     : adminusr
INFO  DataLoad - Started at: 2011-09-06 16:26:11.26
INFO  DataLoad - Count obtained
INFO  DataLoad - Creating values
Processed 1000 records so far plus 1 instances with no variables, current block took 16.97 seconds, 0.95% complete, 0.28 minutes elapsed, 29.55 minutes remaining
Processed 2000 records so far plus 1 instances with no variables, current block took 16.42 seconds, 1.90% complete, 0.56 minutes elapsed, 28.80 minutes remaining
...
Processed 104000 records so far plus 4 instances with no variables, current block took 16.67 seconds, 98.58% complete, 29.11 minutes elapsed, 0.42 minutes remaining
Processed 105000 records so far plus 4 instances with no variables, current block took 16.19 seconds, 99.53% complete, 29.38 minutes elapsed, 0.14 minutes remaining
INFO  DataLoad - Total instances copied into pivot table: 105500
INFO  DataLoad - Total instances with no variable data copied into pivot table: 5
INFO  DataLoad - Finished at: 2011-09-06 16:58:00.891
INFO  DataLoad - DataLoad completed successfully.
```