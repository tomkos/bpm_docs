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

## Class TaskTemplateBean

- java.lang.Object
    - com.ibm.task.clientmodel.bean.TaskTemplateBean

- All Implemented Interfaces:
TaskTemplate, java.io.Serializable

public class TaskTemplateBean
extends java.lang.Object
implements TaskTemplate
Accesses the properties of the original TaskTemplate object
 and adds metadata for national language support and converters. 
A TaskTemplateBean object can be instantiated from
 a TaskTemplate object.
See Also:TaskTemplate, 
Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String ADHOC\_PROPERTY Use the property name to determine labels and converters for the adHoc property. static java.lang.String APPLICATIONDEFAULTSID\_PROPERTY Use the property name to determine labels and converters for the applicationDefaultsID property. static java.lang.String APPLICATIONNAME\_PROPERTY Use the property name to determine labels and converters for the applicationName property. static java.lang.String ASSIGNMENTTYPE\_PROPERTY Use the property name to determine labels and converters for the assignmentType property. static java.lang.String AUTODELETIONMODE\_PROPERTY Use the property name to determine labels and converters for the autoDeletionMode property. static java.lang.String BUSINESSRELEVANT\_PROPERTY Use the property name to determine labels and converters for the businessRelevant property. static java.lang.String CALENDARNAME\_PROPERTY Use the property name to determine labels and converters for the calendarName property. static java.lang.String CONTAINMENTCONTEXTID\_PROPERTY Use the property name to determine labels and converters for the containmentContextID property. static java.lang.String CONTEXTAUTHORIZATIONOFOWNER\_PROPERTY Use the property name to determine labels and converters for the contextAuthorizationOfOwner property. static java.lang.String COPYRIGHT static java.lang.String CUSTOMTEXT1\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT2\_PROPERTY Use the property name to determine labels and converters for the customText2 property. static java.lang.String CUSTOMTEXT3\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT4\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT5\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT6\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT7\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT8\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String DEFINITIONNAME\_PROPERTY Use the property name to determine labels and converters for the definition name property. static java.lang.String DEFINITIONNAMESPACE\_PROPERTY Use the property name to determine labels and converters for the definition namespace property. static java.lang.String DESCRIPTION\_PROPERTY Use the property name to determine labels and converters for the description property. static java.lang.String DISPLAYNAME\_PROPERTY Use the property name to determine labels and converters for the displayName property. static java.lang.String DURATIONUNTILDELETED\_PROPERTY Use the property name to determine labels and converters for the durationUntilDeleted property. static java.lang.String DURATIONUNTILDUE\_PROPERTY Use the property name to determine labels and converters for the durationUntilDue property. static java.lang.String DURATIONUNTILEXPIRES\_PROPERTY Use the property name to determine labels and converters for the durationUntilExpires property. static java.lang.String ESCALATIONTEMPLATEIDS\_PROPERTY Use the property name to determine labels and converters for the escalationTemplateIDs property. static java.lang.String EVENTHANDLERNAME\_PROPERTY Use the property name to determine labels and converters for the eventHandlerName property. static java.lang.String ID\_PROPERTY Use the property name to determine labels and converters for the ID property. static java.lang.String INHERITEDAUTHORIZATION\_PROPERTY Use the property name to determine labels and converters for the inheritedAuthorization property. static java.lang.String INLINE\_PROPERTY Use the property name to determine labels and converters for the property inline. static java.lang.String JNDINAMEOFCALENDAR\_PROPERTY Use the property name to determine labels and converters for the JNDINameOfCalendar property. static java.lang.String JNDINAMEOFSTAFFPLUGINPROVIDER\_PROPERTY Use the property name to determine labels and converters for the JNDINameOfStaffPluginProvider property. static java.lang.String KIND\_PROPERTY Use the property name to determine labels and converters for the kind property. static java.lang.String NAME\_PROPERTY Use the property name to determine labels and converters for the name property. static java.lang.String NAMESPACE\_PROPERTY Use the property name to determine labels and converters for the namespace property. static java.lang.String PRIORITY\_DEFINITION\_PROPERTY Use the property name to determine labels and converters for the priority definition property. static java.lang.String PRIORITY\_PROPERTY Use the property name to determine labels and converters for the priority property. static java.lang.String PROCESSAPPACRONYM\_PROPERTY Use the property name to determine labels and converters for the processAppAcronym property. static java.lang.String PROCESSAPPNAME\_PROPERTY Use the property name to determine labels and converters for the processAppName property. static java.lang.String SNAPSHOTID\_PROPERTY Use the property name to determine labels and converters for the snapshotID property. static java.lang.String SNAPSHOTNAME\_PROPERTY Use the property name to determine labels and converters for the snapshotName property. static java.lang.String STATE\_PROPERTY Use the property name to determine labels and converters for the property state. static java.lang.String SUBSTITUTIONPOLICY\_PROPERTY Use the property name to determine labels and converters for the property substitution policy. static java.lang.String SUPPORTSAUTOMATICCLAIM\_PROPERTY Use the property name to determine labels and converters for the property supportsAutomaticClaim. static java.lang.String SUPPORTSCLAIMIFSUSPENDED\_PROPERTY Use the property name to determine labels and converters for the property supportsClaimIfSuspended. static java.lang.String SUPPORTSDELEGATION\_PROPERTY Use the property name to determine labels and converters for the property supportsClaimIfSuspended. static java.lang.String SUPPORTSFOLLOWONTASKS\_PROPERTY Use the property name to determine labels and converters for the property supportsFollowOnTasks. static java.lang.String SUPPORTSSUBTASKS\_PROPERTY Use the property name to determine labels and converters for the property supportsSubTasks. static java.lang.String TIP\_PROPERTY Use the property name to determine labels and converters for the tip property. static java.lang.String TOOLKITACRONYM\_PROPERTY Use the property name to determine labels and converters for the toolkitAcronym property. static java.lang.String TOOLKITNAME\_PROPERTY Use the property name to determine labels and converters for the toolkitName property. static java.lang.String TOOLKITSNAPSHOTID\_PROPERTY Use the property name to determine labels and converters for the toolkitSnapshotID property. static java.lang.String TOOLKITSNAPSHOTNAME\_PROPERTY Use the property name to determine labels and converters for the toolkitSnapshotName property. static java.lang.String TOPLEVELTOOLKITACRONYM\_PROPERTY Use the property name to determine labels and converters for the topLevelToolkitAcronym property. static java.lang.String TOPLEVELTOOLKITNAME\_PROPERTY Use the property name to determine labels and converters for the topLevelToolkitName property. static java.lang.String TRACKNAME\_PROPERTY Use the property name to determine labels and converters for the trackName property. static java.lang.String TYPE\_PROPERTY Use the property name to determine labels and converters for the type property. static java.lang.String VALIDFROMTIME\_PROPERTY Use the property name to determine labels and converters for the validFromTime property. static java.lang.String WORKBASKETNAME\_PROPERTY Use the property name to determine labels and converters for the workBasketName property.

