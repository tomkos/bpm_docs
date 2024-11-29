# Planning your database configuration

For information about database tuning, see Chapter 5: Database configuration,
tuning, and best practices in IBM Business Process Manager V8.5 Performance Tuning and Best Practices.

For IBM Business Automation Workflow, separate databases
are required for Process, Performance Data Warehouse, and Common database
components. Note that there is no Common database for PostgreSQL.

In IBM Business Automation Workflow
24.x, the Common
database consists of two parts: one part is cell-scoped and used for the entire cell; the other part
is scoped to the deployment environment and must be configured for each deployment environment.

The Process and Performance Data Warehouse components do not
support case-sensitive databases. These databases must not be case sensitive.

- For Microsoft SQL
Server databases, components other than
Process or Performance Data Warehouse require that their databases
be case sensitive.
- For Oracle databases, the Process, Performance Data Warehouse, and Common database components must use a
separate schema or user. They can use the same instance.

- A traditional architecture database
- A multitenant architecture with pluggable
databases

For access to the database schemas, plan to create technical users (systems users) because these
users may not be changed after the deployment environment has been created.

When you configure databases, the system default table spaces are used. However, if you want to
use scripts that create custom table spaces for Business Process Choreographer, the Business Space
components with DB2® and Oracle, and for the Messaging component with Db2 for z/OS®, see the usetablespaces property
as described in the Database and cell properties section of  Configuration properties for the BPMConfig command.

- run BPMConfig -create -sqlfiles properties\_file\_name -outputDir output\_directory
- run BPMConfig -create -de properties\_file\_name when bpm.de.deferSchemaCreation is
set to true.

## Specifying the maximum number of concurrently active databases on a Db2 database server

The maximum number of databases that can be concurrently active on a Db2 database server is specified by the Db2
numdb parameter. If your IBM Business Automation Workflow installation has four Advanced deployment
environments, the default numdb value of 8 is not
sufficient and must be increased to at least 13 (4*3 +1).

```
db2 get database manager configuration
db2 update dbm cfg using numdb 13
db2stop
db2start
```

## Recommendation for LOCKLIST and MAXLOCKS Db2 database configuration parameters

If the Db2 self-tuning memory feature is
enabled, which is the default setting for Db2,
set the LOCKLIST and MAXLOCKS database configuration parameters to AUTOMATIC. These parameters apply
to Linux, Unix, and Windows systems.

## Requirements for Db2 pureScale

## Supported database types and JDBC providers

Your choice of a database depends on your operating system and on the features that you will use
with IBM Business Automation Workflow.

| Database type   | JDBC provider                                                                                                                                                                                                                                                                                                                                  |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Db2             | Db2 Data Server JDBC Provider (XA)                                                                                                                                                                                                                                                                                                             |
| Db2 for z/OS    | DB2 Universal JDBC Provider (XA) DB2 Universal JDBC Provider, to use the connection pool for Db2 for z/OS                                                                                                                                                                                                                                      |
| Oracle          | Oracle JDBC Provider                                                                                                                                                                                                                                                                                                                           |
| SQL Server      | Microsoft SQL Server JDBC Provider                                                                                                                                                                                                                                                                                                             |
| PostgreSQL      | PostgreSQL  JDBC Provider. Supported versions include:  postgresql-42.7.3.jar postgresql-42.6.2.jar postgresql-42.5.6.jar postgresql-42.5.4.jar postgresql-42.4.5.jar  postgresql-42.2.26.jar postgresql-42.2.28.jar postgresql-42.2.29.jar postgresql-42.3.9.jar postgresql-42.3.10.jar mssql-jdbc-12.6.1.jre8.jar mssql-jdbc-12.4.2.jre8.jar |

## Supported JDBC providers

For the product data sources, IBM Business Automation Workflow
requires type 4 JDBC drivers provided by your database vendor for your particular database version.

For Db2, the driver is included with the
product installation files. It is located in
install\_root/jdbcdrivers/DB2, where
install\_root is the installation location of IBM Business Automation Workflow. The JDBC driver provided by IBM Business Automation Workflow might not be the latest JDBC driver level
delivered with your database product. If a later version is available, update to that driver.

For instructions for adding or updating JDBC drivers for your database product, see Configuring JDBC drivers.

## Db2 for z/OS considerations

- RRULOCK=YES
- SKIPUNCI=YES
- NUMLKUS
- NUMLKTS
- LOBVALS
- LOBVALA

- RELEASE(COMMIT)

- Planning the number of databases

To edit the BPMConfig properties file as required, you must know the number of databases that must be set up for a shared or an unshared database environment, for either a new installation or a migration from IBM Business Process Manager. The number of databases can be adjusted based on the configuration of your deployment environment.
- Database time zone and character set considerations

You should not change the time zone of the database server that you use for IBM Business Automation Workflow. The national character set required for Business Automation Workflow is different from the Oracle default value.
- Database privileges

Set database privileges to determine the authority that you must have to create or access your data store tables for each supported database management system.
- Configuring the BPM document store for DB2 on z/OS

IBM Business Automation Workflow V8.5.6 or higher supports the BPM document store for DB2 on z/OS. The BPM document store is a CMIS-enabled document repository that is used to store BPM documents in Business Automation Workflow. This enablement means that it supports the Content Management Interoperability Services (CMIS) standard for interoperability in Enterprise Content Management (ECM) systems. This configuration includes support for the BPM content store, another CMIS-enabled embedded document repository that is used for case management applications. It is only available in Business Automation Workflow with the Basic Case Management feature installed.

## Related tasks

- Configuring JDBC drivers