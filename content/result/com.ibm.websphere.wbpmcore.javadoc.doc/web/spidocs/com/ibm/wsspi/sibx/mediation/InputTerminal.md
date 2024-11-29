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

## Interface InputTerminal

- All Superinterfaces:
Terminal

public interface InputTerminal
extends Terminal
The input terminal of a mediation primitive. Messages arrive for mediation
 via this input terminal defined on a mediation primitive. A mediation
 primitive may define one or more input terminals, each of which must have a 
 unique name.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary

### Method Summary

- Methods inherited from interface com.ibm.wsspi.sibx.mediation.Terminal
getDisplayName, getName, getType