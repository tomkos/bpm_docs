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

## Interface CompensationBehaviour

- public interface CompensationBehaviour
This interface defines symbolic constants that state how to deal with compensation.
 These constants are to be used when a process instance is terminated - see
 BusinessFlowManagerService.forceTerminate(PIID,int).
Since:
5.1

- =========== FIELD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
IGNORE\_COMPENSATION
Symbolic constant that indicates that compenstation is to be ignored.

static int
INVOKE\_COMPENSATION
Symbolic constant that indicates that compenstation is to be invoked, if defined.

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- IGNORE\_COMPENSATION
static final int IGNORE\_COMPENSATION
Symbolic constant that indicates that compenstation is to be ignored.
See Also:Constant Field Values

- INVOKE\_COMPENSATION
static final int INVOKE\_COMPENSATION
Symbolic constant that indicates that compenstation is to be invoked, if defined.
See Also:Constant Field Values