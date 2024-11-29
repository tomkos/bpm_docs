# Preparing an MS SQL database for the User Management Services datasource

## Procedure

1. Create your MS SQL database, for example by issuing the command:
create database umsdb For more information, refer to your database
documentation.
2. Make a note of your values for the following configuration parameters that you will need later
to add to the datasource\_configuration section of the custom resource:
datasource\_configuration:
    dc\_ums\_datasource: # credentials are read from ums\_configuration.admin\_secret\_name
    # oauth database config
      dc\_ums\_oauth\_type: sqlserver
      dc\_ums\_oauth\_host: host\_name
      dc\_ums\_oauth\_port: 1433
      dc\_ums\_oauth\_name: UMSDB
      dc\_ums\_oauth\_driverfiles: mssql-jdbc-8.2.2.jre8.jar
      dc\_ums\_oauth\_ssl: true
    # teamserver database config
      dc\_ums\_teamserver\_type: sqlserver
      dc\_ums\_teamserver\_host: host\_name
      dc\_ums\_teamserver\_port: 1433
      dc\_ums\_teamserver\_name: UMSDB
      dc\_ums\_teamserver\_driverfiles: mssql-jdbc-8.2.2.jre8.jar
      dc\_ums\_teamserver\_ssl: true
Where
host\_name is the host name of the database server, 1433 is the
default port, and UMSDB is the name of the database.