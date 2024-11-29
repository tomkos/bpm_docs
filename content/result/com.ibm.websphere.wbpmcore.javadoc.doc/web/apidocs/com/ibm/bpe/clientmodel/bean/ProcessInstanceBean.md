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

## Class ProcessInstanceBean

- java.lang.Object
    - com.ibm.bpe.clientmodel.bean.ProcessInstanceBean

- All Implemented Interfaces: ProcessInstanceData , java.io.Serializable public class ProcessInstanceBean extends java.lang.Objectimplements ProcessInstanceData Accesses the properties of the original ProcessInstanceData object and adds metadata for national language support and converters. A ProcessInstanceBean object can be instantiated from either a QueryResultSet object or a ProcessInstanceData object. If the bean was instantiated from an original object returned by the Business Process Choreographer API, all properties are loaded. If, however the bean is instantiated from a query only the following properties are loaded from the query result set: If the property is not found in the query result set, the property remains empty. Accessing an empty property requires the bean to load the missing information from the server. Use the static method getLabel(String, Locale) to retrieve the localized label for a property. Use the static method getConverter(String) to retrieve a converter for a property. The return value might be null, as converters are optional. See Also: ProcessInstanceData , QueryResultSet , Serialized Form

```
public class ProcessInstanceBean
extends java.lang.Object
implements ProcessInstanceData
```

Accesses the properties of the original ProcessInstanceData object
 and adds metadata for national language support and converters.

A ProcessInstanceBean object can be instantiated from either a
 QueryResultSet object or a ProcessInstanceData object. 

 If the bean was instantiated from an original object returned by the Business
 Process Choreographer API, all properties are loaded. If, however the bean is
 instantiated from a query only the following properties are loaded from the
 query result set:
 
ID
completionTime
creationTime
description
name
parentProcessInstanceName
startTime
starter
executionState
processTemplateName
processTemplateDisplayName
topLevelProcessInstanceName

 If the property is not found in the query result set, the property remains
 empty. Accessing an empty property requires the bean to load the missing
 information from the server.

