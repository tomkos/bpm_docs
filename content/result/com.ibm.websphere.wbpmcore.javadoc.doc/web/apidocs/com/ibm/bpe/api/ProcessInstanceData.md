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

## Interface ProcessInstanceData

- All Superinterfaces:
java.io.Serializable

All Known Implementing Classes:
ProcessInstanceBean

public interface ProcessInstanceData
extends java.io.Serializable
Accesses the properties of a process instance.
 
 A process instance comes into existence when a process template is instantiated, for example, by
 an initiate or sendMessage request. It is started immediately causing its state initially to be set to
 running. Execution is driven automatically by the process engine.
 
Since:
7.0 - introduced in 5.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
STATE\_COMPENSATED
States that compensation has been finished for the process instance.

static int
STATE\_COMPENSATING
States that compensation has been started for the process instance.

static int
STATE\_COMPENSATION\_FAILED
States that the (sub)process compensation is failed.

static int
STATE\_DELETED
States that the process has been deleted.

static int
STATE\_FAILED
States that the process instance failed to execute.

static int
STATE\_FAILING
States that an expected or unexpected exception has been encountered.

static int
STATE\_FINISHED
States that the process instance completed successfully.

static int
STATE\_INDOUBT
States that the compensation has encounterd a problem.

static int
STATE\_READY
Do not use - internal only.

static int
STATE\_RUNNING
States that the process instance is running.

static int
STATE\_SUSPENDED
States that the (sub)process instance is suspended.

static int
STATE\_TERMINATED
States that the process instance has been terminated because of an external or
 internal request.

static int
STATE\_TERMINATING
States that the (sub)process instance is terminating because of
 an internal request.
    - Method Summary

Methods 

Modifier and Type
Method and Description

TKIID
getAdminTaskID()
Returns the ID of the associated administration task.

int[]
getAvailableActions()
Returns the actions that can be called in the current process instance
 execution state.

java.lang.String
getCompensationSphereName()
Returns the name of the associated compensation sphere.

java.util.Calendar
getCompletionTime()
Returns the completion time of the process instance.

java.util.Calendar
getCreationTime()
Returns the creation time of the process instance.

java.lang.String
getCustomProperty(java.lang.String arg0)
Returns the value of the specified custom property.

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
Returns the description of the process instance.

java.lang.String
getDisplayName()
Returns the display name of the associated process template.

int
getExecutionState()
Returns the execution state of the process instance.

java.lang.String
getFaultName()
Returns the name of the fault if the process instance ended with a fault
 or EngineMissingReplyException if the process instance implements a two-way operation and
 did not navigate the corresponding reply activity.

PIID
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
Returns the last time a property of the process instance changed.

java.util.Calendar
getLastStateChangeTime()
Returns the last time the execution state of the process instance changed.

java.lang.String
getName()
Returns the name of the process instance.

java.util.List
getNamesOfCustomProperties()
Returns the names of all custom properties.

java.lang.String
getOutputMessageTypeName()
Returns the name of the output message type.

java.lang.String
getOutputMessageTypeTypeSystemName()
Deprecated. 
As of version 6.0, no replacement.

AIID
getParentActivityInstanceID()
Returns the object ID of the parent activity instance, if any.

PIID
getParentProcessInstanceID()
Returns the object ID of the parent process instance, if any.

java.lang.String
getParentProcessInstanceName()
Returns the name of the parent process instance, if any.

StaffResultSet
getProcessAdministrators()
Returns the process administrators.

PTID
getProcessTemplateID()
Returns the object ID of the process template this instance is derived from.

java.lang.String
getProcessTemplateName()
Returns the name of the process template this instance is derived from.

java.util.Calendar
getResumptionTime()
Returns the resumption time of the process instance if the process instance
 is suspended and is to be resumed automatically.

java.lang.String
getStarter()
Returns the starter of the process instance.

java.util.Calendar
getStartTime()
Returns the start time of the process instance.

PIID
getTopLevelProcessInstanceID()
Returns the object ID of the topmost process instance in a hierarchy of processes.

java.lang.String
getTopLevelProcessInstanceName()
Returns the name of the topmost process instance in a hierarchy of processes.

ProcessException
getUnhandledException()
Returns the reason why the process instance failed.

java.util.Calendar
getValidFromTime()
Returns the time the process template became or becomes valid.

boolean
isBusinessRelevant()
States whether the process instance is a business relevant or an "auxiliary" step.

boolean
isCompensationDefined()
States whether the process instance can be compensated.

boolean
isContinueOnError()
States whether the process instance
 stops in case of an unhandled error or not.

boolean
isMigrated()
States whether the process instance has been migrated.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- STATE\_FAILING
static final int STATE\_FAILING
States that an expected or unexpected exception has been encountered. The
 process instance is set to the Failed execution state when all Running or
 Terminating activities end.
See Also:Constant Field Values

- STATE\_RUNNING
static final int STATE\_RUNNING
States that the process instance is running.
See Also:Constant Field Values

- STATE\_TERMINATING
static final int STATE\_TERMINATING
States that the (sub)process instance is terminating because of
 an internal request. The process instance is set to the Terminated execution state
 when all Running or Terminating activities end.
See Also:Constant Field Values

- STATE\_TERMINATED
static final int STATE\_TERMINATED
States that the process instance has been terminated because of an external or
 internal request. If the process instance has been terminated because of an external
 forceTerminate request, the invoke compensation parameter setting determines whether
 compensation is started or not (provided that compensation is defined). If
 the process instance
 is a top-level process instance and the auto-delete setting is not set or
 set to 'true', then the process instance is automatically deleted.
See Also:Constant Field Values

- STATE\_SUSPENDED
static final int STATE\_SUSPENDED
States that the (sub)process instance is suspended.
See Also:Constant Field Values

- STATE\_COMPENSATED
static final int STATE\_COMPENSATED
States that compensation has been finished for the process instance. All
 terminated subprocesses are compensated together with their failed top-level
 process instance. If the process instance is a top-level
 process instance and the auto-delete setting is not set or
 set to 'true', then the process instance is automatically deleted.
See Also:Constant Field Values

- STATE\_FAILED
static final int STATE\_FAILED
States that the process instance failed to execute. When the process instance is
 a top-level process and when compensation is to be done, compensation
 is started and the execution state is set to Compensated. If the process
 instance is a top-level process instance and the auto-delete setting is not set or
 set to 'true', then the process instance is automatically deleted.
See Also:Constant Field Values

- STATE\_DELETED
static final int STATE\_DELETED
States that the process has been deleted. This value is not used by the runtime, but by the BPC Observer.
See Also:Constant Field Values

- STATE\_FINISHED
static final int STATE\_FINISHED
States that the process instance completed successfully. If the process
 instance is a top-level process instance and the auto-delete setting is not set
 or set to 'true', then the process instance is automatically deleted.
See Also:Constant Field Values

- STATE\_READY
static final int STATE\_READY
Do not use - internal only.
See Also:Constant Field Values

- STATE\_INDOUBT
static final int STATE\_INDOUBT
States that the compensation has encounterd a problem.
See Also:Constant Field Values

- STATE\_COMPENSATING
static final int STATE\_COMPENSATING
States that compensation has been started for the process instance. All
 terminated subprocesses are compensated together with their failed top-level
 process instance.
See Also:Constant Field Values

- STATE\_COMPENSATION\_FAILED
static final int STATE\_COMPENSATION\_FAILED
States that the (sub)process compensation is failed.
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getID
PIID getID()
Returns the object identifier.
    - getCompletionTime
java.util.Calendar getCompletionTime()
Returns the completion time of the process instance. If the process instance
 is not yet completed, null is returned.
    - getCreationTime
java.util.Calendar getCreationTime()
Returns the creation time of the process instance.
    - getProcessTemplateName
java.lang.String getProcessTemplateName()
Returns the name of the process template this instance is derived from.
    - getProcessTemplateID
PTID getProcessTemplateID()
Returns the object ID of the process template this instance is derived from.
    - getLastModificationTime
java.util.Calendar getLastModificationTime()
Returns the last time a property of the process instance changed.
    - getLastStateChangeTime
java.util.Calendar getLastStateChangeTime()
Returns the last time the execution state of the process instance changed.
    - getName
java.lang.String getName()
Returns the name of the process instance.
    - getCompensationSphereName
java.lang.String getCompensationSphereName()
Returns the name of the associated compensation sphere. Returns null when
 when there is no compensation sphere.
    - getDisplayName
java.lang.String getDisplayName()
Returns the display name of the associated process template.
 Returns null when a display name is not assigned.
    - getDescription
java.lang.String getDescription()
Returns the description of the process instance. If there is no process
 instance description, the description of the associated process template is
 returned. If there is no process template description, null is
 returned. References to variable members specified as %variableName.memberName%
 are resolved.
    - getStartTime
java.util.Calendar getStartTime()
Returns the start time of the process instance.
    - getExecutionState
int getExecutionState()
Returns the execution state of the process instance. Possible execution states are:
 STATE\_RUNNING, STATE\_FINISHED, STATE\_COMPENSATED,
 STATE\_FAILING, STATE\_FAILED, STATE\_TERMINATING, or STATE\_TERMINATED.
    - getTopLevelProcessInstanceID
PIID getTopLevelProcessInstanceID()
Returns the object ID of the topmost process instance in a hierarchy of processes.
 If the current process instance is the topmost process instance itself or
 if the current process instance is a peer process instance,
 the object ID of the current process instance is returned.
    - getTopLevelProcessInstanceName
java.lang.String getTopLevelProcessInstanceName()
Returns the name of the topmost process instance in a hierarchy of processes.
 If the current process instance is the topmost process instance itself or
 if the current process instance is a peer process instance,
 the name of the current process instance is returned.
    - getParentProcessInstanceID
PIID getParentProcessInstanceID()
Returns the object ID of the parent process instance, if any.
 If the current process instance is no child process, null is returned.
    - getParentProcessInstanceName
java.lang.String getParentProcessInstanceName()
Returns the name of the parent process instance, if any. If the current
 process instance is no child process, null is returned.
    - getParentActivityInstanceID
AIID getParentActivityInstanceID()
Returns the object ID of the parent activity instance, if any.
 If the current process instance is no subprocess, null is returned.
    - getStarter
java.lang.String getStarter()
Returns the starter of the process instance.
    - isCompensationDefined
boolean isCompensationDefined()
States whether the process instance can be compensated.
    - getInputMessageTypeName
java.lang.String getInputMessageTypeName()
Returns the name of the input message type.
    - getInputMessageTypeTypeSystemName
java.lang.String getInputMessageTypeTypeSystemName()
Deprecated. As of version 6.0, no replacement.
Returns the name of the type system of the input message.
    - getOutputMessageTypeName
java.lang.String getOutputMessageTypeName()
Returns the name of the output message type. Returns null if the process
 is not yet completed.
    - getOutputMessageTypeTypeSystemName
java.lang.String getOutputMessageTypeTypeSystemName()
Deprecated. As of version 6.0, no replacement.
Returns the name of the type system of the output message. Returns null if the process
 is not yet completed.
    - getFaultName
java.lang.String getFaultName()
Returns the name of the fault if the process instance ended with a fault
 or EngineMissingReplyException if the process instance implements a two-way operation and
 did not navigate the corresponding reply activity.
    - getAvailableActions
int[] getAvailableActions()
Returns the actions that can be called in the current process instance
 execution state.
 Refer to ProcessInstanceActions for the set
 of possible actions.
    - getCustomProperty
java.lang.String getCustomProperty(java.lang.String arg0)
Returns the value of the specified custom property.
 Returns null if the specified custom property is not found.
 
Parameters:arg0 - The name of the custom property for which the value is to be read.
    - getNamesOfCustomProperties
java.util.List getNamesOfCustomProperties()
Returns the names of all custom properties.
 Returns an empty list when there are no custom properties.
    - getProcessAdministrators
StaffResultSet getProcessAdministrators()
                                        throws WorkItemManagerException,
                                               InvalidLengthException
Returns the process administrators.
Throws:
WorkItemManagerException
InvalidLengthException
    - getValidFromTime
java.util.Calendar getValidFromTime()
Returns the time the process template became or becomes valid.
    - getAdminTaskID
TKIID getAdminTaskID()
Returns the ID of the associated administration task.
 Returns null if there is no administration task.
    - isBusinessRelevant
boolean isBusinessRelevant()
States whether the process instance is a business relevant or an "auxiliary" step.
    - isContinueOnError
boolean isContinueOnError()
States whether the process instance
 stops in case of an unhandled error or not. True states that the process instance
 continues navigation in case of an unhandled error. False states that the process instance
 stops navigation in case of an unhandled error to allow for process repair.
Since:
6.1.2.
    - getResumptionTime
java.util.Calendar getResumptionTime()
Returns the resumption time of the process instance if the process instance
 is suspended and is to be resumed automatically. If the process instance
 is not suspended or not to be resumed automatically, null is returned.
Since:
6.1.
    - getUnhandledException
ProcessException getUnhandledException()
Returns the reason why the process instance failed.
Since:
6.1.2.
    - isMigrated
boolean isMigrated()
States whether the process instance has been migrated. True states
 that the process instance has been migrated. False states that the
 process instance has not been migrated.
Since:
7.0.
    - getCustomText1
java.lang.String getCustomText1()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_1.
 Refer to setInlineCustomProperty
 for setting the value.
Since:
7.5.1.
    - getCustomText2
java.lang.String getCustomText2()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_2.
 Refer to setInlineCustomProperty
 for setting the value.
Since:
7.5.1.
    - getCustomText3
java.lang.String getCustomText3()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_3.
 Refer to setInlineCustomProperty
 for setting the value.
Since:
7.5.1.
    - getCustomText4
java.lang.String getCustomText4()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_4.
 Refer to setInlineCustomProperty
 for setting the value.
Since:
7.5.1.
    - getCustomText5
java.lang.String getCustomText5()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_5.
 Refer to setInlineCustomProperty
 for setting the value.
Since:
7.5.1.
    - getCustomText6
java.lang.String getCustomText6()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_6.
 Refer to setInlineCustomProperty
 for setting the value.
Since:
7.5.1.
    - getCustomText7
java.lang.String getCustomText7()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_7.
 Refer to setInlineCustomProperty
 for setting the value.
Since:
7.5.1.
    - getCustomText8
java.lang.String getCustomText8()
Returns the value of the inline custom property named
 InlineCustomProperty.CUSTOM\_TEXT\_8.
 Refer to setInlineCustomProperty
 for setting the value.
Since:
7.5.1.