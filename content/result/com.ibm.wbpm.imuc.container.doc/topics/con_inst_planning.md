# Planning for IBM Business Automation
Workflow on containers

## System requirements

Business Automation Workflow on
containers is based on Red Hat Universal Base Images (UBI) and is Red Hat certified and IBM
certified. To use the Business Automation Workflow images, you must
understand what to do before you install the operator.

The cluster administrator must check the system requirements and make sure that the system can
host and run the deployment. The administrator and the installer (non-administrator user) should
plan the deployment together.

- Kubernetes 1.25 and later
- Kubernetes command line interface (CLI). For more information, see Install and Set Up kubectl. You must use a kubectl version that is within one minor version
difference of your cluster. Using the latest version of kubectl helps avoid unforeseen issues.
Download the latest release with the following
command:curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl" 
To check the version, run the following command:kubectl version --client
- The OpenShift Container Platform (OCP) CLI version that matches the OCP cluster. The CLI has
commands for managing your applications, and lower-level tools to interact with each component of
your system. For more information, see Get Started with the CLI for OpenShift and the
download link. Place the oc binary in a directory that is on your PATH. To check your PATH,
run the following command:echo $PATH When the CLI is in your PATH, it is
available by running the oc command.
- Podman CLI. You can install Podman (the Pod Manager) by running the following command:
yum -y install podmanIf you plan to run the scripts on macOS or you want to
use Docker instead of the Podman CLI, you must install the Docker CLI and add the following line to
the /etc/sysconfig/docker
file:INSECURE\_REGISTRY='--insecure-registry=route' where
route is the name of the route for your image registry. For example,
INSECURE\_REGISTRY='--insecure-registry=default-route-openshift-image-registry.apps.'
Use this solution only for isolated testing or in tightly controlled environments. For more
information, see Deploy a plain HTTP registry.
- An instance of Lightweight Directory Access Protocol (LDAP) for production installation. You can
use either IBM Security Directory Server or Microsoft Active Directory. For more information, see
LDAP configuration.
- Dynamic storage created and ready. For more information, see Storage considerations.
- At least one non-administrator user that can be used to run the deployment script, for example
baw-user.

- Cluster hardware architecture: Intel (AMD64 or x86\_64 the 64-bit edition for Linux x86) on all
platforms, or Linux on IBM Z (s390x) or Linux on IBM Power (ppc64le).
- Node counts: Dual compute nodes for non-production and production clusters. A minimum of three
nodes is needed for medium and large production environments. All cluster configuration needs to
adapt to the size of the projects and the workload that is expected.

| Component                        | CPU                                                                                      | Memory                                                                              | Storage   |
|----------------------------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-----------|
| IBM Business Automation Workflow | 1 control plane with 4 CPUs 1 infrastructure node with 4 CPUs 3 worker nodes with 4 CPUs | 26 Gi on the control plane 8 Gi on the infrastructure node 7 Gi on each worker node | 110 GB    |

## Hardware requirements

See System requirements for hardware resources required for each
capability in small, medium, and large deployment
profiles.

## Storage considerations

See Storage considerations.

## Security considerations

See Security considerations.

## Logging considerations

By default, logging is enabled in your cluster and the logs are stored in a dedicated persistent
data store. You can also collect and forward the standard output stdout logs from
the containers to help you troubleshoot issues and improve their health and performance. See Logging considerations.

## Image tags or digests

For a production installation, choose between image tags or digests. To make sure that a
container always uses the same version of an image, you can specify its digest instead of an image
tag. The digest identifies a specific version of the image, so it is never updated by Kubernetes.
See Choosing image tags or digests.

## Disaster recovery

- Backing up and restoring an IBM Business Automation Workflow container environment

 Containers: 
To protect the environment from data loss and corruption, back up data for the dependency components, such as User Management Service, IBM Process Federation Server, IBM Business Automation Workflow, IBM Content Navigator, Content Platform Engine, Resource Registry, and JMS, deployed in the environment.
- Planning for disaster recovery

 Containers: 
Prepare your IBM Business Automation Workflow container environment to support disaster recovery.