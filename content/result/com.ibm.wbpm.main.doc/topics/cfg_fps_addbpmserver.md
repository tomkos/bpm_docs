# Adding a Business Automation Workflow
system to the federated environment

## Before you begin

- Indexing must be enabled on the Business Automation Workflow system. For more
information, see Enabling indexing of BPD-related data in a federated environment, Enabling indexing of BPEL-related data in a federated environment, and
Enabling indexing of Case-related data in a federated environment.
- For systems running BPEL tasks, Process Portal
must be configured for a federated environment. See Configuring Process Portal for a federated environment.

## Procedure

Complete the following steps to add a Business Automation Workflow system to the federated
environment.

1. Open the server.xml configuration file for
editing.
By default, the configuration file is in the
pfs\_install\_root/usr/servers/server\_name directory on
Process Federation Server.
2. Add an ibmPfs\_federatedSystem element.
This element includes general configuration properties that apply to BPD, BPEL and Case systems:
for more information, see Configuration properties for the Process Federation Server index. Ensure that you specify a value for
the id property.
3 Configure the indexer:
    - To federate a BPD system that runs as part of Business Automation Workflow 24.0.0.0, there is no
indexer to configure in Process Federation Server. Instead, you
must configure Business Automation Workflow
to index directly into the federated data repository as described in Enabling the BPD indexing.
    - To federate a BPD system that runs as part of Business Automation Workflow 23.0.2 and earlier: Note: Federating a Business Automation Workflow 24.0.0.0 BPD system by configuring the <ibmPfs\_bpdIndexer> element in Process Federation Server configurationis deprecated. However, you can upgrade your Business Automation Workflow federated system to24.0.0.0 as usual, and then disable the indexer in Process Federation Server to replace itwith the new federated data repository BPD indexing as documented in Enabling the BPD indexing .
        1. Add the appropriate data source element. Point the data source to the Workflow Server or Process Server database (BPMDB)
that is enabled for indexing. For more information, see Enabling indexing of BPD-related data in a federated environment.
        2 Add and configure the ibmPfs\_bpdIndexer element. For more information about theconfiguration properties, see Configuration properties for the Process Federation Server index .
            - Make sure that the value of the federatedSystemRef property in the
implementation element is the same as the id property in the
ibmPfs\_federatedSystem element.
            - Make sure that the indexer connects directly to the database server by specifying a value for
the dataSourceRef property.
- To federate a BPEL system:

1. Add the appropriate data source element. Point the data source to the database containing the
Business Process Choreographer tables (CMNDB) that is enabled for indexing. For more information,
see Enabling indexing of BPEL-related data in a federated environment.
2 Add and configure the ibmPfs\_bpelIndexer element. For more information aboutthe configuration properties, see Configuration properties for the Process Federation Server index .
    - Make sure that the value of the federatedSystemRef property in the
implementation element is the same as the id property in the
ibmPfs\_federatedSystem element.
    - Make sure that the indexer connects directly to the database server by specifying a value for
the dataSourceRef property.
- To federate a Case system that runs as part of Business Automation Workflow, you must enable the
indexing as documented in Enabling indexing of Case-related data in a federated environment.
4 For all systems: add the appropriate REST retriever implementation element for thesystem. For example, for BPD systems, add and configure the ibmPfs\_bpdRetriever element. For more information about the configuration properties, see Configuration properties for the Process Federation Server index .

- Ensure that the value of the federatedSystemRef property in the
implementation element is the same as the id property in the
ibmPfs\_federatedSystem element.
5. Add the URLs that Workplace and Process Portal use for the federated
environment. Set values for the restUrlPrefix and
taskCompletionUrlPrefix properties. For more information, see Configuration properties for the Process Federation Server index.
6. Save your changes to the server.xml file
and restart Process Federation Server.

## What to do next

- Configure a proxy server, such as IBM HTTP Server, in front of the system. See Configuring IBM HTTP Server for federated environments.
- Set a value for the BPC.ExternalActivityDefaultURL custom property on the
system. By setting this value, you can ensure that BPEL tasks that do not use an external
implementation as the client type run in Process Portal. For more information, see Changing custom properties for Process Portal.