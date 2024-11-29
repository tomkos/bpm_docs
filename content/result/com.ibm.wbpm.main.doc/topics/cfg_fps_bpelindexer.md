# Enabling indexing of BPEL-related data in a federated environment

## Before you begin

If you are federating BPEL-related data from IBM BPM V8.6.0 CF2017.12, verify
that the required APAR is installed on the system. For more information, see Technote
2013237.

## About this task

Updates to the data are logged on the federated server. Process Federation Server monitors the logs for changes. When
changes become available, Process Federation Server
pulls them from the Business Process Choreographer database, and then indexes the changed data.

## Procedure

1 Create the change log tables in the Business Process Choreographer database on thefederated system. Use the create\_bpel\_change\_log.ddl script that is provided with Process Federation Server to create the tables.
    1. On Process Federation Server, go to the
pfs\_install\_root\ibmProcessFederationServer\wlp-ext\dbscripts
directory and go to the directory under it for your specific database type.
    2. Move the create\_bpel\_change\_log.ddl script to your federated
system.
    3 Read the instructions in the script and replace the variables with the correctnames.
        - Replace @SCHEMA@ with the schema name. Because the existing Business Process Choreographer
database user will be writing to the change log tables, ensure that the schema name is consistent
with the schema name that is used for other Business Process Choreographer database tables.
        - Replace @INSTANCE@ with the table space name
4. Run the script. 

For a DB2 database:

db2 connect to CMNDB
db2 -tf create\_bpel\_change\_log.ddl
db2 connect reset

For an Oracle database:

sqlplus system/passw0rd@orcl @create\_bpel\_change\_log.ddl

For an SQL Server database:

sqlcmd -U user\_id -P password -e -i create\_bpel\_change\_log.ddl
2 Configure the federated server to emit changes to the change log tables. The BPEL state observer plug-in on the federated server creates entries in the change log whenBPEL process or task data is updated. The way in which you enable the plug-in depends on whetheryour federated environment includes systems that are running versions of IBM BPM earlier than V8.5.6. After enabling the state observer, in a clustered federated environment, resynchronize the nodesof the application cluster and then restart the application cluster.

The BPEL state observer plug-in on the federated server creates entries in the change log when
BPEL process or task data is updated. The way in which you enable the plug-in depends on whether
your federated environment includes systems that are running versions of IBM BPM earlier than V8.5.6.

- V8.5.6 or later : For federated environments that are running only IBM BPM V8.5.6 or later, use the administrative consoleto enable the plug-in:
    1. Launch the IBM BPM administrative
console.
    2. Click Servers > Clusters > WebSphere application server clusters > cluster
name > Business Flow Manager > Business Process Choreographer containers, then on the Configuration tab, expand State
Observers, and enable the Federation Server Indexing logging
option for both Business Flow Manager and Human Task Manager.
- V8.5 : For federated environments that include servers that are running versions ofIBM BPM V8.5, use thesetStateObserver.py wsadmin command to enable the plug-in:

- From theinstall\_root \ProcessChoreographer\admin directory, run thefollowing command:

<!-- image -->

    - In a network deployment
environment:..\..\bin\wsadmin -f setStateObserver.py -enable IndexerLog  -cluster cluster\_name
    - In a stand-alone
environment:..\..\bin\wsadmin -f setStateObserver.py -enable IndexerLog  -server server\_name
- From theinstall\_root /ProcessChoreographer/admin directory, run thefollowing command: For more information about the setStateObserver.py command, see setStateObserver.py administrative script .

<!-- image -->

<!-- image -->

- In a network deployment
environment:../../bin/wsadmin -f setStateObserver.py -enable IndexerLog -cluster cluster\_name
- In a stand-alone
environment:../../bin/wsadmin -f setStateObserver.py -enable IndexerLog -server server\_name
- Pre-V8.5 : For federated environments that include servers that are running versionsearlier than IBM BPM V8.5, run thesetStateObserver.py wsadmin command from the config directory to enable the plug-in: For more information about the setStateObserver.py command, see setStateObserver.py administrative script .

- From theinstall\_root \ProcessChoreographer\config directory, run thefollowing command:

<!-- image -->

    - In a network deployment
environment:..\..\bin\wsadmin -f setStateObserver.py -enable IndexerLog -cluster cluster\_name
    - In a stand-alone
environment:..\..\bin\wsadmin -f setStateObserver.py -enable IndexerLog -server server\_name
- From theinstall\_root /ProcessChoreographer/config directory, run thefollowing command:

<!-- image -->

<!-- image -->

- In a network deployment
environment:../../bin/wsadmin -f setStateObserver.py -enable IndexerLog -cluster cluster\_name
- In a stand-alone
environment:../../bin/wsadmin -f setStateObserver.py -enable IndexerLog -server server\_name

After enabling the state observer, in a clustered federated environment, resynchronize the nodes
of the application cluster and then restart the application cluster.

3 Enable BPEL indexing on Process Federation Server .

1. Open the server.xml configuration file for
editing.
By default, the configuration file is in the
pfs\_install\_root/usr/servers/server\_name directory on
Process Federation Server.
2. Configure the library and dataSource elements for
your Workflow Server or Process Server
database. The BPEL indexing service uses these properties to connect to the
database.The following code snippet shows an example of configured
library and dataSource elements for a DB2
database:<library id="DB2JCC4Lib">
   <fileset dir="pfs\_install\_root/wlp-ext/jdbcdrivers/DB2" 
      includes="db2jcc4.jar db2jcc\_license\_cisuz.jar"/>
</library>
<dataSource id="bpel\_db2" 
   commitOrRollbackOnCleanup="commit" isolationLevel="TRANSACTION\_READ\_COMMITTED" 
   jndiName="jdbc/bpeldata" type="javax.sql.DataSource"> 
   <jdbcDriver libraryRef="DB2JCC4Lib"/> 
   <properties.db2.jcc serverName="localhost" portNumber="50000" 
      databaseName="CMNDB" user="db2admin" password="db2admin" /> 
</dataSource>
3. Update the configuration properties for the BPEL indexing
service in the ibmPfs\_federatedSystem, ibmPfs\_bpelIndexer,
and ibmPfs\_bpelRetriever elements. For
information about the configuration properties, see Configuration properties for the Process Federation Server index.