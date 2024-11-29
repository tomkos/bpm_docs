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

## Class HumanTaskManagerDelegateFactory

- java.lang.Object
    - com.ibm.task.api.HumanTaskManagerDelegateFactory

- public class HumanTaskManagerDelegateFactory
extends java.lang.Object
Factory to create a HumanTaskManagerDelegate object.
Since:
6.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
LOCAL\_EJB 

static int
REMOTE\_EJB
    - Method Summary Methods Modifier and Type Method and Description static HumanTaskManagerDelegate getHumanTaskManagerDelegate (java.lang.String jndiName) Returns the single instance of a remote HumanTaskManagerDelegate object. static HumanTaskManagerDelegate getHumanTaskManagerDelegate (java.lang.String jndiName, int protocol) Returns the single instance of a local or remote HumanTaskManagerDelegate object.

### Method Summary

| Modifier and Type               | Method and Description                                                                                                                                                            |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static HumanTaskManagerDelegate | getHumanTaskManagerDelegate(java.lang.String jndiName) Returns the single instance of a remote HumanTaskManagerDelegate object.                                                   |
| static HumanTaskManagerDelegate | getHumanTaskManagerDelegate(java.lang.String jndiName,                            int protocol) Returns the single instance of a local or remote HumanTaskManagerDelegate object. |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait