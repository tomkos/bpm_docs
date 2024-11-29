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

## Interface TaskModel

- All Superinterfaces:
java.io.Serializable

public interface TaskModel
extends java.io.Serializable
Wraps task instances and templates that are created spontaneously. These instances
 and templates are also called ad-hoc tasks and ad-hoc templates.
Since:
6.0.1

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static java.lang.String
WSDL\_SCHEMA\_NAMESPACE 

static java.lang.String
XML\_SCHEMA\_NAMESPACE
    - Method Summary

Methods 

Modifier and Type
Method and Description

TTask
getTTask()
Returns the wrapped object, either a task instance or a task template that has been
 created ad-hoc.

ValidationProblem[]
validate()
Validates the wrapped object, either a task instance or a task template that has been
 created ad-hoc.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- XML\_SCHEMA\_NAMESPACE
static final java.lang.String XML\_SCHEMA\_NAMESPACE
See Also:Constant Field Values

- WSDL\_SCHEMA\_NAMESPACE
static final java.lang.String WSDL\_SCHEMA\_NAMESPACE
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getTTask
TTask getTTask()
Returns the wrapped object, either a task instance or a task template that has been
 created ad-hoc.
Returns:TTask -
    The wrapped object. Returns null when no object is wrapped.
    - validate
ValidationProblem[] validate()
Validates the wrapped object, either a task instance or a task template that has been
 created ad-hoc.
Returns:ValidationProblem[] -
    an array of ValidationProblem objects that contain detailed information
    about problems found during validation -
    refer to ValidationProblem.
    Returns an empty array when no problems are found.