# Installing a production deployment

Containers: 
 Installation
of stand-alone IBM Business Automation
Workflow on
containers uses an operator, which is a Kubernetes feature that makes it simpler to install and
update without having to worry about the underlying cloud provider. However, it is important for
cluster administrators and non-administrators who want to install containers to understand the main
concepts and how you interact with the operator.

For more information, see Quick reference Q&A for production deployments. This topic
is for Cloud Pak, although the information is still useful for stand-alone Business Automation Workflow.

Deployment scripts are provided to significantly reduce the number of configuration steps.

## Before you begin

Prepare your environment and install the necessary software before you go to the GitHub
repositories to find resources to install the IBM certified software. See Planning.

- The scripts can be used only on Red Hat (RHEL), CentOS, and macOS.
- You need a cluster admin or a non-admin user in the OpenShift identity provider to run the
deployment script. For more information about users on OpenShift, see Understanding identity provider configuration.
- You can use an existing project in the cluster or create a namespace by entering a new name with
the setup cluster script. It is likely that you create a namespace when you prepare the operator
storage.
- The deployment script needs a storage class name to use for dynamic storage. The administrator
must make a note of the storage class to use, and provide this name to the user who runs the
deployment script. All the container images require persistent volumes (PVs) and persistent volume
claims (PVCs), so review the topics on preparing these PVs and PVCs. For more information, see Storage considerations.

```
db2set DB2\_COMPATIBILITY\_VECTOR= 
db2stop
db2start
```

## About this task

## Procedure

1. Get the software. You must get access to the Cloud Pak container images before you edit the
custom resource file. The Cloud Native Computing Foundation (CNCF) platform type
or "Other" is the only platform that supports a local image registry in the script to set up the
cluster. The OpenShift® Container
Platform
and Red Hat OpenShift Kubernetes Service (ROKS)  platform types support only the
IBM Entitled Registry in the cluster setup script. For instructions, see Getting access to container images.
2 Set up the cluster. You can set up the cluster in two ways. If you plan to usethe IBM Entitled Registry and use the OpenShift ContainerPlatform (OCP) catalog inOperator Hub, you can set up the cluster with the OCP CLI and console. The OCP catalog helps you todiscover the certified products and services that you can install on your system. You can also usean admin script.
    - You can install the operator from the OpenShift Operator Hub to use the operator lifecycle
manager (OLM) in your deployment. OLM helps you to install, update, and manage the lifecycle of all
operators and services that are deployed in OCP clusters. It is part of the Operator Framework, which is an open source toolkit that is designed to
manage Kubernetes applications in an effective, automated, and scalable way. To prepare the cluster
this way, follow the instructions in Setting up the cluster in the Open Shift console.
    - You can store everything that you must install in stand-alone Business Automation Workflow on a local host and
use this server for your deployment. Follow the instructions in Setting up the cluster for an air gapped (offline) deployment.
    - A cluster administrator user can run a script to set up the cluster. The administrator mustalso provide information that they get from the script to a non-administrator user so they can runthe deployment script. Follow the instructions in Setting up the cluster by running a script .Important:
        - When you are told to download the appropriate repository, go to https://github.com/ibmbpm/BAW-Ctnr/tree/24.0.0/archive and get the latest version of
.tar for Business Automation Workflow. Extract the
contents from the .tar file, Use the tar -xvf command to
extract it to the cert-kubernetes directory.
        - When you run the cluster setup script cp4a-clusteradmin-setup.sh, add a
baw parameter:./cp4a-clusteradmin-setup.sh baw
3. If you want to use SSL-enabled LDAP in your container environment, you must create the SSL
secret with the certificate of the LDAP server. Follow the instructions in Configuring SSL-enabled LDAP.
4 Prepare for Business Automation Workflow on containers beforeyou apply your custom resource. If you used the baw-prerequisites.sh script togenerate the database SQL statement files (scripts) and YAML template files for the databasesecrets, then follow the substeps. Notes: If you did not use thebaw-prerequisites.sh script to generate the database SQL statement files(scripts) and YAML template files for the database secrets, then you must follow the manual substeps as listed.

- You can prepare an installation of Business Automation Workflow, by using the
baw-prerequisites.sh script that is provided in the cert-kubernetes archive of
the CASE package. The script generates property files for the selected capabilities in your
deployment and must be run before your deployment is installed. Follow the instructions in Recommended: Preparing databases and LDAP by running a script.
- Ignore any instructions about Workstream Services,Workforce Insights or FIPS related
parameters. These options are not included in stand-alone Business Automation Workflow.

1. Set up and configure a directory server to provide the authentication
repository.
 See Preparing users and groups.
