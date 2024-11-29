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

## Class ProcessTemplateBean

- java.lang.Object
    - com.ibm.bpe.clientmodel.bean.ProcessTemplateBean

- All Implemented Interfaces:
ProcessTemplateData, java.io.Serializable

public class ProcessTemplateBean
extends java.lang.Object
implements ProcessTemplateData
Accesses the properties of the original ProcessTemplateData object
 and adds metadata for national language support and converters. 
A ProcessTemplateBean object can be instantiated from a ProcessTemplateData object.
 

 Use the static method getLabel(String, Locale) to
 retrieve the localized label for a property.
 Use the static method getConverter(String) to
 retrieve a converter for a property. The return value might be null, as converters
 are optional.
 
See Also:ProcessTemplateData, 
Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String APPLICATIONNAME\_PROPERTY Use the property name to determine labels and converters for the applicationName property. static java.lang.String AUTO\_DELETION\_MODE Use the property name to determine labels and converters for the autoDeletionMode property. static java.lang.String AUTODELETE\_PROPERTY Use the property name to determine labels and converters for the autoDelete property. static java.lang.String AUTONOMY\_PROPERTY Use the property name to determine labels and converters for the autonomy property. static java.lang.String AVAILABLEACTIONS\_PROPERTY Use the property name to determine labels and converters for the availableActions property. static java.lang.String COMPENSATIONDEFINED\_PROPERTY Use the property name to determine labels and converters for the compensationDefined property. static java.lang.String CONTINUEONERROR\_PROPERTY Use the property name to determine labels and converters for the continueOnError property. static java.lang.String COPYRIGHT (C) Copyright IBM Corporation 2005, 2011. static java.lang.String CREATIONTIME\_PROPERTY Use the property name to determine labels and converters for the creationTime property. static java.lang.String CUSTOMTEXT1\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT2\_PROPERTY Use the property name to determine labels and converters for the customText2 property. static java.lang.String CUSTOMTEXT3\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT4\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT5\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT6\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT7\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT8\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String DESCRIPTION\_PROPERTY Use the property name to determine labels and converters for the description property. static java.lang.String DISPLAYNAME\_PROPERTY Use the property name to determine labels and converters for the displayName property. static java.lang.String DOCUMENTATION\_PROPERTY Use the property name to determine labels and converters for the documentation property. static java.lang.String EXECUTIONMODE\_PROPERTY Use the property name to determine labels and converters for the executionMode property. static java.lang.String ID\_PROPERTY Use the property name to determine labels and converters for the ID property. static java.lang.String INPUTMESSAGETYPENAME\_PROPERTY Use the property name to determine labels and converters for the inputMessageTypeName property. static java.lang.String INPUTMESSAGETYPETYPESYSTEM\_PROPERTY Deprecated. static java.lang.String LASTMODIFICATIONTIME\_PROPERTY Use the property name to determine labels and converters for the lastModificationTime property. static java.lang.String NAME\_PROPERTY Use the property name to determine labels and converters for the name property. static java.lang.String OUTPUTMESSAGETYPENAME\_PROPERTY Use the property name to determine labels and converters for the outputMessageTypeName property. static java.lang.String OUTPUTMESSAGETYPETYPESYSTEM\_PROPERTY Deprecated. static java.lang.String PROCESSADMINSTRATORS\_PROPERTY Deprecated. static java.lang.String PROCESSAPPACRONYM\_PROPERTY Use the property name to determine labels and converters for the processAppAcronym property. static java.lang.String PROCESSAPPNAME\_PROPERTY Use the property name to determine labels and converters for the processAppName property. static java.lang.String SCHEMAVERSION\_PROPERTY Use the property name to determine labels and converters for the schemaVersion property. static java.lang.String SNAPSHOTID\_PROPERTY Use the property name to determine labels and converters for the snapshotID property. static java.lang.String SNAPSHOTNAME\_PROPERTY Use the property name to determine labels and converters for the snapshotName property. static java.lang.String STATE\_PROPERTY Use the property name to determine labels and converters for the state property. static java.lang.String TARGETNAMESPACE\_PROPERTY Use the property name to determine labels and converters for the targetNamespace property. static java.lang.String TIP\_PROPERTY Use the property name to determine labels and converters for the tip property. static java.lang.String TOOLKITACRONYM\_PROPERTY Use the property name to determine labels and converters for the toolkitAcronym property. static java.lang.String TOOLKITNAME\_PROPERTY Use the property name to determine labels and converters for the toolkitName property. static java.lang.String TOOLKITSNAPSHOTID\_PROPERTY Use the property name to determine labels and converters for the toolkitSnapshotID property. static java.lang.String TOOLKITSNAPSHOTNAME\_PROPERTY Use the property name to determine labels and converters for the toolkitSnapshotName property. static java.lang.String TOPLEVELTOOLKITACRONYM\_PROPERTY Use the property name to determine labels and converters for the topLevelToolkitAcronym property. static java.lang.String TOPLEVELTOOLKITNAME\_PROPERTY Use the property name to determine labels and converters for the topLevelToolkitName property. static java.lang.String TRACKNAME\_PROPERTY Use the property name to determine labels and converters for the trackName property. static java.lang.String VALIDFROMTIME\_PROPERTY Use the property name to determine labels and converters for the validFromTime property. static java.lang.String VERSION\_PROPERTY Use the property name to determine labels and converters for the version property.

