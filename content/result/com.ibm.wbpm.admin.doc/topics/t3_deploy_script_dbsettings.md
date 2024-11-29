<!-- image -->

# Configuring process application data source and set reference
settings

## About this task

- Data sources to run SQL statements during process deployment
- Data sources to run SQL statements during the startup of a process
instance
- Data sources to run SQL snippet activities

The data source required to run an SQL snippet activity
is defined in a BPEL variable of type tDataSource. The database schema
and table names that are required by an SQL snippet activity are defined
in BPEL variables of type tSetReference. You can configure the initial
values of both of these variables.

You can use the wsadmin tool
to specify the data sources.

## Procedure

1. Deploy the process application interactively using the
wsadmin tool.
2. Step through the tasks until you come to the tasks for
updating data sources and set references. Configure
these settings for your environment. The following example shows the
settings that you can change for each of these tasks.
3. Save your changes.

## Example: Updating data sources and set references,
using the wsadmin tool

In the Updating data sources task, you can change data source values for initial variable values
and statements that are used during deployment of the process or when
the process starts. In the Updating set references task, you can configure the settings related to the database schema
and the table names.

```
Task [24]: Updating data sources

//Change data source values for initial variable values at process start

Process name:  Test 
// Name of the process template					
Process start or installation time:  Process start	
// Indicates whether the specified value is evaluated 
//at process startup or process installation
Statement or variable:  Variable	
// Indicates that a data source variable is to be changed		
Data source name:  MyDataSource 
// Name of the variable			
JNDI name:[jdbc/sample]:jdbc/newName	
// Sets the JNDI name to jdbc/newName
```

```
Task [25]: Updating set references

// Change set reference values that are used as initial values for BPEL variables

Process name:  Test 
// Name of the process template					
Variable:  SetRef	
// The BPEL variable name
JNDI name:[jdbc/sample]:jdbc/newName	
// Sets the JNDI name of the data source of the set reference to jdbc/newName
Schema name: [IISAMPLE]
// The name of the database schema
Schema prefix: []:
// The schema name prefix. 
// This setting applies only if the schema name is generated.
Table name: [SETREFTAB]: NEWTABLE
// Sets the name of the database table to NEWTABLE
Table prefix: []:
// The table name prefix.
// This setting applies only if the prefix name is generated.
```