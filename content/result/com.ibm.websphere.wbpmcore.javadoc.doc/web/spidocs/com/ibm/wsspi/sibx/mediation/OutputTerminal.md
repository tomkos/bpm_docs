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

## Interface OutputTerminal

- All Superinterfaces:
Terminal

public interface OutputTerminal
extends Terminal
The output terminal of a mediation primitive. Mediation primitives may
 define zero or more output terminals, each of which must have a unique name.
 A Mediation primitive may
 fire
 its output terminals during processing within the 
 mediate method, passing
 the message. Output terminals are wired to other mediation primitives, or 
 an output of the flow.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description void fire (commonj.sdo.DataObject message) Fires the output terminal.

### Method Summary

| Modifier and Type   | Method and Description                                          |
|---------------------|-----------------------------------------------------------------|
| void                | fire(commonj.sdo.DataObject message) Fires the output terminal. |

- Methods inherited from interface com.ibm.wsspi.sibx.mediation.Terminal
getDisplayName, getName, getType