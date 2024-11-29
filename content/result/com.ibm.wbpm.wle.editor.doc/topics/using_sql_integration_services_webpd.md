# Invoking SQL Integration service flows

## Before you begin

Traditional: 
 Your
Business Automation Workflow administrator
must define the data sources that are needed for your SQL integrations, by using the admin
console.

Containers:

To integrate with SQL, update the Liberty configuration and add the driver
files to your persistent storage. See Configuring custom Liberty data sources.

## About this task

The System Data toolkit includes SQL Integration capabilities that enable integration with
external databases.

The SQL Integration service flows support common database interactions, including support for
parameterized queries. These service flows can automatically map query results directly into the
relevant variable type. The SQL Integration service flows enable you to develop implementations
to

- Read existing data from a database.
- Insert new data to a database.
- Call-stored procedures in your database.

When passing data between a workflow and a connected database, the SQL Integration service flows
allows you to specify SQL data types such as integers, BLOBs, and CLOBs.

- SQL Execute Statement
- SQL Execute Statement (SQLResult)
- SQL Execute Multiple Statements
- SQL Execute Multiple Statements (SQLResult)
- SQL Execute Script (SQLResult)
- SQL Call Stored Procedure
- SQL Call Stored Procedure (SQLStatement)
- SQL Call Stored Procedure (SQLResult)
- SQL Call Multiple Stored Procedures
- SQL Call Multiple Stored Procedures (SQLResult)
- SQL File to Blob
- SQL File to Blob (SQLStatement)
- SQL Blob to File
- SQL Blob to File (SQLStatement)
- SQL File to Clob
- SQL File to Clob (SQLStatement)
- SQL Clob to File
- SQL Clob to File (SQLStatement)
- SQL Get Database Type

## Procedure

1. Open a process application.
2. Click the Toolkits category to see a list of toolkit dependencies
for the current process application.
3. Click the System Data toolkit to see its contents.
4 Click the Services category and then click one of the listed SQL serviceflows. For example,
    - The SQL Execute Statement service flow.
    - The SQL Execute Statement (SQLResult) service flow provides a wrapper
for the SQL Execute Statement service flow and returns the results in a fixed return type,
SQLResult.
5. Switch from the diagram view of the service to the Overview tab and read
its documentation.
6. Switch from the overview of the service to the Variables tab.
7. Click an input or output variable to see its details, such as its type and any default
values. 
To use an SQL integration service flow, you must specify the input and output variables that are
listed in the following table.
Table 1. Input and output parameters for the SQL Execute Statement services.

Name
Type
Description

sql
String
This input parameter provides the SQL statement. For example, if the variable
tw.local.sqlSelectSatatement contains the SQL statement string SELECT name,
place FROM GREETING, enter the variable name tw.local.sqlSelectSatatement
for the sql parameter.

parameters
List of SQLParameter
This input parameter describes the value, type, and mode information for each
'?' parameter that you use in your sql string. For each parameter, specify an SQLParameter object
with an SQLType, the value of the parameter, and a SQLParameterMode. SQLParameterMode can be
IN, OUT or INOUT as defined by the JDBC
specifications of java.sql.ParameterMetaData. For more information about supported types, see the
type property description of the SQLParameter object in JavaScript API in processes and service flows.

maxRows
Integer
This input parameter limits the number of rows that are returned.

returnType
String
This input parameter provides the name of the business object data type that
the results are returned in. If you specify SQLResult the results are transformed
automatically into a list of SQLResult, In this case, you need to create one
variable of type SQLResult and mark it as a list variable.

dataSourceName
String
This input parameter is the JNDI name of the data source that your
administrator defined, for example "jdbc/greetdb".

results
ANY
This output parameter contains the results of the query. The results object is
of the type that you specified for returnType.