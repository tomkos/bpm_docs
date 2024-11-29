# Sample case configuration response files for the BPMConfig command

You can use a sample response file to collect the case management parameters and
configure the case data sources for the upgrade path, using the BPMConfig -update -profile
profile\_name -de DE\_name -caseConfigure command. The
following sample files for Db2, Oracle, and SQL Server are provided as a starting point.

## Sample Db2 response file

```
#Case Management database configuration properties.
#Tue Oct 30 04:38:41 EDT 2018
# IBM Content Navigator (ICN) data source information
# ICN database name
ContentNavigator.datasource.name=CPEDB
# ICN database host
ContentNavigator.datasource.host=mydatabasehost
# ICN database port
ContentNavigator.datasource.port=50000
# ICN database schema
ContentNavigator.datasource.schema=ICNSA
# ICN database data table space, Note: The table space name must be uppercase.
ContentNavigator.datasource.tablespace.data=WFICNTS
# The connection user of ICN database
# To use an existing database authentication alias, uncomment ContentNavigator.datasource.authentication.alias and specify your alias
ContentNavigator.datasource.authentication.alias=BPM\_DB\_ALIAS
ContentNavigator.datasource.authentication.user=db2admin
# The connection password of ICN database
# The password can be plain text or base64 encoded
ContentNavigator.datasource.authentication.password={xor}Pj08Ozo5OA\=\=

# Design Object Store (DOS) data source information
# DOS database name
DesignObjectStore.datasource.name=CPEDB
# DOS database host
DesignObjectStore.datasource.host=mydatabasehost
# DOS database port
DesignObjectStore.datasource.port=50000
# DOS database schema
DesignObjectStore.datasource.schema=DOSSA
# DOS database directory
# datasource.db.dir is a directory on the DB server that should be the same value for the 
ContentNavigator, DesignObjectStore, and TargetObjectStore database settings. It is used when generating the database creation 
scripts to supply the root directory where various database artifacts will be generated. The directory must exist on the database 
server before the database creation scripts run.
DesignObjectStore.datasource.db.dir=C:\\IBM
# DOS database data table space, Note: The table space name must be uppercase.
DesignObjectStore.datasource.tablespace.data=DOSDATATS
# DOS database index table space, Note: The table space name must be uppercase.
DesignObjectStore.datasource.tablespace.index=DOSIDXTS
# DOS database large object table space, Note: The table space name must be uppercase.
DesignObjectStore.datasource.tablespace.largeobject=DOSLOBTS
# To use an existing database authentication alias, uncomment DesignObjectStore.datasource.authentication.alias and specify your alias
#DesignObjectStore.datasource.authentication.alias=BPM\_DB\_ALIAS
# The connection user of DOS database
DesignObjectStore.datasource.authentication.user=db2admin
# The connection password of DOS database
# The password can be plain text or base64 encoded
DesignObjectStore.datasource.authentication.password={xor}Pj08Ozo5OA\=\=

# Target Object Store (TOS) data source information
# TOS database name
TargetObjectStore.datasource.name=CPEDB
# TOS database host
TargetObjectStore.datasource.host=mydatabasehost
# TOS database port
TargetObjectStore.datasource.port=50000
# TOS database schema
TargetObjectStore.datasource.schema=TOSSA
# TOS database directory
# datasource.db.dir is a directory on the DB server that should be the same value for the 
ContentNavigator, DesignObjectStore, and TargetObjectStore database settings. It is used when generating the database creation 
scripts to supply the root directory where various database artifacts will be generated. The directory must exist on the database 
server before the database creation scripts run.
TargetObjectStore.datasource.db.dir=C:\\IBM
# TOS database data table space, Note: The table space name must be uppercase.
TargetObjectStore.datasource.tablespace.data=TOSDATATS
# TOS database index table space, Note: The table space name must be uppercase.
TargetObjectStore.datasource.tablespace.index=TOSIDXTS
# TOS database large object table space, Note: The table space name must be uppercase.
TargetObjectStore.datasource.tablespace.largeobject=TOSLOBTS
# The connection user of TOS database
# To use an existing database authentication alias, uncomment TargetObjectStore.datasource.authentication.alias and specify your alias
#TargetObjectStore.datasource.authentication.alias=BPM\_DB\_ALIAS
TargetObjectStore.datasource.authentication.user=db2admin
# The connection password of TOS database
# The password can be plain text or base64 encoded
TargetObjectStore.datasource.authentication.password={xor}Pj08Ozo5OA\=\=
```

## Sample Oracle response file

