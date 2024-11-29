# Upgrading  IBM Process Federation
Server

- Upgrading IBM Process Federation Server v8.5.x, v8.6.0, v18.x, v19.x, v20.x, v21.x or v22.x to Process Federation Server 24.0.0.0

To upgrade to IBM Process Federation Server 24.0.0.0, follow the instructions to install the 24.0.0.0 refresh pack for each process federation server in the upgraded installation.
- Upgrading Elasticsearch federated data repository to Elasticsearch 8

Process Federation Server federated data repository can is implemented with and external Elasticsearch or OpenSearch cluster. Compared to previous releases of Process Federation Server, using an external Elasticsearch 6.x cluster is no longer supported and using an external Elasticsearch 7.x cluster is deprecated. If you are using Elasticsearch, you must set up an external Elasticsearch 8.x cluster (see Elasticsearch product end of life dates at https://www.elastic.co/support/eol).
- Installing fix packs and interim fixes on IBM Process Federation Server

You can install updates to Process Federation Server interactively or silently. You can then package the updated installation and deploy it to other locations or computers that use the master installation.