2. Optional: 
Prepare customized versions of JDBC drivers to use in your production deployments.
See Preparing customized versions of JDBC drivers.
3. Prepare storage, including the persistent volumes (PVs) and persistent volume claim (PVCs) for
the operator, Business Automation Navigator,
FileNet® Content
Manager,
Business Automation Navigator. Java
Message Service (JMS), and Business Automation Workflow.
Note: Ignore the steps about Workforce Insights.
 See Preparing storage.
4. Optional: 
If you have custom case widgets and custom case extensions that you want to configure, see
Preparing your environment for customizations.
5. Optional: 
If you want to see a visual representation of the extended history for a case, see Optional: Enabling the Timeline Visualizer widget to display Business
Automation Workflow process activity flow.
For more information, see Timeline Visualizer widget.
6. Optional: If you want to enable federation or full text search, you need
to prepare for a federated data repository (Elasticsearch or OpenSearch). To prepare storage, see
Preparing storage for a federated data repository. To set up SCC, see Setting up the security context constraint for a federated data repository. If you prefer, you can also use your own external federated data repository. See Referencing your own federated data repository for Business Automation Workflow on containers.Note: Linux on IBM Z must use an external
federated data repository.

1. Set up and configure a directory server to provide the authentication repository.
 See Preparing users and groups.
2. Create databases for Business Automation Workflow, FileNet Content
Manager, and IBM Business Automation
Navigator.
 See Creating required databases.
3. Optional: 
Prepare customized versions of JDBC drivers to use in your production deployments.
See Preparing customized versions of JDBC drivers.
4. Create the database for User Management Service (UMS).
See Preparing the UMS database.
5. Prepare storage, including the persistent volumes (PVs) and persistent volume claim (PVCs) for
the operator, Business Automation Navigator,
FileNet Content
Manager,
Business Automation Navigator. Java Message
Service (JMS), and Business Automation Workflow.
Note: Ignore the steps about Workforce Insights.
 See Preparing storage.
6. Prepare storage for the federated data repository (Elasticsearch or OpenSearch) cluster that is
deployed  for Process Federation Server.
 See Preparing storage for a federated data repository.If you prefer, you can also use your own external
federated data repository. See Referencing your own federated data repository for Business Automation Workflow on containers.
Note: Linux on IBM Z must use an external
federated data repository.
7. Create secrets for LDAP, Business Automation Workflow, Resource Registry, FileNet Content
Manager, and Business Automation Navigator.
 See Creating secrets to protect sensitive configuration
data.
8. Create the secret for User Management Services.
See Creating the UMS database admin secret.
9. Set up SCC for a federated data repository.
 See Setting up the security context constraint for a federated data repository.
10. Optional: 
If you have custom case widgets and custom case extensions that you want to configure, see
Preparing your environment for customizations.
11. Optional: 
If you want to see a visual representation of the extended history for a case, see Optional: Enabling the Timeline Visualizer widget to display Business
Automation Workflow process activity flow.
For more information, see Timeline Visualizer widget.
5. Install the production deployment. You can install the deployment in two ways.
You can set up the cluster with the IBM operator catalog in the OpenShift Operator Hub, or you can
create a custom resource file by running the deployment script or copying a template. Follow the
instructions in Installing the capability.
6. Optional: 
If you want to configure multiple instances, see Configuring multiple instances of Business Automation Workflow and Workstream Services.
7. Verify that you installed the stand-alone Business Automation Workflow correctly.
See Verifying the installation.
8 After installation, extra steps are needed to confirm that the environment workscorrectly.

1. For FileNet Content
Manager, you must do more tasks to configure and start your domain.
See Completing post-installation tasks for FileNet Content
Manager.
2. For User Management Services, you can
perform optional tasks to configure Business Automation Workflow or to use User Management Services, or create a client
application that starts UMS-protected APIs.
See Completing post-deployment tasks for User Management Services.
3. For Business Automation Navigator, you
must do some additional configuration to ensure that the application works with your content
services environment.
See Completing post-installation tasks for Business Automation Navigator.
4. For most deployments on Red Hat OpenShift Kubernetes Service (ROKS), extra steps are needed to
confirm that the environment works correctly.
See Completing extra post-installation tasks on ROKS.
5. To customize Business Automation Workflow to be federated by
Process Federation Server, see
Installing Process Federation Server.
9. You can customize Business Automation Workflow in many ways.
 For example, you can add custom properties to the runtime configuration, provide
certificates for external routes, configure a reverse proxy, configure the Lightweight Directory
Access Protocol (LDAP), enable full text search, and connect with Workflow Center on premises. See
Customizing Business Automation Workflow on containers.

## Results