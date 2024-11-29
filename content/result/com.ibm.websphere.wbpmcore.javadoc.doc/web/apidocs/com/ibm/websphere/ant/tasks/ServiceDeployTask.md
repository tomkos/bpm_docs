- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class ServiceDeployTask

- java.lang.Object
    - Task
        - com.ibm.websphere.ant.tasks.ServiceDeployTask

- public final class ServiceDeployTask
extends Task
The serviceDeploy task enables you to generate J2EE application ear files from Service Component Architecture (SCA)
 compliant modules so that they may be installed on a Workflow Server. The SCA modules may be project interchange
 zip files exported from a WebSphere Integration Developer workspace or may be simple jar files that contain an sca module file
 and other supporting artifacts.
 
 Additionally the libraryMode option can be used to enable serviceDeploy to build  libraries without an associated SCA module
 
 The structure of the serviceDeploy task is shown below:
 
 

 
 The scaModule attribute is required and is a qualified name to the archive that is to be deployed.

 The wasHome attribute is optional if WAS\_HOME/bin/ws\_ant is used to run ANT. It is required if ws\_ant
 is not used to run ANT. This attribute is the location of a Workflow Server installation that provides
 the serviceDeploy capabilities.

 The workingDirectory attribute is optional and controls where the directory in which serviceDeploy will generate a temporary workspace.

 The outputApplication attribute is optional and controls the name and location of the generated J2EE ear file. If this attribute is not specified,
 then the ear file will be named according to the sca module name and will be generated in the location from which the ANT process was launched.

 The freeForm attribute is optional and controls whether jsp and html files will be copied from the optional j2ee folder of an sca jar file and copied to the
 generated war file. By default, jsp and html files are not copied into the war file.

 The cleanStagingModules attribute is optional and controls whether imported staging modules should be deleted before running the deployer. By default, imported
 staging modules are not deleted.

 The keep attribute is optional and controls whether the generated workspace should be preserved when the deployer task is complete. By default, the
 generated workspace is deleted after deployment.

 The ignoreErrors attribute is optional and controls whether an ear file should be generated despite validation errors. By default, an ear file will not be
 generated if validation errors were flagged during deployment.

 The classPath attribute is optional and controls which external archives (jar, rar, and zip) should be appended to the classpath. By default, no external archives
 are used during deployment.

 The libraryMode attribute is optional and controls whether serviceDeploy allows a stand-alone library as input.

 The uniqueCellID attribute is optional and may be used to create a unique instance of the application.

 The vmArgs attribute is optional and may be used to specify jvm arguments for the deploy process.

 The debug attribute is optional and may be used to specify a trace .options file to enable tracing.

 The noValidate attribute is optional and may be used to specify whether validation should be skipped.

 The clean attribute attribute is optional and is passed to eclipse so that eclipse will regenerate its stored plugin configuration.

 
 To use this task, add the following to your ANT build.xml
 
 

 
 If this serviceDeploy task is not run from an ANT process launched by $WAS\_HOME/bin/ws\_ant, then ${WAS\_HOME}/plugins/com.ibm.soacore.runtime.jar
 must be on the CLASSPATH and the wasHome attribute must be set.

 
 Copyright IBM Corp. 2011

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String[]
excluded\_props
The jvm launched by the serviceDeploy task is initialized with the ANT process's system properties except for those
 properties listed in the excluded\_props field:

java.assistive,
    java.runtime.name,
    sun.boot.library.path,
    java.vm.version,
    java.vm.vendor,
    java.vendor.url,
    path.separator,
    java.vm.name,
    user.country,
    sun.os.patch.level,
    java.vm.specification.name,
    user.dir,
    java.runtime.version,
    java.fullversion,
    java.awt.graphicsenv,
    java.endorsed.dirs,
    os.arch,
    com.ibm.vm.bitmode,
    java.io.tmpdir,
    line.separator,
    java.vm.specification.vendor,
    user.variant,
    java.awt.fonts,
    os.name,
    sun.java2d.fontpath,
    java.library.path,
    java.specification.name,
    java.class.version,
    invokedviajava,
    java.util.prefs.PreferencesFactory,
    os.version,
    user.home,
    user.timezone,
    java.awt.printerjob,
    java.specification.version,
    java.class.path,
    user.name,
    java.vm.specification.version,
    java.home,
    sun.arch.data.model,
    user.language,
    java.specification.vendor,
    awt.toolkit,
    java.vm.info,
    java.version,
    sun.boot.class.path,
    java.vendor,
    file.separator,
    java.vendor.url.bug,
    java.compiler,
    java.util.logging.configureByServer,
    java.util.logging.manager
 
 Any jvm properties may explicitly be passed by the setVMArgs method.
    - Constructor Summary

Constructors 

Constructor and Description

