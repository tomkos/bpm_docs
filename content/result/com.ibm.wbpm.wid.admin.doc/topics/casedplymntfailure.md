<!-- image -->

# Deploying case solution fails with NullPointerException

When deploying the case solution snapshot by using REST API, the deployment fails with
NullPointerException and the following error is displayed:

FNRPA0949E An attempt to reindex case instances to Elasticsearch after a deployment
has failed.

## About this task

com.ibm.casemgmt.intgimpl.deploy.DepLog > err() ENTRY
org.apache.commons.logging.impl.Jdk14Logger@91e678fc
com.ibm.casemgmt.intgimpl.deploy.SolutionDeployer

$SubHandlerContextImpl@933baa2d
A0949E.DEPLOYMENT\_ELASTICSEARCHINDEXING\_FAILED

[2024-05-21T17:23:42.080+0000]

0000011e id=00000000
com.ibm.casemgmt.intgimpl.messages.CaseMgmtLogger > warn() ENTRY
org.apache.commons.logging.impl.Jdk14Logger@91e678fc null java.lang.NullPointerException

at
com.ibm.casemgmt.intgimpl.utils.PFSIndexerHelperLiberty.getRoleMembershipDetails

(PFSIndexerHelperLiberty.java:840)
at
com.ibm.casemgmt.intgimpl.utils.PFSIndexerHelperLiberty.initiatePartialIndexingOperation

(PFSIndexerHelperLiberty.java:159)
at

com.ibm.casemgmt.intgimpl.deploy.SolutionDeployer.deploy(SolutionDeployer.java:287)
at
com.ibm.casemgmt.api.admin.DevelopmentSolution$ProcessPendingActivitiesWorker.process

(DevelopmentSolution.java:851)
at
com.ibm.casemgmt.api.admin.DevelopmentSolution$BackgroundActivitiesProcessor.execute(DevelopmentSolution.java:682)
at com.ibm.casemgmt.intgimpl.BackgroundWorker$2.run(BackgroundWorker.java:116) at
java.security.AccessController.doPrivileged(AccessController.java:783)

at javax.security.auth.Subject.doAs(Subject.java:570) at

com.ibm.websphere.security.auth.WSSubject.doAs(WSSubject.java:174)
at com.ibm.websphere.security.auth.WSSubject.doAs(WSSubject.java:140)

at sun.reflect.GeneratedMethodAccessor230.invoke(Unknown Source)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:55)

ï»¿[2024-05-21T17:23:42.276+0000] 0000011e id=00000000

com.ibm.casemgmt.intgimpl.messages.Message <getText() RETURN

An attempt to reindex case instances to Elasticsearch after a
deployment has failed..

This problem occurs when a user who is assigned a Case
membership no longer exists in the Lightweight Directory Access Protocol (LDAP). To resolve this
error, you need to delete the case membership permissions of the deleted user from the assignment
table by using IBM Administration Console for
Content Platform Engine.

## Procedure

1. Using IBM Administration Console for
Content Platform Engine, go to
Search > New Object Store
search.
2. Use the Assignment Base Class and retrieve the list of
users.
3. Verify the users who are deleted from LDAP.
4. Select the users and delete by using bulk actions.