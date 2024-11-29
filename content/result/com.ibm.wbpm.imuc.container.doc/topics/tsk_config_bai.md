# Configuring event emitters for IBM Business Automation
Workflow on containers

## Procedure

To enable a business event emitter, complete the following steps:

1. Install IBM® Business Automation
Insights by completing the
steps in Installing a Business Automation Insights production
deployment.
2 Log in to OpenShift® ContainerPlatform where IBM Business AutomationInsights is deployed andswitch to the IBM Business AutomationInsights project. Forexample:oc login <URL> --username=<your\_username> --password=<your\_password> oc project <your\_namespace> where:

```
oc login <URL> --username=<your\_username> --password=<your\_password>
oc project <your\_namespace>
```

    - URL is the deployed IBM Business Automation
Insights
OpenShift Container
Platform cluster API
server URL.
    - your\_username is the username of the OpenShift Container
Platform cluster account with
administrator permissions.
    - your\_password is the password for the corresponding username.
3. To enable automatic retrieval of Kafka information, when integrating the Business Automation Insights server with its pod
alongside the Intelligent Task Prioritization
server pod in the same project, set dynamic\_generate\_connection\_info to
true under
shared\_configuration > kafka.
This action enables automatic retrieval of Kafka information, replacing existing connection values.
If set to false, the operator uses provided connection information, regardless of
shared projects. By default, dynamic\_generate\_connection\_info is
false.
4 For manual retrieval of the Kafka service connection information, that you need for theIBM Business AutomationInsights integrationsecret.

1. Get your bootstrap server information: 
oc get kafka iaf-system -o jsonpath='{.status.listeners[?(.name=="external")].bootstrapServers}'
2. Get your Kafka username and password: 
KAFKA\_SECRET=$(oc get kafkauser icp4ba-kafka-auth-0 -o jsonpath='{.status.secret}') 
  oc get kafkauser icp4ba-kafka-auth-0 -o jsonpath='{.status.username}' | base64
  oc get secret ${KAFKA\_SECRET} -o jsonpath='{.data.password}'
3. Get your Kafka CA certificate in the Base64 format: 
oc get kafka iaf-system -o jsonpath='{.status.listeners[?(.name=="external")].certificates[0]}' | base64 -w 0
5. Create the .yaml secret that contains the Kafka client configuration
that is required for connecting to the Kafka server. The connection requires authentication and uses
SSL. All values in the secret must be in the Base64 format.  
For example, your secret might look similar to:
kind: Secret
apiVersion: v1
metadata:
  name: bai-integration-kafka-credential
  namespace: <Business\_Automation\_Workflow\_namespace>
data:
  kafka-password: <Kafka\_password>
  kafka-server-certificate: >-
    <Kafka\_certificate>
  kafka-username: <Kafka\_username>
type: Opaque
Where kafka-server-certificate is the SSL server
certificate.
6 If your custom resource (CR) does not already have the Kafka configuration, add a sectionin the shared\_configuration section of your custom resource (CR) for your Kafkaconnection information. The secret\_name and bootstrap\_servers parameters are required. For example, the Kafka section might look similarto: kafka: secret\_name: "" topic: "" bootstrap\_servers: "" dynamic\_generate\_connection\_info: false where

```
kafka:
  secret\_name: ""
  topic: ""
  bootstrap\_servers: ""
  dynamic\_generate\_connection\_info: false
```