Use the static method getLabel(String, Locale) to
 retrieve the localized label for a property. Use the static method
 getConverter(String) to retrieve a converter for
 a property. The return value might be null, as converters are optional.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String AVAILABLEACTIONS\_PROPERTY Use the property name to determine labels and converters for the applicationName property. static java.lang.String COMPENSATIONSPHERENAME\_PROPERTY Use the property name to determine labels and converters for the compensationSphereName property. static java.lang.String COMPLETIONTIME\_PROPERTY Use the property name to determine labels and converters for the completionTime property. static java.lang.String CONTINUEONERROR\_PROPERTY Use the property name to determine labels and converters for the continueOnError property. static java.lang.String COPYRIGHT (C) Copyright IBM Corporation 2004, 2012. static java.lang.String CREATIONTIME\_PROPERTY Use the property name to determine labels and converters for the creationTime property. static java.lang.String CUSTOMPROPERTY\_PROPERTY Use the property name to determine labels and converters for the customProperty property. static java.lang.String CUSTOMTEXT1\_PROPERTY Use the property name to determine labels and converters for the customText1 property. static java.lang.String CUSTOMTEXT2\_PROPERTY Use the property name to determine labels and converters for the customText2 property. static java.lang.String CUSTOMTEXT3\_PROPERTY Use the property name to determine labels and converters for the customText3 property. static java.lang.String CUSTOMTEXT4\_PROPERTY Use the property name to determine labels and converters for the customText4 property. static java.lang.String CUSTOMTEXT5\_PROPERTY Use the property name to determine labels and converters for the customText5 property. static java.lang.String CUSTOMTEXT6\_PROPERTY Use the property name to determine labels and converters for the customText6 property. static java.lang.String CUSTOMTEXT7\_PROPERTY Use the property name to determine labels and converters for the customText7 property. static java.lang.String CUSTOMTEXT8\_PROPERTY Use the property name to determine labels and converters for the customText8 property. static java.lang.String DESCRIPTION\_PROPERTY Use the property name to determine labels and converters for the description property. static java.lang.String DISPLAYNAME\_PROPERTY Use the property name to determine labels and converters for the displayName property. static java.lang.String EXCEPTIONMESSAGE\_PROPERTY Use the property name to determine labels and converters for theexceptionMessage property. static java.lang.String EXECUTIONSTATE\_PROPERTY Use the property name to determine labels and converters for the executionState property. static java.lang.String FAULTNAME\_PROPERTY Use the property name to determine labels and converters for the faultName property. static java.lang.String ID\_PROPERTY Use the property name to determine labels and converters for the ID property. static java.lang.String INPUTMESSAGETPYENAME\_PROPERTY Use the property name to determine labels and converters for the inputMessageTypeName property. static java.lang.String INPUTMESSAGETYPETYPESYSTEMNAME\_PROPERTY Deprecated. static java.lang.String ISCOMPENSATIONDEFINED\_PROPERTY Use the property name to determine labels and converters for the compensationDefined property. static java.lang.String LASTMODIFICATIONTIME\_PROPERTY Use the property name to determine labels and converters for the lastModificationTime property. static java.lang.String LASTSTATECHANGETIME\_PROPERTY Use the property name to determine labels and converters for the lastStateChange property. static java.lang.String MIGRATED\_PROPERTY Use the property name to determine labels and converters for the Migrated property. static java.lang.String NAME\_PROPERTY Use the property name to determine labels and converters for the name property. static java.lang.String OUTPUTMESSAGETPYENAME\_PROPERTY Use the property name to determine labels and converters for the outputMessageTypeName property. static java.lang.String OUTPUTMESSAGETYPETYPESYSTEMNAME\_PROPERTY Deprecated. static java.lang.String PARENTACTIVITYINSTANCEID\_PROPERTY Use the property name to determine labels and converters for the parentActivityInstanceID property. static java.lang.String PARENTPROCESSINSTANCEID\_PROPERTY Use the property name to determine labels and converters for the parentProcessInstanceID property. static java.lang.String PARENTPROCESSINSTANCENAME\_PROPERTY Use the property name to determine labels and converters for theparentProcessInstanceName property. static java.lang.String PROCESSADMINISTRATORS\_PROPERTY Use the property name to determine labels and converters for the processAdministrators property. static java.lang.String PROCESSAPPACRONYM\_PROPERTY Use the property name to determine labels and converters for the processAppAcronym property. static java.lang.String PROCESSAPPNAME\_PROPERTY Use the property name to determine labels and converters for the processAppName property. static java.lang.String PROCESSTEMPLATEDISPLAYNAME\_PROPERTY Use the property name to determine labels and converters for the processTemplateDisplayName property. static java.lang.String PROCESSTEMPLATEID\_PROPERTY Use the property name to determine labels and converters for the processTemplateID property. static java.lang.String PROCESSTEMPLATENAME\_PROPERTY Use the property name to determine labels and converters for the processTemplateName property. static java.lang.String RESUMPTIONTIME\_PROPERTY Use the property name to determine labels and converters for the resumptionTime property. static java.lang.String SNAPSHOTID\_PROPERTY Use the property name to determine labels and converters for the snapshotID property. static java.lang.String SNAPSHOTNAME\_PROPERTY Use the property name to determine labels and converters for the snapshotName property. static java.lang.String STARTER\_PROPERTY Use the property name to determine labels and converters for the starter property. static java.lang.String STARTTIME\_PROPERTY Use the property name to determine labels and converters for the startTime property. static java.lang.String TIP\_PROPERTY Use the property name to determine labels and converters for the tip property. static java.lang.String TOOLKITACRONYM\_PROPERTY Use the property name to determine labels and converters for the toolkitAcronym property. static java.lang.String TOOLKITNAME\_PROPERTY Use the property name to determine labels and converters for the toolkitName property. static java.lang.String TOOLKITSNAPSHOTID\_PROPERTY Use the property name to determine labels and converters for the toolkitSnapshotID property. static java.lang.String TOOLKITSNAPSHOTNAME\_PROPERTY Use the property name to determine labels and converters for the toolkitSnapshotName property. static java.lang.String TOPLEVELPROCESSINSTANCEID\_PROPERTY Use the property name to determine labels and converters for the topLevelProcessInstanceID property. static java.lang.String TOPLEVELPROCESSINSTANCENAME\_PROPERTY Use the property name to determine labels and converters for the topLevelProcessInstanceName property. static java.lang.String TOPLEVELTOOLKITACRONYM\_PROPERTY Use the property name to determine labels and converters for the topLevelToolkitAcronym property. static java.lang.String TOPLEVELTOOLKITNAME\_PROPERTY Use the property name to determine labels and converters for the topLevelToolkitName property. static java.lang.String TRACKNAME\_PROPERTY Use the property name to determine labels and converters for the trackName property. static java.lang.String UNHANDLEDEXCEPTION\_PROPERTY Use the property name to determine labels and converters for theunhandledException property. static java.lang.String VALIDFROMTIME\_PROPERTY Use the property name to determine labels and converters for thevalidFromTime property

