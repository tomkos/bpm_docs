# Upgrading Elasticsearch federated data repository to Elasticsearch 8

- There no longer is a document type for the documents stored by Process Federation Server in
Elasticsearch indices (as a result of the mapping types removal in Elasticsearch: https://www.elastic.co/guide/en/elasticsearch/reference/8.4/removal-of-types.html)
- As index names starting with "." are deprecated in Elasticsearch 8 (see
https://www.elastic.co/guide/en/elasticsearch/reference/8.4/indices-create-index.html): when
a federated system is declared with an index name of myIndexName, the created
index has the name @myIndexName. In Elasticsearch 6, an index named
.myIndexName was created with an alias of
myIndexName.

If you migrate to Process Federation Server
24.0.0.0 from an existing
topology based on an Elasticsearch 6.x cluster for the federated data repository, you must either
rebuild your federated systems indexes from scratch, or migrate your existing Elasticsearch 6.x
indices to Elasticsearch 8.x.

- From Elasticsearch 7.17.0, you can directly upgrade to Elasticsearch 8
- From a version of Elasticsearch lower that 7.17.0, you must first upgrade your cluster to
Elasticsearch 7.17 and then to Elasticsearch 8

- Rebuilding your federated system indices to upgrade to IBM Process Federation Server 24.0.0.0

Follow this procedure if you choose to rebuild your federated data repository indexes from scratch in order to upgrade to Process Federation Server 24.0.0.0 from an existing topology based on an Elasticsearch 6.x cluster for indexing.
- Migrating existing Elasticsearch 6.x federated data repository indices to upgrade to IBM Process Federation Server 24.0.0.0

Follow this procedure if you choose to migrate your existing Elasticsearch 6.x federated 		data repository indices to Elasticsearch 8.x for your upgrade to Process Federation Server 24.0.0.0.