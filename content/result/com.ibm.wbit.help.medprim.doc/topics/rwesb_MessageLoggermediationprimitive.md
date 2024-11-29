# Message Logger mediation primitive

## Introduction

You can use the Message Logger
mediation primitive to store messages in a relational database, or
in other storage mediums if you use the custom logging functionality.
The Message Logger mediation primitive logs messages to a relational
database using an IBM-defined database schema (table structure). It
can write to other storage mediums, such as flat files, through the
use of the custom logging facility.

The Message Logger mediation
primitive logs an XML transcoded copy of the service message object
(SMO). The default behavior is to log just the message payload but
the mediation primitive can be configured to log the complete SMO,
or a part of the SMO defined by an XPath expression. Along with the
message contents the  mediation primitive also logs a timestamp, the
message identifier, the primitive instance name, the mediation module
instance name and the SMO version number.

If you are using a
relational database, the message that is logged is stored in a database
column called: Message. The other data that is logged
is stored in columns with an appropriate heading, as documented later
in this topic.

The Message
Logger mediation primitive has one input terminal (in),
one output terminal (out) and one fail terminal
(fail). The in terminal
is wired to accept a message and the other terminals are wired to
propagate a message. The input message triggers logging to a database,
or though a custom logger; and if the logging is successful, the out terminal
propagates the original message. If an exception occurs during the
processing of the input message, the fail terminal
propagates the original message, together with any exception information.

The
custom logging implementation is based on the java.util.logging package.

## Details

- Logs to the CommonDB database, using the table MSGLOG.
This table is placed under a schema qualifier that is determined by
your database product. You can specify the default schema name during
the profile creation, when you configure the database. You must use
the correct default schema name for your type of database. Table 1 describes
the structure of the Message Logger database table. For further information,
see the runtime documentation.
- Logs to the CommonDB database identified by the JNDI location jdbc/mediation/messageLog,
and the run time environment creates a data source at jdbc/mediation/messageLog but
points this data source to the CommonDB database. The CommonDB database
has a JNDI location of: jdbc/WPSDB. The jdbc/mediation/messageLog data
source is scoped at the same level as the jdbc/WPSDB data
source.

| Database type   | Default schema   | Additional information                                                                                                                |
|-----------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| DB2 Universal   | <dbUserId>       |                                                                                                                                       |
| DB2 for z/OS    | dbSchemaName     | The database alias name, which is generally the same as dbUserId.                                                                     |
| Oracle          | <dbUserId>       |                                                                                                                                       |
| SQL Server      | dbo              | dbo is the default schema name. DatabaseMetaData::getUserName() returns dbo for embedded drivers, and dbUserId for Microsoft drivers. |

In summary, with version 6.1.2, and later, the default
is for the Message Logger mediation primitive to use the CommonDB
database and for the runtime environment to map the data source at jdbc/mediation/messageLog to
the CommonDB database.

## Migration (only applicable if using a relational database)

- On distributed platforms, the default installation of the runtime
product created a stand-alone application server, and a local Derby
database and datasource. The local Derby database was called EsbLogMedDB.
The Message Logger mediation primitive was configured to use this
Derby database, by default.
- On z/OS®, the installation
of the runtime product created an application server, and a sample
database and datasource. The Message Logger mediation primitive could
be configured to use either a Derby or a DB2® database.

- Manually move old data into the CommonDB database.
- Continue using the previous database. If you want to use the previous location you must manually
configure the required data source.

- Continue storing message information in the database identified by their
jdbc/mediation/messageLog data source.
- Start storing message information in the database identified by their new
jdbc/mediation/messageLog data source.

## Usage

You can use the Message Logger mediation
primitive to store messages that you process later. The logged messages
can be used for various purposes. For example, you could use the logged
messages for data mining, message replay or for auditing.

Because
the data is logged as XML it can be processed by any XML-aware application.
Many databases, including DB2,
provide built-in capabilities to handle XML contained in a database
column. You can also use XML processing code to manipulate the XML
in your Formatter implementation class.

