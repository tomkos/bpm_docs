# Upgrading Process Federation Server

If you installed Process Federation Server 23.0.2 or
22.0.2, you can upgrade to the latest Process Federation Server. There was no
Process Federation Server on
containers in 21.0.3, so to upgrade from 21.0.3, you must install a new Process Federation Server.

## Before you begin

Starting from IBM® Business Automation
Workflow
23.0.2, Elasticsearch is replaced with OpenSearch. This transition does not bring about any user
interface alterations, including custom resource (CR) parameters, statefulset name, and similar
aspects. However, extra steps must be taken for migration as part of the upgrade process.

## Procedure

To upgrade to the latest Process Federation Server, complete the
following steps:

1 For upgrading from 22.0.2 only: Prepare for migration from Elasticsearch toOpenSearch.
    1 Export saved searches before the upgrade. Note: Only users with theadminSavedSearch role can export a saved search. For more information aboutdefining custom authorizations for Process Federation Server users, seeSpecifying Process Federation Server user authorizations onKubernetes .
        1 Call the {PFS\_BASE\_URL}rest/bpm/federated/v1/searches/transfer REST API toexport the saved searches, where PFS\_BASE\_URL can be found by running thecommand:oc get pfs -o=jsonpath='{.items[0].status.endpoints[?(@.name=="Process Federation Server External base URL")].uri}' For more information about the REST API, see REST interface for IBM Process Federation Server resources .The JSON response of this REST API call contains the two following attributes:

```
oc get pfs -o=jsonpath='{.items[0].status.endpoints[?(@.name=="Process Federation Server External base URL")].uri}'
```

            - Status provides the response HTTP status.
            - Results contain all the exported saved searches.
    2. Save the content of the results attribute as a .json file, that you will use
after the upgrade to re-import the saved searches.
2. Scale down Process Federation Server operator
deployment to
0.oc scale deployment ibm-pfs-operator -\-replicas=0
3. Scale down Elasticsearch replicas to
0.oc scale sts <custom-resource-name>-elasticsearch-statefulset -\-replicas=0
4. Back up the data in the Elasticsearch persistent volume claim (PVC). Remove all data in the PVC,
or delete the PVC directly. To get the Elasticsearch PVC, run the following
command:oc get pvc|grep elasticsearch
2 Upgrade your deployment base operator by completing the steps in Upgrading CP4BA multi-pattern clusters from 21.0.3 . Upgradethe base operator before you update the Process Federation Server YAML customresource (CR) file.

- To prevent connection problems during the upgrade, make sure to update your passwords for your
database and directory service provider (LDAP) that are close to expiring.
- When you upgrade from any version, you can upgrade the operator and keep the container image
tags from the previous version.
3. Upgrade the operators to the new version before you apply your custom resource upgrades,
see step 3 in Upgrading on containers.
4 Open the YAML CR file that you used to install Process Federation Server .

- Change the spec.appVersion parameter value in the spec section to the new
version.
- Compare the new custom resource template under descriptors or patterns (for example,
template ibm\_cp4a\_cr\_production\_FC\_process\_federation\_server.yaml) with the custom
resource template that you used to install. Change the image.tag parameter values
in all sections to the new version. Where required, add mandatory parameters to the file and provide
specific values for parameters that previously used the default value.
- Update the properties in the CR file. For more information about parameters, see Parameters.
- If your environment does not support dynamic provisioning and you have
pfs\_configuration.logs.storage.use\_dynamic\_provisioning set to false, you must
create a persistent volume (PV) and persistent volume claim (PVC) for Process Federation Server. Follow the
instructions in the step about creating the Process Federation Server PV and PVC in
Prepare for Process Federation Server. Then, update the
pfs\_configuration.logs.storage.existing\_pvc\_name parameter in the custom resource
to add the PVC name.
- Apply the changed CR file by running the following command:
oc apply -f your\_custom\_resource\_name
5 Verify your Process Federation Server deployment:

1. Verify the configuration of your applications and the status of your pods by running
the following command: 
oc get pods -w
2. Verify the instance details in the CR status fields of the components by running the
following command: 
oc get pfs  <cr\_instance\_name> -o yaml
3. Verify your upgrade to 23.0.2 by running the following command and making sure that
the value of Cloud Pak Version is 23.0.2: 
oc get statefulset | grep pfs
oc get csv|grep ibm-pfs-operator
4. Get your Process Federation Server REST base URL
by running the
command:  oc get pfs -o=jsonpath='{.items[0].status.endpoints[?(@.name=="Process Federation Server External base URL")].uri}'
To access the Process Federation Server REST APIs, see
The Process Federation Server REST APIs
6 For upgrading from 22.0.2 only: Complete migration from Elasticsearch toOpenSearch. The step requires that Business Automation Workflow is federated.

1 Get the User Management Service (UMS) token.
    - Gather the Process Federation Server
UMS\_CLIENT\_ID and UMS\_CLIENT\_PASSWORD from the
<icp4bacluster-instance-name>-pfs-secret-custom Kubernetes secret in
ums.xml property.
    - Request an access token from UMS by calling the following API (the example that is given hereuses curl on the command-line):curl -k -u UMS\_CLIENT\_ID:UMS\_CLIENT\_PASSWORD -X POST -d "grant\_type=password&scope=openid&username=PFS\_USERNAME&password=PFS\_PASSWORD" https://UMS\_SSO\_BASE\_URL/oidc/endpoint/ums/token Where:

```
curl -k -u UMS\_CLIENT\_ID:UMS\_CLIENT\_PASSWORD -X POST -d "grant\_type=password&scope=openid&username=PFS\_USERNAME&password=PFS\_PASSWORD" https://UMS\_SSO\_BASE\_URL/oidc/endpoint/ums/token
```

Where:

        - PFS\_USERNAME and PFS\_PASSWORD are the credentials of the user
for which you request an access token.
        - UMS\_SSO\_BASE\_URL is the location of the
<icp4bacluster-instance-name>-ums-sso-route Kubernetes route in your Workflow
deployment.
2. Import saved searches after the upgrade.Call the POST
PFS\_BASE\_URL/rest/bpm/federated/v1/searches/transfer  REST API, with the
fieldValidationBypass parameter set to true, to import the previously exported
saved searches. For more information about this REST API, see REST interface for IBM Process Federation Server
resources.
A curl command-line example that calls this API to import the saved
searches, previously exported to an exported.json file, by using the UMS access
token to authenticate against Process Federation Server:
curl -k -H "Authorization: Bearer $UMSTOKEN" -H "Content-Type: application/json" -X POST -d @exported.json PFS\_BASE\_URL/rest/bpm/federated/v1/searches/transfer?fieldValidationBypass=true
3. Rebuild the federated systems indexes after the upgrade. After the update, the Process Federation Server business
process definition (BPD) indexers automatically rebuild the federated BPD systems indexes in the new
OpenSearch cluster. Reindexing the case federated systems data must be explicitly triggered by using
the case indexing REST API. For more information about the case indexing REST API, see Indexing case instances.

## What to do next