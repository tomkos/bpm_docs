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

## Interface NotificationEventHandlerPlugin

- All Known Implementing Classes:
NotificationEventHandler

public interface NotificationEventHandlerPlugin
This interface supports the creation of notification event handlers.
 
 Notification events are produced when tasks are escalated. Use the
 NotificationEventHandlerPlugin service provider interface (SPI) to
 create plug-ins to get informed about these escalation events.
 
 For example, you can use the SPI to create additional escalation work items
 or use your own e-mail (Java) application to send e-mals to specific people
 when the task is escalated.
 
 This interface provides methods that are called when an notification event occurs.
 
 Default Implementation Class:

NotificationEventHandler
Since:
6.0
Version:
6.00

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

void
escalationNotification(Task task,
                      Escalation escalation)
This method is called when an escalation of a task is fired.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - escalationNotification
void escalationNotification(Task task,
                          Escalation escalation)
This method is called when an escalation of a task is fired.
 
Note: This method is only called when the escalation action was
 set to 'event'.
Parameters:task - The task that is escalated.escalation - The escalation data.