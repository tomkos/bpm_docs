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

## Interface RecoveryOperation

- public interface RecoveryOperation
The RecoveryOperation interface defines how the events be managed.

 Any sub-system leveraging Recovery needs to implement the interface to delete
 or replay the event data in the sub-system with request from Recovery.

 The implementation needs to be registered.

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
deleteEvent(java.lang.String eventId,
           java.util.Properties context)
Delete the specified event.

void
replayEvent(java.lang.String eventId,
           EventData replayData,
           java.util.Properties context)
Replay the specified event.

EventData
retrieveEvent(java.lang.String eventId,
             java.util.Properties context)
Return the detailed information of the event.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - retrieveEvent
EventData retrieveEvent(java.lang.String eventId,
                      java.util.Properties context)
                        throws RecoveryException
Return the detailed information of the event.
Parameters:eventId - context - 
Returns:
Throws:
RecoveryException
    - deleteEvent
void deleteEvent(java.lang.String eventId,
               java.util.Properties context)
                 throws RecoveryException
Delete the specified event.
 This operation is triggered from Recovery client (FEM or custom program).
 The metadata in Recovery repository and message/record left in sub-system
 will be removed in the same transaction.
Parameters:eventId - context - 
Throws:
RecoveryException
    - replayEvent
void replayEvent(java.lang.String eventId,
               EventData replayData,
               java.util.Properties context)
                 throws RecoveryException
Replay the specified event.
 The metadata in Recovery repository and event data in sub-system will
 be removed in the same transaction.
Parameters:eventId - replayData - modified data, specify null if no modification requiredcontext - 
Throws:
RecoveryException