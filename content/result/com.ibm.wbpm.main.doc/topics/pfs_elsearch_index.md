# Process Federation Server
federated data repository indexes

## How Process Federation Server creates
indexes

```
<ibmPfs\_federatedSystem
    ...
    indexName="myIndex"
    index.number\_of\_replicas="1"
    index.number\_of\_shards="3"
    ...
/>
```

- How tasks are stored in the federated data repository

For each task  to index, a JSON task document is defined by a number of fields that characterize the task, and is stored into the index created for the federated system.
- How process instances are stored in the federated data repository

For each BPD process instance to index, Process Federation Server creates a JSON instance document and stores it into the index created for the BPD federated system.
- How case instances are stored in the federated data repository

For each case instance to index, Process Federation Server creates a JSON instance document and stores it into the index created for the federated system.