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

## Interface ProcessTemplateData

- All Superinterfaces:
java.io.Serializable

All Known Implementing Classes:
ProcessTemplateBean

public interface ProcessTemplateData
extends java.io.Serializable
Accesses the properties of a process template.
 
 A process template is a versioned, deployed, and installed process model that contains
 the specification of a process. It can be instantiated and
 started by issuing appropriate requests, for example, initiate or sendMessage. The execution of the
 process instance is driven automatically by the process engine.
 
Since:
7.5 - introduced in 5.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
AUTO\_DELETE\_NO
States that the process instance is not deleted when it reaches an end execution state.

static int
AUTO\_DELETE\_ON\_SUCCESSFUL\_COMPLETION
States that the process instance is only deleted when it reaches the FINISHED state.

static int
AUTO\_DELETE\_YES
States that the process instance is deleted when it reaches any execution end state.

static int
AUTONOMY\_CHILD
States that the process runs dependent of a potential parent process.

static int
AUTONOMY\_NOT\_APPLICABLE
States that the process is a microflow where the autonomy flag is not applicable.

static int
AUTONOMY\_PEER
States that the process runs independently of a potential parent process.

static java.lang.String
COPYRIGHT 

static int
EXECUTION\_MODE\_LONG\_RUNNING
States that the process is a macroflow.

static int
EXECUTION\_MODE\_MICROFLOW
States that the process is a microflow.

static int
KIND\_BLOCK
States that the process template describes a block construct.

static int
KIND\_PROCESS
States that the process template describes a business process.

static int
SCHEMA\_5\_1
Do not use - internal only.

static int
SCHEMA\_5\_1\_1
Do not use - internal only.

static int
SCHEMA\_6\_0
Do not use - internal only.

static int
SCHEMA\_6\_0\_2
Do not use - internal only.

static int
SCHEMA\_6\_1
Do not use - internal only.

static int
SCHEMA\_6\_1\_2
Do not use - internal only.

static int
SCHEMA\_6\_2
Do not use - internal only.

static int
SCHEMA\_7\_0
Do not use - internal only.

static int
SCHEMA\_7\_5\_0
Do not use - internal only.

static int
SCHEMA\_7\_5\_1
Do not use - internal only.

static int
STATE\_MARKED\_FOR\_DELETION
States that the process template belongs to an application that
 is uninstalled but still referenced by existing activity instances.

static int
STATE\_STARTED
States that the process template is available for process instance creation.

static int
STATE\_STOPPED
States that the process template has been stopped.
    - Method Summary

Methods 

Modifier and Type
Method and Description

TKTID
getAdminTaskTemplateID()
Returns the ID of the associated administration task template.

java.lang.String
getApplicationName()
Returns the name of the application the process template is part of.

boolean
getAutoDelete()
Deprecated. 
As of version 6.1, replaced by getAutoDeletionMode.

int
getAutoDeletionMode()
Returns whether an instance of the process template is automatically or
 conditionally deleted when it reaches an end execution state.

int
getAutonomy()
States whether an instance of the process template runs dependently of a potential parent or not.

int[]
getAvailableActions()
Returns the actions that can be called for the current process template.

java.util.Calendar
getCreationTime()
Returns the creation time of the process template.

java.lang.String
getCustomText1()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_1.

java.lang.String
getCustomText2()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_2.

java.lang.String
getCustomText3()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_3.

java.lang.String
getCustomText4()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_4.

java.lang.String
getCustomText5()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_5.

java.lang.String
getCustomText6()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_6.

java.lang.String
getCustomText7()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_7.

java.lang.String
getCustomText8()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_8.

java.lang.String
getDescription()
Returns the description of the process template.

java.lang.String
getDisplayName()
Returns the display name of the process template.

java.lang.String
getDocumentation()
Returns the documentation of the process template.

int
getExecutionMode()
States whether the process template can be executed as a microflow or as a macroflow.

PTID
getID()
Returns the object identifier.

java.lang.String
getInputMessageTypeName()
Returns the name of the input message type.

java.lang.String
getInputMessageTypeTypeSystemName()
Deprecated. 
As of version 6.0, no replacement.

java.util.Calendar
getLastModificationTime()
Returns the last time a property of the process template changed.

java.lang.String
getName()
Returns the name of the process template.

java.lang.String
getOutputMessageTypeName()
Returns the name of the output message type.

java.lang.String
getOutputMessageTypeTypeSystemName()
Deprecated. 
As of version 6.0, no replacement.

