# Configuring the Process Federation Server database

## Before you begin

## About this task

To configure the Process Federation Server database, you must specify values for
the <library> and the <dataSource> elements in the
server.xml file. Process Federation Server uses this information to connect to
the database. If the Process Federation Server database
uses the same database management system as the business process management systems, the databases
can use the same library specification. In addition, you must specify the database properties in the
ibmPfs\_federatedPersistence element.

## Procedure

1. Open the server.xml configuration file for
editing.
By default, the configuration file is in the
pfs\_install\_root/usr/servers/server\_name directory on
Process Federation Server.
2. Ensure that the server.xml file contains
a configured library element for the database management
system that you are using for the Process Federation Server database.
Uncomment the appropriate library element if
it is commented out.The following code snippet shows
an example of a configured library element for an
IBM DB2 database:<library id="DB2JCC4Lib">
   <fileset dir="pfs\_install\_root/wlp-ext/jdbcdrivers/DB2" 
      includes="db2jcc4.jar db2jcc\_license\_cisuz.jar db2jcc\_license\_cu.jar"/>
</library>
3. Configure the dataSource element for your Process Federation Server database.
Note: You must configure a datasource element with a different
id for each federated system.
Uncomment the appropriate
dataSource element if it is commented out, and specify values for the
databaseName, user, and password properties.The following
code snippet shows an example of a configured dataSource element
for a DB2 database:<dataSource id="pfs\_db2" 
   commitOrRollbackOnCleanup="commit" isolationLevel="TRANSACTION\_READ\_COMMITTED" 
   jndiName="jdbc/pfsdata" type="javax.sql.DataSource"> 
   <jdbcDriver libraryRef="DB2JCC4Lib"/> 
   <properties.db2.jcc serverName="localhost" portNumber="50000" 
      databaseName="PFSDB" user="db2admin" password="db2admin" /> 
</dataSource>
4. Specify the schema name and the data source ID for the Process Federation Server database
instance in the ibmPfs\_federatedPersistence element:
<ibmPfs\_federatedPersistence 
  schemaName="FEDERATED"
	  dataSourceRef="pfs\_db2"/>

schemaName
Not required. The name of the schema that contains the database
tables. It must be the same as the name that was used when the Process Federation Server tables
were created. The default value is FEDERATED.
dataSourceRef
Required. The data source ID for the Process Federation Server database
instance. This property refers to the data source ID that you set
in step 3.

## Results