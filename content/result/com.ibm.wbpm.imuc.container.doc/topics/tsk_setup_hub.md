# Setting up the cluster in the Open Shift console

## About this task

IBM provides operators to OpenShift in the form of catalogs. A catalog is added to an OpenShift
cluster by using a CatalogSource resource. After you apply the
CatalogSource resources, the IBM catalogs appear in the OperatorHub of the OCP
console.

## Procedure

1. Log in to your OCP or ROKS cluster as a cluster administrator.  To allow a
non-administrator user to create the Cloud Pak operators, see Allowing non-cluster administrators to install
Operators.
2 Add the CatalogSource resources to Operator Hub for the versions thatyou want to install. Each interim fix has a specific version and unique digest, which are needed forthe new catalog sources.
    1. To import the YAML into your cluster in the OCP Admin console: # Click the plus icon at the top
of the console. The Import YAML editor opens.
    2. Attach the below catalog source yaml apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: ibm-operator-catalog
  namespace: openshift-marketplace
spec:
  displayName: "IBM Operator Catalog"
  image: icr.io/cpopen/ibm-operator-catalog
  publisher: IBM
  sourceType: grpc
  updateStrategy:
    registryPoll:
      interval: 45m
3. In the OCP console, click Operators to open the
OperatorHub, and then enter Business Automation Workflow
in the Filter by keyword box under All items.
4 Click the Business Automation Workflow on containers catalog item, andclick Install .

1. In the Create Operator Subscription wizard, select the corresponding
channel version.
2. The default mode is All namespaces on the cluster, but you can select
A specific namespace on the cluster under Installation
Mode and select a namespace from the Installed namespace drop-down
list to install in a single or the operator's own namespace. 

Select the NAMESPACE that you created and prepared for the operator
(cp4ba-project). The Cloud Pak operator can be installed in multiple
namespaces, but you must prepare each namespace beforehand. For more information, see Preparing a namespace for the Cloud Pak operator.
Important: Before you install the operators, check for existing installations of the
Business Automation Workflow on Containers. If there are existing operators that are installed in
the openshift-operators namespace, then you must continue to use the All
namespaces on the cluster option. If there are existing operators that are installed in
specific namespaces but not in the openshift-operators namespace, then you must
continue to use the A specific namespace on the cluster option.The
oc get csv -A command shows all the operator installations.
3. Click Install.
4. In the Installed Operators view, verify the status of the
Business Automation Workflow on Containers installation.
5 Verify the Business Automation Workflow on containers operator are running. Tip: If the Cloud Pak operator is inactive for some time, you can delete the operatorpod and let it reconcile.

1. On the left panel in the OCP console, click
Operators > Installed
Operators.
2. Make sure that all the installed operators have the status "Succeeded" in your selected
NAMESPACE:The OLM is now aware of the operators. A ClusterServiceVersion (CSV)
for the operators appear in the target namespace, and APIs provided by the operators are available
to use.

## What to do next

When started, you can monitor the operator logs with the following commands. Where the
NAMESPACE is the project (cp4ba-project) that you created and prepared for the
operator. For an all namespaces installation, the namespace is always
openshift-operators.

```
oc project NAMESPACE
oc logs -f deployment/ibm-cp4a-operator -c operator
```

When the operator is deployed successfully, get the role of the operator to give access to a
specified user.

```
oc get role | grep ibm-cp4a-operator | sort -t"t" -k1r | awk 'NR==1{print $1}'
```

Run the following commands for each specified user that you want to give permission to create a
CP4BA deployment.

```
oc project NAMESPACE
oc adm policy add-role-to-user edit <user\_name> 
oc adm policy add-role-to-user registry-editor <user\_name>
oc adm policy add-role-to-user <role\_name> <user\_name> 
oc adm policy add-cluster-role-to-user icp4aclusters.icp4a.ibm.com-v1-crdview <user\_name>
```

Where <role\_name> is the name of the role that you got
from running the oc get command, and the NAMESPACE is the
project (cp4ba-project) that you created and prepared for the CP4BA deployment.

You can see the list of operators that are installed in your cluster on the Operators  > Installed Operators page.