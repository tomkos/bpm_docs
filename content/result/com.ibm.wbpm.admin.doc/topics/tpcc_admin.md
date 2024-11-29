<!-- image -->

# Administering the compensation service

## About this task

The compensation service must be started on an application
server, when BPEL processes are run on that server. You must perform
this server-level setup consistently for each cluster member. The
compensation service is used to manage updates that might be made
in a number of transactions before the process completes. When
you set up a new application server, the compensation service is enabled
by default.

You can use the administrative console to view and change
properties of the compensation service for application servers.

## Procedure

1. In the administrative console, click Servers > Clusters > WebSphere application server
clusters > cluster\_name.
2. On the Configuration tab, under Container Settings, click Container
Services > Compensation service. This action displays a panel with
the compensation service properties.
3. Make sure that the Enable service at server
startup check box is selected for each server in the cluster.
4. Optional: If necessary, change the compensation
service properties.
5. Click OK.
6. To save your configuration, click Save in the Messages box of the administrative console window.

<!-- image -->