### Field Summary

| Modifier and Type       | Field and Description                                                                                                             |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| static java.lang.String | APPLICATIONNAME\_PROPERTY Use the property name to determine labels and converters for the applicationName property.               |
| static java.lang.String | AUTO\_DELETION\_MODE Use the property name to determine labels and converters for the autoDeletionMode property.                    |
| static java.lang.String | AUTODELETE\_PROPERTY Use the property name to determine labels and converters for the autoDelete property.                         |
| static java.lang.String | AUTONOMY\_PROPERTY Use the property name to determine labels and converters for the autonomy property.                             |
| static java.lang.String | AVAILABLEACTIONS\_PROPERTY Use the property name to determine labels and converters for the availableActions property.             |
| static java.lang.String | COMPENSATIONDEFINED\_PROPERTY Use the property name to determine labels and converters for the compensationDefined property.       |
| static java.lang.String | CONTINUEONERROR\_PROPERTY Use the property name to determine labels and converters for the continueOnError property.               |
| static java.lang.String | COPYRIGHT (C) Copyright IBM Corporation 2005, 2011.                                                                               |
| static java.lang.String | CREATIONTIME\_PROPERTY Use the property name to determine labels and converters for the creationTime property.                     |
| static java.lang.String | CUSTOMTEXT1\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                       |
| static java.lang.String | CUSTOMTEXT2\_PROPERTY Use the property name to determine labels and converters for the customText2 property.                       |
| static java.lang.String | CUSTOMTEXT3\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                       |
| static java.lang.String | CUSTOMTEXT4\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                       |
| static java.lang.String | CUSTOMTEXT5\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                       |
| static java.lang.String | CUSTOMTEXT6\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                       |
| static java.lang.String | CUSTOMTEXT7\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                       |
| static java.lang.String | CUSTOMTEXT8\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                       |
| static java.lang.String | DESCRIPTION\_PROPERTY Use the property name to determine labels and converters for the description property.                       |
| static java.lang.String | DISPLAYNAME\_PROPERTY Use the property name to determine labels and converters for the displayName property.                       |
| static java.lang.String | DOCUMENTATION\_PROPERTY Use the property name to determine labels and converters for the documentation property.                   |
| static java.lang.String | EXECUTIONMODE\_PROPERTY Use the property name to determine labels and converters for the executionMode property.                   |
| static java.lang.String | ID\_PROPERTY Use the property name to determine labels and converters for the ID property.                                         |
| static java.lang.String | INPUTMESSAGETYPENAME\_PROPERTY Use the property name to determine labels and converters for the inputMessageTypeName property.     |
| static java.lang.String | INPUTMESSAGETYPETYPESYSTEM\_PROPERTY Deprecated.                                                                                   |
| static java.lang.String | LASTMODIFICATIONTIME\_PROPERTY Use the property name to determine labels and converters for the lastModificationTime property.     |
| static java.lang.String | NAME\_PROPERTY Use the property name to determine labels and converters for the name property.                                     |
| static java.lang.String | OUTPUTMESSAGETYPENAME\_PROPERTY Use the property name to determine labels and converters for the outputMessageTypeName property.   |
| static java.lang.String | OUTPUTMESSAGETYPETYPESYSTEM\_PROPERTY Deprecated.                                                                                  |
| static java.lang.String | PROCESSADMINSTRATORS\_PROPERTY Deprecated.                                                                                         |
| static java.lang.String | PROCESSAPPACRONYM\_PROPERTY Use the property name to determine labels and converters for the processAppAcronym property.           |
| static java.lang.String | PROCESSAPPNAME\_PROPERTY Use the property name to determine labels and converters for the processAppName property.                 |
| static java.lang.String | SCHEMAVERSION\_PROPERTY Use the property name to determine labels and converters for the schemaVersion property.                   |
| static java.lang.String | SNAPSHOTID\_PROPERTY Use the property name to determine labels and converters for the snapshotID property.                         |
| static java.lang.String | SNAPSHOTNAME\_PROPERTY Use the property name to determine labels and converters for the snapshotName property.                     |
| static java.lang.String | STATE\_PROPERTY Use the property name to determine labels and converters for the state property.                                   |
| static java.lang.String | TARGETNAMESPACE\_PROPERTY Use the property name to determine labels and converters for the targetNamespace property.               |
| static java.lang.String | TIP\_PROPERTY Use the property name to determine labels and converters for the tip property.                                       |
| static java.lang.String | TOOLKITACRONYM\_PROPERTY Use the property name to determine labels and converters for the toolkitAcronym property.                 |
| static java.lang.String | TOOLKITNAME\_PROPERTY Use the property name to determine labels and converters for the toolkitName property.                       |
| static java.lang.String | TOOLKITSNAPSHOTID\_PROPERTY Use the property name to determine labels and converters for the toolkitSnapshotID property.           |
| static java.lang.String | TOOLKITSNAPSHOTNAME\_PROPERTY Use the property name to determine labels and converters for the toolkitSnapshotName property.       |
| static java.lang.String | TOPLEVELTOOLKITACRONYM\_PROPERTY Use the property name to determine labels and converters for the topLevelToolkitAcronym property. |
| static java.lang.String | TOPLEVELTOOLKITNAME\_PROPERTY Use the property name to determine labels and converters for the topLevelToolkitName property.       |
| static java.lang.String | TRACKNAME\_PROPERTY Use the property name to determine labels and converters for the trackName property.                           |
| static java.lang.String | VALIDFROMTIME\_PROPERTY Use the property name to determine labels and converters for the validFromTime property.                   |
| static java.lang.String | VERSION\_PROPERTY Use the property name to determine labels and converters for the version property.                               |

