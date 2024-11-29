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

## Class JspApplicableRoleEnum

- java.lang.Object
    - com.ibm.bpe.api.JspApplicableRoleEnum

- All Implemented Interfaces:
java.io.Serializable

public final class JspApplicableRoleEnum
extends java.lang.Object
implements java.io.Serializable
This enumeration class defines symbolic constants for JSP applicable role
 patterns. These values are to be used when JSP information is retrieved
 from a Web client setting.
Since:
6.0
See Also:Serialized Form

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static JspApplicableRoleEnum
ADMIN
Symbolic constant for applicable role admin.

static JspApplicableRoleEnum
ALL
Symbolic constant for applicable role all.

static java.lang.String
COPYRIGHT 

static JspApplicableRoleEnum
EDITOR
Symbolic constant for applicable role editor.

static JspApplicableRoleEnum
ESCALATION\_RECEIVER
Symbolic constant for applicable role escalationReceiver.

static JspApplicableRoleEnum
ORIGINATOR
Symbolic constant for applicable role originator.

static JspApplicableRoleEnum
OWNER
Symbolic constant for applicable role owner.

static JspApplicableRoleEnum
POTENTIAL\_INSTANCE\_CREATOR
Symbolic constant for applicable role potentialInstanceCreator.

static JspApplicableRoleEnum
POTENTIAL\_OWNER
Symbolic constant for applicable role potentialOwner.

static JspApplicableRoleEnum
POTENTIAL\_STARTER
Symbolic constant for applicable role potentialStarter.

static JspApplicableRoleEnum
READER
Symbolic constant for applicable role reader.

static JspApplicableRoleEnum
STARTER
Symbolic constant for applicable role starter.
    - Method Summary Methods Modifier and Type Method and Description static JspApplicableRoleEnum newJspApplicableRoleEnum (java.lang.String jspApplicableRole) Factory method to create a JspUsageEnum by its string representation. java.lang.String toString () Returns a string representation of the JspUsageEnum object.

### Method Summary

| Modifier and Type            | Method and Description                                                                                                              |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| static JspApplicableRoleEnum | newJspApplicableRoleEnum(java.lang.String jspApplicableRole) Factory method to create a JspUsageEnum by its string  representation. |
| java.lang.String             | toString() Returns a string representation of the JspUsageEnum object.                                                              |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait