# Disaster recovery

For your topology to support disaster recovery, there are several options which depend on
how the federated data is indexed.

For BPD systems where data is directly indexed by Business Automation Workflow, refer to the fail over support documentation.

For systems which are indexed by Process Federation Server, you can choose
one of the following options.

- Backing up and restoring Process Federation Server indexes in the federated data repository

The following procedures apply to BPD and BPEL systems when indexing is done by Process Federation Server, and are based on standard Elasticsearch and OpenSearch snapshots. It also includes backing up Process Federation Server indexers states in Elasticsearch or OpenSearch indexes.
- Disaster recovery using two consumers

An alternative disaster recovery procedure is to have two Process Federation Server clusters federating the same business process management systems. Follow this procedure if the procedure relying on backing up and restoring Process Federation Server indexes in the federated data repository is not suitable. This procedure only applies to BPD and BPEL systems when indexing is done by Process Federation Server.
- Enabling the quick start mode

IBM® Process Federation Server provides a quick start mode that allows you to partially index tasks in the federated data repository based on a past date criteria.  This procedure only applies to BPD and BPEL systems when indexing is done by Process Federation Server.