ServiceDeployTask()
    - Method Summary Methods Modifier and Type Method and Description void execute () This launches the serviceDeploy application in a child jvm, configured according to the user-specified attributes. void setClassPath (java.lang.String classPath) The classPath attribute is optional and is used to specify additional archives (jar, rar, or zip) that must be added to the classpath to successfully generate the J2EE application. void setClean (boolean clean) The clean attribute is optional and is passed to eclipse so that eclipse will regenerate its plugin configuration. void setCleanStagingModules (boolean cleanStagingModules) The cleanStagingModules attribute is optional and controls whether imported staging modules should be deleted before running the deployer. void setDebug (java.lang.String debug) The debug attribute is optional and may be used to specify a .options file to enable tracing . void setFileEncoding (java.lang.String fileEncoding) Deprecated. set the -Dfile.encoding jvm parameter instead void setFreeForm (boolean freeForm) The freeForm attribute is optional and controls whether jsp and html files will be copied from the optional j2ee folder of an sca jar file and copied to the generated war file. void setIgnoreErrors (boolean ignoreErrors) The ignoreErrors attribute is optional and indicates whether an ear file should be exported despite compile or validation errors. void setInternalOptions (java.lang.String internalOptions) void setJavaDebug (java.lang.String javaDebug) Deprecated. no longer applicable void setKeep (boolean keep) The keep attribute is optional and controls whether the generated workspace should be preserved when the deployer task is complete. void setLibraryMode (boolean libraryMode) The libraryMode attribute is optional and controls whether serviceDeploy allows a stand-alone library as input. void setNoJ2EEDeploy (boolean noJ2EEDeploy) Deprecated. no longer applicable void setNoJavaSource (boolean noJavaSource) Deprecated. no longer applicable void setNoValidate (boolean noValidate) The noValidate attribute is optional and may be used to specify whether validation should be skipped. void setOutputApplication (java.lang.String outputApplication) The outputApplication attribute is optional and controls the path and name of the generated ear file. void setProgressMonitor (java.lang.String progressMonitor) Deprecated. no longer applicable void setScaModule (java.lang.String scaModule) The scaModule attribute is mandatory and is the only required attribute for the serviceDeploy task. void setSkipXsdValidate (boolean skipXsdValidate) The skipXsdValidate attribute is optional and may be used to specify whether XSD and WSDL validation should be skipped. void setUniqueCellID (java.lang.String uniqueCellID) The uniqueCellID attribute is optional and may be used to create a unique instance of the application. void setVmArgs (java.lang.String vmArgs) The vmArgs attribute is optional and may be used to specify jvm arguments for the deploy process. void setWasHome (java.lang.String home) The wasHome attribute is optional if WAS\_HOME/bin/ws\_ant is used to run ANT. void setWorkingDirectory (java.lang.String workingDirectory) The workingDirectory attribute is optional and controls where the directory in which serviceDeploy will generate a temporary workspace.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                                                                                         |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                | execute() This launches the serviceDeploy application in a child jvm, configured according to the user-specified attributes.                                                                                                   |
| void                | setClassPath(java.lang.String classPath) The classPath attribute is optional and is used to specify additional archives (jar, rar, or zip) that must be added to the classpath to successfully generate the  J2EE application. |
| void                | setClean(boolean clean) The clean attribute is optional and is passed to eclipse so that eclipse will regenerate its plugin configuration.                                                                                     |
| void                | setCleanStagingModules(boolean cleanStagingModules) The cleanStagingModules attribute is optional and controls whether imported staging modules should be deleted before running the deployer.                                 |
| void                | setDebug(java.lang.String debug) The debug attribute is optional and may be used to specify a .options file to enable tracing .                                                                                                |
| void                | setFileEncoding(java.lang.String fileEncoding) Deprecated.  set the -Dfile.encoding jvm parameter instead                                                                                                                      |
| void                | setFreeForm(boolean freeForm) The freeForm attribute is optional and controls whether jsp and html files will be copied from the optional j2ee folder of an sca jar file and copied to the generated  war file.                |
| void                | setIgnoreErrors(boolean ignoreErrors) The ignoreErrors attribute is optional and indicates whether an ear file should be exported despite compile or validation errors.                                                        |
| void                | setInternalOptions(java.lang.String internalOptions)                                                                                                                                                                           |
| void                | setJavaDebug(java.lang.String javaDebug) Deprecated.  no longer applicable                                                                                                                                                     |
| void                | setKeep(boolean keep) The keep attribute is optional and controls whether the generated workspace should be preserved when the deployer task is complete.                                                                      |
| void                | setLibraryMode(boolean libraryMode) The libraryMode attribute is optional and controls whether serviceDeploy allows a stand-alone library as input.                                                                            |
| void                | setNoJ2EEDeploy(boolean noJ2EEDeploy) Deprecated.  no longer applicable                                                                                                                                                        |
| void                | setNoJavaSource(boolean noJavaSource) Deprecated.  no longer applicable                                                                                                                                                        |
| void                | setNoValidate(boolean noValidate) The noValidate attribute is optional and may be used to specify whether validation should be skipped.                                                                                        |
| void                | setOutputApplication(java.lang.String outputApplication) The outputApplication attribute is optional and controls the path and name of the generated ear file.                                                                 |
| void                | setProgressMonitor(java.lang.String progressMonitor) Deprecated.  no longer applicable                                                                                                                                         |
| void                | setScaModule(java.lang.String scaModule) The scaModule attribute is mandatory and is the only required attribute for the serviceDeploy task.                                                                                   |
| void                | setSkipXsdValidate(boolean skipXsdValidate) The skipXsdValidate attribute is optional and may be used to specify whether XSD and WSDL validation should be skipped.                                                            |
| void                | setUniqueCellID(java.lang.String uniqueCellID) The uniqueCellID attribute is optional and may be used to create a unique instance of the application.                                                                          |
| void                | setVmArgs(java.lang.String vmArgs) The vmArgs attribute is optional and may be used to specify jvm arguments for the deploy process.                                                                                           |
| void                | setWasHome(java.lang.String home) The wasHome attribute is optional if WAS\_HOME/bin/ws\_ant is used to run ANT.                                                                                                                 |
| void                | setWorkingDirectory(java.lang.String workingDirectory) The workingDirectory attribute is optional and controls where the directory in which serviceDeploy will generate a temporary workspace.                                 |

    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait