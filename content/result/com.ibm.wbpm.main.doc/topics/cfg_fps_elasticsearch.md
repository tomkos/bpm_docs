# Configuring the federated data repository service

- Declaring the federated data repository in server.xml

The Process Federation Server configuration must contain an ibmPfs\_remoteElasticsearch configuration element to configure the remote data repository.
- Process Federation Server federated data repository indexes

IBM® Process Federation Server is set up with an external Elasticsearch or OpenSearch cluster and creates an index for each declared federated system. For each task or process instance to index, a JSON task or instance document is created and stored into the index.