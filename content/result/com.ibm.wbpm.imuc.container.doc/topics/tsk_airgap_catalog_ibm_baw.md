# Installing the Cloud Pak catalog and an operator instance

## Before you begin

When you mirrored your environment, you created a parallel offline version of everything that you
needed to install an operator into the OpenShift® Container
Platform. Your deployment in an
air gap environment also needs IBM Cloud® Pak foundational
services, so make sure that your cluster has capacity to install these services, see Hardware requirements and recommendations for foundational
services.

## About this task

Prepare the storage of the operator before you create an instance of the operator.

To install the operator, complete the following steps.

## Procedure

1. Go to the namespace for the operator that you created in Option 2: Mirroring images to a private registry using oc image mirror. 

oc project ${NAMESPACE}
2. Set the environment variable of the --inventory parameter: 
export CASE\_INVENTORY\_SETUP=cp4aOperatorSetup
3. Create and configure a catalog source. 
Note: If the IBMPAK\_HOME environment variable is
set, the downloaded CASE (Container Application Software for Enterprise) is located in
$IBMPAK\_HOME/.ibm-pak/data/mirror/$CASE\_NAME/$CASE\_VERSION/catalog-sources.yaml.
 run the following command.
cat $HOME/.ibm-pak/data/mirror/$CASE\_NAME/$CASE\_VERSION/catalog-sources.yaml | oc apply -f -
4. Verify that the CatalogSource for Cloud Pak for Business Automation and its
dependencies are created.
Run the following command for the GCN:oc get pods -n openshift-marketplace
oc get catalogsource -n openshift-marketplaceRun the following command for the target
CP4BA namespace
(cp4ba-project):
oc get pods -n <CP4BA\_namespace>
oc get catalogsource -n <CP4BA\_namespace>

Check that the following pods are recently
created:ibm-operator-catalog-xsv6z
Check that the catalog sources are recently created.
5. Install the Cloud Pak operator. 
oc ibm-pak launch $CASE\_NAME \
--version $CASE\_VERSION \
--inventory $CASE\_INVENTORY\_SETUP \
--action install-operator \
--namespace $NAMESPACE
6 Verify that the operators are installed. Using the oc login command, log in to the Red Hat OpenShift ContainerPlatform cluster where you planto pull the mirrored images. You can identify your specific oc login by clickingthe user drop-down menu in the Red Hat OpenShift ContainerPlatform console, then clickingCopy Login Command . Run the following commands to check your cluster: It might take up to 15 minutes for all the pods to show the Running status.

Using the oc login command, log in to the Red Hat OpenShift Container
Platform cluster where you plan
to pull the mirrored images. You can identify your specific oc login by clicking
the user drop-down menu in the Red Hat OpenShift Container
Platform console, then clicking
Copy Login Command.

Run the following commands to check your cluster:

    1. oc get pods -n $NAMESPACE
It might take up to 10 minutes or so for all the pods to show the Running
status. 
Tip: If ibm-cp4a-operator is inactive for some time, you can delete
the operator pod and wait for it to reconcile. To confirm that the operator is stuck, check to
see whether the log is providing an output.

oc logs <operator pod> -fIf you see the following issues when
the image is pulled, verify the global pull secret. Also, confirm that the docker registry username
and password are
correct.
Warning Failed <invalid> (x2 over <invalid>) kubelet Error: ImagePullBackOff
Normal Pulling <invalid> (x2 over <invalid>) kubelet Pulling image
The
following command verifies the global pull secrets.

oc -n openshift-config get secret/pull-secret -o jsonpath='{.data.\.dockerconfigjson}' | base64 --decode | tr -d "\r|\n| " > dockerconfig.jsonTo
change the credentials, you can edit the dockerconfig.json file, delete the
registry entries for the registry, and then apply the
changes.
oc set data secret/pull-secret -n openshift-config --from-file=.dockerconfigjson=dockerconfig.json
    2. oc get subscriptions.operators.coreos.com -n $NAMESPACE
If you set any subscriptions to manual, then you must approve any pending
operator updates. It is not recommended to set subscriptions to manual because it
can make the installation error prone when some of the dependency operators are not approved. By
default, all subscriptions are set to automatic.
Tip: Subscriptions for the Cloud Pak foundational services operators are created when
they are "needed". Some subscriptions are created during the installation of the operators. If other
subscriptions are needed, they are created during the installation of the Business Automation Workflow deployment. Business
Teams Service, for example, is installed only "if it is needed". To check for subscriptions that are
waiting for approval, get the installation plans by running the following
command.oc get installPlan
    3. oc get csv -n $NAMESPACE

It might take up to 15 minutes for all the pods to show the Running status.

## Results

When started, you can monitor the operator logs with the following command.

```
oc logs -f deployment/ibm-cp4a-operator -c operator
```

## What to do next

Before you prepare the capabilities that you want to install, you must unpack the
cert-kubernetes repository archive.

```
cd $IBMPAK\_HOME/.ibm-pak/data/cases/$CASE\_NAME/$CASE\_VERSION
tar -xvzf ibm-cs-bawautomation-2.6.0.tgz
cd ibm-cs-bawautomation/inventory
cd cp4aOperatorSdk/files/deploy/crs
tar -xvf 23.0.2.tar
cd cert-kubernetes/scripts/
```

Then, use the instructions on how to prepare your cluster for the capabilities
that you want to install. For more information, see Installing a production deployment.