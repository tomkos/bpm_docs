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

## Interface AutoDeletionMode

- public interface AutoDeletionMode
This interface defines symbolic constants that state whether a process instance is
 automatically deleted once it reaches an end execution state or not.
 These constants are to be used when a process template is asked for the deletion mode
 of derived process instances - refer to ProcessTemplateData.getAutoDeletionMode().
Since:
6.1

- =========== FIELD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
NO
Symbolic constant that indicates that a process instance is not automatically deleted.

static int
ON\_SUCCESSFUL\_COMPLETION
Symbolic constant that indicates that a process instance is automatically deleted when
 it is completed successfully.

static int
YES
Symbolic constant that indicates that a process instance is automatically deleted when
 it reaches an end execution state.

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- NO
static final int NO
Symbolic constant that indicates that a process instance is not automatically deleted.
See Also:Constant Field Values

- YES
static final int YES
Symbolic constant that indicates that a process instance is automatically deleted when
 it reaches an end execution state.
 
 End execution states are STATE\_FINISHED, STATE\_COMPENSATED, STATE\_TERMINATED, or
 STATE\_FAILED. STATE\_FAILED is only an end execution state if
 no compensation is defined.
See Also:Constant Field Values

- ON\_SUCCESSFUL\_COMPLETION
static final int ON\_SUCCESSFUL\_COMPLETION
Symbolic constant that indicates that a process instance is automatically deleted when
 it is completed successfully. If not completed successfully, it is kept to allow for
 failing analysis.
See Also:Constant Field Values