### Field Summary

| Modifier and Type       | Field and Description                                                                                                                        |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| static java.lang.String | AVAILABLEACTIONS\_PROPERTY Use the property name to determine labels and converters for the  applicationName property.                        |
| static java.lang.String | COMPENSATIONSPHERENAME\_PROPERTY Use the property name to determine labels and converters for the  compensationSphereName property.           |
| static java.lang.String | COMPLETIONTIME\_PROPERTY Use the property name to determine labels and converters for the  completionTime property.                           |
| static java.lang.String | CONTINUEONERROR\_PROPERTY Use the property name to determine labels and converters for the continueOnError property.                          |
| static java.lang.String | COPYRIGHT (C) Copyright IBM Corporation 2004, 2012.                                                                                          |
| static java.lang.String | CREATIONTIME\_PROPERTY Use the property name to determine labels and converters for the  creationTime property.                               |
| static java.lang.String | CUSTOMPROPERTY\_PROPERTY Use the property name to determine labels and converters for the  customProperty property.                           |
| static java.lang.String | CUSTOMTEXT1\_PROPERTY Use the property name to determine labels and converters for the customText1 property.                                  |
| static java.lang.String | CUSTOMTEXT2\_PROPERTY Use the property name to determine labels and converters for the customText2 property.                                  |
| static java.lang.String | CUSTOMTEXT3\_PROPERTY Use the property name to determine labels and converters for the customText3 property.                                  |
| static java.lang.String | CUSTOMTEXT4\_PROPERTY Use the property name to determine labels and converters for the customText4 property.                                  |
| static java.lang.String | CUSTOMTEXT5\_PROPERTY Use the property name to determine labels and converters for the customText5 property.                                  |
| static java.lang.String | CUSTOMTEXT6\_PROPERTY Use the property name to determine labels and converters for the customText6 property.                                  |
| static java.lang.String | CUSTOMTEXT7\_PROPERTY Use the property name to determine labels and converters for the customText7 property.                                  |
| static java.lang.String | CUSTOMTEXT8\_PROPERTY Use the property name to determine labels and converters for the customText8 property.                                  |
| static java.lang.String | DESCRIPTION\_PROPERTY Use the property name to determine labels and converters for the  description property.                                 |
| static java.lang.String | DISPLAYNAME\_PROPERTY Use the property name to determine labels and converters for the  displayName property.                                 |
| static java.lang.String | EXCEPTIONMESSAGE\_PROPERTY Use the property name to determine labels and converters for theexceptionMessage  property.                        |
| static java.lang.String | EXECUTIONSTATE\_PROPERTY Use the property name to determine labels and converters for the  executionState property.                           |
| static java.lang.String | FAULTNAME\_PROPERTY Use the property name to determine labels and converters for the  faultName property.                                     |
| static java.lang.String | ID\_PROPERTY Use the property name to determine labels and converters for the  ID property.                                                   |
| static java.lang.String | INPUTMESSAGETPYENAME\_PROPERTY Use the property name to determine labels and converters for the  inputMessageTypeName property.               |
| static java.lang.String | INPUTMESSAGETYPETYPESYSTEMNAME\_PROPERTY Deprecated.                                                                                          |
| static java.lang.String | ISCOMPENSATIONDEFINED\_PROPERTY Use the property name to determine labels and converters for the  compensationDefined property.               |
| static java.lang.String | LASTMODIFICATIONTIME\_PROPERTY Use the property name to determine labels and converters for the  lastModificationTime property.               |
| static java.lang.String | LASTSTATECHANGETIME\_PROPERTY Use the property name to determine labels and converters for the  lastStateChange property.                     |
| static java.lang.String | MIGRATED\_PROPERTY Use the property name to determine labels and converters for the  Migrated property.                                       |
| static java.lang.String | NAME\_PROPERTY Use the property name to determine labels and converters for the  name property.                                               |
| static java.lang.String | OUTPUTMESSAGETPYENAME\_PROPERTY Use the property name to determine labels and converters for the  outputMessageTypeName property.             |
| static java.lang.String | OUTPUTMESSAGETYPETYPESYSTEMNAME\_PROPERTY Deprecated.                                                                                         |
| static java.lang.String | PARENTACTIVITYINSTANCEID\_PROPERTY Use the property name to determine labels and converters for the  parentActivityInstanceID property.       |
| static java.lang.String | PARENTPROCESSINSTANCEID\_PROPERTY Use the property name to determine labels and converters for the  parentProcessInstanceID property.         |
| static java.lang.String | PARENTPROCESSINSTANCENAME\_PROPERTY Use the property name to determine labels and converters for theparentProcessInstanceName  property.      |
| static java.lang.String | PROCESSADMINISTRATORS\_PROPERTY Use the property name to determine labels and converters for the  processAdministrators property.             |
| static java.lang.String | PROCESSAPPACRONYM\_PROPERTY Use the property name to determine labels and converters for the processAppAcronym property.                      |
| static java.lang.String | PROCESSAPPNAME\_PROPERTY Use the property name to determine labels and converters for the processAppName property.                            |
| static java.lang.String | PROCESSTEMPLATEDISPLAYNAME\_PROPERTY Use the property name to determine labels and converters for the  processTemplateDisplayName property.   |
| static java.lang.String | PROCESSTEMPLATEID\_PROPERTY Use the property name to determine labels and converters for the  processTemplateID property.                     |
| static java.lang.String | PROCESSTEMPLATENAME\_PROPERTY Use the property name to determine labels and converters for the  processTemplateName property.                 |
| static java.lang.String | RESUMPTIONTIME\_PROPERTY Use the property name to determine labels and converters for the  resumptionTime property.                           |
| static java.lang.String | SNAPSHOTID\_PROPERTY Use the property name to determine labels and converters for the snapshotID property.                                    |
| static java.lang.String | SNAPSHOTNAME\_PROPERTY Use the property name to determine labels and converters for the snapshotName property.                                |
| static java.lang.String | STARTER\_PROPERTY Use the property name to determine labels and converters for the  starter property.                                         |
| static java.lang.String | STARTTIME\_PROPERTY Use the property name to determine labels and converters for the  startTime property.                                     |
| static java.lang.String | TIP\_PROPERTY Use the property name to determine labels and converters for the tip property.                                                  |
| static java.lang.String | TOOLKITACRONYM\_PROPERTY Use the property name to determine labels and converters for the toolkitAcronym property.                            |
| static java.lang.String | TOOLKITNAME\_PROPERTY Use the property name to determine labels and converters for the toolkitName property.                                  |
| static java.lang.String | TOOLKITSNAPSHOTID\_PROPERTY Use the property name to determine labels and converters for the toolkitSnapshotID property.                      |
| static java.lang.String | TOOLKITSNAPSHOTNAME\_PROPERTY Use the property name to determine labels and converters for the toolkitSnapshotName property.                  |
| static java.lang.String | TOPLEVELPROCESSINSTANCEID\_PROPERTY Use the property name to determine labels and converters for the  topLevelProcessInstanceID property.     |
| static java.lang.String | TOPLEVELPROCESSINSTANCENAME\_PROPERTY Use the property name to determine labels and converters for the  topLevelProcessInstanceName property. |
| static java.lang.String | TOPLEVELTOOLKITACRONYM\_PROPERTY Use the property name to determine labels and converters for the topLevelToolkitAcronym property.            |
| static java.lang.String | TOPLEVELTOOLKITNAME\_PROPERTY Use the property name to determine labels and converters for the topLevelToolkitName property.                  |
| static java.lang.String | TRACKNAME\_PROPERTY Use the property name to determine labels and converters for the trackName property.                                      |
| static java.lang.String | UNHANDLEDEXCEPTION\_PROPERTY Use the property name to determine labels and converters for theunhandledException  property.                    |
| static java.lang.String | VALIDFROMTIME\_PROPERTY Use the property name to determine labels and converters for thevalidFromTime property                                |

