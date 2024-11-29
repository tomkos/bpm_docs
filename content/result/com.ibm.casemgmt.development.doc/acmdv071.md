# Subscriptions and events

1. In the domain navigation pane, select the target object store.
2. In the object store navigation pane, click Data
Design > Classes > Other Classes.
Then, to view an event class, click Event > Object
Change Event > Custom Event. To view a subscription
class, click Class Subscription.

| Display name (symbolic name)                                            | Description                                                                                                                                                   |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Case File Event (CmAcmCaseFileEvent)                                    | Represents an event that occurs when a Case Folder or Case Subfolder has its file method called to file a Document object.                                    |
| Case Related Event (CmAcmCaseRelatedEvent)                              | Represents an event that occurs when a relationship is established between two cases.                                                                         |
| Case Unfile Event (CmAcmCaseUnfileEvent)                                | Represents an event that occurs when a document is unfiled from a case.                                                                                       |
| Directory Validation Event (CmAcmDirectoryValidationEvent)              | Represents an event that occurs when the verification that the Rules repository directory is present on the Content Platform Engine server takes place.       |
| Document Create Case Subscription (CmAcmDocumentCreateCaseSubscription) | Represents a synchronous subscription to the Create event on Document classes. Class subscriptions of this class are created by the solution deployment tool. |
| Rule Deployment Event (CmAcmRuleDeploymentEvent)                        | Represents an event that occurs when a business rule is deployed.                                                                                             |
| Rule Export Event (CmAcmRuleExportEvent)                                | Represents an event that occurs when a business rule is exported.                                                                                             |
| Rule Reset Event (CmAcmRuleResetEvent)                                  | Represents an event that occurs when a business rule is reset.                                                                                                |
| Task Workflow Launch Subscription (CmAcmTaskWorkflowLaunchSubscription) | Represents an asynchronous subscription to the Change State event of a Case Activity.                                                                         |