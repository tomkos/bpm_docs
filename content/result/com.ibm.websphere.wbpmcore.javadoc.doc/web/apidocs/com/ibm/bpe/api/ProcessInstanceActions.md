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

## Interface ProcessInstanceActions

- public interface ProcessInstanceActions
This interface defines symbolic constants for all actions that can be performed on
 process instances. These constants are to be used when determining the actions
 allowed in the current process instance execution state.
 Currently allowed actions are returned
 when calling the getAvailableActions()
 method on a process instance.
Since:
7.0 - introduced in 5.0

- =========== FIELD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
CLAIMPROCESSOWNERSHIP
Symbolic constant for process instance action claim process ownership

static java.lang.String
COPYRIGHT 

static int
CREATEMESSAGE
Symbolic constant for process instance action create message.

static int
CREATEWORKITEM
Symbolic constant for process instance action create work item.

static int
DELETE
Symbolic constant for process instance action delete.

static int
DELETEWORKITEM
Symbolic constant for process instance action delete work item.

static int
FORCETERMINATE
Symbolic constant for process instance action force terminate.

static int
FORCETERMINATEANDCOMPENSATE
Symbolic constant for process instance force terminate and compensate.

static int
GETACTIVEEVENTHANDLER
Symbolic constant for process instance action get active event handlers.

static int
GETACTIVITYINSTANCE
Symbolic constant for process instance action get avtivity instance.

static int
GETALLACTIVITIES
Symbolic constant for process instance action get all activities.

static int
GETALLVARIABLENAMES
Symbolic constant for process instance action get all variable names.

static int
GETALLWORKITEMS
Symbolic constant for process instance action get all work items.

static int
GETCORRELATIONSETINSTANCES
Symbolic constant for process instance action get correlation set instances

static int
GETCUSTOMATTRIBUTE
Deprecated. 
Use GETCUSTOMPROPERTY.

static int
GETCUSTOMPROPERTY
Symbolic constant for process instance action get customer property.

static int
GETCUSTOMPROPERTYNAMES
Symbolic constant for process instance action get customer property names.

static int
GETFAULTMESSAGE
Symbolic constant for process instance action get fault message.

static int
GETINITIALVARIABLEVALUE
Symbolic constant for process instance action get initial variable value.

static int
GETINPUTMESSAGE
Symbolic constant for process instance action get input message.

static int
GETOUTPUTMESSAGE
Symbolic constant for process instance action get output message.

static int
GETPROCESSINSTANCE
Symbolic constant for process instance action get process instance.

static int
GETROLEINFO
Symbolic constant for process instance action to retrieve role related information.

static int
GETUISETTINGS
Symbolic constant for process instance action get UI settings.

static int
GETVARIABLE
Symbolic constant for process instance action get variable.

static int
GETWORKITEMS
Symbolic constant for process instance action get workitems.

static int
INITIALIZECORRELATIONSET
Symbolic constant for process instance action initialize correlation set

static int
MIGRATE
Symbolic constant for process instance action migrate

static int
RESTART
Symbolic constant for process instance action restart.

static int
RESUME
Symbolic constant for process instance action resume.

static int
SENDEVENT
Deprecated. 
As of version 7.5, no replacement.

static int
SETCUSTOMATTRIBUTE
Deprecated. 
Use SETCUSTOMPROPERTY.

static int
SETCUSTOMPROPERTY
Symbolic constant for process instance action set customer property.

static int
SETVARIABLE
Symbolic constant for process instance action set variable.

static int
SUSPEND
Symbolic constant for process instance action suspend.

static int
TESTMIGRATION
Symbolic constant for test migration method which is used to test if a given instance
 can be migrated to the target template.

static int
TRANSFERWORKITEM
Symbolic constant for process instance action transfer work item.

static int
UNINITIALIZECORRELATIONSET
Symbolic constant for process instance action delete correlation set

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- FORCETERMINATE
static final int FORCETERMINATE
Symbolic constant for process instance action force terminate.
See Also:Constant Field Values

- GETINPUTMESSAGE
static final int GETINPUTMESSAGE
Symbolic constant for process instance action get input message.
See Also:Constant Field Values

- GETOUTPUTMESSAGE
static final int GETOUTPUTMESSAGE
Symbolic constant for process instance action get output message.
See Also:Constant Field Values

- GETFAULTMESSAGE
static final int GETFAULTMESSAGE
Symbolic constant for process instance action get fault message.
See Also:Constant Field Values

- GETVARIABLE
static final int GETVARIABLE
Symbolic constant for process instance action get variable.
See Also:Constant Field Values

- GETCUSTOMATTRIBUTE
static final int GETCUSTOMATTRIBUTE
Deprecated. Use GETCUSTOMPROPERTY.
Symbolic constant for process instance action get customer attribute.
See Also:Constant Field Values

