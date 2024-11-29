# Configuring Intelligent Task Prioritization on IBM Business Automation
Workflow on containers

## Before you begin

## Procedure

To configure Intelligent Task Prioritization on stand-alone IBM Business Automation
Workflow on containers, complete
the following steps:

1. Uncomment the baml\_configuration section in the IBM Business Automation
Workflow custom resource (CR)
template.
2. To enable automatic retrieval of OpenSearch information, when integrating the Business Automation Insights server with its pod
alongside the Intelligent Task Prioritization
server pod in the same project, set dynamic\_generate\_connection\_info to
true under baml\_configuration > intelligent\_task\_prioritization > search\_engine. This enables automatic retrieval of OpenSearch
information, replacing existing connection values. If set to false, the operator
uses provided connection information, regardless of shared projects. By default,
dynamic\_generate\_connection\_info is false.
3 For manual retrieval of OpenSearch information, log in to the namespace where IBM Business AutomationInsights is deployed andswitch to the IBM Business AutomationInsights project. Forexample:oc login <URL> --username=<your\_username> --password=<your\_password> oc project <your\_namespace> where:

```
oc login <URL> --username=<your\_username> --password=<your\_password>
oc project <your\_namespace>
```

    - URL is the deployed IBM Business Automation
Insights
OpenShift® Container
Platform cluster API
server URL.
    - your\_username is the username of the OpenShift Container
Platform cluster account with
administrator permissions.
    - your\_password is the password for the corresponding username.
4 Prepare to configure OpenSearch parameters for your secret.

1. Get the OpenSearch server URL by running the following command:
oc get route opensearch-route -o jsonpath='https://{.status.ingress[?(.routerName=="default")].host}'
OpenSearch does not have a specific port number. The default value is 443.
2. Get the Search Engine certificate in the Base64 format by running the following command:

SEARCH\_CERTIFICATION\_SECRET=$(oc get secret -o name | grep ibm-elasticsearch-tls-secret)
oc get ${SEARCH\_CERTIFICATION\_SECRET} -o jsonpath='{.data.ca\.crt}'
3. Get the Search Engine user information by running the following commands:

SEARCH\_INSTANCE=$(oc get ElasticsearchCluster -o name | head -1)
if [[ -z $(oc get $SEARCH\_INSTANCE -o jsonpath='{.spec.credentialSecret}') ]]; then SEARCH\_SECRET=$(oc get secret -o name | grep ibm-elasticsearch-cred-secret); else SEARCH\_SECRET=$(oc get $SEARCH\_INSTANCE -o jsonpath='{.spec.credentialSecret}') ; fi
echo -n elastic | base64  # encoded user name
oc get ${SEARCH\_SECRET} -o jsonpath='{.data.elastic}' # encoded password
5. Create the IBM Business Automation
Machine Learning Server secret that is
required for connecting to the IBM Business Automation
Insights Search Engine
server. 
All values must be in the Base64 format. For example, use the following as a template:
kind: Secret
apiVersion: v1
metadata:
  name: bai-integration-es-credential
  namespace: <BAML\_namespace>
data:
  password: <SearchEngine\_password>
  ca.crt: >-
     <SearchEngine\_certificate>
  username: <SearchEngine\_username>
type: Opaque where ca.crt is the SSL server certificate.
6 Add the Search Engine connection information into the baml\_configuration intelligent\_task\_prioritization section of your CR. The Search Engineadmin\_secret\_name parameter and endpoint are mandatory when youare connecting to stand-alone IBM Business AutomationInsights . For example, thesection looks similar to: search\_engine: endpoint: "" secret\_name: "" dynamic\_generate\_connection\_info: false where

```
search\_engine:
  endpoint: ""
  secret\_name: ""
  dynamic\_generate\_connection\_info: false
```

- endpoint is the search engine endpoint URL that connects to the search engine
cluster. The parameter is in the format https://hostname:port. You can omit the
port value when the value is 443. Configure this parameter to enable a stand-alone
IBM Business Automation
Insights connection.
For
example:endpoint: "https://iaf-system-es-bai.apps.bai.cp.fyre.ibm.com:443"
- secret\_name is the name of the Kubernetes secret that holds the authentication
information that is required for the search engine server. Enter the name of the secret that you
created in the previous step.
- dynamic\_generate\_connection\_info triggers automatic retrieval of OpenSearch
information, if set to true.
7. Enable Intelligent Task Prioritization in the baw\_configuration section
of your CR by changing the value of either show\_task\_prioritization\_service\_toggle
or always\_run\_task\_prioritization\_service to be true.
8. Apply your custom resource by running the following command: 
oc apply -f <Business\_Automation\_Workflow\_CR\_file>