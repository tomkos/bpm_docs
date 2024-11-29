# Setting up the cluster by running a script

## Before you begin

Make sure that you prepared your cluster with the necessary infrastructure and software. For more
information, see Installing a production deployment.

## About this task

The cluster setup script is one of four core scripts (cluster setup, prerequisites, deployment,
and post-install) that are provided to help you install the Business Automation Workflow capabilities. You
must be a cluster administrator to run the setup script. For more information, see Cloud Pak roles and personas.

The cluster setup script identifies or creates a namespace and applies the custom resource
definitions (CRD). It then adds the specified user to the ibm-cp4a-operator role,
binds the role to the service account, and applies a security context constraint (SCC) for Business Automation Workflow.

The script also prompts the administrator to take note of the cluster hostname and a dynamic
storage class on the cluster. These names must be provided to the user who runs the deployment
script.

A new installation of Business Automation Workflow always includes a
namespace-scoped instance of foundational services when you use the scripts.

Use the following steps to complete the setup.

## Procedure

1. Download the appropriate repository to a Linux based
machine (RHEL) or a client to a linux-based machine or VM that runs Podman natively. 

For more information about downloading cert-kubernetes, see Installing a production deployment.
2. Optional: If you want to run the script in silent mode, create the
environment variables that are needed for your installation. For more information, see Environment variables for silent mode
installation.
3. Log in to the target cluster as the <cluster-admin> user.

Using the Red Hat OpenShift command line interface (CLI), use the following command.
oc login https://<cluster-ip>:<port> -u <cluster-admin> -p <password>
On Red Hat OpenShift Kubernetes service (ROKS), if you are not already logged in, use the
following command.
oc login --token=<token> --server=https://<cluster-ip>:<port>
4. Change the directory to the extracted cert-kubernetes/scripts
folder. 
cd ${PATH\_TO\_EXTRACTED\_FILES}/cert-kubernetes/scripts
5 Run the cluster setup script and follow the prompts in the command window. ./cp4a-clusteradmin-setup.sh baw

```
./cp4a-clusteradmin-setup.sh baw
```

    1. Select the platform type: ROKS (1) or OCP (2).
    2. Select the deployment type production.
    3. If you want to install Business Automation Workflow as a private catalog
rather than in the global catalog namespace (GCN), select Yes. The GCN uses the
operator-marketplace namespace, the private option uses the target namespace of
your Business Automation Workflow
deployment. The default is No.When you enable a private catalog, provide a new
or existing project name (for example - cp4ba-project) for the deployment namespace. Choose a
non-admin user on your cluster. For more information, see Preparing a namespace for the Cloud Pak operator. If an
existing Cloud Pak for Business Automation
operator is found in another project on your cluster, confirm that you want to deploy another
Cloud Pak for Business Automation operator in the
new project by entering Yes. Install a Cloud Pak for Business Automation operator in each
namespace where you want to install a Cloud Pak for Business Automation deployment.
When
you select No to enable a private catalog, then enter the name for a new project or
an existing project (cp4ba-project) for the target deployment namespace. Then
choose an existing user on your cluster. A non-admin user is recommended.
    4. Enter Yes or No to confirm whether you want to use
the images in the IBM Entitlement Registry.
    5. If you replied Yes to use the IBM Entitlement Registry, enter your IBM
Entitled Registry key and login credentials (user and password). If you want to load the
container images to a local registry, then set up the cluster by mirroring the images instead of
running the cp4a-clusteradmin-setup.sh script. For more information, see Setting up the cluster and use a local image
registry.
Tip: If you ran the cp4a-clusteradmin-setup.sh
script and you see one or more of the following messages, then make sure that you start Docker or
Podman and run the script
again.Error saving credentials: error storing credentials
Error: unable to connect
The Entitlement Registry key failed
6. Monitor the operator pods until they show a STATUS of 'Running'.

oc get pod -w
Tip: If ibm-cp4a-operator is inactive for some time, you can delete
the operator pod and reconcile it. To confirm that the operator is stuck, check to see whether
the log is providing an output.

oc project <namespace of Business Automation Workflow operator>
NAMESPACE=$(oc project -q)
podname=$(oc get pod -n $NAMESPACE | grep ibm-cp4a-operator | awk '{print $1}')
oc logs $podname -f
You can also list the ClusterServiceVersion (CSV) to verify the version of the
running operators on your cluster.
oc get csv -n $NAMESPACE
Note: The version number (23.2.0) of the installed operator corresponds to the channel for Business Automation Workflow
23.0.2.
If you set any subscriptions to manual, then you must approve any pending
operator updates. It is not recommended to set subscriptions to manual because the
installation can be error prone when some of the dependency operators are not approved. By default,
all subscriptions are set to automatic.
Tip: Subscriptions for the Cloud Pak foundational services operators are created when
they are "needed". Some subscriptions are created during the installation of the operators. If other
subscriptions are needed, they are created during the installation of the Business Automation Workflow deployment. Business
Teams Service, for example, is installed only "if it is needed". To check for subscriptions that are
waiting for approval, get the installation plans by running the following
command.oc get installPlan

## Results

When the script is finished, the available storage class names are displayed along with the
infrastructure node name. Take a note of the following information and provide it to the Business Automation Workflow admin user as they
are needed for the deployment script:

1. Project name or namespace.
2. Username to log in to the cluster.

## What to do next

You can see the list of operators that are installed in your cluster on the Operators  > Installed Operators page.

To verify the foundational services installation, check whether all the pods in the target
Business Automation Workflow deployment
namespace are running. Use the following command:

```
oc get pods -n $NAMESPACE
```

Continue to prepare everything that you need for each capability that you want to install in
Recommended: Preparing databases and LDAP by running a script.