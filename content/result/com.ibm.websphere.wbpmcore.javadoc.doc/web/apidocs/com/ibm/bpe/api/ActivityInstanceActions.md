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

## Interface ActivityInstanceActions

- public interface ActivityInstanceActions
This interface defines symbolic constants for all actions that can be performed on
 activity instances. These constants are to be used when determining the actions
 allowed in the current activity instance execution state.
 Currently allowed actions are returned
 when calling the getAvailableActions()
 method on an activity instance.
Since:
7.0 - introduced in 5.0

- =========== FIELD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
CANCELCLAIM
Symbolic constant for activity instance action cancel claim.

static int
CANCELSKIPREQUEST
Symbolic constant for activity instance action ummark for skip.

static int
CLAIM
Symbolic constant for activity instance action claim.

static int
COMPLETE
Symbolic constant for activity instance action complete.

static int
COMPLETEANDJUMP
Symbolic constant for activity instance action complete and jump.

static java.lang.String
COPYRIGHT 

static int
CREATEMESSAGE
Symbolic constant for activity instance action create message.

static int
CREATEWORKITEM
Symbolic constant for activity instance action create work item.

static int
DELETEWORKITEM
Symbolic constant for activity instance action delete work item.

static int
FORCECOMPLETE
Symbolic constant for activity instance action force complete.

static int
FORCECOMPLETEANDJUMP
Symbolic constant for activity instance action force complete and jump.

static int
FORCEFOREACHCOUNTERVALUES
Symbolic constant for activity instance action force forEach counter values

static int
FORCEJOINCONDITION
Symbolic constant for activity instance action force join condition

static int
FORCELOOPCONDITION
Symbolic constant for activity instance action force loop condition

static int
FORCENAVIGATE
Symbolic constant for activity instance action force navigate

static int
FORCERETRY
Symbolic constant for activity instance action force retry.

static int
GETACTIVITYINSTANCE
Symbolic constant for activity instance action get activity instance.

static int
GETALLVARIABLENAMES
Symbolic constant for activity instance action get all variable names.

static int
GETALLWORKITEMS
Symbolic constant for activity instance action get all work items.

static int
GETBRANCHES
Symbolic constant for activity instance action get branches

static int
GETCORRELATIONSETINSTANCES
Symbolic constant for activity instance action get correlation set instances

static int
GETCUSTOMATTRIBUTE
Deprecated. 
As of version 6.0, replaced by GETCUSTOMPROPERTY.

static int
GETCUSTOMPROPERTY
Symbolic constant for activity instance action get custom property.

static int
GETCUSTOMPROPERTYNAMES
Symbolic constant for activity instance actions get custom property names.

static int
GETEVENTOUTPUTMESSAGE
Symbolic constant for activity instance action get output message for a receive event.

static int
GETFAULTMESSAGE
Symbolic constant for activity instance action get fault message.

static int
GETFAULTNAMES
Symbolic constant for activity instance action get fault names.

static int
GETINITIALVARIABLEVALUE
Symbolic constant for activity instance action get initial variable value.

static int
GETINPUTMESSAGE
Symbolic constant for activity instance action get input message.

static int
GETINPUTVARIABLENAMES
Symbolic constant for activity instance actions get input variable names.

static int
GETJUMPTARGETNAMES
Symbolic constant for activity instance action get jump targets

static int
GETOUTGOINGLINKS
Symbolic constant for activity instance action get outgoing links

static int
GETOUTPUTMESSAGE
Symbolic constant for activity instance action get output message.

static int
GETOUTPUTVARIABLENAMES
Symbolic constant for activity instance actions get output variable names.

static int
GETROLEINFO
Symbolic constant for activity instance action to retrieve role related information.

static int
GETUISETTINGS
Symbolic constant for activity instance action get UI settings.

static int
GETUSERINPUT
Symbolic constant for activity instance action get user input.

static int
GETVARIABLE
Symbolic constant for activity instance actions get variable.

static int
GETVARIABLENAMES
Symbolic constant for activity instance actions get variable names.

static int
GETWORKITEMS
Symbolic constant for activiyt instance actions get work item.

static int
JUMP
Symbolic constant for activity instance action jump

static int
RESCHEDULE
Deprecated. 
As of version 7.0, replaced by RESCHEDULE\_TIMER.

static int
RESCHEDULE\_TIMER
Symbolic constant for activity instance action reschedule a timer

static int
SENDEVENT
Symbolic constant for activity instance send event.

static int
SETCUSTOMATTRIBUTE
Deprecated. 
As of version 6.0, replaced by SETCUSTOMPROPERTY.