StaffResultSet
getProcessAdministrators()
Deprecated. 
As of version 6.0.2, replaced by HumanTaskManager.getUsersInRole(getAdminTaskTemplateID(), WorkItem.REASON\_ADMINISTRATOR).

java.lang.String
getProcessAppAcronym()
Returns an acronym for the process application.

java.lang.String
getProcessAppName()
Returns the name of the process application that contains the process template.

int
getSchemaVersion()
Returns the version of the XML schema that describes the process template.

java.lang.String
getSnapshotID()
Returns the unique identifier of a snapshot that contains the process template.

java.lang.String
getSnapshotName()
Returns the name of a snapshot that contains the process template.

int
getState()
Returns the state of the process template.

java.lang.String
getTargetNamespace()
Returns the target namespace of the process template.

java.lang.String
getToolkitAcronym()
Returns the acronym of a toolkit that contains the process template.

java.lang.String
getToolkitName()
Returns the name of a toolkit that contains the process template.

java.lang.String
getToolkitSnapshotID()
Returns the unique ID of a toolkit snapshot that contains the process template.

java.lang.String
getToolkitSnapshotName()
Returns the name of a toolkit snapshot that contains the process template.

java.lang.String
getTopLevelToolkitAcronym()
Returns the acronym of the topmost toolkit that contains the process template.

java.lang.String
getTopLevelToolkitName()
Returns the name of the topmost toolkit that contains the process template.

java.lang.String
getTrackName()
Returns the name of the track that contains the process template.

java.util.Calendar
getValidFromTime()
Returns the time the process template became or becomes valid.

java.lang.String
getVersion()
Deprecated. 
As of version 7.5, no replacement.

boolean
isBusinessRelevant()
States whether a process instance derived from this template is a business relevant or an "auxiliary" step.

boolean
isCompensationDefined()
For a BPEL process, states whether an instance of the process template can be compensated.

boolean
isContinueOnError()
States whether process instances derived from this template
 stop in case of an unhandled error or not.

boolean
isTip()
States whether the process template is contained in a snapshot or whether it is
 more current.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- STATE\_MARKED\_FOR\_DELETION
static final int STATE\_MARKED\_FOR\_DELETION
States that the process template belongs to an application that
 is uninstalled but still referenced by existing activity instances.
See Also:Constant Field Values

- STATE\_STOPPED
static final int STATE\_STOPPED
States that the process template has been stopped. Process
 instances cannot be created from the process template.
See Also:Constant Field Values

- STATE\_STARTED
static final int STATE\_STARTED
States that the process template is available for process instance creation.
See Also:Constant Field Values

- SCHEMA\_6\_0
static final int SCHEMA\_6\_0
Do not use - internal only.
See Also:Constant Field Values

- SCHEMA\_7\_5\_1
static final int SCHEMA\_7\_5\_1
Do not use - internal only.
See Also:Constant Field Values

- SCHEMA\_6\_1\_2
static final int SCHEMA\_6\_1\_2
Do not use - internal only.
See Also:Constant Field Values

- SCHEMA\_6\_1
static final int SCHEMA\_6\_1
Do not use - internal only.
See Also:Constant Field Values

- SCHEMA\_7\_5\_0
static final int SCHEMA\_7\_5\_0
Do not use - internal only.
See Also:Constant Field Values

- SCHEMA\_6\_2
static final int SCHEMA\_6\_2
Do not use - internal only.
See Also:Constant Field Values

- SCHEMA\_5\_1\_1
static final int SCHEMA\_5\_1\_1
Do not use - internal only.
See Also:Constant Field Values

- SCHEMA\_5\_1
static final int SCHEMA\_5\_1
Do not use - internal only.
See Also:Constant Field Values

- SCHEMA\_6\_0\_2
static final int SCHEMA\_6\_0\_2
Do not use - internal only.
See Also:Constant Field Values

- SCHEMA\_7\_0
static final int SCHEMA\_7\_0
Do not use - internal only.
See Also:Constant Field Values

- EXECUTION\_MODE\_LONG\_RUNNING
static final int EXECUTION\_MODE\_LONG\_RUNNING
States that the process is a macroflow.
See Also:Constant Field Values

- EXECUTION\_MODE\_MICROFLOW
static final int EXECUTION\_MODE\_MICROFLOW
States that the process is a microflow.
See Also:Constant Field Values

- AUTONOMY\_NOT\_APPLICABLE
static final int AUTONOMY\_NOT\_APPLICABLE
States that the process is a microflow where the autonomy flag is not applicable.
See Also:Constant Field Values

