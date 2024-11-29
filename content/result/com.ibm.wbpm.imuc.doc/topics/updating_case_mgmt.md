# Enabling the case management features

## About this task

## Procedure

To enable the features required for case management:

1. Run the following command to point the network shared directory to a folder: 
BPMConfig.bat|sh -update -profile DmgrProfileName -de DE\_NAME -networkDirectory NETWORK\_DIRECTORY -component CaseManager

The network shared directory contains the case management properties files and
must be accessible to all the application cluster members in the deployment environment. Specify the
full path to the network shared directory.Important: The network shared directory must
be accessible to each server in the deployment environment for the case management features to work
properly.

During configuration of the deployment environment, the
rulesRepo folder is created under the
BAW\_install\_root/CaseManagement/properties default network
shared directory. If you use a different directory as the network shared directory, make sure the
rulesRepo folder exists under the directory you use.
2. To enable IBM
FileNet® Process Designer,
see Configuring IBM Business Automation Workflow to use the stand-alone IBM FileNet Process Designer.
3. To use a version control system (VCS) for your case solutions, run the following command to
enable this feature: 

BPMConfig.bat|sh -update -profile DmgrProfileName -de DE\_NAME -enableVCS true -component CaseManager [-vcsSandboxPath vcsSandboxPath -vcsHeartbeatInterval vcsHeartbeatInterval -vcsCommitTimeout vcsCommitTimeout -vcsDeliverTimeout vcsDeliverTimeout [-vcsAdditionalParameters vcsAdditionalParameters] 

This command takes the following values:
enableVCS true | false
The enabled or disabled state of version control system (VCS) integration. The default value is
false, which means that VCS integration is not enabled and none of the other
parameters apply.
vcsSandboxPath
Enter the fully qualified path to the sandbox to be used for version control system integration.
If IBM Case Manager is in a cluster environment, the sandbox must be on a shared file system that is
available to all nodes in the cluster.
vcsHeartbeatInterval
Enter the time in seconds that must elapse between periodic updates from a version control
system integration commit or deliver script before the commit or deliver operation is marked as a
failure. The default value is 60. If you do not specify a value, the
heartbeat is disabled.
vcsCommitTimeout
Enter the time in seconds for a version control system integration commit script to run before
the commit operation is marked as a failure. The default value is 120.
vcsDeliverTimeout
Enter the time in seconds for a version control system integration deliver script to run before
the deliver operation is marked as a failure. The default value is 600.
vcsAdditionalParameters
Enter any additional parameters for version control system integration that users are to be
prompted for during a commit or deliver. Separate the parameters with commas as follows:
VCS ID,Project Name,Approving Manager

For more information, see Integrating with a version control system (VCS).
4 To use IBM Forms inyour case solutions, run the following command to enable this feature: BPMConfig.bat|sh -update -profile DmgrProfileName -de DE\_NAME -caseForms -type ibmForms [-ibmFormsRenderApp ibmFormsRenderApp -translatorURL translatorURL -ibmFormsDirectory ibmFormsDirectory ] This command takes the following values:type eForms | ibmForms To integrate IBM Forms into your case solutions, specify ibmForms , which means that both IBM Forms and IBMFileNet eForms for P8 are enabled. The defaultvalue is eForms , which means that only IBMFileNet eForms for P8 is enabled and none ofthe other parameters apply. ibmFormsRenderApp The IBM Forms renderingapplication that displays forms to the user. The valid values are: translatorURL The IBM Forms translator URL. ibmFormsDirectory The IBM Forms directorywhere IBM Forms isinstalled. Specify the full path to the directory. The default directory is C:\ProgramFiles\IBM\Forms Server\8.0 . Note: You can ignore this step if you do not intend to use IBM Forms . If you do not run thisstep, the Component Health Center shows a red X for Case. Important: IBM Forms can be enabledwhen you are using the embedded IBM Content Navigator. Once setExternalNavigator command is used, IBM Forms is disabled and cannot be enabled for an external IBM ContentNavigator configuration.

```
BPMConfig.bat|sh -update -profile DmgrProfileName -de DE\_NAME -caseForms -type ibmForms [-ibmFormsRenderApp ibmFormsRenderApp -translatorURL translatorURL -ibmFormsDirectory ibmFormsDirectory]
```

    - html - Use the Webform Server Translator for rendering. You must specify
the Webform Server Translator URL.
    - xfdl - Use the viewer for rendering. The viewer renders a form in raw
format without converting it to HTML.
    - autoDetect - Automatically detect the rendering application. Specify this
value if you do not know which component is installed.

IBM Forms can be enabled
when you are using the embedded IBM Content Navigator. Once setExternalNavigator
command is used, IBM Forms
is disabled and cannot be enabled for an external IBM Content
Navigator
configuration.

## Related information

- BPMConfig command-line utility
- Configuration properties for the BPMConfig command