### Field Summary

| Modifier and Type       | Field and Description                                                                                                                            |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| static java.lang.String | ADHOC\_PROPERTY Use the property name to determine labels and converters for the  adHoc property.                                                 |
| static java.lang.String | APPLICATIONDEFAULTSID\_PROPERTY Use the property name to determine labels and converters for the  applicationDefaultsID property.                 |
| static java.lang.String | APPLICATIONNAME\_PROPERTY Use the property name to determine labels and converters for the  applicationName property.                             |
| static java.lang.String | ASSIGNMENTTYPE\_PROPERTY Use the property name to determine labels and converters for the  assignmentType property.                               |
| static java.lang.String | AUTODELETIONMODE\_PROPERTY Use the property name to determine labels and converters for the  autoDeletionMode property.                           |
| static java.lang.String | BUSINESSRELEVANT\_PROPERTY Use the property name to determine labels and converters for the  businessRelevant property.                           |
| static java.lang.String | CALENDARNAME\_PROPERTY Use the property name to determine labels and converters for the  calendarName property.                                   |
| static java.lang.String | CONTAINMENTCONTEXTID\_PROPERTY Use the property name to determine labels and converters for the  containmentContextID property.                   |
| static java.lang.String | CONTEXTAUTHORIZATIONOFOWNER\_PROPERTY Use the property name to determine labels and converters for the  contextAuthorizationOfOwner property.     |
| static java.lang.String | COPYRIGHT                                                                                                                                        |
| static java.lang.String | CUSTOMTEXT1\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                                      |
| static java.lang.String | CUSTOMTEXT2\_PROPERTY Use the property name to determine labels and converters for the customText2 property.                                      |
| static java.lang.String | CUSTOMTEXT3\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                                      |
| static java.lang.String | CUSTOMTEXT4\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                                      |
| static java.lang.String | CUSTOMTEXT5\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                                      |
| static java.lang.String | CUSTOMTEXT6\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                                      |
| static java.lang.String | CUSTOMTEXT7\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                                      |
| static java.lang.String | CUSTOMTEXT8\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                                      |
| static java.lang.String | DEFINITIONNAME\_PROPERTY Use the property name to determine labels and converters for the  definition name property.                              |
| static java.lang.String | DEFINITIONNAMESPACE\_PROPERTY Use the property name to determine labels and converters for the  definition namespace property.                    |
| static java.lang.String | DESCRIPTION\_PROPERTY Use the property name to determine labels and converters for the  description property.                                     |
| static java.lang.String | DISPLAYNAME\_PROPERTY Use the property name to determine labels and converters for the  displayName property.                                     |
| static java.lang.String | DURATIONUNTILDELETED\_PROPERTY Use the property name to determine labels and converters for the  durationUntilDeleted property.                   |
| static java.lang.String | DURATIONUNTILDUE\_PROPERTY Use the property name to determine labels and converters for the  durationUntilDue property.                           |
| static java.lang.String | DURATIONUNTILEXPIRES\_PROPERTY Use the property name to determine labels and converters for the  durationUntilExpires property.                   |
| static java.lang.String | ESCALATIONTEMPLATEIDS\_PROPERTY Use the property name to determine labels and converters for the  escalationTemplateIDs property.                 |
| static java.lang.String | EVENTHANDLERNAME\_PROPERTY Use the property name to determine labels and converters for the  eventHandlerName property.                           |
| static java.lang.String | ID\_PROPERTY Use the property name to determine labels and converters for the  ID property.                                                       |
| static java.lang.String | INHERITEDAUTHORIZATION\_PROPERTY Use the property name to determine labels and converters for the  inheritedAuthorization property.               |
| static java.lang.String | INLINE\_PROPERTY Use the property name to determine labels and converters for the property inline.                                                |
| static java.lang.String | JNDINAMEOFCALENDAR\_PROPERTY Use the property name to determine labels and converters for the  JNDINameOfCalendar property.                       |
| static java.lang.String | JNDINAMEOFSTAFFPLUGINPROVIDER\_PROPERTY Use the property name to determine labels and converters for the  JNDINameOfStaffPluginProvider property. |
| static java.lang.String | KIND\_PROPERTY Use the property name to determine labels and converters for the  kind property.                                                   |
| static java.lang.String | NAME\_PROPERTY Use the property name to determine labels and converters for the  name property.                                                   |
| static java.lang.String | NAMESPACE\_PROPERTY Use the property name to determine labels and converters for the  namespace property.                                         |
| static java.lang.String | PRIORITY\_DEFINITION\_PROPERTY Use the property name to determine labels and converters for the  priority definition property.                     |
| static java.lang.String | PRIORITY\_PROPERTY Use the property name to determine labels and converters for the  priority property.                                           |
| static java.lang.String | PROCESSAPPACRONYM\_PROPERTY Use the property name to determine labels and converters for the  processAppAcronym property.                         |
| static java.lang.String | PROCESSAPPNAME\_PROPERTY Use the property name to determine labels and converters for the  processAppName property.                               |
| static java.lang.String | SNAPSHOTID\_PROPERTY Use the property name to determine labels and converters for the  snapshotID property.                                       |
| static java.lang.String | SNAPSHOTNAME\_PROPERTY Use the property name to determine labels and converters for the  snapshotName property.                                   |
| static java.lang.String | STATE\_PROPERTY Use the property name to determine labels and converters for the property state.                                                  |
| static java.lang.String | SUBSTITUTIONPOLICY\_PROPERTY Use the property name to determine labels and converters for the property substitution policy.                       |
| static java.lang.String | SUPPORTSAUTOMATICCLAIM\_PROPERTY Use the property name to determine labels and converters for the property  supportsAutomaticClaim.               |
| static java.lang.String | SUPPORTSCLAIMIFSUSPENDED\_PROPERTY Use the property name to determine labels and converters for the property  supportsClaimIfSuspended.           |
| static java.lang.String | SUPPORTSDELEGATION\_PROPERTY Use the property name to determine labels and converters for the property  supportsClaimIfSuspended.                 |
| static java.lang.String | SUPPORTSFOLLOWONTASKS\_PROPERTY Use the property name to determine labels and converters for the property  supportsFollowOnTasks.                 |
| static java.lang.String | SUPPORTSSUBTASKS\_PROPERTY Use the property name to determine labels and converters for the property  supportsSubTasks.                           |
| static java.lang.String | TIP\_PROPERTY Use the property name to determine labels and converters for the  tip property.                                                     |
| static java.lang.String | TOOLKITACRONYM\_PROPERTY Use the property name to determine labels and converters for the  toolkitAcronym property.                               |
| static java.lang.String | TOOLKITNAME\_PROPERTY Use the property name to determine labels and converters for the  toolkitName property.                                     |
| static java.lang.String | TOOLKITSNAPSHOTID\_PROPERTY Use the property name to determine labels and converters for the  toolkitSnapshotID property.                         |
| static java.lang.String | TOOLKITSNAPSHOTNAME\_PROPERTY Use the property name to determine labels and converters for the  toolkitSnapshotName property.                     |
| static java.lang.String | TOPLEVELTOOLKITACRONYM\_PROPERTY Use the property name to determine labels and converters for the  topLevelToolkitAcronym property.               |
| static java.lang.String | TOPLEVELTOOLKITNAME\_PROPERTY Use the property name to determine labels and converters for the  topLevelToolkitName property.                     |
| static java.lang.String | TRACKNAME\_PROPERTY Use the property name to determine labels and converters for the  trackName property.                                         |
| static java.lang.String | TYPE\_PROPERTY Use the property name to determine labels and converters for the  type property.                                                   |
| static java.lang.String | VALIDFROMTIME\_PROPERTY Use the property name to determine labels and converters for the  validFromTime property.                                 |
| static java.lang.String | WORKBASKETNAME\_PROPERTY Use the property name to determine labels and converters for the  workBasketName property.                               |

- Fields inherited from interface com.ibm.task.api.TaskTemplate
ASSIGNMENT\_TYPE\_PARALLEL, ASSIGNMENT\_TYPE\_SINGLE, AUTH\_NONE, AUTH\_READER, AUTO\_DELETE\_ON\_COMPLETION, AUTO\_DELETE\_ON\_SUCCESSFUL\_COMPLETION, AUTONOMY\_CHILD, AUTONOMY\_NOT\_APPLICABLE, AUTONOMY\_PEER, INHERITED\_AUTH\_ADMINISTRATOR, INHERITED\_AUTH\_ALL, INHERITED\_AUTH\_NONE, KIND\_ADMINISTRATIVE, KIND\_HUMAN, KIND\_ORIGINATING, KIND\_PARTICIPATING, STATE\_STARTED, STATE\_STOPPED, SUBSTITUTION\_POLICY\_NO\_SUBSTITUTION, SUBSTITUTION\_POLICY\_SELECT\_USER\_IF\_PRESENT, SUBSTITUTION\_POLICY\_SUBSTITUTE\_IF\_ABSENT

- Constructor Summary

Constructors 

Modifier
Constructor and Description

 
TaskTemplateBean(TaskTemplate data,
                HTMConnection htmConnection)
Constructs a new  object from an original TaskTemplate object.

