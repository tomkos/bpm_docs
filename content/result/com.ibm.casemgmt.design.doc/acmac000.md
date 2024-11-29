# Command syntax

The syntax topics uses several conventions to indicate
variable, parameters, required items, and optional items. Enter all
commands on a single line, even if the command or syntax examples
wrap to the next line.

```
command\_name -option\_1 variable\_1 [-option\_2 variable\_2]
 [-option\_3 variable\_3 | -option\_4]
```

- addPrincipals command

The addPrincipals command adds a user or group to a project area. Users who are not assigned to a project area cannot log in to Case Builder.
- addSolutions command

The addSolutions command adds a solution to a project area. A solution can belong to only one project area.
- applySolutionAuditManifest command

The applySolutionAuditManifest command applies a solution audit configuration that you previously created by using the administration client. The solution must be deployed before you apply the audit configuration. You must specify a target environment if the solution is in a production environment.
- applySolutionSecurityManifest command

The applySolutionSecurityManifest command applies a solution security configuration that you have previously created by using the IBM® Business Automation Workflow administration client. The solution must be deployed before you apply the security configuration. You must specify a target environment if the solution is in a production environment.
- checkStatus command

The checkStatus command checks the status of the specified configuration task.
- createCaseAnalyzerStore command

The createCaseAnalyzerStore command creates and enables a Case Analyzer store for use with the IBM Case Monitor Dashboard.
- createCaseHistoryStore command

The createCaseHistoryStore command creates and enables an event case history for use with extended case history features. For example, if you want to view the progression of a case over time by using the Timeline Visualizer widget, you must create and enable a case history store.
- defineProjectArea command

The defineProjectArea command defines a new project area for the development environment. You use project areas to limit the effects of resetting the test environment. You can define new project areas or define a default project area if you did not run the Define the Default Project Area task when you configured IBM Business Automation Workflow.
- deleteProjectArea command

The deleteProjectArea command deletes a project area from the development environment. You cannot delete the default project area or a project area that has solutions assigned to it.
- execute command

The execute command applies the settings from a configuration XML file for the specified configuration task.
- execute\_sa command

The execute\_sa command applies the values in the input file to copy a solution, create a solution from a template, convert a solution to a template, or list the properties and document classes in an object store.
- exportSolution command

The exportSolution command exports a solution or a solution template to a solution package to prepare for importing the solution or template to another workflow environment.
- exportSolutionAuditManifest command

The exportSolutionAuditManifest command exports a list of audit configurations that are associated with a solution to prepare for importing the audit configurations to another IBM Business Automation Workflow environment.
- exportSolutionSecurityManifest command

The exportSolutionSecurityManifest command exports a list of security configurations that are associated with a solution to prepare for importing the security configurations to another IBM Business Automation Workflow environment.
- generateConfig command

The generateConfig command generates one or more configuration XML files for the specified configuration task to configure an IBM Business Automation Workflow application.
- generate\_input\_sa command

The generate\_input\_sa command generates the input file for copying a solution, creating a solution from a template, converting a solution to a template, or listing the properties and document classes in an object store.
- generateObjectStoreDataMap command

The generateObjectStoreDataMap command generates the object store data map for mapping the object stores that are contained in a solution package to the appropriate object stores in the target environment.
- generateServiceDataMap command

The generateServiceDataMap command creates the service data map XML file for importing a solution or solution template into another environment.
- gui command

The gui command opens the IBM Business Automation Workflow Case configuration tool  graphical user interface. The graphical user interface presents the same functions as the command-line version, but with dialogs and fields for editing the properties and settings.
- importSolution command

The importSolution command imports a case management solution or solution template package into another environment.
- importSolutionAuditManifest command

The importSolutionAuditManifest command imports an audit   configuration package from one environment into another environment.
- importSolutionManifest command

The importSolutionManifest command imports a case management solution from a version control system into another environment by using a manifest and a set of files.
- importSolutionSecurityManifest command

The importSolutionSecurityManifest command imports a security   configuration package from one environment into another environment.
- listPrincipals command

The listPrincipals command lists the users and groups that are assigned to a project area. Users who are not assigned to a project area cannot log in to Case Builder.
- listSolutions command

The listSolutions command lists the solutions that are assigned to a project area.
- listTasks command

The listTasks command displays a list of the activities and the activity files in the configuration profile.
- modifyProjectArea command

The modifyProjectArea command changes the project area description or connection point.
- moveTask command

The moveTask command moves an activity to a different position in the list of activities. The activity position determines the order that the activities are run when you run all the activities at the same time. You use the listTasks command to show the activity order.
- removePrincipals command

The removePrincipals command removes a user or group from a project area. Users who are not assigned to a project area cannot log in to Case Builder.
- removeSolutions command

The removeSolutions command removes a solution from a project area. When you remove a solution from a project area, the solution is automatically added to the default project area.
- removeTask command

The removeTask command removes the specified activity from the configuration profile. When you remove the activity, the configuration XML file is deleted from the profile directory. You cannot recover an activity file that has been deleted from a profile.
- storePasswords command

The storePasswords command prompts for passwords that are blank in a profile and stores the encrypted passwords in the file. Storing encrypted passwords might not be FIPS 140-2 compliant, and you can cancel the command after the prompt about compliance.
- test command

The test command runs the test feature for a task or a profile environment. Some tasks do not have a test function.