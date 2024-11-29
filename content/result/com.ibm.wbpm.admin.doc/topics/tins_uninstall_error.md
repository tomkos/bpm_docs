# Uninstalling multiple server and tooling products causes errors

## Types of errors and warnings

The types of
errors or warnings you receive vary, depending on the combination
of products that you attempt to uninstall:

- If you uninstall server and tooling products (for example, IBM Integration
Designer, IBM Business Process Manager
Advanced, IBM Workflow
Server Test
environment, and IBM Process
Designer)
at the same time, you might see the following errors:2195 ERROR 01:13:39.22 **PAKENGINE** ERROR: NGIAction.execute : null 
2197 ERROR 01:13:39.50 **PAKENGINE** ERROR: PakInstaller.installPak : null 
2199 ERROR 01:13:39.76 **PAKENGINE** ERROR: The [UNINSTALL] PAK operation failed. Error: null 
2201 INFO 01:13:40.12 **PAKENGINE** INFO: PAK action ends - Operation: UNINSTALL PAK file: C:\Program Files (x86)\IBM\WebSphere\AppServer\_5\_9b\properties\version\nif\backup\atlas.client.pak. 
2202 ERROR CRIMABA65E664E 01:13:40.12 Unexpected exception
- If you uninstall tooling products (for example, IBM Integration
Designer and
Forms Designer 4.0) and the IBM Workflow
Server Test
Environment at the same time, you might see the following warnings:Failed to delete C:\AppServer\bin 
1437 WARNING CRIMC9CB8AE9AW 39:48.47 Failed to delete C:\AppServer\BPM 
1438 WARNING CRIMC9CB8AE9AW 39:48.53 Failed to delete C:\AppServer\configuration 
1439 WARNING CRIMC9CB8AE9AW 39:48.61 Failed to delete C:\AppServer\features 
1440 WARNING CRIMC9CB8AE9AW 39:48.68 Failed to delete C:\AppServer\java 
1441 WARNING CRIMC9CB8AE9AW 39:48.75 Failed to delete C:\AppServer\lib 
1442 WARNING CRIMC9CB8AE9AW 39:48.83 Failed to delete C:\AppServer\links 
1443 WARNING CRIMC9CB8AE9AW 39:48.98 Failed to delete C:\AppServer\logs 
1444 WARNING CRIMC9CB8AE9AW 39:49.06 Failed to delete C:\AppServer\optionalLibraries 
1445 WARNING CRIMC9CB8AE9AW 39:49.14 Failed to delete C:\AppServer\ProcessChoreographer 
1446 WARNING CRIMC9CB8AE9AW 39:49.22 Failed to delete C:\AppServer\profiles 
1447 WARNING CRIMC9CB8AE9AW 39:49.45 Failed to delete C:\AppServer\properties 
1448 WARNING CRIMC9CB8AE9AW 39:49.53 Failed to delete C:\AppServer\scriptLibraries 
1449 WARNING CRIMC9CB8AE9AW 39:49.61 Failed to delete C:\AppServer\systemApps 
1450 WARNING CRIMC9CB8AE9AW 39:49.68 Failed to delete C:\AppServer\temp 
1451 WARNING CRIMC9CB8AE9AW 39:49.76 Failed to delete C:\AppServer
- If you uninstall tooling products and server product packages
(for example, IBM Integration
Designer,
the IBM Workflow
Server Test
Environment, and IBM Process
Designer)
at the same time, you might see the following errors:java.lang.IllegalStateException: No metadata found for installed IU com.ibm.wid.splashpath..com.ibm.wid.splashpath.set 6.1.0.v20071130\_1200.
com.ibm.cic.agent.internal.core.InstallRegistry$ProfileInstallRegistry.getInstalledIU(InstallRegistry.java:1064)
com.ibm.cic.agent.internal.core.InstallRegistry$ContextInstallRegistry.getInstalledIU(InstallRegistry.java:845)
com.ibm.cic.agent.internal.core.InstallRegistry$ContextInstallRegistry.getInstalledIU(InstallRegistry.java:845)
com.ibm.cic.agent.internal.core.InstallRegistry$ContextInstallRegistry.addInstalledIUs(InstallRegistry.java:834)
com.ibm.cic.agent.internal.core.InstallRegistry$ContextInstallRegistry.getInstalledIUs(InstallRegistry.java:826)
com.ibm.cic.agent.core.InstallContextTree.computePairs(InstallContextTree.java:205)
com.ibm.cic.agent.core.InstallContextTree.getPairs(InstallContextTree.java:181)
com.ibm.cic.agent.internal.core.MetadataReplacer.extractMetadataReplacementPairs(MetadataReplacer.java:123)
com.ibm.cic.agent.internal.core.MetadataReplacer.extractMetadataReplacementPairs(MetadataReplacer.java:114)
com.ibm.cic.agent.internal.core.MetadataReplacer.replace(MetadataReplacer.java:84)
com.ibm.cic.agent.internal.core.Director.expandAndQualify(Director.java:1167)
com.ibm.cic.agent.internal.core.Director.getSizeInfo(Director.java:231)
com.ibm.cic.agent.internal.core.Director.getSizeInfo(Director.java:173)
com.ibm.cic.agent.core.Agent.getSizeInfo(Agent.java:2446)
com.ibm.cic.agent.core.SpaceInfoUtils.getTotalSizeInfo(SpaceInfoUtils.java:212)
com.ibm.cic.agent.core.SpaceInfoUtils.getEclipseCacheLocationSizeListMap(SpaceInfoUtils.java:106)
com.ibm.cic.agent.core.SpaceInfoUtils.validateAvailableSpace(SpaceInfoUtils.java:268)
com.ibm.cic.agent.core.AgentUtil.validateJobs(AgentUtil.java:158)
com.ibm.cic.agent.core.Agent.uninstall(Agent.java:1550)
com.ibm.cic.agent.core.Agent.uninstall(Agent.java:1595)
com.ibm.cic.agent.internal.ui.wizards.UninstallWizard.performTask(UninstallWizard.java:113)
com.ibm.cic.agent.internal.ui.wizards.AgentUIWizard$2.run(AgentUIWizard.java:467)
com.ibm.cic.common.ui.internal.parts.ProgressPart$ProgressJob.run(ProgressPart.java:104)
org.eclipse.core.internal.jobs.Worker.run(Worker.java:54)

## Resolving the problem