# Disaster recovery using two consumers

An alternative disaster recovery procedure is to have two Process Federation Server clusters
federating the same business process management systems. Follow this procedure if the procedure
relying on backing up and restoring Process Federation Server indexes in the
federated data repository is not suitable. This procedure only applies to BPD and BPEL systems when
indexing is done by Process Federation Server.

## Before you begin

This procedure requires stopping the active cluster to maintain the fallback cluster. The
recommended disaster recovery procedure relies on taking federated data repository index snapshots
on the active cluster and restore them on the fallback cluster. For more details on this procedure,
see Backing up and restoring Process Federation
Server indexes in the federated data repository.

For more details about the consumer columns, see  Identifying and removing inactive change log consumers.

## About this task

This procedure requires one cluster to be the active cluster, and the other to be the fallback
cluster which is the one you switch to when the active cluster fails.

Keep the active cluster running during working hours, and at night or over the week-end, shut it
down. Then start the fallback cluster so that its federated data repository gets updated with the
latest changes performed on the federated business process management system.

As soon as all the change log rows are marked as consumed by the fallback cluster, or after a
fair amount of time, shut down the fallback cluster and then restart the active cluster. In this way
the fallback cluster remains “nearly” up-to-date with the latest changes on the federated systems.
Also, in case of disaster, and when there's a switch from the active cluster, it will take less time
for the fallback cluster to get the federated data repository back in sync with the federated
system.

## Procedure

1. Configure 2 different Process Federation Server clusters
federating the same business process management systems, and make sure that the
indexName property of the <ibmPfs\_federatedSystem>
configuration elements is different from one cluster to another. One of the clusters will be the
active cluster, and the other one the fallback cluster.
2. Start the nodes on the active cluster and keep the node of the fallback cluster shut
down.
3. Out of business hours, shut down the nodes on the active cluster, and then start the
nodes of the fallback cluster.
4 Let the fallback cluster run for some time, ideally until it has processed all theunconsumed change log entries.
    1. To get unconsumed change log entries first identify which CONSUMER\_00x column
is used by the fallback cluster for each federated system. Identify the column used by the fallback
cluster for a federated system by executing the following SQL query where
<indexName> must be replaced with the indexName property of the
<ibmPfs\_federatedSystem> configuration element:
SELECT COLUMN\_NAME FROM PFS\_BPD\_CHANGE\_LOG\_CONSUMER WHERE CONSUMER\_ID=’<indexName>’;
    2. With the proper column being identified, you can monitor how many change log entries remain
unconsumed by the fallback cluster for this federated system using the following SQL query, which is
an example that assumes that the column returned previously was COLUMN\_002.
SELECT COUNT(*) FROM PFS\_BPD\_CHANGE\_LOG WHERE CONSUMER\_002 < 20;
    3. Perform this monitoring for all the federated systems.
5. Once the fallback cluster has had enough time to synchronize its federated data
repository with the latest changes on all federated systems, stop all the nodes of the fallback
cluster.
6. Once all the nodes of the fallback cluster have been shut down, restart the nodes of the
active cluster.
7. Repeat the above procedure daily if possible, and whenever there is a disaster on the
active topology.
8. Make sure that the active Process Federation Server cluster is
completely shut down and then switch to the fallback topology.  In a reasonable amount of
time, the federated data repository gets back in sync with the database.