# Verifying the installation of IBM Business Automation
Workflow on containers

## Procedure

1. Wait for about 45 minutes, depending on your computer's performance. Then, check the status of
the pods. Get the names of the pods that were deployed by running the following command:

oc get pod -n my\_project

The following example shows a successful pod status. The pods are all running or completed,
depending on their type.
NAME                                                        READY   STATUS      RESTARTS   AGE 
bawstandalone-bawins1-baw-case-init-job-wglb9               0/1     Completed   1          23h
bawstandalone-bawins1-baw-content-init-job-f5pwt            0/1     Completed   1          23h
bawstandalone-bawins1-baw-db-init-job-w8kfz                 0/1     Completed   0          23h
bawstandalone-bawins1-baw-jms-0                             1/1     Running     0          23h
bawstandalone-bawins1-baw-ltpa-d85xb                        0/1     Completed   0          23h
bawstandalone-bawins1-baw-oidc-registry-job-jz4nj           0/1     Completed   0          23h
bawstandalone-bawins1-baw-server-0                          1/1     Running     0          7h35m
bawstandalone-cmis-deploy-69f8b5d64c-hsfcz                  1/1     Running     0          22h
bawstandalone-cpe-deploy-55886bd44d-6jmkq                   1/1     Running     0          23h
bawstandalone-dba-rr-e52b17d1a9                             1/1     Running     0          23h
bawstandalone-graphql-deploy-79978bcb57-bhv8s               1/1     Running     0          23h
bawstandalone-navigator-deploy-7c65849f4b-pj4xf             1/1     Running     0          23h
bawstandalone-rr-backup-28616585-dzhgs                      0/1     Completed   0          4m26s
bawstandalone-rr-setup-pod                                  0/1     Completed   0          23h
bawstandalone-ums-scim-deployment-78594868dc-2db82          1/1     Running     0          23h
bawstandalone-ums-scim-deployment-78594868dc-cnk7g          1/1     Running     0          23h
bawstandalone-ums-sso-deployment-6585c57457-6xllt           1/1     Running     0          23h
bawstandalone-ums-sso-deployment-6585c57457-gr69g           1/1     Running     0          23h
bawstandalone-ums-teams-deployment-6dfd6bd7c-2zjnp          1/1     Running     0          23h
bawstandalone-ums-teams-deployment-6dfd6bd7c-zkm2b          1/1     Running     0          23h
ibm-content-operator-7c4d6c698d-kbjzp                       1/1     Running     0          23h
ibm-cp4a-operator-699675ddcf-r68zp                          1/1     Running     0          7h40m
ibm-pfs-operator-74676566fb-56ngd                           1/1     Running     0          23h
ibm-workflow-operator-5d7d665465-tf5wz                      1/1     Running     0          23h
2. To check the deployment status and see the containers that were created and started, run the
following command with the specific namespace:

cert-kubernetes/scripts/baw-std-healthcheck.sh -n <namespace>
3. For each pod, check under Events to see that the images were successfully pulled. Check whether
the containers were created and started, by running the following command with the specific pod
name.

oc describe pod pod\_name -n my\_project
4 Get the URLs and log in to Process Portal , Case Client , and Workplace . Use either of thefollowing methods to get the URL of the web applications and the user credentials to log in. If you are using self-signed certificates, you must first go to the following URL and acceptthe self-signed certificate:
    - Access the Config Maps from the Red Hat OpenShift web console.
        - Log in to your cluster web console.
        - Select your namespace.
        - In the left window, select Workloads > Config Maps.
        - Find cp4ba-access-info. You can get dashboard information from
workflow-server-access-info.
        - Access Process Portal,
Case Client, and Workplace by using the URLs in
workflow-server-access-info.
- Access Process Portal , Workplace , andCase Client .
    - Process Portal URL:
https://workflow\_hostname/ProcessPortal where
workflow\_hostname corresponds to the
baw\_configuration.hostname property in your custom resource file.
    - Workplace URL:
https://workflow\_hostname/Workplace where
workflow\_hostname
 corresponds to the baw\_configuration.hostname property in your custom
resource file.
    - Case Client URL:
https://navigator\_hostname/navigator where
navigator\_hostname corresponds to the
navigator\_configuration.hostname property in your custom resource file.

- https://workflow\_hostname where
workflow\_hostname corresponds to the
baw\_configuration.hostname property in your custom resource file.
5 Check the status and endpoints for Business Automation Workflow from the Red HatOpenShift console or from the command line.

- Check the status and endpoints from the Red Hat OpenShift console.
    1. In the left menu, select Operators > Installed Operators.
    2. In the beginning of the right window, select your project (namespace).
    3. Click the installed operator for IBM Cloud Pak for Business
Automation.
    4. Go to the CP4BA deployment tab page.
    5. Click your deployment (for example, icp4adeploy).
    6. Go to the YAML tab page.
    7. Find the top level status: element. Then check every component status. For
example:  status:
                         components:
                                ...
                               baw:
                                 bawDeployment: Ready
                                 bawService: Ready
                                 bawZenIntegration: Ready
                               baml:
                                 bamlDeployment: Ready
                                 bamlService: Ready
                                 ...
    8. Under status: search for endpoints, then check the endpoints.
For example:endpoints:
                       ...
                       - name: BAW Login URL
                         scope: External
                         type: UI
                         uri: 'https://baw-bawins1-tensor.apps.bawdev-large-x100.cp.fyre.ibm.com/ProcessPortal'
                         ...
    9. You can also check the endpoints in the Details page.

- Check the status and endpoints from the command line.
    1. To get your deployment name, run the following
command:oc get ICP4ACluster -n <your\_project>
    2. To get the deployment YAML and check the status and endpoints, run the following
command:  oc get ICP4ACluster icp4adeploy -o yaml