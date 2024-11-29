# Process Federation Server
components overview

## Terminology

The terms federated system or federated instance can refer to either an
IBM Business Process Manager
 or a
Business Automation Workflow server that is
part of the federated environment.

## Architecture

Process Federation Server
provides end users with a unified view of tasks and instances running on different Business Automation Workflow and Case Manager federated
systems.

<!-- image -->

## REST APIs

- retrieving information from federated systems through the retrievers (Launch Entities and
Systems Metadata REST APIs).
- performing searches into the federated data repository indexes to return lists of tasks and
process instances (Tasks List and Process Instances list REST APIs).
- storing saved searches in Process Federation Server database (Saved
search REST API).
- storing reusable queries in a federated data repository index (Reusable queries V2).
- returning data for the Team Performance Dashboard.

## Indexers and retrievers

For each federated system to configure, two components must be configured: an indexer and a
retriever.

The indexer inserts JSON documents that describe all the instances and/or tasks that run
on the federated system into a federated data repository index. Each federated system has its own
single index, and depending on the version and on the type (BPD, BPEL or Case) of the system that
you want to federate, the indexer runs either on Process Federation Server or on Business Automation Workflow nodes.

- constantly poll the federated system’s database to identify which tasks and process instances
must be indexed into the federated data repository.
- perform SQL queries to the database to build the document that will be indexed into
Elasticsearch for each identified task and process instance.
- perform maintenance operations on the database tables involved in the indexing.
- in Business Automation Workflow 24.0.0.0,
the BPD indexer was redesigned and is now configured and runs on the Business Automation Workflow federated system. For
older BPD versions and for BPEL, the indexer is still configured and runs as part of Process Federation Server.

The Case indexer indexes Case instances into the federated data repository.

- To federate a system hosting business process definition (BPD) process instances and tasks, youmust define the indexer either in Process Federation Server or in Business Automation Workflow , depending on yourversion of Business Automation Workflow :
    - For Business Automation Workflow
24.0.0.0, there is no indexer to configure in Process Federation Server. Instead,
Business Automation Workflow must be
configured to index directly in the federated data repository as documented in Configuring Business
Automation Workflow to index to the federated data repository.
    - For Business Automation Workflow 23.0.2
and earlier, you must configure the indexer in the Process Federation Server configuration
through an <ibmPfs\_bpdIndexer> element. For more details, see Enabling indexing of BPD-related data in a federated environment.Note: Federating a Business Automation Workflow
24.0.0.0 BPD system by configuring the <ibmPfs\_bpdIndexer> element in Process Federation Server configuration
is deprecated. However, you can upgrade your Business Automation Workflow federated system to
24.0.0.0 as usual, and then disable the indexer in Process Federation Server to replace it
with the new federated data repository BPD indexing as documented in Enabling the BPD indexing.
- To federate a system hosting BPEL process instances and tasks, you must configure the indexer in
Process Federation Server
configuration through a <ibmPfs\_bpelIndexer> element. For more details, see
Enabling indexing of BPEL-related data in a federated environment.
- To federate a Case Manager system, you must
configure the indexer in Case Manager configuration as
described in Indexing case instances.

- the system status
- the list of launchable entities
- the teams memberships of users

- To federate the BPMN (BPD) process instances and tasks hosted by a Business Automation Workflow system, you must
configure the retriever through a <ibmPfs\_bpdRetriever> element. For more
details, see The ibmPfs\_bpdRetriever element.
- To federate the BPEL process instances and tasks hosted by a Business Automation Workflow system, you must
configure the retriever through a <ibmPfs\_bpelRetriever> element. For more
details, see The ibmPfs\_bpelRetriever element.
- To federate a Case Manager system, you must
configure the indexer in Case Manager configuration as documented in Enabling indexing of Case-related data in a federated environment.

## External components

- The federated data repository :
    - can be either Elasticsearch or Opensearch, which must be setup separately:
        - Elasticsearch 8.x - all versions (note that versions prior to 8.x are not supported).
        - OpenSearch 2.x - all versions from 2.5.0.
        - For more information about the remote federated data repository configuration, see Declaring the federated data
repository in server.xml.
- stores the data about each federated systems. Each federated system has its own index.
- an additional index is used to store reusable queries.
- Relational database to store saved searches. All Process Federation Server instances share
the same relational database.