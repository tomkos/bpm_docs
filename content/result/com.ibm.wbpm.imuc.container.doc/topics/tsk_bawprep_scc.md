# Setting up the security context constraint for a federated data repository

## About this task

The pods that are running the federated data repository require the hosting worker nodes to be
configured to disable swapping and increase the limit on the number of open file descriptors.

- You must disable memory swapping on all worker nodes by setting the sysctl
value vm.swappiness to 1. See Disable swapping for Elasticsearch.
- You must increase the limit on the number of open file descriptors for the user that is running
Elasticsearch or OpenSearch by setting the sysctl value
vm.max\_map\_count to 65,536 or higher. See File descriptors.

```
oc get scc
```

## Procedure

To update the worker node configuration, choose one of the following
options:

- Option 1: (Recommended) If you are allowed to run privileged containers, let the privilegedcontainer update the worker node configuration.
    1. Create a service account that is named ibm-es-service-account and ask the
cluster administrator to add the system-privileged SCC to the newly created service account in the
current namespace by running the following commands in
order:# Create a new service account named ibm-es-service-account
oc create serviceaccount ibm-es-service-account

# Add system-privileged security context constraint (SCC) to the newly created service account
oc adm policy add-scc-to-user privileged -z ibm-es-service-account -n <namespace\_name>
    2. In your custom resource file, set the value of the
elasticsearch\_configuration.privileged property to true and set
the value of the elasticsearch\_configuration.service\_account property to the newly
created service account ibm-es-service-account. The node configuration will be
updated by using a privileged init container, which will run the appropriate sysctl
commands.elasticsearch\_configuration:
  ...
  privileged: true
  service\_account: ibm-es-service-account
  ...
- Option 2: If privileged containers are not allowed and the
elasticsearch\_configuration.privileged property is set to false in the custom
resource configuration file, ask the cluster administrator to run a command like the following
sample command to change the memory swapping and descriptor properties on each worker node:

sysctl -w vm.max\_map\_count=262144 && sed -i '/^vm.max\_map\_count /d' /etc/sysctl.conf && echo 'vm.max\_map\_count = 262144' >> /etc/sysctl.conf && sysctl -w vm.swappiness=1 && sed -i '/^vm.swappiness /d' /etc/sysctl.conf && echo 'vm.swappiness=1' >> /etc/sysctl.conf