- AUTONOMY\_CHILD
static final int AUTONOMY\_CHILD
States that the process runs dependent of a potential parent process.
See Also:Constant Field Values

- AUTONOMY\_PEER
static final int AUTONOMY\_PEER
States that the process runs independently of a potential parent process.
See Also:Constant Field Values

- AUTO\_DELETE\_ON\_SUCCESSFUL\_COMPLETION
static final int AUTO\_DELETE\_ON\_SUCCESSFUL\_COMPLETION
States that the process instance is only deleted when it reaches the FINISHED state.
See Also:Constant Field Values

- AUTO\_DELETE\_YES
static final int AUTO\_DELETE\_YES
States that the process instance is deleted when it reaches any execution end state.
See Also:Constant Field Values

- AUTO\_DELETE\_NO
static final int AUTO\_DELETE\_NO
States that the process instance is not deleted when it reaches an end execution state.
See Also:Constant Field Values

- KIND\_BLOCK
static final int KIND\_BLOCK
States that the process template describes a block construct.
See Also:Constant Field Values

- KIND\_PROCESS
static final int KIND\_PROCESS
States that the process template describes a business process.
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getID
PTID getID()
Returns the object identifier.
    - getAutoDelete
boolean getAutoDelete()
Deprecated. As of version 6.1, replaced by getAutoDeletionMode.
Returns whether an instance of the process template is
 deleted when it reaches an end execution state.
 While being deprecated, this method returns true for
 processes that specify 'yes' or 'onSuccessfulCompletion' for the autoDelete attribute.
 
 End execution states are STATE\_FINISHED, STATE\_COMPENSATED, STATE\_TERMINATED, or
 STATE\_FAILED. STATE\_FAILED is only an end execution state if
 no compensation is defined.
    - getAvailableActions
int[] getAvailableActions()
Returns the actions that can be called for the current process template.
 Refer to ProcessTemplateActions for the set
 of possible actions.
    - getCreationTime
java.util.Calendar getCreationTime()
Returns the creation time of the process template.
    - getDescription
java.lang.String getDescription()
Returns the description of the process template. If there is no
 description, null is returned.
    - getDocumentation
java.lang.String getDocumentation()
Returns the documentation of the process template. If there is no
 documentation, a null string is returned.
    - getState
int getState()
Returns the state of the process template.
 
 Returns whether the process template is started, stopped, or marked for deletion.
    - getSchemaVersion
int getSchemaVersion()
Returns the version of the XML schema that describes the process template.
    - getLastModificationTime
java.util.Calendar getLastModificationTime()
Returns the last time a property of the process template changed.
    - getName
java.lang.String getName()
Returns the name of the process template.
    - getApplicationName
java.lang.String getApplicationName()
Returns the name of the application the process template is part of.
    - getDisplayName
java.lang.String getDisplayName()
Returns the display name of the process template. If there is no display name,
 null is returned.
    - getValidFromTime
java.util.Calendar getValidFromTime()
Returns the time the process template became or becomes valid.
    - getVersion
java.lang.String getVersion()
Deprecated. As of version 7.5, no replacement.
Returns a user-specified version of the process template. If there is no
 user-defined version, a null string is returned.
    - getExecutionMode
int getExecutionMode()
States whether the process template can be executed as a microflow or as a macroflow.
 
 Returns either EXECUTION\_MODE\_MICROFLOW or EXECUTION\_MODE\_LONG\_RUNNING.
    - getAutonomy
int getAutonomy()
States whether an instance of the process template runs dependently of a potential parent or not.
 
 Returns either AUTONOMY\_PEER or AUTONOMY\_CHILD.
    - isCompensationDefined
boolean isCompensationDefined()
For a BPEL process, states whether an instance of the process template can be compensated.
    - getInputMessageTypeName
java.lang.String getInputMessageTypeName()
Returns the name of the input message type. A BPEL process returns a value when there
 is only a single receive or a single pick with a single on-message that creates the
 process instance.
    - getInputMessageTypeTypeSystemName
java.lang.String getInputMessageTypeTypeSystemName()
Deprecated. As of version 6.0, no replacement.
Returns the name of the type system of the input message. A BPEL process returns a value when there
 is only a single receive or a single pick with a single on-message that creates the
 process instance.
    - getOutputMessageTypeName
java.lang.String getOutputMessageTypeName()
Returns the name of the output message type. A BPEL process returns a value when there
 is only a single receive or a single pick with a single on-message that creates the
 process instance.
    - getOutputMessageTypeTypeSystemName
