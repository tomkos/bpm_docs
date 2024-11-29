# Preparing a Db2® database for the User Management Services

## Procedure

1. Create the UMS SSO option database.
For example, you can create a database named UMSDB by running the following
command:
db2 create database UMSDB automatic storage yes using codeset UTF-8 territory US pagesize 32768
2. Optional: 
Create a separate database for the UMS Teams option if you do not want it to share the UMS SSO
oauth database. For example, named UMSTSDB.
3. Optional: 
Create one or more failover servers for the UMS database(s).
To cover the possibility that the primary server is unavailable during the initial connection
attempt, you can configure a list of failover servers, as described in Configuring client reroute for applications that use DB2® databases.
4 Make a note of the datasource information that you will need later to add to thedatasource\_configuration section of the custom resource: datasource\_configuration: dc\_ums\_datasource: # credentials are read from ums\_configuration.admin\_secret\_name # oauth database config dc\_ums\_oauth\_type: db2 dc\_ums\_oauth\_host: host\_name dc\_ums\_oauth\_port: 50000 dc\_ums\_oauth\_name: UMSDB dc\_ums\_oauth\_schema: OAuth\_DB\_Schema dc\_ums\_oauth\_driverfiles: db2jcc4.jar, db2jcc\_license\_cu.jar dc\_ums\_oauth\_alternate\_hosts: "server1.db2.example.com, server2.db2.example.com" dc\_ums\_oauth\_alternate\_ports: "50443, 51443" dc\_ums\_oauth\_ssl: true # teamserver database config dc\_ums\_teamserver\_type: db2 dc\_ums\_teamserver\_host: host\_name dc\_ums\_teamserver\_port: 50000 dc\_ums\_teamserver\_name: UMSTSDB dc\_ums\_teamserver\_driverfiles: db2jcc4.jar, db2jcc\_license\_cu.jar dc\_ums\_teamserver\_alternate\_hosts: "server1.db2.example.com, server2.db2.example.com" dc\_ums\_teamserver\_alternate\_ports: "50443, 51443" dc\_ums\_teamserver\_ssl: true Important: If you do not have a separate teams database, UMSTSDB, specify identical values for thedc\_ums\_teamserver\_ parameters as for the dc\_ums\_oauth\_ ones. If you have multiple failover servers, for example, You will specify them as comma-separated lists, forexample: dc\_ums\_oauth\_alternate\_hosts: "server1.db2.example.com, server2.db2.example.com" dc\_ums\_oauth\_alternate\_ports: "50443, 51443" ... dc\_ums\_teamserver\_alternate\_hosts: "server1.db2.example.com, server2.db2.example.com" dc\_ums\_teamserver\_alternate\_ports: "50443, 51443"

```
datasource\_configuration:
  dc\_ums\_datasource: # credentials are read from ums\_configuration.admin\_secret\_name
    # oauth database config
    dc\_ums\_oauth\_type: db2
    dc\_ums\_oauth\_host: host\_name
    dc\_ums\_oauth\_port: 50000
    dc\_ums\_oauth\_name: UMSDB
    dc\_ums\_oauth\_schema: OAuth\_DB\_Schema
    dc\_ums\_oauth\_driverfiles: db2jcc4.jar, db2jcc\_license\_cu.jar
    dc\_ums\_oauth\_alternate\_hosts: "server1.db2.example.com, server2.db2.example.com"
    dc\_ums\_oauth\_alternate\_ports: "50443, 51443"
    dc\_ums\_oauth\_ssl: true
    # teamserver database config
    dc\_ums\_teamserver\_type: db2
    dc\_ums\_teamserver\_host: host\_name
    dc\_ums\_teamserver\_port: 50000
    dc\_ums\_teamserver\_name: UMSTSDB
    dc\_ums\_teamserver\_driverfiles: db2jcc4.jar, db2jcc\_license\_cu.jar
    dc\_ums\_teamserver\_alternate\_hosts: "server1.db2.example.com, server2.db2.example.com"
    dc\_ums\_teamserver\_alternate\_ports: "50443, 51443"
    dc\_ums\_teamserver\_ssl: true
```

If you do not have a separate teams database, UMSTSDB, specify identical values for the
dc\_ums\_teamserver\_ parameters as for the dc\_ums\_oauth\_ ones.

    - server1.db2.company.com on port 50443
    - server2.db2.company.com on port 51443

```
dc\_ums\_oauth\_alternate\_hosts: "server1.db2.example.com, server2.db2.example.com"
    dc\_ums\_oauth\_alternate\_ports: "50443, 51443"
    ...
    dc\_ums\_teamserver\_alternate\_hosts: "server1.db2.example.com, server2.db2.example.com"
    dc\_ums\_teamserver\_alternate\_ports: "50443, 51443"
```