- Fields inherited from interface com.ibm.bpe.api.ProcessTemplateData
AUTO\_DELETE\_NO, AUTO\_DELETE\_ON\_SUCCESSFUL\_COMPLETION, AUTO\_DELETE\_YES, AUTONOMY\_CHILD, AUTONOMY\_NOT\_APPLICABLE, AUTONOMY\_PEER, EXECUTION\_MODE\_LONG\_RUNNING, EXECUTION\_MODE\_MICROFLOW, KIND\_BLOCK, KIND\_PROCESS, SCHEMA\_5\_1, SCHEMA\_5\_1\_1, SCHEMA\_6\_0, SCHEMA\_6\_0\_2, SCHEMA\_6\_1, SCHEMA\_6\_1\_2, SCHEMA\_6\_2, SCHEMA\_7\_0, SCHEMA\_7\_5\_0, SCHEMA\_7\_5\_1, STATE\_MARKED\_FOR\_DELETION, STATE\_STARTED, STATE\_STOPPED

- Constructor Summary

Constructors 

Constructor and Description

ProcessTemplateBean(ProcessTemplateData data,
                   BFMConnection bfmConnection)
Constructs a new ProcessTemplateBean from an original
 ProcessTemplateData object.

ProcessTemplateBean(PTID id,
                   BFMConnection bfmConnection)