- GETCUSTOMPROPERTY
static final int GETCUSTOMPROPERTY
Symbolic constant for process instance action get customer property.
See Also:Constant Field Values

- SETCUSTOMATTRIBUTE
static final int SETCUSTOMATTRIBUTE
Deprecated. Use SETCUSTOMPROPERTY.
Symbolic constant for process instance action set customer attribute.
See Also:Constant Field Values

- SETCUSTOMPROPERTY
static final int SETCUSTOMPROPERTY
Symbolic constant for process instance action set customer property.
See Also:Constant Field Values

- DELETE
static final int DELETE
Symbolic constant for process instance action delete.
See Also:Constant Field Values

- GETPROCESSINSTANCE
static final int GETPROCESSINSTANCE
Symbolic constant for process instance action get process instance.
See Also:Constant Field Values

- GETUISETTINGS
static final int GETUISETTINGS
Symbolic constant for process instance action get UI settings.
See Also:Constant Field Values

- SENDEVENT
static final int SENDEVENT
Deprecated. As of version 7.5, no replacement.
Symbolic constant for process instance action send event.
See Also:Constant Field Values

- GETALLWORKITEMS
static final int GETALLWORKITEMS
Symbolic constant for process instance action get all work items.
See Also:Constant Field Values

- GETALLACTIVITIES
static final int GETALLACTIVITIES
Symbolic constant for process instance action get all activities.
See Also:Constant Field Values

- CREATEMESSAGE
static final int CREATEMESSAGE
Symbolic constant for process instance action create message.
See Also:Constant Field Values

- CREATEWORKITEM
static final int CREATEWORKITEM
Symbolic constant for process instance action create work item.
See Also:Constant Field Values

- DELETEWORKITEM
static final int DELETEWORKITEM
Symbolic constant for process instance action delete work item.
See Also:Constant Field Values

- TRANSFERWORKITEM
static final int TRANSFERWORKITEM
Symbolic constant for process instance action transfer work item.
See Also:Constant Field Values

- SETVARIABLE
static final int SETVARIABLE
Symbolic constant for process instance action set variable.
See Also:Constant Field Values

- GETWORKITEMS
static final int GETWORKITEMS
Symbolic constant for process instance action get workitems.
See Also:Constant Field Values

- FORCETERMINATEANDCOMPENSATE
static final int FORCETERMINATEANDCOMPENSATE
Symbolic constant for process instance force terminate and compensate.
See Also:Constant Field Values

- SUSPEND
static final int SUSPEND
Symbolic constant for process instance action suspend.
See Also:Constant Field Values

- RESUME
static final int RESUME
Symbolic constant for process instance action resume.
See Also:Constant Field Values

- GETACTIVITYINSTANCE
static final int GETACTIVITYINSTANCE
Symbolic constant for process instance action get avtivity instance.
See Also:Constant Field Values

- RESTART
static final int RESTART
Symbolic constant for process instance action restart.
See Also:Constant Field Values

- GETACTIVEEVENTHANDLER
static final int GETACTIVEEVENTHANDLER
Symbolic constant for process instance action get active event handlers.
See Also:Constant Field Values

- GETALLVARIABLENAMES
static final int GETALLVARIABLENAMES
Symbolic constant for process instance action get all variable names.
See Also:Constant Field Values

- GETINITIALVARIABLEVALUE
static final int GETINITIALVARIABLEVALUE
Symbolic constant for process instance action get initial variable value.
See Also:Constant Field Values

- CLAIMPROCESSOWNERSHIP
static final int CLAIMPROCESSOWNERSHIP
Symbolic constant for process instance action claim process ownership
See Also:Constant Field Values

- GETCUSTOMPROPERTYNAMES
static final int GETCUSTOMPROPERTYNAMES
Symbolic constant for process instance action get customer property names.
See Also:Constant Field Values

- GETCORRELATIONSETINSTANCES
static final int GETCORRELATIONSETINSTANCES
Symbolic constant for process instance action get correlation set instances
See Also:Constant Field Values

- INITIALIZECORRELATIONSET
static final int INITIALIZECORRELATIONSET
Symbolic constant for process instance action initialize correlation set
See Also:Constant Field Values

- UNINITIALIZECORRELATIONSET
static final int UNINITIALIZECORRELATIONSET
Symbolic constant for process instance action delete correlation set
See Also:Constant Field Values

- MIGRATE
static final int MIGRATE
Symbolic constant for process instance action migrate
See Also:Constant Field Values

- GETROLEINFO
static final int GETROLEINFO
Symbolic constant for process instance action to retrieve role related information.
 States whether getUsersInRole() can be called.
Since:
7.0.0.2
See Also:Constant Field Values

- TESTMIGRATION
static final int TESTMIGRATION
Symbolic constant for test migration method which is used to test if a given instance
 can be migrated to the target template.
See Also:Constant Field Values