static int
SETCUSTOMPROPERTY
Symbolic constant for activity instance action set custom properties.

static int
SETEVENTOUTPUTMESSAGE
Symbolic constant for activity instance action set output message for a receive event.

static int
SETFAULTMESSAGE
Symbolic constant for activity instance action set fault message.

static int
SETOUTPUTMESSAGE
Symbolic constant for activity instance action set output message.

static int
SETUSERINPUT
Symbolic constant for activity instance action set user input.

static int
SETVARIABLE
Symbolic constant for activiyt instance actions set variable.

static int
SKIP
Symbolic constant for activity instance action skip.

static int
SKIPANDJUMP
Symbolic constant for activity instance action skip and jump.

static int
TRANSFERWORKITEM
Symbolic constant for activity instance action transfer work item.

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- CLAIM
static final int CLAIM
Symbolic constant for activity instance action claim.
See Also:Constant Field Values

- COMPLETE
static final int COMPLETE
Symbolic constant for activity instance action complete.
See Also:Constant Field Values

- CANCELCLAIM
static final int CANCELCLAIM
Symbolic constant for activity instance action cancel claim.
See Also:Constant Field Values

- SETOUTPUTMESSAGE
static final int SETOUTPUTMESSAGE
Symbolic constant for activity instance action set output message.
See Also:Constant Field Values

- SETUSERINPUT
static final int SETUSERINPUT
Symbolic constant for activity instance action set user input.
See Also:Constant Field Values

- SETCUSTOMATTRIBUTE
static final int SETCUSTOMATTRIBUTE
Deprecated. As of version 6.0, replaced by SETCUSTOMPROPERTY.
Symbolic constant for activity instance action set custom attributes.
See Also:Constant Field Values

- SETCUSTOMPROPERTY
static final int SETCUSTOMPROPERTY
Symbolic constant for activity instance action set custom properties.
See Also:Constant Field Values

- GETOUTPUTMESSAGE
static final int GETOUTPUTMESSAGE
Symbolic constant for activity instance action get output message.
See Also:Constant Field Values

- GETINPUTMESSAGE
static final int GETINPUTMESSAGE
Symbolic constant for activity instance action get input message.
See Also:Constant Field Values

- GETFAULTMESSAGE
static final int GETFAULTMESSAGE
Symbolic constant for activity instance action get fault message.
See Also:Constant Field Values

- GETCUSTOMATTRIBUTE
static final int GETCUSTOMATTRIBUTE
Deprecated. As of version 6.0, replaced by GETCUSTOMPROPERTY.
Symbolic constant for activity instance action get custom attribute.
See Also:Constant Field Values

- GETCUSTOMPROPERTY
static final int GETCUSTOMPROPERTY
Symbolic constant for activity instance action get custom property.
See Also:Constant Field Values

- GETACTIVITYINSTANCE
static final int GETACTIVITYINSTANCE
Symbolic constant for activity instance action get activity instance.
See Also:Constant Field Values

- GETUSERINPUT
static final int GETUSERINPUT
Symbolic constant for activity instance action get user input.
See Also:Constant Field Values

- GETUISETTINGS
static final int GETUISETTINGS
Symbolic constant for activity instance action get UI settings.
See Also:Constant Field Values

- SETFAULTMESSAGE
static final int SETFAULTMESSAGE
Symbolic constant for activity instance action set fault message.
See Also:Constant Field Values

- SENDEVENT
static final int SENDEVENT
Symbolic constant for activity instance send event.
See Also:Constant Field Values

- FORCECOMPLETE
static final int FORCECOMPLETE
Symbolic constant for activity instance action force complete.
See Also:Constant Field Values

- FORCERETRY
static final int FORCERETRY
Symbolic constant for activity instance action force retry.
See Also:Constant Field Values

- GETEVENTOUTPUTMESSAGE
static final int GETEVENTOUTPUTMESSAGE
Symbolic constant for activity instance action get output message for a receive event.
See Also:Constant Field Values

- SETEVENTOUTPUTMESSAGE
static final int SETEVENTOUTPUTMESSAGE
Symbolic constant for activity instance action set output message for a receive event.
See Also:Constant Field Values

- GETALLWORKITEMS
static final int GETALLWORKITEMS
Symbolic constant for activity instance action get all work items.
See Also:Constant Field Values

- CREATEMESSAGE
static final int CREATEMESSAGE
Symbolic constant for activity instance action create message.
See Also:Constant Field Values

- CREATEWORKITEM
static final int CREATEWORKITEM
Symbolic constant for activity instance action create work item.
See Also:Constant Field Values