protected 
TaskTemplateBean(TKTID id,
                HTMConnection htmConnection,
                java.util.Locale locale)
Constructs a TaskTemplateBean from a task template id.

- Method Summary Methods Modifier and Type Method and Description ACOID getApplicationDefaultsID () Returns the applicationDefaultsID property. java.lang.String getApplicationName () Returns the applicationName property. int getAssignmentType () Returns the property assignmentType . int getAutoDeletionMode () Returns the property autoDeletionMode . int getAutonomy () Returns the property autonomy . java.lang.String getCalendarName () Returns the property calendarName . OID getContainmentContextID () Returns the property containmentContextID . int getContextAuthorizationOfOwner () Returns the property contextAuthorizationOfOwner . static SimpleConverter getConverter (java.lang.String propertyName) Returns the default converter for a given property. java.lang.String getCustomText1 () Returns the property customText1 . java.lang.String getCustomText2 () Returns the property customText2 . java.lang.String getCustomText3 () Returns the property customText3 . java.lang.String getCustomText4 () Returns the property customText4 . java.lang.String getCustomText5 () Returns the property customText5 . java.lang.String getCustomText6 () Returns the property customText6 . java.lang.String getCustomText7 () Returns the property customText7 . java.lang.String getCustomText8 () Returns the property customText8 . java.lang.String getDefinitionName () Returns the property definition name . java.lang.String getDefinitionNamespace () Returns the property definition namespace . com.ibm.bpc.clientcore.util.LocalisedString getDescription () Returns the localised description. java.lang.String getDescription (java.util.Locale locale) Returns the property description . com.ibm.bpc.clientcore.util.LocalisedString getDisplayName () Returns the localised display name. java.lang.String getDisplayName (java.util.Locale locale) Returns the property displayName . java.lang.String getDurationUntilDeleted () Returns the property durationUntilDeleted . java.lang.String getDurationUntilDue () Returns the property durationUntilDue . java.lang.String getDurationUntilExpires () Returns the property durationUntilExpires . java.lang.String getEventHandlerName () Returns the property eventHandlerName . TKTID getID () Returns the property ID . int getInheritedAuthorization () Returns the property inheritedAuthorization . MessageWrapper getInputMessageWrapper () Retrieves the input message. java.lang.String getJNDINameOfCalendar () Returns the property JNDINameOfCalendar . java.lang.String getJNDINameOfStaffPluginProvider () Returns the property JNDINameOfStaffPluginProvider . int getKind () Returns the property kind . static java.lang.String getLabel (java.lang.String propertyName) Returns the resource bundle key for a property static java.lang.String getLabel (java.lang.String propertyName, java.util.Locale locale) Returns the label for a property from the resource bundle. java.util.List getLocalesOfDescriptions () Returns the property localesOfDescriptions . java.util.List getLocalesOfDisplayNames () Returns the property localesOfDisplayNames . java.lang.String getName () Returns the property name . java.lang.String getNamespace () Returns the property namespace . java.lang.Integer getPriority () Returns the property priority . java.lang.String getPriorityDefinition () Returns the property priority definition . java.lang.String getProcessAppAcronym () Returns the processAppAcronym property. java.lang.String getProcessAppName () Returns the processAppName property. java.lang.String getSnapshotID () Returns the snapshotID property. java.lang.String getSnapshotName () Returns the snapshotName property. int getState () Returns the property state . int getSubstitutionPolicy () Returns the property substitutionPolicy . java.lang.String getToolkitAcronym () Returns the toolkitAcronym property. java.lang.String getToolkitName () Returns the toolkitName property. java.lang.String getToolkitSnapshotID () Returns the toolkitSnapshotID property. java.lang.String getToolkitSnapshotName () Returns the toolkitSnapshotName property. java.lang.String getTopLevelToolkitAcronym () Returns the topLevelToolkitAcronym property. java.lang.String getTopLevelToolkitName () Returns the topLevelToolkitName property. java.lang.String getTrackName () Returns the trackName property. java.lang.String getType () Returns the property type . java.util.Calendar getValidFromTime () Returns the property validFromTime . java.lang.String getWorkBasketName () Returns the workBasketName property. boolean isAdHoc () Returns the property adHoc . boolean isBusinessRelevant () Returns the property businessRelevant . boolean isInline () Returns the property inline . boolean isSupportsAutomaticClaim () Returns the property supportsAutomaticClaim . boolean isSupportsClaimIfSuspended () Returns the property supportsClaimIfSuspended . boolean isSupportsDelegation () Returns the property supportsDelegation . boolean isSupportsFollowOnTasks () Returns the property supportsFollowOnTasks . boolean isSupportsSubTasks () Returns the property supportsSubTasks . boolean isTip () Returns the property tip . static boolean isValid (java.lang.String propertyName) Checks if the property is valid. boolean supportsAutomaticClaim () Returns the property supportsAutomaticClaim . boolean supportsClaimIfSuspended () Returns the property supportsClaimIfSuspended . boolean supportsDelegation () Returns the property supportsDelegation . boolean supportsFollowOnTasks () Returns the property supportsFollowOnTasks . boolean supportsSubTasks () Returns the property supportsSubTasks .

### Method Summary

| Modifier and Type                           | Method and Description                                                                                                              |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| ACOID                                       | getApplicationDefaultsID() Returns the applicationDefaultsID property.                                                              |
| java.lang.String                            | getApplicationName() Returns the applicationName property.                                                                          |
| int                                         | getAssignmentType() Returns the property assignmentType.                                                                            |
| int                                         | getAutoDeletionMode() Returns the property autoDeletionMode.                                                                        |
| int                                         | getAutonomy() Returns the property autonomy.                                                                                        |
| java.lang.String                            | getCalendarName() Returns the property calendarName.                                                                                |
| OID                                         | getContainmentContextID() Returns the property containmentContextID.                                                                |
| int                                         | getContextAuthorizationOfOwner() Returns the property contextAuthorizationOfOwner.                                                  |
| static SimpleConverter                      | getConverter(java.lang.String propertyName) Returns the default converter for a given property.                                     |
| java.lang.String                            | getCustomText1() Returns the property customText1.                                                                                  |
| java.lang.String                            | getCustomText2() Returns the property customText2.                                                                                  |
| java.lang.String                            | getCustomText3() Returns the property customText3.                                                                                  |
| java.lang.String                            | getCustomText4() Returns the property customText4.                                                                                  |
| java.lang.String                            | getCustomText5() Returns the property customText5.                                                                                  |
| java.lang.String                            | getCustomText6() Returns the property customText6.                                                                                  |
| java.lang.String                            | getCustomText7() Returns the property customText7.                                                                                  |
| java.lang.String                            | getCustomText8() Returns the property customText8.                                                                                  |
| java.lang.String                            | getDefinitionName() Returns the property definition name.                                                                           |
| java.lang.String                            | getDefinitionNamespace() Returns the property definition namespace.                                                                 |
| com.ibm.bpc.clientcore.util.LocalisedString | getDescription() Returns the localised description.                                                                                 |
| java.lang.String                            | getDescription(java.util.Locale locale) Returns the property description.                                                           |
| com.ibm.bpc.clientcore.util.LocalisedString | getDisplayName() Returns the localised display name.                                                                                |
| java.lang.String                            | getDisplayName(java.util.Locale locale) Returns the property displayName.                                                           |
| java.lang.String                            | getDurationUntilDeleted() Returns the property durationUntilDeleted.                                                                |
| java.lang.String                            | getDurationUntilDue() Returns the property durationUntilDue.                                                                        |
| java.lang.String                            | getDurationUntilExpires() Returns the property durationUntilExpires.                                                                |
| java.lang.String                            | getEventHandlerName() Returns the property eventHandlerName.                                                                        |
| TKTID                                       | getID() Returns the property ID.                                                                                                    |
| int                                         | getInheritedAuthorization() Returns the property inheritedAuthorization.                                                            |
| MessageWrapper                              | getInputMessageWrapper() Retrieves the input message.                                                                               |
| java.lang.String                            | getJNDINameOfCalendar() Returns the property JNDINameOfCalendar.                                                                    |
| java.lang.String                            | getJNDINameOfStaffPluginProvider() Returns the property JNDINameOfStaffPluginProvider.                                              |
| int                                         | getKind() Returns the property kind.                                                                                                |
| static java.lang.String                     | getLabel(java.lang.String propertyName) Returns the resource bundle key for a property                                              |
| static java.lang.String                     | getLabel(java.lang.String propertyName,         java.util.Locale locale) Returns the label for a property from the resource bundle. |
| java.util.List                              | getLocalesOfDescriptions() Returns the property localesOfDescriptions.                                                              |
| java.util.List                              | getLocalesOfDisplayNames() Returns the property localesOfDisplayNames.                                                              |
| java.lang.String                            | getName() Returns the property name.                                                                                                |
| java.lang.String                            | getNamespace() Returns the property namespace.                                                                                      |
| java.lang.Integer                           | getPriority() Returns the property priority.                                                                                        |
| java.lang.String                            | getPriorityDefinition() Returns the property priority definition.                                                                   |
| java.lang.String                            | getProcessAppAcronym() Returns the processAppAcronym property.                                                                      |
| java.lang.String                            | getProcessAppName() Returns the processAppName property.                                                                            |
| java.lang.String                            | getSnapshotID() Returns the snapshotID property.                                                                                    |
| java.lang.String                            | getSnapshotName() Returns the snapshotName property.                                                                                |
| int                                         | getState() Returns the property state.                                                                                              |
| int                                         | getSubstitutionPolicy() Returns the property substitutionPolicy.                                                                    |
| java.lang.String                            | getToolkitAcronym() Returns the toolkitAcronym property.                                                                            |
| java.lang.String                            | getToolkitName() Returns the toolkitName property.                                                                                  |
| java.lang.String                            | getToolkitSnapshotID() Returns the toolkitSnapshotID property.                                                                      |
| java.lang.String                            | getToolkitSnapshotName() Returns the toolkitSnapshotName property.                                                                  |
| java.lang.String                            | getTopLevelToolkitAcronym() Returns the topLevelToolkitAcronym property.                                                            |
| java.lang.String                            | getTopLevelToolkitName() Returns the topLevelToolkitName property.                                                                  |
| java.lang.String                            | getTrackName() Returns the trackName property.                                                                                      |
| java.lang.String                            | getType() Returns the property type.                                                                                                |
| java.util.Calendar                          | getValidFromTime() Returns the property validFromTime.                                                                              |
| java.lang.String                            | getWorkBasketName() Returns the workBasketName property.                                                                            |
| boolean                                     | isAdHoc() Returns the property adHoc.                                                                                               |
| boolean                                     | isBusinessRelevant() Returns the property businessRelevant.                                                                         |
| boolean                                     | isInline() Returns the property inline.                                                                                             |
| boolean                                     | isSupportsAutomaticClaim() Returns the property supportsAutomaticClaim.                                                             |
| boolean                                     | isSupportsClaimIfSuspended() Returns the property supportsClaimIfSuspended.                                                         |
| boolean                                     | isSupportsDelegation() Returns the property supportsDelegation.                                                                     |
| boolean                                     | isSupportsFollowOnTasks() Returns the property supportsFollowOnTasks.                                                               |
| boolean                                     | isSupportsSubTasks() Returns the property supportsSubTasks.                                                                         |
| boolean                                     | isTip() Returns the property tip.                                                                                                   |
| static boolean                              | isValid(java.lang.String propertyName) Checks if the property is valid.                                                             |
| boolean                                     | supportsAutomaticClaim() Returns the property supportsAutomaticClaim.                                                               |
| boolean                                     | supportsClaimIfSuspended() Returns the property supportsClaimIfSuspended.                                                           |
| boolean                                     | supportsDelegation() Returns the property supportsDelegation.                                                                       |
| boolean                                     | supportsFollowOnTasks() Returns the property supportsFollowOnTasks.                                                                 |
| boolean                                     | supportsSubTasks() Returns the property supportsSubTasks.                                                                           |

    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait