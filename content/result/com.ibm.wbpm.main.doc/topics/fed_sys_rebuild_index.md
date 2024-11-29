# Rebuilding an index

If problems occur with the Process Federation Server index, you
might need to rebuild it. Complete the following steps to rebuild an index.

1. Stop all process federation servers.
2. Delete the index by using the native Elasticsearch or OpenSearch API on the remote Elasticsearch
or OpenSearch server.
3. Restart all process federation servers. The index is rebuilt.

For BPD systems where indexing is directly done by Business Automation Workflow, refer to the create-index and rebuild maintenance operations in Understanding the federated data repository indexing.