- DELETEWORKITEM
static final int DELETEWORKITEM
Symbolic constant for activity instance action delete work item.
See Also:Constant Field Values

- TRANSFERWORKITEM
static final int TRANSFERWORKITEM
Symbolic constant for activity instance action transfer work item.
See Also:Constant Field Values

- GETFAULTNAMES
static final int GETFAULTNAMES
Symbolic constant for activity instance action get fault names.
See Also:Constant Field Values

- GETWORKITEMS
static final int GETWORKITEMS
Symbolic constant for activiyt instance actions get work item.
See Also:Constant Field Values

- GETVARIABLE
static final int GETVARIABLE
Symbolic constant for activity instance actions get variable.
See Also:Constant Field Values

- SETVARIABLE
static final int SETVARIABLE
Symbolic constant for activiyt instance actions set variable.
See Also:Constant Field Values

- GETCUSTOMPROPERTYNAMES
static final int GETCUSTOMPROPERTYNAMES
Symbolic constant for activity instance actions get custom property names.
See Also:Constant Field Values

- GETINPUTVARIABLENAMES
static final int GETINPUTVARIABLENAMES
Symbolic constant for activity instance actions get input variable names.
See Also:Constant Field Values

- GETOUTPUTVARIABLENAMES
static final int GETOUTPUTVARIABLENAMES
Symbolic constant for activity instance actions get output variable names.
See Also:Constant Field Values

- GETVARIABLENAMES
static final int GETVARIABLENAMES
Symbolic constant for activity instance actions get variable names.
See Also:Constant Field Values

- SKIP
static final int SKIP
Symbolic constant for activity instance action skip.
See Also:Constant Field Values

- CANCELSKIPREQUEST
static final int CANCELSKIPREQUEST
Symbolic constant for activity instance action ummark for skip.
See Also:Constant Field Values

- SKIPANDJUMP
static final int SKIPANDJUMP
Symbolic constant for activity instance action skip and jump.
See Also:Constant Field Values

- COMPLETEANDJUMP
static final int COMPLETEANDJUMP
Symbolic constant for activity instance action complete and jump.
See Also:Constant Field Values

- FORCECOMPLETEANDJUMP
static final int FORCECOMPLETEANDJUMP
Symbolic constant for activity instance action force complete and jump.
See Also:Constant Field Values

- GETALLVARIABLENAMES
static final int GETALLVARIABLENAMES
Symbolic constant for activity instance action get all variable names.
See Also:Constant Field Values

- GETINITIALVARIABLEVALUE
static final int GETINITIALVARIABLEVALUE
Symbolic constant for activity instance action get initial variable value.
See Also:Constant Field Values

- GETOUTGOINGLINKS
static final int GETOUTGOINGLINKS
Symbolic constant for activity instance action get outgoing links
See Also:Constant Field Values

- GETBRANCHES
static final int GETBRANCHES
Symbolic constant for activity instance action get branches
See Also:Constant Field Values

- FORCENAVIGATE
static final int FORCENAVIGATE
Symbolic constant for activity instance action force navigate
See Also:Constant Field Values

- RESCHEDULE
static final int RESCHEDULE
Deprecated. As of version 7.0, replaced by RESCHEDULE\_TIMER.
Symbolic constant for activity instance action reschedule.
See Also:Constant Field Values

- RESCHEDULE\_TIMER
static final int RESCHEDULE\_TIMER
Symbolic constant for activity instance action reschedule a timer
See Also:Constant Field Values

- GETJUMPTARGETNAMES
static final int GETJUMPTARGETNAMES
Symbolic constant for activity instance action get jump targets
See Also:Constant Field Values

- JUMP
static final int JUMP
Symbolic constant for activity instance action jump
See Also:Constant Field Values

- FORCEJOINCONDITION
static final int FORCEJOINCONDITION
Symbolic constant for activity instance action force join condition
See Also:Constant Field Values

- FORCELOOPCONDITION
static final int FORCELOOPCONDITION
Symbolic constant for activity instance action force loop condition
See Also:Constant Field Values

- FORCEFOREACHCOUNTERVALUES
static final int FORCEFOREACHCOUNTERVALUES
Symbolic constant for activity instance action force forEach counter values
See Also:Constant Field Values

- GETCORRELATIONSETINSTANCES
static final int GETCORRELATIONSETINSTANCES
Symbolic constant for activity instance action get correlation set instances
See Also:Constant Field Values

- GETROLEINFO
static final int GETROLEINFO
Symbolic constant for activity instance action to retrieve role related information.
 States whether getUsersInRole() can be called.
Since:
7.0.0.2
See Also:Constant Field Values