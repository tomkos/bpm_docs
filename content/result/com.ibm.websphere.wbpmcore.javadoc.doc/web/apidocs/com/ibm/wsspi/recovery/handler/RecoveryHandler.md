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

## Class RecoveryHandler

- java.lang.Object
    - com.ibm.wsspi.recovery.handler.RecoveryHandler

- public abstract class RecoveryHandler
extends java.lang.Object
The RecoveryHandler interface defines how the exception will be handled
 by Recovery.

 Any sub-system leveraging Recovery needs can call the interface to hand over the
 exception to Recovery handler, which will generate a failed event. The original event
 data (message, record) is still in the sub-system.

 Usage:
 RecoveryHandler.getInstance().handleException(eventId, exception, context);

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COMPONENT\_NAME\_PROPERTY
SCA Component name where the exception happened.

static java.lang.String
COMPONENT\_TYPE\_JMS
Component types for components.

static java.lang.String
COMPONENT\_TYPE\_MQ 

static java.lang.String
COMPONENT\_TYPE\_PROPERTY
Type of binding that received the message.

static java.lang.String
COPYRIGHT 

static java.lang.String
EXPIRATION\_PROPERTY
Expiration time of the failed event
 The property is mandatory.

static java.lang.String
FAILURE\_TIME\_PROPERTY
The timestamp when the exception happened.

static java.lang.String
INTERACTION\_TYPE\_PROPERTY
SCA interaction type
 Property value type: String

static java.lang.String
MODULE\_NAME\_PROPERTY
SCA Module name where the exception happened.

static java.lang.String
OPERATION\_NAME\_PROPERTY
Operation name (of the SCA interface) where the exception happened
 The property is mandatory.

static java.lang.String
RESUBMIT\_DESTINATION\_PROPERTY
Resubmit destination of the failed event
 The property is mandatory.
    - Constructor Summary

Constructors 

Constructor and Description

RecoveryHandler()
    - Method Summary Methods Modifier and Type Method and Description static RecoveryHandler getInstance () Gets an instance of RecoveryHandler. abstract void handleException (java.lang.String eventId, java.lang.Exception exception, java.util.Properties context) Hand over the exception from sub-system to Recovery handler.

### Method Summary

| Modifier and Type      | Method and Description                                                                                                                                                                            |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static RecoveryHandler | getInstance() Gets an instance of RecoveryHandler.                                                                                                                                                |
| abstract void          | handleException(java.lang.String eventId,                java.lang.Exception exception,                java.util.Properties context) Hand over the exception from sub-system to Recovery handler. |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait