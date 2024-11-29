# Updating the Business Automation Workflow on containers
deployment after an LDAP password change

## Procedure

To change the LDAP admin user password in the Business Automation Workflow deployment,
Log in to the LDAP server as the LDAP admin.
Change the LDAP admin user's password. You also need to update this updated password in the
Business Automation Workflow deployment
to avoid errors, by following the steps described below:

1. Log in to the Administration Console for Content Platform
Engine by using your
LDAP admin user and the updated password. You can find the login URL from the configMaps
"icp4adeploy-cp4ba-access-info" under your namespace.
2. Open the domain properties page for the FileNet P8 domain.
3. Continue to update the password in Process Engine Component Manager in the Administration Console for Content Platform
Engine. Find your TOS
object store, expand Administrative > Workflow
System > Isolated Regions, then expand the isolated
region that you are using and Component Queues, select the queue and update
the password as shown in the following example.
4. Scale down the operator deployment.
5 Wait for Kubernetes (Red Hat OpenShift) to stop the existing pods (the pod terminations mighttake several minutes). You can monitor the status of your pods by using the Red Hat OpenShift orKubernetes command "oc get pods -w" .
    - Content Platform Engine
    - Navigator
    - Workflow server
6. Update appLoginPassword with the new password in the secret
"ibm-fncm-secret" and "ibm-ban-secret".
7. Scale up the operator deployment. Wait for Kubernetes (Red Hat OpenShift) to create the new pods (the pod
creation might take several minutes). You can monitor the status of your pods by using the Red Hat
OpenShift or Kubernetes command "oc get pods
-w".
8. Go to the Navigator pod by running the command "oc exec -it <navigator\_pod>
bash". For example, oc exec -it icp4adeploy-navigator-deploy-5669544494-n76ls
bash, then delete the file "config.ok" under 
/opt/ibm/plugins/properties.
9 Delete the jobs basaut-content-init-job andbas-case-init-job , wait for the operator to reconcile, and create the newjobs. Delete the case init job:

1. Get the content-init-job name: 
oc get job | grep content-init-job
2. Delete the job: 
oc get job <content-init-job-name>

1. Get the case-init-job
name:oc get job | grep case-init-job
2. Delete the job:oc delete job <case-init-job-name>
10. If you have more than one target object store, re-run Register project area or Register target
environment in the Case administration client for each additional
target object store.
11. Restart IBM® Content
Navigator, Content Platform Engine and IBM Business Automation
Workflow pods.