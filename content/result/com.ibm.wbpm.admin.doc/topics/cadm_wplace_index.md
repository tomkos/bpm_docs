# Administering the federated data repository indexes

To take advantage of this enhanced search experience, you must enable the
indexing of BPD and case data in the federated data repository. Note that the federated data
repository indexing is needed to enable the REST APIs for advanced search support. See REST APIs for advanced searches support.

- Configuring the federated data repository connection

Business Automation Workflow can index data about business process definition (BPD) process instances and task and case instances in the federated data repository, which can be either Elasticsearch or OpenSearch. If you enable both the BPD indexing and the case indexing, the same federated data repository is used to store the BPD and case data.
- Enabling and configuring the federated data repository BPD indexing

Business Automation Workflow can index data about business process definition (BPD) process instances and tasks in the federated data repository.
- Understanding the federated data repository BPD indexing

The cornerstone of the federated data repository indexing is the queue, which is populated by the BPD engine. The indexing queue is shared among all the nodes of the Business Automation Workflow cluster.
- Indexing case instances

The case management tools support indexing of case instances in a federated data repository index. Full reindexing and live index updates are supported.