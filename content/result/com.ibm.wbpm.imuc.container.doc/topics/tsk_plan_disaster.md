# Planning for disaster recovery

Containers: 
Prepare your
IBM® Business Automation
Workflow container
environment to support disaster recovery.

## Procedure

Complete the following steps:

1 Prepare the environment to support disaster recovery:
    1. Set up an IBM Db2®
high availability disaster recovery (HADR) primary node and secondary node across the primary
environment and the secondary environment. When a disaster happens, the secondary environment can
work with the Db2
secondary node.
    2. Use the shared storage across the primary environment and the secondary environment. The storage
is used for the Persistence Volume (PV).
    3. Back up the secure definition that used to protect the configuration data in the primary
environment.
    4. Back up the PV and Persistent Volume Claim (PVC) definitions used in the primary
environment.
    5. Back up the customer resource (CR) definition used to deploy in the primary environment.
2. Set up the secondary environment following the instructions in Preparing for a production deployment, so that the secondary
environment can be used to deploy Business Automation Workflow.
3. On the secondary environment, use the backup secure definition to create the same security as
the primary environment uses.
4. On the secondary environment, use the backup PV and PVC definition to create the PV and PVC
that access the shared storage.
5 Prepare the CR definition for the secondary environment:

1 The following host names might be different between the primary environment and secondaryenvironment. Modify them if they are different.
    - Router host name
    - Redis server host name
2. If the number of Kubernetes worker nodes are different between the primary environment and
secondary environments, modify the elasticsearch\_configuration.anti\_affinity
parameter to make these values the same.
3. Reuse the folders and files that were created with a specified UID in the primary environment
for the secondary environment by updating the
shared\_configuration.sc\_run\_as\_user paramter in the CR definition to be the
same UID as the primary environment uses.
6 Deploy the secondary environment: Important: Don't start the primary environment and secondary environment at the sametime.

- If necessary, use the Db2 secondary nodes to take
over the Db2 workload
from the Db2 primary
node.
- Deploy the secondary environment with the modified CR definition.