```
#Case Management database configuration properties.
#Thu Nov 01 04:40:39 EDT 2018
# IBM Content Navigator (ICN) data source information
ContentNavigator.datasource.name=BAWDB
ContentNavigator.datasource.host=oracleDBHost
ContentNavigator.datasource.port=1521
# Content Navigator database directory
# datasource.db.dir is a directory on the DB server that should be the same value for the 
ContentNavigator, DesignObjectStore, and TargetObjectStore database settings. It is used when generating the database creation 
scripts to supply the root directory where various database artifacts will be generated. The directory must exist on the database 
server before the database creation scripts run.
ContentNavigator.datasource.db.dir=C:\\IBM
# To use an LDAP-based URL or Oracle RAC URL or a custom URL (anything other than the Oracle Single Client Access Name (SCAN)), uncomment this property and enter the related URL
#ContentNavigator.datasource.url=jdbc\:oracle\:thin\:@ldap\://myldaphost\:9802/mydb1,cn\=OracleContext,dc\=mycom,dc\=com
ContentNavigator.datasource.tablespace.data=icnts
ContentNavigator.datasource.authentication.user=icnuser
# The password can be plain text or base64 encoded
ContentNavigator.datasource.authentication.password={xor}Lz4sLChvLTs\=

# Design Object Store (DOS) data source information
DesignObjectStore.datasource.name=BAWDB
DesignObjectStore.datasource.host=oracleDBHost
DesignObjectStore.datasource.port=1521
# DOS database directory
# datasource.db.dir is a directory on the DB server that should be the same value for the 
ContentNavigator, DesignObjectStore, and TargetObjectStore database settings. It is used when generating the database creation 
scripts to supply the root directory where various database artifacts will be generated. The directory must exist on the database 
server before the database creation scripts run.
DesignObjectStore.datasource.db.dir=C:\\IBM
# To use an LDAP-based URL or Oracle RAC URL or a custom URL (anything other than the Oracle Single Client Access Name (SCAN)), uncomment this property and enter the related URL
# DesignObjectStore.datasource.url=jdbc\:oracle\:thin\:@ldap\://myldaphost\:9802/mydb1,cn\=OracleContext,dc\=mycom,dc\=com
DesignObjectStore.datasource.tablespace.data=dosts
DesignObjectStore.datasource.authentication.user=dosuser
# The password can be plain text or base64 encoded
DesignObjectStore.datasource.authentication.password={xor}OzAsLz4sLChvLTs\=

# Target Object Store (TOS) data source information
TargetObjectStore.datasource.name=BAWDB
TargetObjectStore.datasource.host=oracleDBHost
TargetObjectStore.datasource.port=1521
# TOS database directory
# datasource.db.dir is a directory on the DB server that should be the same value for the 
ContentNavigator, DesignObjectStore, and TargetObjectStore database settings. It is used when generating the database creation 
scripts to supply the root directory where various database artifacts will be generated. The directory must exist on the database 
server before the database creation scripts run.
TargetObjectStore.datasource.db.dir=C:\\IBM
# To use an LDAP-based URL or Oracle RAC URL or a custom URL (anything other than the Oracle Single Client Access Name (SCAN)), uncomment this property and enter the related URL
#TargetObjectStore.datasource.url=jdbc\:oracle\:thin\:@ldap\://myldaphost\:9802/mydb1,cn\=OracleContext,dc\=mycom,dc\=com
TargetObjectStore.datasource.tablespace.data=tosts
TargetObjectStore.datasource.authentication.user=tosuser
# The password can be plain text or base64 encoded
TargetObjectStore.datasource.authentication.password={xor}Lz4sLChvLTs\=
```

## Sample SQL Server response file

```
#Case Management database configuration properties.
#Thu Nov 01 05:58:55 EDT 2018
# IBM Content Navigator (ICN) data source information
ContentNavigator.datasource.schema=icnsa
ContentNavigator.datasource.name=ICNDB
ContentNavigator.datasource.host=sqlserverHost
ContentNavigator.datasource.port=1433
# If windows authentication is used, set this property to true and comment out the user and password properties 
ContentNavigator.datasource.authentication.windows=false
ContentNavigator.datasource.authentication.user=sqluser
# The password can be plain text or base64 encoded
ContentNavigator.datasource.authentication.password={xor}Lz4sLChvLTs\=

# Design Object Store (DOS) data source information
DesignObjectStore.datasource.name=DOSDB
DesignObjectStore.datasource.host=sqlserverHost
DesignObjectStore.datasource.port=1433
DesignObjectStore.datasource.schema=DOSSA
# DOS database directory
# datasource.db.dir is a directory on the DB server that should be the same value for the 
ContentNavigator, DesignObjectStore, and TargetObjectStore database settings. It is used when generating the database creation 
scripts to supply the root directory where various database artifacts will be generated. The directory must exist on the database 
server before the database creation scripts run.
DesignObjectStore.datasource.db.dir=C:\\IBM
# If windows authentication is used, set this property to true and comment out the user and password properties
DesignObjectStore.datasource.authentication.windows=false
DesignObjectStore.datasource.authentication.user=sqluser
# The password can be plain text or base64 encoded
DesignObjectStore.datasource.authentication.password={xor}Lz4sLChvLTs\=

# Target Object Store (TOS) data source information
TargetObjectStore.datasource.name=TOSDB
TargetObjectStore.datasource.host=sqlserverHost
TargetObjectStore.datasource.port=1433
TargetObjectStore.datasource.schema=TOSSA
# TOS database directory
# datasource.db.dir is a directory on the DB server that should be the same value for the 
ContentNavigator, DesignObjectStore, and TargetObjectStore database settings. It is used when generating the database creation 
scripts to supply the root directory where various database artifacts will be generated. The directory must exist on the database 
server before the database creation scripts run.
TargetObjectStore.datasource.db.dir=C:\\IBM
# If windows authentication is used, set this property to true and comment out the user and password properties 
TargetObjectStore.datasource.authentication.windows=false
TargetObjectStore.datasource.authentication.user=sqluser
# The password can be plain text or base64 encoded
TargetObjectStore.datasource.authentication.password={xor}Lz4sLChvLTs\=
```