- Fields inherited from interface com.ibm.bpe.api.ProcessInstanceData
STATE\_COMPENSATED, STATE\_COMPENSATING, STATE\_COMPENSATION\_FAILED, STATE\_DELETED, STATE\_FAILED, STATE\_FAILING, STATE\_FINISHED, STATE\_INDOUBT, STATE\_READY, STATE\_RUNNING, STATE\_SUSPENDED, STATE\_TERMINATED, STATE\_TERMINATING

- Constructor Summary

Constructors 

Constructor and Description

ProcessInstanceBean(PIID id,
                   BFMConnection bfmConnection)
Constructs a new ProcessInstanceBean from a process instance id

ProcessInstanceBean(ProcessInstanceData processInstance,
                   BFMConnection bfmConnection)
Constructs a new ProcessInstanceBean from an original
 ProcessInstanceData object.

ProcessInstanceBean(QueryResultSet resultSet,
                   BFMConnection bfmConnection)
Constructs a new ProcessInstanceBean from a
 QueryResultSet.

ProcessInstanceBean(QueryResultSet resultSet,
                   java.lang.String processDataViewName,
                   BFMConnection bfmConnection)
Constructs a new ProcessInstanceBean from a
 QueryResultSet.

- Method Summary Methods Modifier and Type Method and Description TKIID getAdminTaskID () Returns the adminTaskID property. int[] getAvailableActions () Returns the availableActions property. java.lang.String getCompensationSphereName () Returns the compensationSphereName property. java.util.Calendar getCompletionTime () Returns the completionTime property. static SimpleConverter getConverter (java.lang.String propertyName) Returns the default converter for a given property. java.util.Calendar getCreationTime () Returns the creationTime property. java.lang.String getCustomProperty (java.lang.String propertyName) Returns the customProperty property. java.lang.String getCustomText1 () Returns the customText1 property. java.lang.String getCustomText2 () Returns the customText2 property. java.lang.String getCustomText3 () Returns the customText3 property. java.lang.String getCustomText4 () Returns the customText4 property. java.lang.String getCustomText5 () Returns the customText5 property. java.lang.String getCustomText6 () Returns the customText6 property. java.lang.String getCustomText7 () Returns the customText7 property. java.lang.String getCustomText8 () Returns the customText8 property. java.lang.String getDescription () Returns the description property. java.lang.String getDisplayName () Returns the displayName property. int getExecutionState () Returns the executionState property. MessageWrapper getFaultMessageWrapper () Retrieves the fault message. java.lang.String getFaultName () Returns the faultName property. PIID getID () Returns the ID property. java.lang.String getInputMessageTypeName () Returns the inputMessageTypeName property. java.lang.String getInputMessageTypeTypeSystemName () Deprecated. MessageWrapper getInputMessageWrapper () Retrieves the input message. static java.lang.String getLabel (java.lang.String propertyName) Returns the resource bundle key for a property static java.lang.String getLabel (java.lang.String propertyName, java.util.Locale locale) Returns the label for a property from the resource bundle. java.util.Calendar getLastModificationTime () Returns the lastModificationTime property. java.util.Calendar getLastStateChangeTime () Returns the lastStateChangeTime property. java.lang.String getName () Returns the name property. java.util.List getNamesOfCustomProperties () Returns the namesOfCustomProperties property. java.lang.String getOutputMessageTypeName () Returns the outputMessageTypeName property. java.lang.String getOutputMessageTypeTypeSystemName () Deprecated. MessageWrapper getOutputMessageWrapper () Retrieves the output message. AIID getParentActivityInstanceID () Returns the parentActivityInstanceID property. PIID getParentProcessInstanceID () Returns the parentProcessInstanceID property. java.lang.String getParentProcessInstanceName () Returns the parentProcessInstanceName property. StaffResultSet getProcessAdministrators () Returns the processAdministrators property. java.lang.String getProcessAppAcronym () Returns the processAppAcronym property. java.lang.String getProcessAppName () Returns the processAppName property. java.lang.String getProcessTemplateDisplayName () Returns the processTemplateDisplayName property. PTID getProcessTemplateID () Returns the processTemplateID property. java.lang.String getProcessTemplateName () Returns the processTemplateName property. java.util.Calendar getResumptionTime () Returns the resumptionTime property. java.lang.String getSnapshotID () Returns the snapshotID property. java.lang.String getSnapshotName () Returns the snapshotName property. java.lang.String getStarter () Returns the starter property. java.util.Calendar getStartTime () Returns the startTime property. java.lang.String getToolkitAcronym () Returns the toolkitAcronym property. java.lang.String getToolkitName () Returns the toolkitName property. java.lang.String getToolkitSnapshotID () Returns the toolkitSnapshotID property. java.lang.String getToolkitSnapshotName () Returns the toolkitSnapshotName property. PIID getTopLevelProcessInstanceID () Returns the topLevelProcessInstanceID property. java.lang.String getTopLevelProcessInstanceName () Returns the topLevelProcessInstanceName property. java.lang.String getTopLevelToolkitAcronym () Returns the topLevelToolkitAcronym property. java.lang.String getTopLevelToolkitName () Returns the topLevelToolkitName property. java.lang.String getTrackName () Returns the trackName property. ProcessException getUnhandledException () Retrieves the unhandled exception. java.util.Calendar getValidFromTime () Returns the validFromTime property. boolean isBusinessRelevant () Returns the businessRelevant property. boolean isCompensationDefined () Returns the compensationDefined property. boolean isContinueOnError () Returns the continueOnError property. boolean isMigrated () States whether the process instance has been migrated. boolean isTip () Returns the isTip property. static boolean isValid (java.lang.String propertyName) Checks whether the property is valid. void setExecutionState (int state) Changes the executionState property of the process instance.

