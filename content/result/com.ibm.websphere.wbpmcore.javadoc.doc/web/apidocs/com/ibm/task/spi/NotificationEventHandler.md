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

## Class NotificationEventHandler

- java.lang.Object
    - com.ibm.task.spi.NotificationEventHandler

- All Implemented Interfaces:
NotificationEventHandlerPlugin

public class NotificationEventHandler
extends java.lang.Object
implements NotificationEventHandlerPlugin
This class provides a default implementation for the Human Task Manager
 NotificationEventHandlerPlugin
 interface.
 
 Note that it is best practice to inherit from this class instead of implementing
 the interface directly. This helps to ensure upward compatibility of your code.
Since:
6.0.2

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Constructor Summary

Constructors 

Constructor and Description

NotificationEventHandler()
    - Method Summary Methods Modifier and Type Method and Description void escalationNotification (Task task, Escalation escalation) This method is called when an escalation of a task is fired.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                      |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| void                | escalationNotification(Task task,                       Escalation escalation) This method is called when an escalation of a task is fired. |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait