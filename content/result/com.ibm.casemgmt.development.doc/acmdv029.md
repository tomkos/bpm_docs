# Target object store extensions

## Choice lists

1. In the domain navigation pane, select the target object store.
2. In the object store navigation pane, click Data
Design > Choice Lists.

| Display name                                | Description                                                                                                                        |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| CmAcmActionChoiceList                       | Defines choices that indicate the type of a comment.                                                                               |
| CmAcmAuditConfigurationStateChoiceList      | Defines choices that indicate the status of an applied audit configuration.                                                        |
| CmAcmCaseStateChoiceList                    | Defines choices that indicate that state of a case folder.                                                                         |
| CmAcmDeploymentStateChoiceList              | Defines choices that indicate the deployment state of a deployed solution folder.                                                  |
| CmAcmDisabledStateChoiceList                | Defines choices that indicate the disabled state of an activity.                                                                   |
| CmAcmGroupModeChoiceList                    | Defines choices that indicate whether an activity is not grouped, in an exclusive group, or in an inclusive group.                 |
| CmAcmIntegrationTypeChoiceList              | Defines choices that indicate the type of repository with which Business Automation Workflow is integrated.                        |
| CmAcmLaunchModeChoiceList                   | Defines choices that indicate the launch mode state of an activity.                                                                |
| CmAcmPreconditionStateChoiceList            | Defines choices that indicate the state of an activity precondition.                                                               |
| CmAcmRelationshipTypeChoiceList             | Defines choices that indicate the type of relationship between two cases.                                                          |
| CmAcmRequiredStateChoiceList                | Choice items for the possible required states for a case activity.                                                                 |
| CmAcmSecurityConfigurationStateChoiceList   | Defines choices that indicate the status of an applied security configuration.                                                     |
| CmAcmTargetEnvironmentTypeChoiceList        | Defines choices that indicate whether the target environment is a development environment or a production environment.             |
| CmAcmTriggerTypeChoiceList                  | Defines choices that indicate the trigger type for an activity type.                                                               |
| CmAcmUserLaunchedTaskWorkflowTypeChoiceList | Defines choices that indicate whether a workflow is a Content Platform Engine workflow or a Business Automation Workflow workflow. |
| IcnRepositoryTypeChoiceList                 | Defines choices that indicate the type of workflow repository that is used for an external document.                               |

## Custom object classes

1. In the domain navigation pane, select the target object store.
2. In the object store navigation pane, click Data
Design > Classes > Custom
Object.

| Display name (symbolic name)                                         | Description                                                                                      |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Deployed Activity Type Info (CmAcmDeployedTaskTypeInfo)              | Represents an activity type that is deployed for a solution.                                     |
| Precondition Checker Parameters (CmAcmPreconditionCheckerParameters) | Tracks the options and filters that are passed as parameter values for the precondition checker. |
| Task Workflow Parameters (CmAcmTaskWorkflowParameters)               | Represents the mapping of the parameters that are used in an activity workflow.                  |

## Document class

1. In the domain navigation pane, select the target object store.
2. In the object store navigation pane, click Data
Design > Classes > Document.

| Display name (symbolic name)            | Description                                                                                               |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------|
| External Document (IcnExternalDocument) | Represents a document that is stored in a repository other than this case management target object store. |

## Folder classes

1. In the domain navigation pane, select the target object store.
2. In the object store navigation pane, click Data
Design > Classes > Folder.
3. For certain classes, expand the parent class as indicated in the following table.

| Display name (symbolic name)                 | Description                                                                                                                                                                                                                                               |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Base Case (CmAcmBaseCase)                    | Represents the base abstract class for the Case Folder and Case Subfolder classes.                                                                                                                                                                        |
| Case Folder (CmAcmCaseFolder)                | Represents the base, abstract class for Case Folder instances. The Case Folder class is the class from which subclasses for case types that are part of a solution are derived. To view this class, click Base Class in the object store navigation pane. |
| Case Subfolder (CmAcmCaseSubfolder)          | Represents a subfolder under a Case Folder instance. To view this class, click Base Class in the object store navigation pane.                                                                                                                            |
| Case Type Subfolder (CmAcmCaseTypeSubfolder) | Represents a folder that is used to enable security inheritance from a Deployed Case Type folder down to a Case folder.                                                                                                                                   |
| Deployed Case Type (CmAcmDeployedCaseType)   | Represents a Case Type instance within a Deployed Solution. Certain artifacts of that case type are in this folder hierarchy.                                                                                                                             |
| Deployed Solution (CmAcmDeployedSolution)    | Represents a Case Solution folder in a deployed solution. Certain solution artifacts and the case types and instances are in this folder hierarchy.                                                                                                       |

## Other classes

1. In the domain navigation pane, select the target object store.
2. In the object store navigation pane, click Data Design > Classes > Other Classes.
3. For certain classes, expand the parent class as indicated in the following table.

| Display name (symbolic name)                                            | Description                                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Case Comment (CmAcmCaseComment)                                         | Represents the base class for comments that are associated with a specific case. A case comment can be associated with the case or with a document, activity, or work item in the case. To view this class, click Annotation in the object store navigation pane. |
| Case File Event (CmAcmCaseFileEvent)                                    | Records the filing of a document into a case for auditing purposes.To view this class, click Event > Object Change Event > Custom Event in the object store navigation pane.                                                                                      |
| Case Related Event (CmAcmCaseRelatedEvent)                              | Records the creation of a relationship between two cases for auditing purposes.To view this class, click Event > Object Change Event > Custom Event in the object store navigation pane.                                                                          |
| Case Relationship (CmAcmCaseRelationship)                               | Represents the relationship between two cases.To view this class, click Link in the object store navigation pane.                                                                                                                                                 |
| Case Activity (CmAcmCaseTask)                                           | Represents the base, abstract class for a Case Activity. To view this class, click Activity in the object store navigation pane.                                                                                                                                  |
| Case Unfile Event (CmAcmCaseUnfileEvent)                                | Records the unfiling of a document from a case for auditing purposes.To view this class, click Event > Object Change Event > Custom Event in the object store navigation pane.                                                                                    |
| Directory Validation Event (CmAcmDirectoryValidationEvent)              | Validates the presence of the rules repository directory on the Content Platform Engine server.To view this class, click Event > Object Change Event > Custom Event in the object store navigation pane.                                                          |
| Document Create Case Subscription (CmAcmDocumentCreateCaseSubscription) | Represents a synchronous subscription to the Create event on Document classes. Class subscriptions of this class are created by the solution deployment tool. To view this class, click Class Subscription in the object store navigation pane.                   |
| Dynamic Task (CmAcmDynamicTask)                                         | Represents a custom activity that a user creates in Case Manager Client.To view this class, click Activity > Case Activity in the object store navigation pane.                                                                                                   |
| Rule Deployment Event (CmAcmRuleDeploymentEvent)                        | Causes rules to be deployed to the rules repository directory on the Content Platform Engine server.To view this class, click Event > Object Change Event > Custom Event in the object store navigation pane.                                                     |
| Rule Export Event (CmAcmRuleExportEvent)                                | Causes the rules in a solution to be exported to a package and uploaded to the design object storeTo view this class, click Event > Object Change Event > Custom Event in the object store navigation pane.                                                       |
| Rule Reset Event (CmAcmRuleResetEvent)                                  | Causes the rules repository directory to be reset.To view this class, click Event > Object Change Event > Custom Event in the object store navigation pane.                                                                                                       |
| Task Comment (CmAcmTaskComment)                                         | Represents a comment for a case activity. To view this class, click Annotation > Case Comment in the object store navigation pane.                                                                                                                                |
| Task With Initiating Document (CmAcmTaskWithInitiatingDocument)         | Represents the base, abstract class for a Case Activity that has a file precondition.To view this class, click Activity > Case Activity in the object store navigation pane.                                                                                      |
| Task Workflow Launch Subscription (CmAcmTaskWorkflowLaunchSubscription) | Represents an asynchronous subscription to the Change State event of a Case Activity. To view this class, click Class Subscription in the object store navigation pane.                                                                                           |
| Version Series Comment (CmAcmVersionSeriesComment)                      | Represents a comment for a document in a case. To view this class, click Annotation > Case Comment in the object store navigation pane.                                                                                                                           |
| Work Item Comment (CmAcmWorkItemComment)                                | Represents a comment for a case work item. To view this class, click Annotation > Case Comment > Activity Comment in the object store navigation pane.                                                                                                            |