# Enabling indexing of BPD-related data in a federated environment

When a business process definition (BPD) runs on a Business Automation Workflow or IBM® BPM system, BPD-related data
is written to the Workflow Server or IBM Process
Server database
(BPMDB).

- If indexing to the federated data repository is made from Process Federation Server, you must
create change log tables in the Workflow Server or Process Server database, and
enable BPD indexing on Process Federation Server.
- If the federated system is a BPD runtime from Business Automation Workflow 24.0.0.0, indexing from
Process Federation Server is
deprecated, and instead you must enable the federated data repository BPD indexing in Business Automation Workflow as described in Enabling the BPD indexing.

## Before you begin

- If you are enabling indexing on an IBM BPM
system that is earlier than V8.5.6, verify that the required APARs are installed on the system. For
more information, see Technote
1699090.
- Verify that the Workflow Server or the Process
Server on the federated server is stopped.

## About this task

Updates to the data are logged on the federated server. Process Federation Server monitors the logs for changes. When
changes become available, Process Federation Server
pulls them from the Workflow Server or Process
Server database, and then indexes the changed data.

By default, BPD process instances are not indexed as separate documents in the federated data
repository. You can enable indexing of process instances for a BPD federated system (see BPD process instance indexing).

- A task is assigned.
- A task is completed and the business data is updated.
- The due date or at-risk date of a task is changed.
- The priority of a task is changed.
- The associated process instance changes state (completed, suspended, resumed, terminated,
restarted, or failed).

## Procedure

1 Create the change log tables in the Workflow Server or Process Server database on the federatedsystem. Use the create\_bpd\_change\_log.ddl script that is provided with Process Federation Server to create the tables.
    1. On Process Federation Server, go to the
pfs\_install\_root\ibmProcessFederationServer\wlp-ext\dbscripts
directory and go to the directory under it for your specific database type.
    2. Move the create\_bpd\_change\_log.ddl script to your federated
system.
    3 Read the instructions in the script and replace the variables with the correctnames.
        - Replace @SCHEMA@ with the schema name. Because the existing database user will be writing to
the change log tables, ensure that the schema name is consistent with the schema name that is used
for other federated system database tables.
4. Run the script. 

For DB2:

db2 connect to BPMDB
db2 -tf create\_bpd\_change\_log.ddl
db2 connect reset

For Oracle:

sqlplus system/passw0rd@orcl @create\_bpd\_change\_log.ddl

For SQL Server:

sqlcmd -U user\_id -P password -e -i create\_bpd\_change\_log.ddl
2 Configure the federated server to emit changes to the change log tables. Update the 100Custom.xml file on the federated server to include thefederated-index-enabled configuration parameter. For information about where tofind the 100Custom.xml file, see Location of 100Custom configuration files .

Update the 100Custom.xml file on the federated server to include the
federated-index-enabled configuration parameter. For information about where to
find the 100Custom.xml file, see Location of 100Custom configuration files.

1. Open the 100Custom.xml file in a text editor and add the
following code
snippet: <server>
  <search-index merge="mergeChildren">
     <federated-index-enabled merge="replace">true</federated-index-enabled>
   </search-index>
</server>For
more information about the 100Custom.xml file, see The 100Custom.xml file and configuration.
2. Save your changes.
3. Restart the Workflow Server or the
Process Server on the federated server.
4. Resynchronize the nodes of the application cluster and then restart the application
cluster.
3 Enable BPD indexing on Process Federation Server .

1. Open the server.xml configuration file for
editing.
By default, the configuration file is in the
pfs\_install\_root/usr/servers/server\_name directory on
Process Federation Server.
2. Configure the library and dataSource elements for
your Workflow Server or Process Server
database. The BPD indexing service uses these properties to connect to the
database.The following code snippet shows an example of configured
library and dataSource elements for a DB2
database:<library id="DB2JCC4Lib">
   <fileset dir="pfs\_install\_root/wlp-ext/jdbcdrivers/DB2" 
      includes="db2jcc4.jar db2jcc\_license\_cisuz.jar"/>
</library>
<dataSource id="bpd\_db2" 
   commitOrRollbackOnCleanup="commit" isolationLevel="TRANSACTION\_READ\_COMMITTED" 
   jndiName="jdbc/bpmdata" type="javax.sql.DataSource"> 
   <jdbcDriver libraryRef="DB2JCC4Lib"/> 
   <properties.db2.jcc serverName="localhost" portNumber="50000" 
      databaseName="BPMDB" user="db2admin" password="db2admin" /> 
</dataSource>
3. Update the configuration properties for the BPD indexing
service in the  ibmPfs\_federatedSystem, ibmPfs\_bpdIndexer,
and ibmPfs\_bpdRetriever elements. For
information about the configuration properties, see Configuration properties for the Process Federation Server index.

- BPD process instance indexing

By default, when configuring the <ibmPfs\_bpdIndexer> tag, BPD process instances are indexed by Process Federation Server in the federated data repository. Your federated systems must be properly set up for process instance indexing. It is also possible to disable process instance indexing in your Process Federation Server configuration file.