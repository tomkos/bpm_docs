# Preparing an Oracle database for the User Management Services datasource

## Procedure

1. Create a user, for example, C##UMS, to represent the schema and grant the user
privileges to create resources:
sqlplus sys AS sysdba;

CREATE USER C##UMS IDENTIFIED BY secret\_password;

GRANT CREATE TABLE TO C##UMS;
GRANT CREATE SESSION TO C##UMS;
GRANT CREATE SEQUENCE TO C##UMS;
GRANT UNLIMITED TABLESPACE TO C##UMS;Where
secret\_password is the password that you must specify with the user in the
ibm-baw-ums-secret secret.
2 Make a note of the following datasource information: Later, you will need update the datasource\_configuration section of thecustomresource: datasource\_configuration: dc\_ums\_datasource: # credentials are read from ums\_configuration.admin\_secret\_name # oauth database config dc\_ums\_oauth\_type: oracle dc\_ums\_oauth\_host: host\_name dc\_ums\_oauth\_port: 1521 dc\_ums\_oauth\_name: SID dc\_ums\_oauth\_schema: DB\_user\_ID dc\_ums\_oauth\_oracle\_service\_name: DB\_service\_name dc\_ums\_oauth\_ssl: false dc\_ums\_oauth\_driverfiles: ojdbc8.jar, orai18n.jar # teamserver database config dc\_ums\_teamserver\_type: oracle dc\_ums\_teamserver\_host: host\_name dc\_ums\_teamserver\_port: 1521 dc\_ums\_teamserver\_name: SID dc\_ums\_teamserver\_oracle\_service\_name: DB\_service\_name dc\_ums\_teamserver\_ssl: false dc\_ums\_teamserver\_driverfiles: ojdbc8.jar, orai18n.jar Important: For Oracle RAC, specify the host name of the SCAN listener as the value of thedc\_ums\_oauth\_host and dc\_ums\_teamserver\_host parameters.
    - host\_name is the name of your database host
    - SID is the SID of your database, for example orcl. Tip: To determine the SID of your database, on the database host
perform:SELECT sys\_context('userenv','instance\_name') FROM dual;
The response
provides the SID, for
example:SYS\_CONTEXT('USERENV','INSTANCE\_NAME')
--------------------------------------------------------------------------------
orcl
    - DB\_user\_ID is your database user ID, for example
C##UMS
    - If you connect to an Oracle Real Application Clusters (RAC) environment using Single Client
Access Name (SCAN), note DB\_service\_name, which is the database
service name for the datasource, for example ORCL.Tip: To determine the
service name, on the SCAN host perform:select name from v$database;The
response provides the service name, which is case-sensitive, for
example:NAME
---------
ORCL

```
datasource\_configuration:
    dc\_ums\_datasource: # credentials are read from ums\_configuration.admin\_secret\_name
    # oauth database config
      dc\_ums\_oauth\_type: oracle
      dc\_ums\_oauth\_host: host\_name
      dc\_ums\_oauth\_port: 1521
      dc\_ums\_oauth\_name: SID
      dc\_ums\_oauth\_schema: DB\_user\_ID
      dc\_ums\_oauth\_oracle\_service\_name: DB\_service\_name
      dc\_ums\_oauth\_ssl: false
      dc\_ums\_oauth\_driverfiles: ojdbc8.jar, orai18n.jar
    # teamserver database config
      dc\_ums\_teamserver\_type: oracle
      dc\_ums\_teamserver\_host: host\_name
      dc\_ums\_teamserver\_port: 1521
      dc\_ums\_teamserver\_name: SID
      dc\_ums\_teamserver\_oracle\_service\_name: DB\_service\_name
      dc\_ums\_teamserver\_ssl: false
      dc\_ums\_teamserver\_driverfiles: ojdbc8.jar, orai18n.jar
```