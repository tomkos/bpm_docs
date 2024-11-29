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

## Interface EventHandlerTemplateData

- All Superinterfaces: java.io.Serializable public interface EventHandlerTemplateData extends java.io.Serializable Accesses the properties of an event (action) that can be triggered as part of an active event handler. BPEL event handlers allow for receiving external events and requests concurrently with the running process instance. This is especially helpful for events and requests that may occur at arbitrary times and an arbitrary number of times. There are two types of events. When the message constituting an event arrives, the activity specified in the corresponding event handler is carried out. The event, however, remains enabled, even for concurrent use. Since: 6.0

```
public interface EventHandlerTemplateData
extends java.io.Serializable
```

BPEL event handlers allow for receiving external events and requests
 concurrently with the running process instance.
 This is especially helpful for events and requests that may occur at arbitrary times
 and an arbitrary number of times.
 
 There are two types of events.
 
Events can be incoming messages that correspond to a request/response
 or one-way operation in WSDL. For instance, a status query is likely to be a
 request/response operation, whereas a cancellation may be a one-way operation.
 Events can be alarms, that go off after user-set times. Alarms are not described
 by this data object since they are handled automatically.
 
 When the message constituting an event arrives, the activity specified in the corresponding
 event handler is carried out. The event, however, remains enabled, even for concurrent use.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
KIND\_ON\_ALARM
The event handler is signaled after a specific duration of time (timeout event) or at a specific point in time.

static int
KIND\_ON\_ALARM\_REPEATING
The event handler is signaled after a specific duration of time (timeout event)
 or at a specific point in time and the alarm is repeated after defined intervals.

static int
KIND\_ON\_MESSAGE
The event handler waits for a message to arrive.
    - Method Summary

Methods 

Modifier and Type
Method and Description

int[]
getAvailableActions()
Returns the actions that can be called for the current event handler.

EHTID
getID()
Returns the object identifier.

java.lang.String
getInputMessageTypeName()
Returns the name of the input message type.

int
getKind()
Returns the kind of the event that is waited for.

java.lang.String
getOperationName()
Returns the name of the operation.

java.lang.String
getPortTypeName()
Returns the name of the partner's port type.

java.lang.String
getPortTypeNamespace()
Returns the namespace of the operation.

PTID
getProcessTemplateID()
Returns the object ID of the process template that contains the event handler.

java.lang.String
getProcessTemplateName()
Returns the name of the process template that contains the event handler.

boolean
isTwoWayOperation()
Returns whether the service to be called is a two-way
 operation or not.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- KIND\_ON\_ALARM\_REPEATING
static final int KIND\_ON\_ALARM\_REPEATING
The event handler is signaled after a specific duration of time (timeout event)
 or at a specific point in time and the alarm is repeated after defined intervals.
See Also:Constant Field Values

- KIND\_ON\_MESSAGE
static final int KIND\_ON\_MESSAGE
The event handler waits for a message to arrive.
See Also:Constant Field Values

- KIND\_ON\_ALARM
static final int KIND\_ON\_ALARM
The event handler is signaled after a specific duration of time (timeout event) or at a specific point in time.
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getID
EHTID getID()
Returns the object identifier.
    - getAvailableActions
int[] getAvailableActions()
Returns the actions that can be called for the current event handler.
 Refer to EventHandlerTemplateActions for the set
 of possible actions.
    - getKind
int getKind()
Returns the kind of the event that is waited for.
 
 Possible values are:
 KIND\_ON\_MESSAGE, KIND\_ON\_ALARM, KIND\_ON\_ALARM\_REPEATING.
    - isTwoWayOperation
boolean isTwoWayOperation()
Returns whether the service to be called is a two-way
 operation or not.
    - getPortTypeNamespace
java.lang.String getPortTypeNamespace()
Returns the namespace of the operation.
    - getPortTypeName
java.lang.String getPortTypeName()
Returns the name of the partner's port type.
    - getOperationName
java.lang.String getOperationName()
Returns the name of the operation.
    - getProcessTemplateID
PTID getProcessTemplateID()
Returns the object ID of the process template that contains the event handler.
    - getInputMessageTypeName
java.lang.String getInputMessageTypeName()
Returns the name of the input message type.
    - getProcessTemplateName
java.lang.String getProcessTemplateName()
Returns the name of the process template that contains the event handler.