Constructs a new ProcessTemplateBean from a process template id.

- Method Summary Methods Modifier and Type Method and Description java.util.List getActivityServiceTemplates () Returns the list of starting activities for the process template. TKTID getAdminTaskTemplateID () Returns the property adminTaskTemplateID . java.lang.String getApplicationName () Returns the property applicationName . boolean getAutoDelete () Deprecated. int getAutoDeletionMode () Returns the property autoDeletionMode . int getAutonomy () Returns the property autonomy . int[] getAvailableActions () Returns the property availableActions . static SimpleConverter getConverter (java.lang.String propertyName) Returns the default converter for a given property. java.util.Calendar getCreationTime () Returns the property creationTime . java.lang.String getCustomText1 () Returns the property customText1 . java.lang.String getCustomText2 () Returns the property customText2 . java.lang.String getCustomText3 () Returns the property customText3 . java.lang.String getCustomText4 () Returns the property customText4 . java.lang.String getCustomText5 () Returns the property customText5 . java.lang.String getCustomText6 () Returns the property customText6 . java.lang.String getCustomText7 () Returns the property customText7 . java.lang.String getCustomText8 () Returns the property customText8 . java.lang.String getDescription () Returns the property description . java.lang.String getDisplayName () Returns the property displayName . java.lang.String getDocumentation () Returns the property documentation . int getExecutionMode () Returns the property executionMode . PTID getID () Returns the property ID . java.lang.String getInputMessageTypeName () Returns the property inputMessageTypeName . java.lang.String getInputMessageTypeTypeSystemName () Deprecated. static java.lang.String getLabel (java.lang.String propertyName) Returns the resource bundle key for a property static java.lang.String getLabel (java.lang.String propertyName, java.util.Locale locale) Returns the label for a property from the resource bundle. java.util.Calendar getLastModificationTime () Returns the property lastModificationTime . java.lang.String getName () Returns the property name . java.lang.String getOutputMessageTypeName () Returns the property outputMessageTypeName . java.lang.String getOutputMessageTypeTypeSystemName () Deprecated. StaffResultSet getProcessAdministrators () Deprecated. java.lang.String getProcessAppAcronym () Returns the processAppAcronym property. java.lang.String getProcessAppName () Returns the processAppName property. int getSchemaVersion () Returns the property schemaVersion . java.lang.String getSnapshotID () Returns the snapshotID property. java.lang.String getSnapshotName () Returns the snapshotName property. int getState () Returns the property state . java.lang.String getTargetNamespace () Returns the property targetNamespace . java.lang.String getToolkitAcronym () Returns the toolkitAcronym property. java.lang.String getToolkitName () Returns the toolkitName property. java.lang.String getToolkitSnapshotID () Returns the toolkitSnapshotID property. java.lang.String getToolkitSnapshotName () Returns the toolkitSnapshotName property. java.lang.String getTopLevelToolkitAcronym () Returns the topLevelToolkitAcronym property. java.lang.String getTopLevelToolkitName () Returns the topLevelToolkitName property. java.lang.String getTrackName () Returns the trackName property. java.util.Calendar getValidFromTime () Returns the property validFromTime . java.lang.String getVersion () Returns the property version . boolean isBusinessRelevant () Returns the businessRelevant property. boolean isCompensationDefined () Returns the compensationDefined property. boolean isContinueOnError () Returns the continueOnError property. boolean isTip () Returns the isTip property. static boolean isValid (java.lang.String propertyName) Checks if the property is valid.

### Method Summary

