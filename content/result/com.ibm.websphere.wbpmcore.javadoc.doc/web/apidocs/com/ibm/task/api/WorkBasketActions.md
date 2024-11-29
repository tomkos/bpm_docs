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

## Interface WorkBasketActions

- public interface WorkBasketActions
This interface defines symbolic constants for all actions that can be performed on
 work baskets. These constants are to be used when determining the actions
 allowed by the currently logged-on user.
 Currently allowed actions are returned when calling the
 getAvailableActionsForWorkBasket()
 or getAvailableActionFlagsForWorkBaskets()
 methods for a work basket.
Since:
6.2.0.3

- =========== FIELD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
CREATEWORKBASKET
Symbolic constant for work basket action create.

static int
CUSTOMACTION1
Symbolic constants for custom work basket actions.

static int
CUSTOMACTION10 

static int
CUSTOMACTION11 

static int
CUSTOMACTION12 

static int
CUSTOMACTION13 

static int
CUSTOMACTION14 

static int
CUSTOMACTION15 

static int
CUSTOMACTION16 

static int
CUSTOMACTION17 

static int
CUSTOMACTION18 

static int
CUSTOMACTION19 

static int
CUSTOMACTION2 

static int
CUSTOMACTION20 

static int
CUSTOMACTION3 

static int
CUSTOMACTION4 

static int
CUSTOMACTION5 

static int
CUSTOMACTION6 

static int
CUSTOMACTION7 

static int
CUSTOMACTION8 

static int
CUSTOMACTION9 

static int
DELETEWORKBASKET
Symbolic constant for work basket action delete.

static int
DISTRIBUTE
Symbolic constant for work basket action distribute.

static int
GETDISTRIBUTIONTARGETS
Symbolic constant for work basket action get distribution targets.

static int
GETROLEINFO
Symbolic constant for work basket action get (all) work items.

static int
GETWORKBASKET
Symbolic constant for work basket action get work basket.

static int
GETWORKBASKETDEFINITION
Symbolic constant for work basket action get work basket definition.

static int
OPEN
Symbolic constant for work basket action open.

static int
TRANSFERFROMWORKBASKET
Symbolic constant for work basket action transfer from work basket.

static int
TRANSFERTOWORKBASKET
Symbolic constant for work basket action transfer to work basket.

static int
UPDATE
Symbolic constant for work basket action update.

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- CUSTOMACTION1
static final int CUSTOMACTION1
Symbolic constants for custom work basket actions.
See Also:Constant Field Values

- CUSTOMACTION2
static final int CUSTOMACTION2
See Also:Constant Field Values

- CUSTOMACTION3
static final int CUSTOMACTION3
See Also:Constant Field Values

- CUSTOMACTION4
static final int CUSTOMACTION4
See Also:Constant Field Values

- CUSTOMACTION5
static final int CUSTOMACTION5
See Also:Constant Field Values

- CUSTOMACTION6
static final int CUSTOMACTION6
See Also:Constant Field Values

- CUSTOMACTION7
static final int CUSTOMACTION7
See Also:Constant Field Values

- CUSTOMACTION8
static final int CUSTOMACTION8
See Also:Constant Field Values

- CUSTOMACTION9
static final int CUSTOMACTION9
See Also:Constant Field Values

- CUSTOMACTION10
static final int CUSTOMACTION10
See Also:Constant Field Values

- CUSTOMACTION11
static final int CUSTOMACTION11
See Also:Constant Field Values

- CUSTOMACTION12
static final int CUSTOMACTION12
See Also:Constant Field Values

- CUSTOMACTION13
static final int CUSTOMACTION13
See Also:Constant Field Values

- CUSTOMACTION14
static final int CUSTOMACTION14
See Also:Constant Field Values

- CUSTOMACTION15
static final int CUSTOMACTION15
See Also:Constant Field Values

- CUSTOMACTION16
static final int CUSTOMACTION16
See Also:Constant Field Values

- CUSTOMACTION17
static final int CUSTOMACTION17
See Also:Constant Field Values

- CUSTOMACTION18
static final int CUSTOMACTION18
See Also:Constant Field Values

- CUSTOMACTION19
static final int CUSTOMACTION19
See Also:Constant Field Values

- CUSTOMACTION20
static final int CUSTOMACTION20
See Also:Constant Field Values

- GETWORKBASKET
static final int GETWORKBASKET
Symbolic constant for work basket action get work basket.
See Also:Constant Field Values

- GETROLEINFO
static final int GETROLEINFO
Symbolic constant for work basket action get (all) work items.
See Also:Constant Field Values

- GETDISTRIBUTIONTARGETS
static final int GETDISTRIBUTIONTARGETS
Symbolic constant for work basket action get distribution targets.
See Also:Constant Field Values

- DISTRIBUTE
static final int DISTRIBUTE
Symbolic constant for work basket action distribute.
See Also:Constant Field Values

- TRANSFERFROMWORKBASKET
static final int TRANSFERFROMWORKBASKET
Symbolic constant for work basket action transfer from work basket.
See Also:Constant Field Values

- TRANSFERTOWORKBASKET
static final int TRANSFERTOWORKBASKET
Symbolic constant for work basket action transfer to work basket.
See Also:Constant Field Values

- GETWORKBASKETDEFINITION
static final int GETWORKBASKETDEFINITION
Symbolic constant for work basket action get work basket definition.
See Also:Constant Field Values

- CREATEWORKBASKET
static final int CREATEWORKBASKET
Symbolic constant for work basket action create.
See Also:Constant Field Values

- UPDATE
static final int UPDATE
Symbolic constant for work basket action update.
See Also:Constant Field Values

- DELETEWORKBASKET
static final int DELETEWORKBASKET
Symbolic constant for work basket action delete.
See Also:Constant Field Values

- OPEN
static final int OPEN
Symbolic constant for work basket action open.
See Also:Constant Field Values