# Configuring JDBC drivers

IBM® Business Automation Workflow includes Java database
connectivity (JDBC) drivers for DB2 databases. The versions of the DB2 JDBC drivers that are
included are determined by the levels of the corresponding database products that were supported by
the particular release of Business Automation Workflow. You should
update the JDBC drivers whenever another level of a database product is released, to avoid
unexpected errors from failures that originate from the drivers. If you are using Oracle or SQL
Server databases, you must configure your own JDBC drivers.

For the product data sources, Business Automation Workflow
requires type 4 JDBC drivers provided by your database vendor for your specific database version. It
is a good idea to use a custom path for your JDBC drivers, even if you are using DB2.

## Procedure

To configure or update your JDBC drivers, complete the following steps:

1. Determine the version of the JDBC drivers that are available for a specific level of your
database product. 
You can determine the version of JDBC drivers that are available for a specific level of DB2
by checking DB2 JDBC driver versions and downloads. Also see Advanced database
support for IBM Business Automation Workflow on distributed platforms.
2. If you already have JDBC drivers installed, determine the current version of your JDBC drivers
in Business Automation Workflow by running the following command
(where database\_product is one of DB2, Oracle, or SQL Server):
install\_root/my\_jdbc\_directory/database\_productFor
example
(DB2):cd /opt/IBM/BPM/jdbcdrivers/DB2
/opt/IBM/BPM/java/bin/java -cp db2jcc4.jar com.ibm.db2.jcc.DB2Jcc -versioncd C:\IBM\BPM\jdbcdrivers\DB2
C:\IBM\BPM\java\bin\java -cp db2jcc4.jar com.ibm.db2.jcc.DB2Jcc -versionFor
example
(Oracle):
cd /opt/IBM/BPM/myOraclejdbc/
/opt/IBM/BPM/java/bin/java -jar ojdbc10.jar
3 Stop your environment by completing the following substeps:
    1. Stop the clusters.
    2. Stop all node agents in your environment.
    3. Stop the deployment manager.
4 In the Business Automation Workflow installation root on theBusiness Automation Workflow deployment manager and every managednode machine, create a custom directory for your JDBC drivers and copy the required JDBC driversinto it. For example, you could create the following custom directory for your DB2 JDBC drivers:install\_root /mydb2jdbc The databaseproducts and corresponding JDBC drivers are shown in the following table: Database product JDBC driver DB2 DB2 for z/OS Oracle SQL Server Business Automation Workflow 24.x and laterreleases support the following JDBC drivers: PostgreSQL

```
install\_root/mydb2jdbc
```

The database
products and corresponding JDBC drivers are shown in the following table:

| Database product   | JDBC driver                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DB2                | db2jcc4.jar db2jcc\_license\_cisuz.jar db2jcc\_license\_cu.jar                                                                                                                                                                                                                                                                                                                                                                                                      |
| DB2 for z/OS       | db2jcc4.jar db2jcc\_license\_cisuz.jar db2jcc\_license\_cu.jar                                                                                                                                                                                                                                                                                                                                                                                                      |
| Oracle             | ojdbc8.jar or ojdbc10.jar                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| SQL Server         | Business Automation Workflow 24.x and later releases support the following JDBC drivers:  mssql-jdbc-11.2.0.jre8.jar mssql-jdbc-10.2.0.jre8.jar mssql-jdbc-9.4.1.jre8.jar mssql-jdbc-9.2.1.jre8.jar mssql-jdbc-8.4.1.jre8.jar mssql-jdbc-8.2.2.jre8.jar mssql-jdbc-7.0.0.jre8.jar sqljdbc42.jar mssql-jdbc-6.4.0.jre8.jar mssql-jdbc-6.2.2.jre8.jar mssql-jdbc-12.2.0.jre8.jar mssql-jdbc-12.4.1.jre8.jar mssql-jdbc-12.6.1.jre8.jar mssql-jdbc-12.4.2.jre8.jar |
| PostgreSQL         | postgresql-42.7.3.jar postgresql-42.6.2.jar postgresql-42.5.6.jar postgresql-42.5.4.jar postgresql-42.4.5.jar  postgresql-42.2.26.jar postgresql-42.2.28.jar postgresql-42.2.29.jar postgresql-42.3.9.jar postgresql-42.3.10.jar                                                                                                                                                                                                                                |

