# Message Logger mediation primitive properties

## Enabled enabled

Defines whether the message is mediated by the
Message Logger mediation primitive. By default the mediate action of the Message Logger mediation
primitive is enabled. You can suspend the mediate action by clearing the check box.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | true              |

## Root root

An XPath 1.0 expression representing the scope of the
message to be logged.

| Field detail   | Value and notes                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Valid values   | XPathNote: You can specify: /, /context, /body, /headers, or your own XPath expression. / refers to the complete SMO, /context refers to the context of the SMO, /body refers to the body section of the SMO, and /headers refers to the headers of the SMO. If you specify your own XPath expression, the part of the SMO you specify is processed. The message to be logged is converted to XML from the point specified by Root. |
| Default        | /body                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Transaction mode transactionMode

Defines whether to commit changes to the
database, in the flow's transaction or in a new transaction.

| Field detail   | Value and notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Valid values   | Same 0 If you specify Same, the message is logged in the flow's transaction. By default, the flow is executed under a local transaction although the mediation component can be configured to run under a global transaction. If a global transaction is specified and a failure occurs in the flow, the global transaction, including the log operation, is rolled back.  New 1 If you specify New, the message is logged in its own local transaction. In this case, if a failure occurs in the flow, the message logging is not rolled back.  Note: |
| Default        | Same                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## Logging type loggingType

Identifies whether to log the message to a
Database or using the custom logging functionality.

| Field detail   | Value and notes              |
|----------------|------------------------------|
| Required       | Yes                          |
| Valid values   | Database 0  Custom 1   Note: |
| Default        | Database                     |

## Data source name dataSourceJNDIName

The JNDI name of the datasource that
defines where the data will be logged.

| Field detail   | Value and notes                                                                                                           |
|----------------|---------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                       |
| Valid values   | StringNote:                                                                                                               |
| Default        | jdbc/mediation/messageLogFrom version 6.1.x onwards, the default jdbc/mediation/messageLog maps to the CommonDB database. |

## Handler handler

You can provide a Handler implementation class to
customize the behavior of the custom logger. You can log through more than one Handler
implementation class if you want. Optionally, you can provide Formatter implementation classes,
Filter implementation classes, or both.

| Field detail   | Value and notes                                             |
|----------------|-------------------------------------------------------------|
| Required       | Yes                                                         |
| Valid values   | StringNote:                                                 |
| Default        | com.ibm.ws.sibx.mediation.primitives.logger.WESBFileHandler |

## Formatter formatter

You can provide a Formatter implementation class
with a Handler implementation to customize the behavior of the custom logger. For more information,
see Java 2
SDK, Standard Edition Documentation.

| Field detail   | Value and notes                                           |
|----------------|-----------------------------------------------------------|
| Required       | Yes                                                       |
| Valid values   | StringNote:                                               |
| Default        | com.ibm.ws.sibx.mediation.primitives.logger.WESBFormatter |

## Filter filter

You can provide a Filter implementation class with a
Handler implementation class to customize the behavior of the custom logger. For more information,
see Java 2
SDK, Standard Edition Documentation.

| Field detail   | Value and notes                                        |
|----------------|--------------------------------------------------------|
| Required       | Yes                                                    |
| Valid values   | StringNote:                                            |
| Default        | com.ibm.ws.sibx.mediation.primitives.logger.WESBFilter |

## Literal literal

Identifies the exact content of what is logged by
the custom logging functionality. This is used in conjunction with the Formatter value.

| Field detail   | Value and notes                                           |
|----------------|-----------------------------------------------------------|
| Required       | Yes                                                       |
| Valid values   | StringNote: See the java.util.logging docs for specifics. |
| Default        | {0},{1},{2},{3},{4},{5}                                   |

## Level level

Identifies the level at which the message is logged by
the custom logging functionality. For more information, see Java 2 SDK, Standard Edition
Documentation.

| Field detail   | Value and notes                                                          |
|----------------|--------------------------------------------------------------------------|
| Required       | Yes                                                                      |
| Valid values   | Severe 0  Warning 1  Info 2  Config 3  Fine 4  Finer 5  Finest 6   Note: |
| Default        | Info                                                                     |

## Considerations

- If the Data source name is not valid, or the
data source cannot be obtained from JNDI, a runtime exception occurs.
- If the database cannot be found, or the database returns an error,
a runtime exception occurs.
- If you want to create your own database resources, the runtime
product provides data definition language (ddl) files that describe
the table schema. The Table.ddl files are stored at: install\_root/util/EsbLoggerMediation/database\_
type/Table.ddl. Where database\_ type refers
to the type of database. If you create your own database and want
to use the default JNDI name for your data source, you must remove
the default data source.
- If you want to create the table ESBLOG.MSGLOG on
an Oracle database, the ESBLOG  user must exist. In order to add the
ESBLOG user you must have SYSDBA privileges. When you install and
configure your runtime product, you can define the Common  database
as being an Oracle database and the installation process can create
the  table ESBLOG.MSGLOG in the CommonDB database.
The ESBLOG user must exist before you  try to create the table ESBLOG.MSGLOG.
- If the XPath expression is not found in the input message, an
entry is still logged in the database but the Message column
is empty.
- If more than one Message Logger mediation primitive is used in
a particular flow, the display name must be unique.
- There is no mediation primitive specifically designed to access
data logged to a database. However, you can access the database using
the Database Lookup mediation primitive, a Custom Mediation primitive,
a Java™ component or an external
application. If you write a custom SCA component you can access the
database using a Java Database
Connectivity (JDBC) call, your own Enterprise Java Beans (EJB) or the JDBCMediator. The JDBCMediator
is described under the section Using the Java Database Connectivity Mediator Service in
the WebSphere® Application
Server information center.

Consider the following when using the Message Logger mediation
primitive with custom logger:

- In any Formatter implementation class, a call to <LogRecord>.getParameters(),
will always return an Object array containing six elements. 
Table 1. Formatter implementation
class array content

Element
Object Type
Item
Description

0
String
Time Stamp
The UTC timestamp, indicating when the message
was logged to the database. 

1
String
Message ID
The message ID, from the SMO. 

2
String
Mediation Name
The name of the mediation primitive instance
that logged the message. 

3
String
Module Name
The name of the mediation module instance that
contains the Message Logger primitive. 

4
Data Object
Message
The SMO, or part of the SMO. 

5
String
version
The version of the logged SMO.

You should decide how much of this information you want
to log using a combination of the Literal property value and the Formatter
implementation.
- In the Filter implementation class, there is scope to perform
some complex filtering on which messages get logged, by performing
a <LogRecord>.getParameters() call and testing
the returned results.

## Sample XML code

```
<node name="MessageLogger1" type="MessageLogger">
  <property name="root" value="/context/failInfo"/>
  <inputTerminal/>
  <outputTerminal>
    <wire targetNode="MQHeaderSetter1"/>
  </outputTerminal>
  <failTerminal/>
</node>
```