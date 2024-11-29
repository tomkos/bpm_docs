# Rebuilding your federated system indices to upgrade to IBM® Process Federation
Server
24.0.0.0

## About this task

The following steps describe how to rebuild your indexes.

## Procedure

1. Stop all the Process Federation Server
servers.
2. Upgrade Process Federation Server to 24.0.0.0.
3. Setup a new Elasticsearch 8 cluster.
4. Update the Process Federation Server configuration
files (server.xml) to reference the new Elasticsearch 8 cluster endpoints as
the federated data repository.
5. Start the Process Federation Server
servers.