5 If you are using Microsoft SQL Server, complete the followingsubsteps to accommodate JDBC distributed transaction components andWindows authentication:

1. Copy the sqljdbc\_xa.dll file from
the Microsoft JDBC driver package that you downloaded to the Binn directory
of the SQL Server computer. For a default SQL Server install, the
location of the Binn directory is C:/Program
Files/Microsoft SQL Server/MSSQL10\_50.MSSQLSERVER/MSSQL/Binn.
Use the sqljdbc\_xa.dll file in the x64 folder.
2. Run the xa\_install.sql database
script on SQL Server. For example; from the command prompt, run sqlcmd
-i xa\_install.sql. This script installs the extended stored
procedures that are called by sqljdbc\_xa.dll.
These extended stored procedures implement distributed transaction
and XA support for the Microsoft SQL Server JDBC Driver. You will
need to run this script as an administrator of the SQL Server instance.
You can ignore errors about unable to drop procedures that don't exist.
3. If you configured Windows authentication, copy the sqljdbc\_auth.dll file
from the Microsoft JDBC driver package that you downloaded to the Binn directory
of the SQL Server computer. For a default SQL Server install, the
location of the Binn directory is C:/Program
Files/Microsoft SQL Server/MSSQL10\_50.MSSQLSERVER/MSSQL/Binn.
Use the sqljdbc\_auth.dll file in the x64 folder.
6 Change the JDBC driver variables to point to your custom JDBC driver directory. In a networkdeployment environment, run this command to update the deployment manager and run it again for eachmanaged node. In a stand-alone environment, update the path on the server. BPMConfig -update -profile profile\_name -node node\_name -jdbcDriverPath jdbc\_driver\_path where: For example, the following commands update the JDBC driver path for the deployment managerand two managednodes.BPMConfig -update -profile Dmgr01 -node Dmgr01 -jdbcDriverPath ${WAS\_INSTALL\_ROOT} \myOraclejdbc\BPMConfig -update -profile Dmgr01 -node Node01 -jdbcDriverPath ${WAS\_INSTALL\_ROOT} \myOraclejdbc\BPMConfig -update -profile Dmgr01 -node Node02 -jdbcDriverPath /opt/myOraclejdbc/

```
BPMConfig -update -profile profile\_name -node node\_name -jdbcDriverPath jdbc\_driver\_path
```

- profile\_name is the name of the deployment manager
profile
- node\_name is the name of the deployment manager node or
managed node that you are setting the JDBC driver path for
- jdbc\_driver\_path is the directory containing the JDBC
drivers

```
BPMConfig -update -profile Dmgr01 -node Dmgr01 -jdbcDriverPath ${WAS\_INSTALL\_ROOT}\myOraclejdbc\
BPMConfig -update -profile Dmgr01 -node Node01 -jdbcDriverPath ${WAS\_INSTALL\_ROOT}\myOraclejdbc\
BPMConfig -update -profile Dmgr01 -node Node02 -jdbcDriverPath /opt/myOraclejdbc/
```

7 Restart your environment by completing the following substeps:

1. Start the deployment manager.
2. Start the node agent.
3. Start the clusters.
8. Verify that the updated JDBC versions have been applied.
For example, to verify that the JDBC version has been updated for
DB2, locate the string DSRA8203I in the SystemOut.log file,
as shown in the following output:  [3/17/14 11:57:26:122 BRT] 00000000 InternalGener I   DSRA8203I: Database product name : DB2/AIX64
[3/17/14 11:57:26:123 BRT] 00000000 InternalGener I   DSRA8204I: Database product version : SQL09075
[3/17/14 11:57:26:124 BRT] 00000000 InternalGener I   DSRA8205I: JDBC driver name  : IBM Data Server Driver for JDBC and SQLJ
[3/17/14 11:57:26:124 BRT] 00000000 InternalGener I   DSRA8206I: JDBC driver version  : 4.13.80
[3/17/14 11:57:26:124 BRT] 00000000 InternalGener I   DSRA8218I: JDBC driver specification level  : 4.0