# Logging and tracing for Process Federation Server

## About this task

```
<logging consoleLogLevel="INFO" traceFormat="ENHANCED" traceSpecification="*=info" />
```

## Procedure

1. Open the server.xml configuration file for
editing.
By default, the configuration file is in the
pfs\_install\_root/usr/servers/server\_name directory on
Process Federation Server.
2. Extend the traceSpecification property
for each component that you want to trace, for example, traceSpecification="*=info:com.ibm.bpm.federated.*=all"
 ".  The following table shows the available
trace specifications for Process Federation Server components:
Table 1. Trace specifications for Process Federation Server components

Trace specification
Description

com.ibm.bpm.federated.*=all
Traces all the Process Federation Server components.

com.ibm.bpm.federated.query.rest.*=all
Traces requests from the Process Federation Server REST
APIs.

com.ibm.bpm.federated.indexer.bpd.*=all

com.ibm.bpm.federated.indexer.bpel.*=all

Traces the indexing service on federated systems. You can enable tracing for
BPD systems, BPEL systems, or both.

com.ibm.bpm.federated.retriever.bpd.*=all

com.ibm.bpm.federated.retriever.bpel.*=all

com.ibm.bpm.federated.retriever.casemgr.*=all

Traces the retrieval service on federated systems. You can enable tracing for
BPD systems, BPEL systems, Case systems or a combination of those.

com.ibm.bpm.elasticsearch.receiver.*=all
Traces the Elasticsearch and OpenSearch indexing methods.

com.ibm.wbimonitor.partitioning.*=all
Traces the indexer partitioning service. The
service coordinates the indexing services across cluster members.

com.ibm.bpm.elasticsearch.client.*=all
com.ibm.bpm.elasticsearch.universalclient.*=all
Traces the remote federated data repository client.

com.ibm.bpm.query.rest.SAVED\_SEARCH\_PERFORMANCE\_LOGGER=all
Traces performance of saved searches