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

## Class JspUsageEnum

- java.lang.Object
    - com.ibm.task.api.JspUsageEnum

- All Implemented Interfaces:
java.io.Serializable

public final class JspUsageEnum
extends java.lang.Object
implements java.io.Serializable
This enumeration class defines symbolic constants for JSP usage patterns. These
 values are to be used when JSP location information is retrieved from a Web client setting.
Since:
6.0 - introduced in 5.1
See Also:JspLocation, 
WebClientSetting, 
Serialized Form

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static JspUsageEnum
FAULT
Symbolic constant for a JSP that displays a fault of a task.

static JspUsageEnum
INFO
Deprecated.  

static JspUsageEnum
INPUT
Symbolic constant for a JSP that displays the input of a task.

static JspUsageEnum
INSTANCE
Deprecated.  

static JspUsageEnum
MAP
Symbolic constant for a JSP that maps task data in a HTML form into the format of the task's output.

static JspUsageEnum
OUTPUT
Symbolic constant for a JSP that displays the output of a task.

static JspUsageEnum
PAGE
Symbolic constant for a JSP that displays all information about a task, including input and output.

static JspUsageEnum
TEMPLATE
Deprecated.
    - Method Summary Methods Modifier and Type Method and Description static JspUsageEnum newJspUsageEnum (java.lang.String jspUsageEnum) Factory method to create a JspUsageEnum by its string representation. java.lang.String toString () Returns a string representation of the JspUsageEnum object.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                |
|---------------------|-----------------------------------------------------------------------------------------------------------------------|
| static JspUsageEnum | newJspUsageEnum(java.lang.String jspUsageEnum) Factory method to create a JspUsageEnum by its string  representation. |
| java.lang.String    | toString() Returns a string representation of the JspUsageEnum object.                                                |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait