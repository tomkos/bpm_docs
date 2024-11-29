# Enabling full text search for Business Automation Workflow on
containers

## About this task

If you want to enable full text search, you need to prepare for a federated data repository
(Elasticsearch or OpenSearch).

## Procedure

1 To prepare for the external federated data repository:
    1. Prepare storage. For more information, see Preparing storage for a federated data repository.
    2. Set up the security context constraint (SCC). For more information, see Setting up the security context constraint for a federated data repository.
    3. Apply a ProcessFederatedSystem CR. 
apiVersion: icp4a.ibm.com/v1
kind: ProcessFederationServer
metadata:
  name: elasticsearchdeploy
spec:
  appVersion: 23.2.0
  #ibm\_license: accept
  license:
    accept: true
  shared\_configuration: 
    #root\_ca\_secret: icp4a-root-ca
    sc\_deployment\_license: production
    sc\_delivery\_type: baw
    sc\_deployment\_context: BAW
    storage\_configuration:
      sc\_fast\_file\_storage\_classname: <required>
      sc\_medium\_file\_storage\_classname: <required>
      sc\_slow\_file\_storage\_classname: <required>
      sc\_deployment\_hostname\_suffix: <required>
  elasticsearch\_configuration:
    ## - disable memory swapping by setting the sysctl value vm.swappiness to 1.
    ## - increase the limit on the number of open files descriptors for the user running Elasticsearch by setting sysctl value vm.max\_map\_count to 65,536 or higher.
    ## When set to true, a privileged init container will execute the appropriate sysctl commands to update the worker node configuration to match Elasticsearch requirements.
    ## When set to false, you must ask the cluster administrator to change the memory swapping and descriptor properties on each worker node.
    privileged: <required>
    ## If elasticsearch\_configuration.privileged is set to true, you must create a service account that has the privileged SecurityContextConstraint to allow running 
    ## privileged containers. See "Preparing SecurityContextConstraints (SCC) requirements" at knowledge center for instructions.
    ##
    ## If elasticsearch\_configuration.privileged is set to false, see "Preparing SecurityContextConstraints (SCC) requirements" at knowledge center for instructions.
    ## Under above condition, you do not need input service account, then default service account "{{ meta.name }}-elasticsearch-service-account" will be created.
    service\_account: <required>
2. Add the connection information in the IBM Business Automation
Workflow CR.

baw\_configuration:
- elasticsearch:
      endpoint: <required>
      admin\_secret\_name: <required>
  full\_text\_search:
      enable: true 
To get the endpoint and admin secret, run the following
command.oc get pfs elasticsearchdeploy -o=jsonpath='{.status.endpoints[?(@.name=="Elasticsearch Internal https URL")].uri}'
oc get secret|grep elasticsearchNote: If you are using your own
federated data repository, the admin secret must contain two keys: username and
password.
3. Apply the updated IBM Business Automation
Workflow CR.