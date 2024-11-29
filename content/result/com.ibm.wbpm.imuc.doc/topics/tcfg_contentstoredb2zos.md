# Configuring the BPM document store for DB2 on z/OS

IBM® Business Automation Workflow V8.5.6 or higher supports
the BPM document store for DB2 on z/OS. The BPM document store is a CMIS-enabled document repository that is
used to store BPM documents in Business Automation Workflow.
This enablement means that it supports the Content Management Interoperability Services (CMIS)
standard for interoperability in Enterprise Content Management (ECM) systems. This configuration
includes support for the BPM content store, another
CMIS-enabled embedded document repository that is used for case management applications. It is only
available in Business Automation Workflow with the Basic Case
Management feature installed.

## About this task

You also have the option of using an external ECM system
instead of the BPM document store. Read
the following steps for configuring IBM BPM with the BPM document store. See Configuring an existing external Content Platform Engine to configure IBM BPM with an external
ECM system.

The BPM document store is an
optional component that uses its own database. After it is configured,
it remains always enabled.

To configure the BPM document store, you
can either update the properties file to include it before you create
the deployment environment, or you can update the deployment environment
later using the BPMConfig -upgrade -de -component command.

Since
the BPMConfig command is necessary for this configuration,
see BPMConfig command-line utility to learn more about this command.
The topic includes how the BPMConfig command can
be used with a configuration properties file like the one you will
create. If you are updating your deployment environment to add the
BPM document store, you also need to know how to export the properties
file that is required to update your deployment environment.

## Procedure

Either when you first create the deployment environment
or at a later time, complete the following steps:

1 If you are updating your deployment environment to addthe BPM document store, ensure that the configuration propertiesfile correctly reflects the topology of the IBM BPM deployment environmentby exporting the configuration properties file using the BPMConfig command. The configuration properties file is named deployment\_environment .properties (where deployment\_environment isthe name of the deployment environment). The file is located in theoutput directory that you specify when you run the command.Note: Ifthere is only one deployment environment in the WebSphere cell, youcan omit the -de option.
    - On Microsoft Windows operating systems, run the following BPMConfig.bat command:install\_root\bin\BPMConfig.bat -export -profile deployment\_manager\_profile\_name [-de deployment\_environment\_name] -outputDir path\_to\_configuration\_files
    - On Linux and UNIX-based operating systems, run the following BPMConfig.sh command:install\_root/bin/BPMConfig.sh -export -profile deployment\_manager\_profile\_name [-de deployment\_environment\_name] -outputDir path\_to\_configuration\_files
2. Open your deployment environment properties file in an
editor.
3. Specify the EmbeddedECM and CMIS components
on the application cluster and specify the DocumentStoreAdmin component
on the support cluster. For example:In a single cluster
topology, where cluster 1 has both application and
support capabilities and the next available component index number
is 2, add entries that are similar to those in the
following example:bpm.de.cluster.1.capability.1.component.2.name=EmbeddedECM
bpm.de.cluster.1.capability.1.component.3.name=CMIS
bpm.de.cluster.1.capability.3.component.1.name=DocumentStoreAdmin 
In
a three cluster topology, where cluster 1 has application
capability and the next available component index number is 2,
and where cluster 3 has support capability and the
next available component index number is 1, add entries
that are similar to those in the following example:bpm.de.cluster.1.capability.1.component.2.name=EmbeddedECM
bpm.de.cluster.1.capability.1.component.3.name=CMIS
bpm.de.cluster.3.capability.1.component.1.name=DocumentStoreAdmin
4. Add a database definition EmbeddedEcmDb to
the application cluster that uses the same cluster index as in the
previous step. For example, add an entry that is similar
to the following example: bpm.de.cluster.1.db=SharedDb,PerformanceDB,EmbeddedEcmDb
5. Add the definition of the new EmbeddedEcmDb database.
For example, for a DB2 for z/OS database that is named X8BPMDB,
if the next free database index is 5, add entries
that are similar to the following example: bpm.de.db.5.name=EmbeddedEcmDb
bpm.de.db.5.dbCapabilities=EmbeddedECM
bpm.de.db.5.type=DB2zOS
bpm.de.db.5.hostname=winmvsea
bpm.de.db.5.portNumber=446
bpm.de.db.5.connectionLocation=DSNV10EP
bpm.de.db.5.databaseName=X8BPMDB
bpm.de.db.5.schema=X8BPM
bpm.de.db.5.vcat=DSNV10EP
bpm.de.db.5.bptable4k=BP1
bpm.de.db.5.bptable8k=BP8K1
bpm.de.db.5.bptable16k=BP16K1
bpm.de.db.5.bptable32k=BP32K1
bpm.de.db.5.bpindex=BP2
bpm.de.db.5.bplob4k=BP3
bpm.de.db.5.volumes='*'
bpm.de.db.5.stogrp=X8DBSTO
bpm.de.db.5.roleMapping.1.name=DbUser
bpm.de.db.5.roleMapping.1.alias=BPM\_DB\_ALIAS
bpm.de.db.5.roleMapping.2.name=DbUserXAR
bpm.de.db.5.roleMapping.2.alias=BPM\_DB\_ALIAS
6 Create or update the deployment environment.

- If you are creating your deployment environment for the first
time, after you make all your changes and update the properties file,
run the BPMConfig -create command. For example:BPMConfig -create -de DE1.properties
- If you are updating your deployment environment to add the BPM document store , completethe following steps.
    1. Run the BPMConfig -upgrade -component EmbeddedECM command.
You must run the command on the deployment manager node. The following
example shows how to run the command:BPMConfig -upgrade -de DE1.properties -component EmbeddedECMAfter
you run the command, synchronize the nodes so that the managed nodes
obtain the latest configuration file changes.
    2 Run the database script.
        1. The database script is in dmgr\_profile\_root/dbscripts\_upgrade.
The script is named createSchema\_Advanced.sql for
an Advanced deployment environment and createSchema\_Standard.sql for
a Standard deployment environment.
        2. Copy the script to your database machine and run the script. For
example:db2 -tf createSchema\_Advanced.sql
3. Restart the deployment environment.

## Related information

- BPMConfig command-line utility