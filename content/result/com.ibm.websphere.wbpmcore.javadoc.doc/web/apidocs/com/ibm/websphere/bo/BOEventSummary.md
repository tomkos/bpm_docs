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

## Interface BOEventSummary

- public interface BOEventSummary
The BOEventSummary interface represents the client programming model
 interface for the BOEventSummary service.  The BOEventSummary service
 provides low level operations for adding annotations to the Business Objects
 in a Business Graph. Each Business Object can be annotated with an Object
 Event ID or an Event.  These two annotations are both typed as Strings.

- ======== NESTED CLASS SUMMARY ======== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Nested Class Summary

Nested Classes 

Modifier and Type
Interface and Description

static interface 
BOEventSummary.ObjectContext
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
clear()
Removes all the Object Context objects in the Event Summary.

java.lang.String
getEvent(commonj.sdo.DataObject businessObject)
Returns the Event name associated with the Business Object.

java.util.List
getObjectContexts()
Returns the list of Object Context objects for each Business
 Object in the Business Graph that has either an Object Event ID
 and/or an Event name associated with it.

java.lang.String
getObjectEventID(commonj.sdo.DataObject businessObject)
Returns the Object Event ID associated with the Business Object.

void
removeEvent(commonj.sdo.DataObject businessObject)
Removes the Event name associated with the Business Object.

void
removeObjectEventID(commonj.sdo.DataObject businessObject)
Removes the Object Event ID associated with the Business Object.

void
setEvent(commonj.sdo.DataObject businessObject,
        java.lang.String event)
Annotate the Business Object with an Event name.

void
setObjectEventID(commonj.sdo.DataObject businessObject,
                java.lang.String objectEventID)
Annotate the Business Object with an Object Event ID that uniquely
 identiifes it in the graph of Business Objects.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - setObjectEventID
void setObjectEventID(commonj.sdo.DataObject businessObject,
                    java.lang.String objectEventID)
Annotate the Business Object with an Object Event ID that uniquely
 identiifes it in the graph of Business Objects.

 The Business Object must be contained in a Business Graph that
 contains the Event Summary.
Parameters:businessObject - The Business Object to annotate with an Object
 Event ID stringobjectEventID - A string to uniquely identify the Business
 Object
    - getObjectEventID
java.lang.String getObjectEventID(commonj.sdo.DataObject businessObject)
Returns the Object Event ID associated with the Business Object.

 The Business Object must be contained in a Business Graph that
 contains the Event Summary.
Parameters:businessObject - The Business Object to annotate with an Object
 Event ID string
Returns:Returns the Object Event ID string that uniquely identifies
 the Business Object
    - removeObjectEventID
void removeObjectEventID(commonj.sdo.DataObject businessObject)
Removes the Object Event ID associated with the Business Object.

 The Business Object must be contained in a Business Graph that
 contains the Event Summary.
Parameters:businessObject - The Business Object to annotate with an Object
 Event ID string
    - setEvent
void setEvent(commonj.sdo.DataObject businessObject,
            java.lang.String event)
Annotate the Business Object with an Event name.  This field can
 be used to annotate a Business Object instance with any string.

 The Business Object must be contained in a Business Graph that
 contains the Event Summary.
Parameters:businessObject - The Business Object to annotate with the
 Event nameevent - The Event name
    - getEvent
java.lang.String getEvent(commonj.sdo.DataObject businessObject)
Returns the Event name associated with the Business Object.

 The Business Object must be contained in a Business Graph that
 contains the Event Summary.
Parameters:businessObject - The Business Object to annotate with the
 Event name
Returns:Returns the Event name
    - removeEvent
void removeEvent(commonj.sdo.DataObject businessObject)
Removes the Event name associated with the Business Object.

 The Business Object must be contained in a Business Graph that
 contains the Event Summary.
Parameters:businessObject - The Business Object to annotate with the
 Event name
    - getObjectContexts
java.util.List getObjectContexts()
Returns the list of Object Context objects for each Business
 Object in the Business Graph that has either an Object Event ID
 and/or an Event name associated with it.
Returns:A List of ObjectContext objects
    - clear
void clear()
Removes all the Object Context objects in the Event Summary.