- secret\_name is the name of the secret that you created in the previous
step.
- topic is the name of the topic in the Kafka cluster that is sent business
events. The default value is 'icp4ba-bai-ingress'.
- bootstrap\_servers is a comma-separated list of hosts and ports that connect to
the Kafka cluster. The hosts and ports are in the format
host:port.
- dynamic\_generate\_connection\_info triggers automatic retrieval of Kafka
information, if set to true.
7. If you want to enable the Business Process Modeling Notation (BPMN) event emitter, add
configuration in your CR. For more information about the parameters, see Parameters. For more information about the Business Process Modeling Notation (BPMN) event emitter, see
BPMN summary event formats. The configuration might
look similar
to:    ##  IBM Business Automation Insights integration configuration
    business\_event:
      ## Whether to enable event monitoring for Dynamic Event Framework events for the Workflow Services container.
      ## If Business Automation Insights and the Machine Learning Server parameters are configured, this parameter must be set to true.
      enable: false
      ## Whether to enable the task record in generated events. This optional parameter is equivalent to the task-record-enabled parameter,
      ## Also see https://www.ibm.com/support/knowledgecenter/SSYHZ8\_20.0.x/com.ibm.dba.bai/topics/ref\_bai\_bpmn\_summary\_formats.html
      enable\_task\_record: true
      ## Whether to record additional task information in generated events.
      ## If Business Automation Insights and the Machine Learning Server parameters are configured, this parameter must be set to true.
      ## This parameter is equivalent to the enable\_task\_api\_def parameter.
      ## Also see https://www.ibm.com/support/knowledgecenter/SSYHZ8\_20.0.x/com.ibm.dba.bai/topics/ref\_bai\_bpmn\_summary\_formats.html
      enable\_task\_api: false
      ## List of the subscription configurations. Each subscription attribute is listed in the rest of this table.
      ## app\_name: Name of the application that is the source of the events that are to be monitored.
      ## version: Version of the application to be monitored.
      ## component\_type: Type of the component to be monitored.
      ## component\_name: Name of the component to be monitored.
      ## element\_type: Type of element to be monitored. BPMN types are PROCESS, ACTIVITY, EVENT, and GATEWAY.
      ## element\_name: Name of the element to be monitored.
      ## nature: Nature of the event. One element can send events of various natures, such as STARTED, ACTIVE, COMPLETED.
      ##         The BPMN nature categories are STARTED, COMPLETED, TERMINATED, DELETED, FAILED, CAUGHT, THROWN, EXPECTED, ACTIVE, READY, RESOURCE\_ASSIGNED, ACTIVE, LOOP\_CONDITION\_TRUE, LOOP\_CONDITION\_FALSE, and MULTIPLE\_INSTANCES\_STARTED.
      subscription:
      - {'app\_name': '*','version': '*','component\_type': '*','component\_name': '*','element\_type': '*','element\_name': '*','nature': '*'}
8. If you want to enable the Case event emitter, add a configuration in your CR. For more
information about the parameters, see Parameters. The configuration
might look similar to:event\_emitter:
    ## Target Object Store name of CASE
  - tos\_name: "BAWINS1TOS"
    ## Connection point name for Target Object Store.
    connection\_point\_name: "P8Admins"
    ## Creation date of the events.
    ## The emitter starts processing the events from that date. If a bookmark exists, the emitter ignores this parameter and processes the events from the bookmark.
    date\_sql: "<Required>"
    ## Up to 8-character alphanumeric string without underscores.
    ## This value is always required. While processing, the emitter tracks the events that are processed by using the Content Engine Audit Processing Bookmark with a display name that is based on this value.
    ## Therefore, if the emitter is restarted and if the bookmark exists, the emitter processes the events from the last bookmark.
    logical\_unique\_id: "<Required>"
    ## Comma-separated list of all the case solution names that need to be processed, e.g "solution1, solution2". Default value is "*". Add all the solutions that you want to be processed before you deploy the Case event emitter.
    solution\_list: "*"
    ## Comma-separated list of all the case types that need to be processed, e.g "casetype1, casetype2". Default value is "".
    casetype\_list: ""
    ## Case event emitter batch size. Default value is 1000.
    emitter\_batch\_size: 1000
    ## Whether to process FileNet Process Engine events in addition to IBM Business Automation Workflow events. Default value is true.
    process\_pe\_events: true
9. Apply the changes in the CR by running the following command: 
oc apply -f <Business\_Automation\_Workflow\_standalone\_custom\_resource>