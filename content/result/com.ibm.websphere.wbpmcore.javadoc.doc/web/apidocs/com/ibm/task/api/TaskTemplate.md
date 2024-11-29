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

## Interface TaskTemplate

- All Superinterfaces:
java.io.Serializable

All Known Implementing Classes:
TaskTemplateBean

public interface TaskTemplate
extends java.io.Serializable
Accesses the properties of a task template.
 
 A task template is a versioned model that contains the specification
 of a task. The task can be an operation performed by a person, for example, the
 completion of a form or document, an operation performed by a machine,
 or an IBM Business Automation Workflow subprocess.
 
 A task template has input, output, and faults to describe data passed to
 tasks derived from the template and data resulting from task execution.
 A task template can be instantiated by issuing appropriate requests, for example,
 createTask().
 
Since:
7.5 - introduced in 6.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
ASSIGNMENT\_TYPE\_PARALLEL
States that a task derived from this template can be assigned to multiple persons in parallel.

static int
ASSIGNMENT\_TYPE\_SINGLE
States that a task derived from this template can only be assigned to a single person.

static int
AUTH\_NONE
States that no operations can be executed on the associated context.

static int
AUTH\_READER
States that operations can be executed on the associated context that require
 Reader authority, for example, reading the properties of a process instance.

static int
AUTO\_DELETE\_ON\_COMPLETION
States that a completed task instance derived from this template
 is deleted when the duration until deletion has passed.

static int
AUTO\_DELETE\_ON\_SUCCESSFUL\_COMPLETION
States that a task instance derived from this template
 is deleted when it reaches the FINISHED state.

static int
AUTONOMY\_CHILD
States that task instances derived from this template run dependently of a potential parent process.

static int
AUTONOMY\_NOT\_APPLICABLE
States that the autonomy flag is not applicable.

static int
AUTONOMY\_PEER
States that task instances derived from this template run independently of a potential parent process.

static java.lang.String
COPYRIGHT 

static int
INHERITED\_AUTH\_ADMINISTRATOR
States that administrator authorizations of all parent tasks in the parent task hierarchy
 are inherited by a subtask derived from this template.

static int
INHERITED\_AUTH\_ALL
States that, additionally to the administrators, all other authorizations for parent tasks
 in the parent task hierarchy are inherited as reader authorization by a subtask
 derived from this template.

static int
INHERITED\_AUTH\_NONE
States that no authorization is inherited from parent tasks by a subtask derived from this template.

static int
KIND\_ADMINISTRATIVE
States that tasks derived from this template are administration tasks.

static int
KIND\_HUMAN
States that tasks derived from this template are created and processed by humans.

static int
KIND\_ORIGINATING
States that tasks derived from this template are tasks whose
 services are invoked and tracked by the Human Task Manager.

static int
KIND\_PARTICIPATING
States that tasks derived from this template are processed by humans but tracked
 by the Human Task Manager.

static int
STATE\_STARTED
States that the task template is available for task instance creation.

static int
STATE\_STOPPED
States that the task template has been stopped.

static int
SUBSTITUTION\_POLICY\_NO\_SUBSTITUTION
States that no substitution should take place.

static int
SUBSTITUTION\_POLICY\_SELECT\_USER\_IF\_PRESENT
States that only present users should act for absent users.

static int
SUBSTITUTION\_POLICY\_SUBSTITUTE\_IF\_ABSENT
States that substitutes should act for absent users.
    - Method Summary

Methods 

Modifier and Type
Method and Description

ACOID
getApplicationDefaultsID()
Returns the ID of the application component that specifies the defaults for
 tasks derived from this template.

java.lang.String
getApplicationName()
Returns the name of the application the task template is part of.

int
getAssignmentType()
Returns whether tasks derived from this template can be assigned to a single person or
 to multiple persons in parallel.

int
getAutoDeletionMode()
Returns whether an instance derived from the task template is automatically or
 conditionally deleted when it reaches an end execution state.

int
getAutonomy()
States for stand-alone tasks whether an instance of the task template
 runs dependently of a potential parent or not.

java.lang.String
getCalendarName()
Returns the name of the calendar used, for example, for expiration calculations.

OID
getContainmentContextID()
Returns the ID of the context the task template belongs to.

int
getContextAuthorizationOfOwner()
Returns the authorization rights of owners of tasks that are derived
 from this template to the associated context.

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
getDefinitionName()
Returns the name of the task template definition in the TEL.

java.lang.String
getDefinitionNamespace()
Returns the namespace of the task template definition in the TEL.

java.lang.String
getDescription(java.util.Locale arg0)
Returns the description in the specified locale.

java.lang.String
getDisplayName(java.util.Locale arg0)
Returns the display name in the specified locale.

java.lang.String
getDurationUntilDeleted()
Returns the duration that task instances derived from this template are kept after they
 have reached an end state.

java.lang.String
getDurationUntilDue()
Returns the duration when tasks derived from this template become due.

java.lang.String
getDurationUntilExpires()
Returns the duration when tasks derived from this template expire once they are activated.

java.lang.String
getEventHandlerName()
Returns the name of the associated event handler.

TKTID
getID()
Returns the object identifier.

int
getInheritedAuthorization()
States for a subtask derived from this template which kind of authorization is inherited from parent tasks.

java.lang.String
getJNDINameOfCalendar()
Returns the JNDI name of a user-defined calendar.

java.lang.String
getJNDINameOfStaffPluginProvider()
Returns the JNDI name of a user-defined people directory configuration.

int
getKind()
Returns the kind of tasks derived from this template.

java.util.List
getLocalesOfDescriptions()
Returns the locales of all descriptions.

java.util.List
getLocalesOfDisplayNames()
Returns the locales of all display names.

java.lang.String
getName()
Returns the name of the task template.

java.lang.String
getNamespace()
Returns the namespace that categorizes the task template.

java.lang.Integer
getPriority()
Returns the priority of tasks derived from this template.

java.lang.String
getPriorityDefinition()
Returns the priority definition for tasks derived from this template.

java.lang.String
getProcessAppAcronym()
Returns an acronym for the process application.

java.lang.String
getProcessAppName()
Returns the name of the process application that contains the task template.

java.lang.String
getSnapshotID()
Returns the unique identifier of a snapshot that contains the task template.

java.lang.String
getSnapshotName()
Returns the name of a snapshot that contains the task template.

int
getState()
States whether the task template is started or stopped.

int
getSubstitutionPolicy()
Returns the substitution policy that takes place when people assignments are performed
 for tasks derived from this task template.

java.lang.String
getToolkitAcronym()
Returns the acronym of a toolkit that contains the task template.

java.lang.String
getToolkitName()
Returns the name of a toolkit that contains the task template.

java.lang.String
getToolkitSnapshotID()
Returns the unique ID of a toolkit snapshot that contains the task template.

java.lang.String
getToolkitSnapshotName()
Returns the name of a toolkit snapshot that contains the task template.

java.lang.String
getTopLevelToolkitAcronym()
Returns the acronym of the topmost toolkit that contains the task template.

java.lang.String
getTopLevelToolkitName()
Returns the name of the topmost toolkit that contains the task template.

java.lang.String
getTrackName()
Returns the name of the track that contains the task template.

java.lang.String
getType()
Returns the type of the task template.

java.util.Calendar
getValidFromTime()
Returns the time the task template became or becomes valid.

java.lang.String
getWorkBasketName()
Returns the name of the work basket tasks derived from this template should belong to.

boolean
isAdHoc()
States whether the task template has been created ad hoc.

boolean
isBusinessRelevant()
States whether a task derived from this template is a business relevant or an "auxiliary" step.

boolean
isInline()
States whether the task template describes an inline task or not.

boolean
isTip()
States whether the task template is contained in a snapshot or whether it is
 more current.

boolean
supportsAutomaticClaim()
States whether a task derived from this template is claimed automatically when it
 becomes ready.

boolean
supportsClaimIfSuspended()
States whether tasks derived from this template can be claimed even if they
 are suspended.

boolean
supportsDelegation()
States whether tasks derived from this template support delegation, for example,
 by transferring work items.

boolean
supportsFollowOnTasks()
States whether tasks derived from this template support the creation
 of follow-on tasks.

boolean
supportsSubTasks()
States whether tasks derived from this template support the creation
 of subtasks.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- KIND\_PARTICIPATING
static final int KIND\_PARTICIPATING
States that tasks derived from this template are processed by humans but tracked
 by the Human Task Manager.
See Also:Constant Field Values

- KIND\_ADMINISTRATIVE
static final int KIND\_ADMINISTRATIVE
States that tasks derived from this template are administration tasks.
See Also:Constant Field Values

- KIND\_HUMAN
static final int KIND\_HUMAN
States that tasks derived from this template are created and processed by humans.
See Also:Constant Field Values

- KIND\_ORIGINATING
static final int KIND\_ORIGINATING
States that tasks derived from this template are tasks whose
 services are invoked and tracked by the Human Task Manager.
See Also:Constant Field Values

- AUTH\_READER
static final int AUTH\_READER
States that operations can be executed on the associated context that require
 Reader authority, for example, reading the properties of a process instance.
See Also:Constant Field Values

- AUTH\_NONE
static final int AUTH\_NONE
States that no operations can be executed on the associated context.
See Also:Constant Field Values

- STATE\_STOPPED
static final int STATE\_STOPPED
States that the task template has been stopped. Task
 instances cannot be created from the task template.
See Also:Constant Field Values

- STATE\_STARTED
static final int STATE\_STARTED
States that the task template is available for task instance creation.
See Also:Constant Field Values

- AUTO\_DELETE\_ON\_SUCCESSFUL\_COMPLETION
static final int AUTO\_DELETE\_ON\_SUCCESSFUL\_COMPLETION
States that a task instance derived from this template
 is deleted when it reaches the FINISHED state. If the task instance
 completes successfully, then it is deleted when the duration until deletion
 has passed. If the task instance did not complete successfully, it
 it is not deleted regardless of the specification of the duration until deletion.
See Also:Constant Field Values

- AUTO\_DELETE\_ON\_COMPLETION
static final int AUTO\_DELETE\_ON\_COMPLETION
States that a completed task instance derived from this template
 is deleted when the duration until deletion has passed.
See Also:Constant Field Values

- SUBSTITUTION\_POLICY\_SELECT\_USER\_IF\_PRESENT
static final int SUBSTITUTION\_POLICY\_SELECT\_USER\_IF\_PRESENT
States that only present users should act for absent users.
 If all users and their subsitutes are absent or excluded by people assignment criteria,
 users originally resolved are returned.
See Also:Constant Field Values

- SUBSTITUTION\_POLICY\_NO\_SUBSTITUTION
static final int SUBSTITUTION\_POLICY\_NO\_SUBSTITUTION
States that no substitution should take place.
 All users resolved by people assignment criteria are returned.
See Also:Constant Field Values

- SUBSTITUTION\_POLICY\_SUBSTITUTE\_IF\_ABSENT
static final int SUBSTITUTION\_POLICY\_SUBSTITUTE\_IF\_ABSENT
States that substitutes should act for absent users.
 If all substitutes are absent or explicitely excluded by people assignment criteria,
 default people assignments are performed, for example, task administrators become potential owners.
See Also:Constant Field Values

- AUTONOMY\_NOT\_APPLICABLE
static final int AUTONOMY\_NOT\_APPLICABLE
States that the autonomy flag is not applicable.
 Task instances derived from this template are inline tasks.
See Also:Constant Field Values

- AUTONOMY\_CHILD
static final int AUTONOMY\_CHILD
States that task instances derived from this template run dependently of a potential parent process.
See Also:Constant Field Values

- AUTONOMY\_PEER
static final int AUTONOMY\_PEER
States that task instances derived from this template run independently of a potential parent process.
See Also:Constant Field Values

- ASSIGNMENT\_TYPE\_PARALLEL
static final int ASSIGNMENT\_TYPE\_PARALLEL
States that a task derived from this template can be assigned to multiple persons in parallel.
See Also:Constant Field Values

- ASSIGNMENT\_TYPE\_SINGLE
static final int ASSIGNMENT\_TYPE\_SINGLE
States that a task derived from this template can only be assigned to a single person.
See Also:Constant Field Values

- INHERITED\_AUTH\_NONE
static final int INHERITED\_AUTH\_NONE
States that no authorization is inherited from parent tasks by a subtask derived from this template.
See Also:Constant Field Values

- INHERITED\_AUTH\_ALL
static final int INHERITED\_AUTH\_ALL
States that, additionally to the administrators, all other authorizations for parent tasks
 in the parent task hierarchy are inherited as reader authorization by a subtask
 derived from this template.
 For example, reader authorizations, potential\_owner authorizations etc
 are all inherited as reader authorizations.
See Also:Constant Field Values

- INHERITED\_AUTH\_ADMINISTRATOR
static final int INHERITED\_AUTH\_ADMINISTRATOR
States that administrator authorizations of all parent tasks in the parent task hierarchy
 are inherited by a subtask derived from this template.
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getID
TKTID getID()
Returns the object identifier.
    - getApplicationDefaultsID
ACOID getApplicationDefaultsID()
Returns the ID of the application component that specifies the defaults for
 tasks derived from this template. Any property set explicitly on the task template
 or task overwrites the defaults provided by the application component.
    - getApplicationName
java.lang.String getApplicationName()
Returns the name of the application the task template is part of.
    - supportsAutomaticClaim
boolean supportsAutomaticClaim()
States whether a task derived from this template is claimed automatically when it
 becomes ready. This function requires that there is a single potential owner.
    - isBusinessRelevant
boolean isBusinessRelevant()
States whether a task derived from this template is a business relevant or an "auxiliary" step. A
 business relevant step can, for example, be logged into the audit trail.
    - isAdHoc
boolean isAdHoc()
States whether the task template has been created ad hoc. True states that
 the task template has been created ad hoc. False states that the task template
 has been deployed.
    - isInline
boolean isInline()
States whether the task template describes an inline task or not. True states that
 the task template describes an inline task. False states
 that the task template does not describe an inline task.
    - getCalendarName
java.lang.String getCalendarName()
Returns the name of the calendar used, for example, for expiration calculations. If
 not set, null is returned and the WebSphere default calendar is used. If a JNDI name
 for a user-defined calendar is specified, then the calendar name is the name of a
 method implementing that user-defined calendar - see
 getJNDINameOfCalendar.
 
 For details on calendars refer to the WebSphere Application Server documentation.
    - getContainmentContextID
OID getContainmentContextID()
Returns the ID of the context the task template belongs to. This ID
 is used for task template and instance deletion. In other words, when the context
 is deleted, the task template and derived instances are also deleted.
    - getDescription
java.lang.String getDescription(java.util.Locale arg0)
Returns the description in the specified locale.
 Returns the description in the default locale when a description in
 the specified locale is not found.
 
 If no locale is specified, the description in the default locale is returned
 or any available description, if there is only a single description.
 References to variable members specified as %variableName.memberName%
 are resolved.
 
Parameters:arg0 - The locale for which the description is to be provided.
    - getLocalesOfDescriptions
java.util.List getLocalesOfDescriptions()
Returns the locales of all descriptions.
 Returns an empty list when there are no descriptions.
    - getDisplayName
java.lang.String getDisplayName(java.util.Locale arg0)
Returns the display name in the specified locale.
 Returns the display name in the default locale when a display name in
 the specified locale is not found.
 
 If no locale is specified, the display name in the default locale is returned
 or any available display name, if there is only a single display name.
 
Parameters:arg0 - The locale for which the display name is to be provided.
    - getLocalesOfDisplayNames
java.util.List getLocalesOfDisplayNames()
Returns the locales of all display names.
 Returns an empty list when there are no display names.
    - getDurationUntilDeleted
java.lang.String getDurationUntilDeleted()
Returns the duration that task instances derived from this template are kept after they
 have reached an end state. When the duration has passed, they get deleted.
 
 A specification TimerSpecification.DURATION\_IMMEDIATE
 means that task instances are deleted immediately.
 A specification TimerSpecification.DURATION\_INFINITE
 means that task instances are not deleted automatically.
 
 If not set, then stand-alone invocation or collaboration tasks are kept
 whereas stand-alone to-do tasks are deleted immediately.
 Collaboration, invocation, and to-do tasks are also known as
 human, originating, and participating tasks.
 
 Inline tasks are always deleted together with their container, for example, the process instance.
 
 Note that this setting is checked depending on the automatic deletion mode -
 AutoDeletionMode.
    - getDurationUntilDue
java.lang.String getDurationUntilDue()
Returns the duration when tasks derived from this template become due.
    - getDurationUntilExpires
java.lang.String getDurationUntilExpires()
Returns the duration when tasks derived from this template expire once they are activated.
    - getJNDINameOfCalendar
java.lang.String getJNDINameOfCalendar()
Returns the JNDI name of a user-defined calendar. If
 not set, null is returned and a WebSphere supported calendar is used -
 see getCalendarName.
 
 For details on calendars refer to the WebSphere Application Server documentation.
    - getJNDINameOfStaffPluginProvider
java.lang.String getJNDINameOfStaffPluginProvider()
Returns the JNDI name of a user-defined people directory configuration.
    - getKind
int getKind()
Returns the kind of tasks derived from this template.
 
 Possible values are:
 KIND\_HUMAN, KIND\_ORIGINATING, KIND\_PARTICIPATING, KIND\_ADMINISTRATIVE.
    - getName
java.lang.String getName()
Returns the name of the task template.
    - getNamespace
java.lang.String getNamespace()
Returns the namespace that categorizes the task template.
    - getDefinitionName
java.lang.String getDefinitionName()
Returns the name of the task template definition in the TEL.
Since:
6.1.
    - getDefinitionNamespace
java.lang.String getDefinitionNamespace()
Returns the namespace of the task template definition in the TEL.
Since:
6.1.
    - getPriority
java.lang.Integer getPriority()
Returns the priority of tasks derived from this template.
 This priority is taken when there is no priority definition -
 see getPriorityDefinition.
 
 No special meaning
 is associated with this property. Escalations may, however, increase
 the priority of associated tasks. A caller can, for example,
 use it for sorting a list of tasks.
    - getType
java.lang.String getType()
Returns the type of the task template. A type can be used to categorize tasks
 derived from this template. Returns null when there is no associated type.
    - supportsDelegation
boolean supportsDelegation()
States whether tasks derived from this template support delegation, for example,
 by transferring work items.
    - supportsSubTasks
boolean supportsSubTasks()
States whether tasks derived from this template support the creation
 of subtasks.
    - supportsClaimIfSuspended
boolean supportsClaimIfSuspended()
States whether tasks derived from this template can be claimed even if they
 are suspended. True states that
 a task can be claimed if it is suspended. False states that a task cannot
 be claimed if it is suspended.
    - getValidFromTime
java.util.Calendar getValidFromTime()
Returns the time the task template became or becomes valid.
    - getContextAuthorizationOfOwner
int getContextAuthorizationOfOwner()
Returns the authorization rights of owners of tasks that are derived
 from this template to the associated context.
 
 Possible values are:
 AUTH\_NONE, AUTH\_READER.
    - getEventHandlerName
java.lang.String getEventHandlerName()
Returns the name of the associated event handler. Returns
 null if there is no event handler.
    - getState
int getState()
States whether the task template is started or stopped.
 
 Returns either STATE\_STARTED or STATE\_STOPPED.
    - getAutoDeletionMode
int getAutoDeletionMode()
Returns whether an instance derived from the task template is automatically or
 conditionally deleted when it reaches an end execution state. Refer to
 AutoDeletionMode for the possible deletion modes.
 
 End execution states are STATE\_FINISHED, STATE\_FAILED, STATE\_TERMINATED, or
 STATE\_EXPIRED.
 
 Note that task instances are actually deleted depending on the duration until deletion specification -
 refer to getDurationUntilDeleted.
Since:
6.1.
    - getPriorityDefinition
java.lang.String getPriorityDefinition()
Returns the priority definition for tasks derived from this template.
 
 The priority is evaluated when a task is started.
 When the priority cannot be evaluated, for example, the definition cannot be
 converted to a numeric value, then the default for priorities, 5, is taken.
 When there is no priority definition, then the value from the priority property
 is taken - see getPriority.
 
 No special meaning is associated with this property.
 Escalations may, however, increase the priority of associated tasks. A caller
 can, for example, use it for sorting a list of tasks.
Since:
6.1.
    - getSubstitutionPolicy
int getSubstitutionPolicy()
Returns the substitution policy that takes place when people assignments are performed
 for tasks derived from this task template.
 
 Possible substitution policies are SUBSTITUTION\_POLICY\_NO\_SUBSTITUTION, SUBSTITUTION\_POLICY\_SUBSTITUTE\_IF\_ABSENT,
 SUBSTITUTION\_POLICY\_SELECT\_USER\_IF\_PRESENT.
Since:
6.1.
    - supportsFollowOnTasks
boolean supportsFollowOnTasks()
States whether tasks derived from this template support the creation
 of follow-on tasks.
Since:
6.1.
    - getAutonomy
int getAutonomy()
States for stand-alone tasks whether an instance of the task template
 runs dependently of a potential parent or not.
 Returns either AUTONOMY\_PEER or AUTONOMY\_CHILD.
 
 For inline tasks, AUTONOMY\_NOT\_APPLICABLE is returned.
 Inline tasks are always dependent on their parents.
Since:
6.2.
    - getAssignmentType
int getAssignmentType()
Returns whether tasks derived from this template can be assigned to a single person or
 to multiple persons in parallel.
 
 Possible assignment types are ASSIGNMENT\_TYPE\_SINGLE,
 ASSIGNMENT\_TYPE\_PARALLEL.
Since:
7.0.
    - getInheritedAuthorization
int getInheritedAuthorization()
States for a subtask derived from this template which kind of authorization is inherited from parent tasks.
 
 Possible values are INHERITED\_AUTH\_NONE, INHERITED\_AUTH\_ADMINISTRATOR,
 INHERITED\_AUTH\_ALL.
Since:
7.0.
    - getWorkBasketName
java.lang.String getWorkBasketName()
Returns the name of the work basket tasks derived from this template should belong to.
 Returns null if tasks should not belong to any work basket per default.
Since:
7.0.
    - getSnapshotID
java.lang.String getSnapshotID()
Returns the unique identifier of a snapshot that contains the task template.
 Returns null if the template is not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getSnapshotName
java.lang.String getSnapshotName()
Returns the name of a snapshot that contains the task template.
 Returns null if the template is not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getTrackName
java.lang.String getTrackName()
Returns the name of the track that contains the task template.
 Returns null if the template is not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getProcessAppName
java.lang.String getProcessAppName()
Returns the name of the process application that contains the task template.
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
Returns the unique ID of a toolkit snapshot that contains the task template.
 Returns null if the template is not contained in a toolkit or
 not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getToolkitSnapshotName
java.lang.String getToolkitSnapshotName()
Returns the name of a toolkit snapshot that contains the task template.
 Returns null if the template is not contained in a toolkit or
 not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getToolkitName
java.lang.String getToolkitName()
Returns the name of a toolkit that contains the task template.
 Returns null if the template is not contained in a toolkit or
 not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getToolkitAcronym
java.lang.String getToolkitAcronym()
Returns the acronym of a toolkit that contains the task template.
 Returns null if the template is not contained in a toolkit or
 not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getTopLevelToolkitName
java.lang.String getTopLevelToolkitName()
Returns the name of the topmost toolkit that contains the task template.
 Returns null if the template is not contained in a toolkit or
 not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - getTopLevelToolkitAcronym
java.lang.String getTopLevelToolkitAcronym()
Returns the acronym of the topmost toolkit that contains the task template.
 Returns null if the template is not contained in a toolkit or
 not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
    - isTip
boolean isTip()
States whether the task template is contained in a snapshot or whether it is
 more current. True states that the task template is a tip and not contained in a snapshot.
 False states that the task template is contained in a snapshot - see
 getSnapshotName - or
 that the task template is not deployed as part of an application of the
 Workflow Server configured for the business process definition engine.
Since:
7.5.
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