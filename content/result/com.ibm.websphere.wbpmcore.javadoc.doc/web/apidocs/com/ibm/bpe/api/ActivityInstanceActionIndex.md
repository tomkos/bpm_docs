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

## Interface ActivityInstanceActionIndex

- public interface ActivityInstanceActionIndex
This interface defines symbolic constants to be used as a column index for the array of
 available action flags - see
 getAvailableActionFlags().
Since:
7.0.0.2 - introduced in 6.0

- =========== FIELD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
CANCELCLAIM 

static int
CANCELSKIPREQUEST 

static int
CLAIM 

static int
COMPLETE 

static int
COMPLETEANDJUMP 

static java.lang.String
COPYRIGHT 

static int
CREATEMESSAGE 

static int
CREATEWORKITEM 

static int
DELETEWORKITEM 

static int
FORCECOMPLETE 

static int
FORCECOMPLETEANDJUMP 

static int
FORCEFOREACHCOUNTERVALUES 

static int
FORCEJOINCONDITION 

static int
FORCELOOPCONDITION 

static int
FORCENAVIGATE 

static int
FORCERETRY 

static int
GETACTIVITYINSTANCE 

static int
GETALLVARIABLENAMES 

static int
GETALLWORKITEMS 

static int
GETBRANCHES 

static int
GETCORRELATIONSETINSTANCES 

static int
GETCUSTOMPROPERTY 

static int
GETCUSTOMPROPERTYNAMES 

static int
GETFAULTMESSAGE 

static int
GETFAULTNAMES 

static int
GETINITIALVARIABLEVALUE 

static int
GETINPUTMESSAGE 

static int
GETINPUTVARIABLENAMES 

static int
GETJUMPTARGETNAMES 

static int
GETOUTGOINGLINKS 

static int
GETOUTPUTMESSAGE 

static int
GETOUTPUTVARIABLENAMES 

static int
GETROLEINFO 

static int
GETUISETTINGS 

static int
GETVARIABLE 

static int
GETVARIABLENAMES 

static int
GETWORKITEMS 

static int
JUMP 

static int
MAX\_COUNT 

static int
RESCHEDULE
Deprecated. 
As of version 7.0, replaced by RESCHEDULE\_TIMER.

static int
RESCHEDULE\_TIMER 

static int
SETCUSTOMPROPERTY 

static int
SETFAULTMESSAGE 

static int
SETOUTPUTMESSAGE 

static int
SETVARIABLE 

static int
SKIP 

static int
SKIPANDJUMP 

static int
TRANSFERWORKITEM

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- CANCELCLAIM
static final int CANCELCLAIM
See Also:Constant Field Values

- CLAIM
static final int CLAIM
See Also:Constant Field Values

- COMPLETE
static final int COMPLETE
See Also:Constant Field Values

- CREATEMESSAGE
static final int CREATEMESSAGE
See Also:Constant Field Values

- CREATEWORKITEM
static final int CREATEWORKITEM
See Also:Constant Field Values

- DELETEWORKITEM
static final int DELETEWORKITEM
See Also:Constant Field Values

- FORCECOMPLETE
static final int FORCECOMPLETE
See Also:Constant Field Values

- FORCERETRY
static final int FORCERETRY
See Also:Constant Field Values

- GETACTIVITYINSTANCE
static final int GETACTIVITYINSTANCE
See Also:Constant Field Values

- GETALLWORKITEMS
static final int GETALLWORKITEMS
See Also:Constant Field Values

- GETCUSTOMPROPERTY
static final int GETCUSTOMPROPERTY
See Also:Constant Field Values

- GETCUSTOMPROPERTYNAMES
static final int GETCUSTOMPROPERTYNAMES
See Also:Constant Field Values

- GETFAULTMESSAGE
static final int GETFAULTMESSAGE
See Also:Constant Field Values

- GETFAULTNAMES
static final int GETFAULTNAMES
See Also:Constant Field Values

- GETINPUTMESSAGE
static final int GETINPUTMESSAGE
See Also:Constant Field Values

- GETOUTPUTMESSAGE
static final int GETOUTPUTMESSAGE
See Also:Constant Field Values

- GETUISETTINGS
static final int GETUISETTINGS
See Also:Constant Field Values

- GETVARIABLE
static final int GETVARIABLE
See Also:Constant Field Values

- GETWORKITEMS
static final int GETWORKITEMS
See Also:Constant Field Values

- SETCUSTOMPROPERTY
static final int SETCUSTOMPROPERTY
See Also:Constant Field Values

- SETFAULTMESSAGE
static final int SETFAULTMESSAGE
See Also:Constant Field Values

- SETOUTPUTMESSAGE
static final int SETOUTPUTMESSAGE
See Also:Constant Field Values

- SETVARIABLE
static final int SETVARIABLE
See Also:Constant Field Values

- TRANSFERWORKITEM
static final int TRANSFERWORKITEM
See Also:Constant Field Values

- GETINPUTVARIABLENAMES
static final int GETINPUTVARIABLENAMES
See Also:Constant Field Values

- GETOUTPUTVARIABLENAMES
static final int GETOUTPUTVARIABLENAMES
See Also:Constant Field Values

- GETVARIABLENAMES
static final int GETVARIABLENAMES
See Also:Constant Field Values

- SKIP
static final int SKIP
See Also:Constant Field Values

- CANCELSKIPREQUEST
static final int CANCELSKIPREQUEST
See Also:Constant Field Values

- SKIPANDJUMP
static final int SKIPANDJUMP
See Also:Constant Field Values

- COMPLETEANDJUMP
static final int COMPLETEANDJUMP
See Also:Constant Field Values

- FORCECOMPLETEANDJUMP
static final int FORCECOMPLETEANDJUMP
See Also:Constant Field Values

- GETALLVARIABLENAMES
static final int GETALLVARIABLENAMES
See Also:Constant Field Values

- GETINITIALVARIABLEVALUE
static final int GETINITIALVARIABLEVALUE
See Also:Constant Field Values

- GETOUTGOINGLINKS
static final int GETOUTGOINGLINKS
See Also:Constant Field Values

- GETBRANCHES
static final int GETBRANCHES
See Also:Constant Field Values

- FORCENAVIGATE
static final int FORCENAVIGATE
See Also:Constant Field Values

- RESCHEDULE\_TIMER
static final int RESCHEDULE\_TIMER
See Also:Constant Field Values

- RESCHEDULE
static final int RESCHEDULE
Deprecated. As of version 7.0, replaced by RESCHEDULE\_TIMER.
See Also:Constant Field Values

- GETJUMPTARGETNAMES
static final int GETJUMPTARGETNAMES
See Also:Constant Field Values

- JUMP
static final int JUMP
See Also:Constant Field Values

- FORCEJOINCONDITION
static final int FORCEJOINCONDITION
See Also:Constant Field Values

- FORCELOOPCONDITION
static final int FORCELOOPCONDITION
See Also:Constant Field Values

- FORCEFOREACHCOUNTERVALUES
static final int FORCEFOREACHCOUNTERVALUES
See Also:Constant Field Values

- GETCORRELATIONSETINSTANCES
static final int GETCORRELATIONSETINSTANCES
See Also:Constant Field Values

- GETROLEINFO
static final int GETROLEINFO
See Also:Constant Field Values

- MAX\_COUNT
static final int MAX\_COUNT
See Also:Constant Field Values