# Simple disaster recovery

In situations that can tolerate periodic planned system outages, stop the primary system, and
ensure that all resources are consistent. Then, copy all the configuration data and runtime data
from the primary data center to a secondary data center and restore the data in the secondary data
center.

In such a setup (see Figure 1), Business Automation Workflow is configured to communicate with
Content Platform Engine. The document object operation that case solutions or other applications
request stores objects in the Content Platform Engine. The file storage area stores the related
objects for the Content Platform Engine. The shared folder shares the information between the
Business Automation Workflow clusters and the Content Platform Engine clusters. During the
configuration, the host address information or related information is persisted into the
configuration data for the engine to use. After the system is restored in the secondary data center,
the servers in the secondary data center must use the same configuration data and use the same
hostname to configure the host address or related items. The hostnames and directory locations from
the primary data center must be available in the secondary data center.

Figure 1. Simple disaster recovery

- Installation and configuration

For installation and configuration considerations, hostname and folders are required.