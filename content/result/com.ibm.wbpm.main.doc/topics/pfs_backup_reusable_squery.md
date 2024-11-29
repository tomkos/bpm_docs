# Backing-up and restoring reusable search queries

Reusable search queries managed with the /v2/search/queries REST
APIs are stored into a dedicated index of the federated data repository.

The name of this index defaults to ibmpfsqueries but it can be
customized with the searchQueriesIndexName configuration attribute of the
<ibmPfs\_remoteElasticsearch> configuration element in
server.xml.

- For Elasticsearch, see the Elasticsearch: Snapshot and restore reference
documentation.
- For OpenSearch, see the Opensearch: Take and restore snapshots reference
documentation.