java.lang.String getOutputMessageTypeTypeSystemName()
Deprecated. As of version 6.0, no replacement.
Returns the name of the type system of the output message. A BPEL process returns a value when there
 is only a single receive or a single pick with a single on-message that creates the
 process instance.
    - getProcessAdministrators
StaffResultSet getProcessAdministrators()
                                        throws WorkItemManagerException,
                                               InvalidLengthException
Deprecated. As of version 6.0.2, replaced by HumanTaskManager.getUsersInRole(getAdminTaskTemplateID(), WorkItem.REASON\_ADMINISTRATOR).
Returns the process administrators defined for instances of the process template.
Throws:
WorkItemManagerException
InvalidLengthException
    - getTargetNamespace
java.lang.String getTargetNamespace()
Returns the target namespace of the process template.
    - isBusinessRelevant
boolean isBusinessRelevant()
States whether a process instance derived from this template is a business relevant or an "auxiliary" step. A
 business relevant step can, for example, be logged into the audit trail.
    - getAdminTaskTemplateID
TKTID getAdminTaskTemplateID()
Returns the ID of the associated administration task template.
    - isContinueOnError
boolean isContinueOnError()
States whether process instances derived from this template
 stop in case of an unhandled error or not. True states that process instances
 continue navigation in case of an unhandled error. False states that process instances
 stop navigation in case of an unhandled error to allow for process repair.
Since:
6.1.2.
    - getSnapshotID
java.lang.String getSnapshotID()
Returns the unique identifier of a snapshot that contains the process template.
 Returns null if the template is not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getSnapshotName
java.lang.String getSnapshotName()
Returns the name of a snapshot that contains the process template.
 Returns null if the template is not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getTrackName
java.lang.String getTrackName()
Returns the name of the track that contains the process template.
 Returns null if the template is not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getProcessAppName
java.lang.String getProcessAppName()
Returns the name of the process application that contains the process template.
 Returns null if the template is not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getProcessAppAcronym
java.lang.String getProcessAppAcronym()
Returns an acronym for the process application.
 Returns null if the template is not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getToolkitSnapshotID
java.lang.String getToolkitSnapshotID()
Returns the unique ID of a toolkit snapshot that contains the process template.
 Returns null if the template is not contained in a toolkit or
 not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getToolkitSnapshotName
java.lang.String getToolkitSnapshotName()
Returns the name of a toolkit snapshot that contains the process template.
 Returns null if the template is not contained in a toolkit or
 not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getToolkitName
java.lang.String getToolkitName()
Returns the name of a toolkit that contains the process template.
 Returns null if the template is not contained in a toolkit or
 not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getToolkitAcronym
java.lang.String getToolkitAcronym()
Returns the acronym of a toolkit that contains the process template.
 Returns null if the template is not contained in a toolkit or
 not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getTopLevelToolkitName
java.lang.String getTopLevelToolkitName()
Returns the name of the topmost toolkit that contains the process template.
 Returns null if the template is not contained in a toolkit or
 not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getTopLevelToolkitAcronym
java.lang.String getTopLevelToolkitAcronym()
Returns the acronym of the topmost toolkit that contains the process template.
 Returns null if the template is not contained in a toolkit or
 not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - isTip
boolean isTip()
States whether the process template is contained in a snapshot or whether it is
 more current. True states that the process template is a tip and not contained in a snapshot.
 False states that the process template is contained in a snapshot - see
 getSnapshotName - or
 that the process template is not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getAutoDeletionMode
int getAutoDeletionMode()
Returns whether an instance of the process template is automatically or
 conditionally deleted when it reaches an end execution state. Refer to
 AutoDeletionMode for the possible deletion modes.
 
 End execution states are STATE\_FINISHED, STATE\_COMPENSATED, STATE\_TERMINATED, or
 STATE\_FAILED. STATE\_FAILED is only an end execution state if
 no compensation is defined.
Since:
6.1.
    - getCustomText1
java.lang.String getCustomText1()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_1.
Since:
7.5.1.
    - getCustomText2
java.lang.String getCustomText2()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_2.
Since:
7.5.1.
    - getCustomText3
java.lang.String getCustomText3()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_3.
Since:
7.5.1.
    - getCustomText4
java.lang.String getCustomText4()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_4.
Since:
7.5.1.
    - getCustomText5
java.lang.String getCustomText5()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_5.
Since:
7.5.1.
    - getCustomText6
java.lang.String getCustomText6()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_6.
Since:
7.5.1.
    - getCustomText7
java.lang.String getCustomText7()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_7.
Since:
7.5.1.
    - getCustomText8
java.lang.String getCustomText8()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_8.
Since:
7.5.1.