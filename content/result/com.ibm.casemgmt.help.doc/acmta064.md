# Online deployment of a solution snapshot fails after adding or changing a security manifest

## Symptoms

The online deployment fails with an error that is similar to the following one:

[7/24/20 22:35:15:971 UTC] 000001b1 api I
com.ibm.casemgmt.intgimpl.deploy.handlers.ce.DocumentClassDefinitionHandler getClassDefinition
getClassDefinition superClassSymName:\_Document [7/24/20 22:35:17:031 UTC] 000001b1 api E
com.ibm.casemgmt.intgimpl.messages.CaseMgmtLogger error The method failed because an object or
property is read-only. Read-only property PropertyDefaultString cannot be updated.
com.filenet.api.exception.EngineRuntimeException: FNRCE0057E: E\_READ\_ONLY: The method failed because
an object or property is read-only. Read-only property PropertyDefaultString cannot be updated. at
com.filenet.apiimpl.property.PropertiesImpl.checkSettable(PropertiesImpl.java:699) at
com.filenet.apiimpl.property.PropertiesImpl.checkSettable(PropertiesImpl.java:666) at
com.filenet.apiimpl.property.PropertiesImpl.putValue(PropertiesImpl.java:370) at
com.filenet.apiimpl.core.PropertyDefinitionStringImpl.set\_PropertyDefaultString(PropertyDefinitionStringImpl.java:53)
at
com.ibm.casemgmt.intgimpl.deploy.handlers.ce.CaseClassDefinitionHandler.setExternalDataURI(CaseClassDefinitionHandler.java:224)
at
com.ibm.casemgmt.intgimpl.deploy.handlers.ce.CaseClassDefinitionHandler.getClassDefinition(CaseClassDefinitionHandler.java:149)
at
com.ibm.casemgmt.intgimpl.deploy.handlers.ce.CEClassDefinitionHandler.preLoadClassDefinition(CEClassDefinitionHandler.java:222)
at
com.ibm.casemgmt.intgimpl.deploy.handlers.ce.CaseClassDefinitionHandler.preLoadClassDefinition(CaseClassDefinitionHandler.java:64)
at com.ibm.casemgmt.intgimpl.deploy.handlers.CaseTypeHandler.prePEDeploy(CaseTypeHandler.java:326)
at
com.ibm.casemgmt.intgimpl.deploy.handlers.RootSolutionHandler$26.doStepWork(RootSolutionHandler.java:921)
at com.ibm.casemgmt.intgimpl.deploy.DeploymentStep.carryOutStep(DeploymentStep.java:79) at
com.ibm.casemgmt.intgimpl.deploy.handlers.RootSolutionHandler.deploy(RootSolutionHandler.java:927)
at com.ibm.casemgmt.intgimpl.deploy.SolutionDeployer.deploy(SolutionDeployer.java:224) at
com.ibm.casemgmt.api.admin.DevelopmentSolution$ProcessPendingActivitiesWorker.process(DevelopmentSolution.java:836)
at
com.ibm.casemgmt.api.admin.DevelopmentSolution$BackgroundActivitiesProcessor.execute(DevelopmentSolution.java:667)
at com.ibm.casemgmt.intgimpl.BackgroundWorker$2.run(BackgroundWorker.java:116) at
java.security.AccessController.doPrivileged(AccessController.java:770) at
javax.security.auth.Subject.doAs(Subject.java:570) at
com.ibm.websphere.security.auth.WSSubject.doAs(WSSubject.java:196) at
com.ibm.websphere.security.auth.WSSubject.doAs(WSSubject.java:153) at
sun.reflect.GeneratedMethodAccessor239.invoke(Unknown Source) at
sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:55) at
java.lang.reflect.Method.invoke(Method.java:508) at
com.filenet.apiimpl.util.J2EEUtilWS.doAs(J2EEUtilWS.java:236) at
com.filenet.api.util.UserContext.doAs(UserContext.java:151) at
com.ibm.casemgmt.intgimpl.BackgroundWorker.run(BackgroundWorker.java:113) at
java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1160) at
java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:635) at
java.lang.Thread.run(Thread.java:820)

## Causes

The configured system user that is used for online deployment has not been added to the security
manifest.

## Resolving the problem

1. On the workflow server, launch the IBM Content
Navigator
bawadmin desktop.
2. In the security manifest, add the configured system user (e.g. ECMoC\_Service\_Account).
3. In Workflow Center, deploy another solution snapshot online to the workflow server.