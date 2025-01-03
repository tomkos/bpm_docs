# History and analytics extensions

The history and analytics extensions configure several properties on source object classes to be
audited individually. Only the individual properties are then recorded, rather than the entire
source object on the audited event. For a property to be audited on a source object, the
corresponding property definition on the class must be configured for auditing. Specifically, the
AuditAs property of the property definition must be set to an event property that
holds the value of the source object property.

The classes contain properties that are audited by default and where their
corresponding values are found on the event objects.

For a property that is not audited by default, you can set the
AuditAs property in the property definition to audit that property. When an event
is raised on the object, the property is then audited.

1. In the domain navigation pane, select the target object store.
2. In the object store navigation pane, click Data Design > Classes and then click the class.
3. On the Properties Definition tab, click the property that you want to audit
to open the Property Definition dialog box. Click the More
tab.
4. From the Audit as list, select the event property template that is to be
used to audit the property.

| Display name (symbolic name)                       | Description                                                                                                                                                                                    |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Case Comment (CmAcmCaseComment)                    | Represents the base class for comments that are associated with a specific case. A case comment can be associated with the case or with a document, activity, or work item in the case.        |
| Case Folder (CmAcmCaseFolder)                      | The Case Folder class and its subclasses are extended with auditing configuration settings that are accessible by the applications that you configure for case analytics and for case history. |
| Case Subfolder (CmAcmCaseSubfolder)                | Represents a subfolder under a Case Folder instance.                                                                                                                                           |
| Case Activity (CmAcmCaseTask)                      | Represents the base, abstract class for a Case Activity.                                                                                                                                       |
| Document (Document)                                | A single version of a document stored in an object store.                                                                                                                                      |
| Task Comment (CmAcmTaskComment)                    | Represents a comment for a case activity.                                                                                                                                                      |
| Version Series Comment (CmAcmVersionSeriesComment) | Represents a comment for a document in a case.                                                                                                                                                 |
| Work Item Comment (CmAcmWorkItemComment)           | Represents a comment for a case work item.                                                                                                                                                     |