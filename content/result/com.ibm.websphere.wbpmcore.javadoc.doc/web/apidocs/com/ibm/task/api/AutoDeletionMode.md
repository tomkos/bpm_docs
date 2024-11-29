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
This interface defines symbolic constants that state whether a task instance is
 automatically deleted once it reaches an end execution state or not.
 These constants are to be used when a task template or instance is asked for the deletion mode
 - refer to TaskTemplate.getAutoDeletionMode() or Task.getAutoDeletionMode().
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
ON\_COMPLETION
Symbolic constant that indicates that a task instance is automatically deleted when
 it reaches an end execution state.

static int
ON\_SUCCESSFUL\_COMPLETION
Symbolic constant that indicates that a task instance is automatically deleted when
 it is completed successfully.

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- ON\_COMPLETION
static final int ON\_COMPLETION
Symbolic constant that indicates that a task instance is automatically deleted when
 it reaches an end execution state.
 
 End execution states are STATE\_FINISHED, STATE\_FAILED, STATE\_TERMINATED, or
 STATE\_EXPIRED.
See Also:Constant Field Values

- ON\_SUCCESSFUL\_COMPLETION
static final int ON\_SUCCESSFUL\_COMPLETION
Symbolic constant that indicates that a task instance is automatically deleted when
 it is completed successfully. If not completed successfully, it is kept to allow for
 failing analysis.
See Also:Constant Field Values