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

## Interface OperationMode

- public interface OperationMode
This interface defines symbolic constants that state whether the human task manager database is used
 as an archive or for production purposes.
 When the human task manager database is used as an archive, only read access to stored objects is supported.
 All method calls that try to change the human task manager archive are rejected. An
 ArchiveUnsupportedOperationException is thrown.
Since:
6.2.0.3

- =========== FIELD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static int
ARCHIVE
Symbolic constant that indicates that the human task manager database is used as an archive.

static java.lang.String
COPYRIGHT 

static int
RUNTIME
Symbolic constant that indicates that the human task manager database is used for production purposes.

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- ARCHIVE
static final int ARCHIVE
Symbolic constant that indicates that the human task manager database is used as an archive.
See Also:Constant Field Values

- RUNTIME
static final int RUNTIME
Symbolic constant that indicates that the human task manager database is used for production purposes.
See Also:Constant Field Values