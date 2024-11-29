# Using IBM Business Automation Workflow SQL
Integration services (deprecated)

## Before you begin

Check with your database administrator that you have
access to the database and tables that you need to integrate. Your Business Automation Workflow administrator
must have already defined the datasource using the admin console.

## About this task

The System Data toolkit includes SQL Integration services
to enable you to easily integrate with external databases.

The SQL Integration services support common database interactions,
including support for parameterized queries. These services can automatically
map query results directly into the relevant variable type. The SQL
Integration services enable you to develop implementations to:

- Read existing data from a database.
- Insert new data to a database.
- Call stored procedures in your database.

When passing data between Business Automation Workflow and a
connected database, the SQL Integration services enable you to specify
SQL data types such as integers, BLOBs, and CLOBs.

The SQL Integration services are Java-based integrations that
bind to a specific method in the teamworks.SQLConnector Java class.
Although you cannot alter the SQL Integration services, you can open
them in the Designer in IBM Process
Designer to
see the method implemented by each one and the available input and
output variables as outlined in the following procedure.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application in the Designer view.
3. Click the indicator next to the Toolkits category to see
a list of toolkit dependencies for the current process application.
4. Click the indicator next to the System Data toolkit to
see its contents.
5 Click the Implementation categoryand then double-click one of the listed SQL services.
    - The SQL Execute Statement service
    - The SQL Execute Statement (SQLResult) service
provides a wrapper for the SQL Execute Statement service and returns
the results in a fixed return type, SQLResult.
6. In the service diagram, click the Java Integration component
to select it.
7. Click the Definition option in the
properties to display the Java Class and method implemented by the
service.
8. Switch from the diagram view of the service by clicking
the Variables tab.
9. Click an Input or Output variable to see its details, such
as its type and default values (where applicable). To
use an SQL integration service you must specify the input and output
variables that are listed in the following table.
Table 1. Input
and output parameters for the SQL Execute Statement services

Name
Type
Description

sql
String
This input parameter provides the SQL statement.
For example, if the variable tw.local.sqlSelectSatatement contains
the SQL statement string SELECT name, place FROM GREETING,
enter the variable name tw.local.sqlSelectSatatement for
the sql parameter

parameters
List of SQLParameter
This input parameter describes the value, type, and mode information for each
'?' parameter that you use in your sql string. For each parameter, specify an SQLParameter object
with an SQLType, the value of the parameter, and a SQLParameterMode. SQLParameterMode can be
IN, OUT or INOUT as defined by the JDBC
specifications of java.sql.ParameterMetaData. For more information about supported types, see the
type property description of the SQLParameter object in  JavaScript API in processes and service flows.

maxRows
Integer
This input parameter limits the number of rows
that are returned.

returnType
String
This input parameter provides the name of the
business object data type that the results are returned in. If you
specify SQLResult the results are transformed automatically
into a list of SQLResult, In this case, you only
need to create one variable of type SQLResult and
mark it as a list variable.

dataSourceName
String
This input parameter is the JNDI name of the
data source that your Business Automation Workflow administrator
defined, for example "jdbc/greetdb".

results
ANY
This output parameter contains the results of
the query. The results object is of the type that you specified for returnType.