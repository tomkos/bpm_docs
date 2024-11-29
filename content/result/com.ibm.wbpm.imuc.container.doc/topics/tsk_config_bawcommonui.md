# Optional: Enabling Common UI

Common UI enables you to work with content from various sources in one user interface. It
contains Workplace,
which is an user interface application that runs on the Application Engine server and has an desktop
configured in Business Automation Navigator.

To enable Workplace
in the Common UI console, complete the following steps.

1 Prepare the capabilities.
    1. To prepare Application Engine, see
Preparing to install Application Engine.
    2. To enable user former selection in Workplace on Application Engine, you must enable Application Engine data persistence. See Optional: Configuring Application Engine with data
persistence.
    3. To prepare Business Automation Navigator,
see Optional: Configuring Application Engine with data
persistence.
2 Update your IBM® Cloud Pak for BusinessAutomation custom resource toadd Resource Registry , Application Engine , and Business Automation Navigator configuration: For example, after you configure those components, your custom resource might look similarto:apiVersion: icp4a.ibm.com/v1kind: ICP4AClustermetadata: name: icp4deployspec: appVersion: 23.2.0 ibm\_license: accept bts\_configuration: true resource\_registry\_configuration: replica\_size: 1 application\_engine\_configuration: - name: workspace admin\_user: "<Required> " data\_persistence: enable: false database: host: "<Required> " name: "<Required> " port: "<Required> " type: "<Required> " enable\_ssl: "<Required> " db\_cert\_secret\_name: "<Required> " navigator\_configuration: ban\_secret\_name: ibm-ban-secret datasource\_configuration: dc\_ssl\_enabled: "<Required> " dc\_icn\_datasource: dc\_database\_type: "<Required> " dc\_common\_icn\_datasource\_name: "ECMClientDS" database\_servername: "<Required> " database\_port: "<Required> " database\_name: "<Required> " database\_ssl\_secret\_name: "<Required> " dc\_oracle\_icn\_jdbc\_url: "<Required> "

1. To configure Application Engine, see
Configuring Application Engine. For Application Engine parameters, see Application Engine parameters.
2. To configure Business Automation Navigator, see Configuring Business Automation Navigator. For Business Automation Navigator parameters, see IBM Business Automation Navigator parameters.

```
apiVersion: icp4a.ibm.com/v1
kind: ICP4ACluster
metadata:
  name: icp4deploy
spec:
  appVersion: 23.2.0
  ibm\_license: accept
  bts\_configuration: true
  resource\_registry\_configuration:
    replica\_size: 1
  application\_engine\_configuration:
  - name: workspace
    admin\_user: "<Required>"
    data\_persistence:
      enable: false
    database:
      host: "<Required>"
      name: "<Required>"
      port: "<Required>"
      type: "<Required>"
      enable\_ssl: "<Required>"
      db\_cert\_secret\_name: "<Required>"
  navigator\_configuration:
    ban\_secret\_name: ibm-ban-secret
  datasource\_configuration:
    dc\_ssl\_enabled: "<Required>"
    dc\_icn\_datasource:
      dc\_database\_type: "<Required>"
      dc\_common\_icn\_datasource\_name: "ECMClientDS"
      database\_servername: "<Required>"
      database\_port: "<Required>"
      database\_name: "<Required>"
      database\_ssl\_secret\_name: "<Required>"
      dc\_oracle\_icn\_jdbc\_url: "<Required>"
```

3. Apply the custom resource and wait a few minutes for your resources to initiate.
4. Run oc get icp4acluster -o yaml to make sure that Resource Registry, IBM Business Automation Application, and Business Automation Navigator are ready. Make sure
that the status of .status.components.prereq.rootCAStatus is
ready, .status.components.prereq.rootCASecretName contains the
correct secret name, and .status.endpoints["Resource Registry"] appears in the
endpoints list.
5. Complete your Application Engine
configuration by completing the steps in Completing post-installation tasks for Application
Engine.
6. Complete your Business Automation Navigator configuration by completing the steps in Completing post-installation tasks for Business Automation
Navigator.
7. Wait a few minutes for the Process Federation Server operator to
create the Workplace
<PFSCRName>-workplace-job.