- One database, which can be either the CommonDB database or another database.
- Multiple schemas in one database, including the CommonDB database. Multiple schemas can be
useful for z/OS, because there can be only one
physical database throughout the z/OS system. Multiple schemas allow you
to compartmentalize data held on one database. For example, you might have test data and production
data on the same database, but under different schemas.
- Multiple databases. Two or more Message Logger mediation primitives can log to differentdatabases. For example, you might want to log to a DB2database and an Oracle database.
    - Because there can be only one physical database throughout a z/OS system, additional databases must
exist on other systems. You could have other databases on any of the following systems: other z/OS systems,
distributed systems.

Each Message Logger mediation primitive must have a Handler implementation class specified. If
you have multiple Message Logger mediation primitives they can either use the same Handler
implementation class or any number of appropriate Handler implementation classes. You can,
optionally, provide Formatter implementation classes, Filter implementation classes, or both.

By default, the default Handler implementation class logs every message to a file stored in the
system temporary directory as defined by the java.io.tmpdir system property, this is typically /tmp
or /var/tmp on a Unix system and C:\Documents and Settings\<user>\Local Settings\Temp on a
windows system. The file will be called MessageLog.log.

- {0} would then be substituted with the Time Stamp value - logMessageParameters[0]
- {1} would then be substituted with the Message ID value - logMessageParameters[1]
- {2} would then be substituted with the Mediation Name value - logMessageParameters[2]
- {3} would then be substituted with the Module Name value - logMessageParameters[3]
- {4} would then be substituted with the Message value - logMessageParameters[4]
- {5} would then be substituted with the version value - logMessageParameters[5]

```
29/04/08 15:11,9A85B1D2-0119-4000-E000-13E4091443BC,MessageLogger1,CustomLogging,abc,6
```

- Handler property : com.ibm.ws.sibx.mediation.primitives.logger.WESBFileHandler
- Formatter property : com.ibm.ws.sibx.mediation.primitives.logger.WESBFormatter
- Filter property : com.ibm.ws.sibx.mediation.primitives.logger.WESBFilter

## With a relational database

- One database, which can be either the CommonDB database or another
database.
- Multiple schemas in one database, including the CommonDB database.
Multiple schemas can be useful for z/OS,
because there can be only one physical database throughout the z/OS
system. Multiple schemas allow you to compartmentalize data held on
one database. For example, you might have test data and production
data on the same database, but under different schemas.
- Multiple databases. Two or more Message Logger mediation primitivescan log to different databases. For example, you might want to logto a DB2 database and an Oracledatabase.
    - Because there can be only one physical database throughout a z/OS
system, additional databases must exist on other systems. You could
have other databases on any of the following systems: other z/OS systems, distributed
systems.

## With custom logging

Each Message Logger
mediation primitive must have a Handler implementation class specified.
If you have multiple Message Logger mediation primitives they can
either use the same Handler implementation class or any number of
appropriate Handler implementation classes. You can, optionally, provide
Formatter implementation classes, Filter implementation classes, or
both.

By default, the default Handler implementation class
logs every message to a file stored in the system temporary directory
as defined by the java.io.tmpdir system property, this is typically
 /tmp or /var/tmp on a Unix system and C:\Documents and Settings\<user>\Local
Settings\Temp on a windows system. The file will be called MessageLog.log.

- {0} would then be substituted with the Time Stamp value - logMessageParameters[0]
- {1} would then be substituted with the Message ID value - logMessageParameters[1]
- {2} would then be substituted with the Mediation Name value -
logMessageParameters[2]
- {3} would then be substituted with the Module Name value - logMessageParameters[3]
- {4} would then be substituted with the Message value - logMessageParameters[4]
- {5} would then be substituted with the version value - logMessageParameters[5]

```
29/04/08 15:11,9A85B1D2-0119-4000-E000-13E4091443BC,MessageLogger1,CustomLogging,abc,6
```

- Handler property : com.ibm.ws.sibx.mediation.primitives.logger.WESBFileHandler
- Formatter property : com.ibm.ws.sibx.mediation.primitives.logger.WESBFormatter
- Filter property : com.ibm.ws.sibx.mediation.primitives.logger.WESBFilter

- Message Logger mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)