| Modifier and Type       | Method and Description                                                                                                              |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| java.util.List          | getActivityServiceTemplates() Returns the list of starting activities for the process template.                                     |
| TKTID                   | getAdminTaskTemplateID() Returns the property adminTaskTemplateID.                                                                  |
| java.lang.String        | getApplicationName() Returns the property applicationName.                                                                          |
| boolean                 | getAutoDelete() Deprecated.                                                                                                         |
| int                     | getAutoDeletionMode() Returns the property autoDeletionMode.                                                                        |
| int                     | getAutonomy() Returns the property autonomy.                                                                                        |
| int[]                   | getAvailableActions() Returns the property availableActions.                                                                        |
| static SimpleConverter  | getConverter(java.lang.String propertyName) Returns the default converter for a given property.                                     |
| java.util.Calendar      | getCreationTime() Returns the property creationTime.                                                                                |
| java.lang.String        | getCustomText1() Returns the property customText1.                                                                                  |
| java.lang.String        | getCustomText2() Returns the property customText2.                                                                                  |
| java.lang.String        | getCustomText3() Returns the property customText3.                                                                                  |
| java.lang.String        | getCustomText4() Returns the property customText4.                                                                                  |
| java.lang.String        | getCustomText5() Returns the property customText5.                                                                                  |
| java.lang.String        | getCustomText6() Returns the property customText6.                                                                                  |
| java.lang.String        | getCustomText7() Returns the property customText7.                                                                                  |
| java.lang.String        | getCustomText8() Returns the property customText8.                                                                                  |
| java.lang.String        | getDescription() Returns the property description.                                                                                  |
| java.lang.String        | getDisplayName() Returns the property displayName.                                                                                  |
| java.lang.String        | getDocumentation() Returns the property documentation.                                                                              |
| int                     | getExecutionMode() Returns the property executionMode.                                                                              |
| PTID                    | getID() Returns the property ID.                                                                                                    |
| java.lang.String        | getInputMessageTypeName() Returns the property inputMessageTypeName.                                                                |
| java.lang.String        | getInputMessageTypeTypeSystemName() Deprecated.                                                                                     |
| static java.lang.String | getLabel(java.lang.String propertyName) Returns the resource bundle key for a property                                              |
| static java.lang.String | getLabel(java.lang.String propertyName,         java.util.Locale locale) Returns the label for a property from the resource bundle. |
| java.util.Calendar      | getLastModificationTime() Returns the property lastModificationTime.                                                                |
| java.lang.String        | getName() Returns the property name.                                                                                                |
| java.lang.String        | getOutputMessageTypeName() Returns the property outputMessageTypeName.                                                              |
| java.lang.String        | getOutputMessageTypeTypeSystemName() Deprecated.                                                                                    |
| StaffResultSet          | getProcessAdministrators() Deprecated.                                                                                              |
| java.lang.String        | getProcessAppAcronym() Returns the processAppAcronym property.                                                                      |
| java.lang.String        | getProcessAppName() Returns the processAppName property.                                                                            |
| int                     | getSchemaVersion() Returns the property schemaVersion.                                                                              |
| java.lang.String        | getSnapshotID() Returns the snapshotID property.                                                                                    |
| java.lang.String        | getSnapshotName() Returns the snapshotName property.                                                                                |
| int                     | getState() Returns the property state.                                                                                              |
| java.lang.String        | getTargetNamespace() Returns the property targetNamespace.                                                                          |
| java.lang.String        | getToolkitAcronym() Returns the toolkitAcronym property.                                                                            |
| java.lang.String        | getToolkitName() Returns the toolkitName property.                                                                                  |
| java.lang.String        | getToolkitSnapshotID() Returns the toolkitSnapshotID property.                                                                      |
| java.lang.String        | getToolkitSnapshotName() Returns the toolkitSnapshotName property.                                                                  |
| java.lang.String        | getTopLevelToolkitAcronym() Returns the topLevelToolkitAcronym property.                                                            |
| java.lang.String        | getTopLevelToolkitName() Returns the topLevelToolkitName property.                                                                  |
| java.lang.String        | getTrackName() Returns the trackName property.                                                                                      |
| java.util.Calendar      | getValidFromTime() Returns the property validFromTime.                                                                              |
| java.lang.String        | getVersion() Returns the property version.                                                                                          |
| boolean                 | isBusinessRelevant() Returns the businessRelevant property.                                                                         |
| boolean                 | isCompensationDefined() Returns the compensationDefined property.                                                                   |
| boolean                 | isContinueOnError() Returns the continueOnError property.                                                                           |
| boolean                 | isTip() Returns the isTip property.                                                                                                 |
| static boolean          | isValid(java.lang.String propertyName) Checks if the property is valid.                                                             |

    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait