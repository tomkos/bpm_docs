# Monitoring installed snapshots on each workflow server from Workflow Center

## About this task

## Procedure

To monitor installed snapshots, complete the following steps:

- For online servers, all snapshots are grouped by process app or toolkit. For each snapshot,
you see an instance count, which is the sum of all running, suspended, or failed instances for all
processes in the snapshot. while the online server is connected, this information is regularly
updated depending on the heartbeat interval. The host name is also displayed for the server that
last sent an update to Workflow Center for a particular
deployment environment. Note: If the instance count is zero, it will cause instance migration
options from that snapshot to be hidden.
- For offline servers, you see a list of all snapshot deployment packages that have been
created. They are grouped by process app.Note: This information is lost when the offline server is
deleted.