### Method Summary

| Modifier and Type       | Method and Description                                                                                                              |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| TKIID                   | getAdminTaskID() Returns the adminTaskID property.                                                                                  |
| int[]                   | getAvailableActions() Returns the availableActions property.                                                                        |
| java.lang.String        | getCompensationSphereName() Returns the compensationSphereName property.                                                            |
| java.util.Calendar      | getCompletionTime() Returns the completionTime property.                                                                            |
| static SimpleConverter  | getConverter(java.lang.String propertyName) Returns the default converter for a given property.                                     |
| java.util.Calendar      | getCreationTime() Returns the creationTime property.                                                                                |
| java.lang.String        | getCustomProperty(java.lang.String propertyName) Returns the customProperty property.                                               |
| java.lang.String        | getCustomText1() Returns the customText1 property.                                                                                  |
| java.lang.String        | getCustomText2() Returns the customText2 property.                                                                                  |
| java.lang.String        | getCustomText3() Returns the customText3 property.                                                                                  |
| java.lang.String        | getCustomText4() Returns the customText4 property.                                                                                  |
| java.lang.String        | getCustomText5() Returns the customText5 property.                                                                                  |
| java.lang.String        | getCustomText6() Returns the customText6 property.                                                                                  |
| java.lang.String        | getCustomText7() Returns the customText7 property.                                                                                  |
| java.lang.String        | getCustomText8() Returns the customText8 property.                                                                                  |
| java.lang.String        | getDescription() Returns the description property.                                                                                  |
| java.lang.String        | getDisplayName() Returns the displayName property.                                                                                  |
| int                     | getExecutionState() Returns the executionState property.                                                                            |
| MessageWrapper          | getFaultMessageWrapper() Retrieves the fault message.                                                                               |
| java.lang.String        | getFaultName() Returns the faultName property.                                                                                      |
| PIID                    | getID() Returns the ID property.                                                                                                    |
| java.lang.String        | getInputMessageTypeName() Returns the inputMessageTypeName property.                                                                |
| java.lang.String        | getInputMessageTypeTypeSystemName() Deprecated.                                                                                     |
| MessageWrapper          | getInputMessageWrapper() Retrieves the input message.                                                                               |
| static java.lang.String | getLabel(java.lang.String propertyName) Returns the resource bundle key for a property                                              |
| static java.lang.String | getLabel(java.lang.String propertyName,         java.util.Locale locale) Returns the label for a property from the resource bundle. |
| java.util.Calendar      | getLastModificationTime() Returns the lastModificationTime property.                                                                |
| java.util.Calendar      | getLastStateChangeTime() Returns the lastStateChangeTime property.                                                                  |
| java.lang.String        | getName() Returns the name property.                                                                                                |
| java.util.List          | getNamesOfCustomProperties() Returns the namesOfCustomProperties property.                                                          |
| java.lang.String        | getOutputMessageTypeName() Returns the outputMessageTypeName property.                                                              |
| java.lang.String        | getOutputMessageTypeTypeSystemName() Deprecated.                                                                                    |
| MessageWrapper          | getOutputMessageWrapper() Retrieves the output message.                                                                             |
| AIID                    | getParentActivityInstanceID() Returns the parentActivityInstanceID property.                                                        |
| PIID                    | getParentProcessInstanceID() Returns the parentProcessInstanceID property.                                                          |
| java.lang.String        | getParentProcessInstanceName() Returns the parentProcessInstanceName property.                                                      |
| StaffResultSet          | getProcessAdministrators() Returns the processAdministrators property.                                                              |
| java.lang.String        | getProcessAppAcronym() Returns the processAppAcronym property.                                                                      |
| java.lang.String        | getProcessAppName() Returns the processAppName property.                                                                            |
| java.lang.String        | getProcessTemplateDisplayName() Returns the processTemplateDisplayName property.                                                    |
| PTID                    | getProcessTemplateID() Returns the processTemplateID property.                                                                      |
| java.lang.String        | getProcessTemplateName() Returns the processTemplateName property.                                                                  |
| java.util.Calendar      | getResumptionTime() Returns the resumptionTime property.                                                                            |
| java.lang.String        | getSnapshotID() Returns the snapshotID property.                                                                                    |
| java.lang.String        | getSnapshotName() Returns the snapshotName property.                                                                                |
| java.lang.String        | getStarter() Returns the starter property.                                                                                          |
| java.util.Calendar      | getStartTime() Returns the startTime property.                                                                                      |
| java.lang.String        | getToolkitAcronym() Returns the toolkitAcronym property.                                                                            |
| java.lang.String        | getToolkitName() Returns the toolkitName property.                                                                                  |
| java.lang.String        | getToolkitSnapshotID() Returns the toolkitSnapshotID property.                                                                      |
| java.lang.String        | getToolkitSnapshotName() Returns the toolkitSnapshotName property.                                                                  |
| PIID                    | getTopLevelProcessInstanceID() Returns the topLevelProcessInstanceID property.                                                      |
| java.lang.String        | getTopLevelProcessInstanceName() Returns the topLevelProcessInstanceName property.                                                  |
| java.lang.String        | getTopLevelToolkitAcronym() Returns the topLevelToolkitAcronym property.                                                            |
| java.lang.String        | getTopLevelToolkitName() Returns the topLevelToolkitName property.                                                                  |
| java.lang.String        | getTrackName() Returns the trackName property.                                                                                      |
| ProcessException        | getUnhandledException() Retrieves the unhandled exception.                                                                          |
| java.util.Calendar      | getValidFromTime() Returns the validFromTime property.                                                                              |
| boolean                 | isBusinessRelevant() Returns the businessRelevant property.                                                                         |
| boolean                 | isCompensationDefined() Returns the compensationDefined property.                                                                   |
| boolean                 | isContinueOnError() Returns the continueOnError property.                                                                           |
| boolean                 | isMigrated() States whether the process instance has been migrated.                                                                 |
| boolean                 | isTip() Returns the isTip property.                                                                                                 |
| static boolean          | isValid(java.lang.String propertyName) Checks whether the property is valid.                                                        |
| void                    | setExecutionState(int state) Changes the executionState property of the process  instance.                                          |

    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait