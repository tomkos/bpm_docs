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

## Interface ApplicationComponent

- All Superinterfaces:
java.io.Serializable

All Known Implementing Classes:
ApplicationComponentBean

public interface ApplicationComponent
extends java.io.Serializable
Accesses the properties of an application component.
 
 An application component specifies default values for task instances, for example,
 default values that control the life-cycle of tasks. These default values can be
 overwritten by specific values of task templates or task instances themselves.
 
 There are two pre-defined application components, HTM for the Human Task Manager and
 BFM for the Business Flow Manager.
 
Since:
6.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

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

java.lang.String
getCalendarName()
Returns the name of the calendar used, for example, for expiration calculations.

java.lang.String
getDurationUntilDeleted()
Returns the duration that task instances belonging to this application component
 are kept after they reached an end state.

java.lang.String
getEventHandlerName()
Returns the name of the event handler that gets associated to tasks
 that belong to this component.

ACOID
getID()
Returns the object identifier.

java.lang.String
getJNDINameOfCalendar()
Returns the JNDI name of a user-defined calendar.

java.lang.String
getJNDINameOfStaffPluginProvider()
Returns the JNDI name of a user-defined people directory configuration.

java.lang.String
getName()
Returns the name of the application component.

int
getSubstitutionPolicy()
Returns the substitution policy that takes place when people assignments are performed
 for tasks that belong to this application component.

boolean
isBusinessRelevant()
States whether a task that belongs to this application component is a business
 relevant or an "auxiliary" step.

boolean
supportsAutomaticClaim()
States whether a task that belongs to this application component
 is claimed automatically when it
 becomes ready.

boolean
supportsClaimIfSuspended()
States whether tasks that belong to this application component
 can be claimed even if they are suspended.

boolean
supportsDelegation()
States whether tasks that belong to this application component
 support delegation, for example, by transferring work items.

boolean
supportsFollowOnTasks()
States whether tasks that belong to this application component
 support the creation of follow-on tasks.

boolean
supportsSubTasks()
States whether tasks that belong to this application component
 support the creation of subtasks.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
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

- Method Detail

### Method Detail

    - getID
ACOID getID()
Returns the object identifier.
    - getName
java.lang.String getName()
Returns the name of the application component.
    - supportsAutomaticClaim
boolean supportsAutomaticClaim()
States whether a task that belongs to this application component
 is claimed automatically when it
 becomes ready. This function requires that there is a single potential owner.
    - isBusinessRelevant
boolean isBusinessRelevant()
States whether a task that belongs to this application component is a business
 relevant or an "auxiliary" step. A
 business relevant step can, for example, be logged into the audit trail.
    - getDurationUntilDeleted
java.lang.String getDurationUntilDeleted()
Returns the duration that task instances belonging to this application component
 are kept after they reached an end state. When the duration has passed,
 they get deleted.
 
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
    - getCalendarName
java.lang.String getCalendarName()
Returns the name of the calendar used, for example, for expiration calculations. If
 not set, null is returned and the WebSphere default calendar is used. If a JNDI name
 for a user-defined calendar is specified, then the calendar name is the name of a
 method implementing that user-defined calendar - see
 getJNDINameOfCalendar.
 
 For details on calendars refer to the WebSphere Application Server documentation.
    - getJNDINameOfCalendar
java.lang.String getJNDINameOfCalendar()
Returns the JNDI name of a user-defined calendar. If
 not set, null is returned and a WebSphere supported calendar is used -
 see getCalendarName.
 
 For details on calendars refer to the WebSphere Application Server documentation.
    - getJNDINameOfStaffPluginProvider
java.lang.String getJNDINameOfStaffPluginProvider()
Returns the JNDI name of a user-defined people directory configuration.
    - supportsDelegation
boolean supportsDelegation()
States whether tasks that belong to this application component
 support delegation, for example, by transferring work items.
    - supportsSubTasks
boolean supportsSubTasks()
States whether tasks that belong to this application component
 support the creation of subtasks.
    - supportsClaimIfSuspended
boolean supportsClaimIfSuspended()
States whether tasks that belong to this application component
 can be claimed even if they are suspended. True states that
 tasks can be claimed if they are suspended. False states that tasks cannot
 be claimed if they are suspended.
    - getEventHandlerName
java.lang.String getEventHandlerName()
Returns the name of the event handler that gets associated to tasks
 that belong to this component. Returns null if there is no event handler.
    - getSubstitutionPolicy
int getSubstitutionPolicy()
Returns the substitution policy that takes place when people assignments are performed
 for tasks that belong to this application component.
 
 Possible substitution policies are SUBSTITUTION\_POLICY\_NO\_SUBSTITUTION, SUBSTITUTION\_POLICY\_SUBSTITUTE\_IF\_ABSENT,
 SUBSTITUTION\_POLICY\_SELECT\_USER\_IF\_PRESENT.
Since:
6.1.
    - supportsFollowOnTasks
boolean supportsFollowOnTasks()
States whether tasks that belong to this application component
 support the creation of follow-on tasks.
Since:
6.1.