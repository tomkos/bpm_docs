# Design object store extensions

## Choice lists

1. In the domain navigation pane, select the design object store.
2. In the object store navigation pane, click Data
Design > Choice Lists.

| Display name                         | Description                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CmAcmIntegrationTypeChoiceList       | Defines choices for the types of repository in which case documents are stored. By default, this value is set to FileNet® P8 repositories for solutions, project areas, target environments, and target object stores.                                                                                                                        |
| CmAcmRuleTypeChoiceList              | Defines choices that indicate whether a business rule is text-based or table-based.                                                                                                                                                                                                                                                           |
| CmAcmTargetEnvironmentTypeChoiceList | Defines choices that indicate whether the target environment is a development environment or a production environment.                                                                                                                                                                                                                        |
| CmAcmTypeChoiceList                  | Defines choices that indicate the type of a page. The choice list is used by the Type (CmAcmType) property of the Page (CmAcmPage) class.                                                                                                                                                                                                     |
| CmAcmVcsStatusChoiceList             | Defines the choices that indicate the status of the Commit and Deliver actions in Case Builder, which are related to version control system (VCS) integration. The choice list is used by the Commit Status (CmAcmVcsCommitStatus) and Deliver Status (CmAcmVcsDeliverStatus) properties of the VCS Execution State (CmAcmVcsExecutionState). |

## Custom object classes

1. In the domain navigation pane, select the design object store.
2. In the object store navigation pane, click Data
Design > Classes > Custom
Object.

| Display name (symbolic name)                     | Description                                                                                                  |
|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Draft Area (CmAcmDraftArea)                      | Defines an area that contains the saved solution artifact definitions.                                       |
| Solution Lock Control (CmAcmSolutionLockControl) | Defines the definition entries for locks in a solution and tracks the save sequence number for the solution. |

## Document classes

1. In the domain navigation pane, select the design object store.
2. In the object store navigation pane, click Data
Design > Classes > Document.

| Display name (symbolic name)                      | Description                                                                                                                                                                                    |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Connection Definition (CmAcmConnectionDefinition) | Defines the Case Builder or Case Client association with the target environment. One connection definition exists for each target environment to which a case management solution is deployed. |
| Page (CmAcmPage)                                  | Defines a page that contains the widgets that are required to complete a task.                                                                                                                 |
| Rule (CmAcmRule)                                  | Defines a business rule.                                                                                                                                                                       |
| VCS Execution State (CmAcmVcsExecutionState)      | Defines the status of actions that are related to the version control system for a solution, such as commit and deliver.                                                                       |
| View (CmAcmView)                                  | Defines a view for the Properties widget.                                                                                                                                                      |
| Widgets Package (CmAcmWidgetsPackage)             | Defines a package of widgets that can be used in workflows.                                                                                                                                    |

## Folder classes

1. In the domain navigation pane, select the design object store.
2. In the object store navigation pane, click Data
Design > Classes > Folder.

| Display name (symbolic name)           | Description                                                                                                                                                                                                                                                                                            |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ReinitArtifacts (CmAcmReinitArtifacts) | Defines a folder that contains artifacts that are used when the test environment is reset. These artifacts include code modules and documents from the target object store, the manifest of the target environment, and the status of the most recent (current or past) reset of the test environment. |
| Solution Folder (CmAcmSolutionFolder)  | Defines a folder for a solution.                                                                                                                                                                                                                                                                       |