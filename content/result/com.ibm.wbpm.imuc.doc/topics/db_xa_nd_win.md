# Configuring XA transactions

## About this task

Failure to configure the XA transactions can result
in the following error when the server starts:javax.transaction.xa.XAException:
com.microsoft.sqlserver.jdbc.SQLServerException: Failed to create
the XA control connection. Error: "Could not find stored procedure
'master..xp\_sqljdbc\_xa\_init\_ex'."..

The
MS DTC service should be marked Automatic in Service Manager to make
sure that it is running when the SQL Server service is started.

## Procedure

1 To enable MS DTC for XA transactions, complete the following steps:
    1. Select Control Panel > Administrative Tools > Component Services.
    2. Select Distributed Transaction CoordinatorComponent Services > Computers > My Computer.
    3. Right-click Local DTC and then select
Properties.
    4. Click the Security tab on the Local DTC
Properties window.
    5. Select the Enable XA Transactions check box, and click
OK. This will restart the MS DTC service.
    6. Click OK again to close the Properties window, and then close
Component Services.
    7. Restart SQL Server to ensure that it syncs up with the MS DTC changes.
2 Configure the JDBC Distributed TransactionComponents:

1. Download the sqljdbc\_xa.dll file from the Microsoft site.
2. Copy the sqljdbc\_xa.dll file to the
Binn directory (for a default SQL Server install, the location is 
C:\Program Files\Microsoft SQL
Server\MSSQL12.MSSQLSERVER\MSSQL\Binn) of the SQL Server computer. Use
the sqljdbc\_xa.dll file in the x64 folder.
3. Run the xa\_install.sql database script on SQL Server. For example; from
the command prompt, run sqlcmd -i xa\_install.sql. This script installs the extended
stored procedures that are called by sqljdbc\_xa.dll. These extended stored
procedures implement distributed transaction and XA support for the Microsoft SQL Server JDBC
Driver. You will need to run this script as an administrator of the SQL Server instance. You can
ignore errors about unable to drop procedures that don't exist.
3 Follow these steps for configuring Windowsauthentication:

- Locate the sqljdbc\_auth.dll file in the Microsoft
JDBC driver package.
- Copy the sqljdbc\_auth.dll file to the
Binn directory (for a default SQL Server install, the location is
C:/Program Files/Microsoft SQL Server/MSSQL12.MSSQLSERVER/MSSQL/Binn) of the
SQL Server computer. Use the sqljdbc\_auth.dll file in the x64
folder.

## What to do next

1. From Start menu, click Microsoft SQL Server 2014 > Configuration Tools > SQL Server Configuration Manager.
2. Expand SQL Server Network Configuration > Protocols for MSSQLSERVER (where MSSQLSERVER corresponds to the instance name that you
defined when you installed SQL Server).
3. Locate TCP/IP.
4. Double click TCP/IP and enable it under the
Protocol tab.
5. Click the IP Addresses tab to enable the TCP port for each configured IP
address.

```
Lock request time out period exceeded.; nested exception is com.microsoft.sqlserver.jdbc.SQLServerException: 
  Lock request time out period exceeded.
```