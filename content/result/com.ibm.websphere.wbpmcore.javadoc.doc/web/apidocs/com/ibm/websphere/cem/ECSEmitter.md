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

## Class ECSEmitter

- java.lang.Object
    - com.ibm.websphere.cem.ECSEmitter

- All Implemented Interfaces:
com.ibm.events.emitter.Emitter

Deprecated. 
To emit CEI events, instead of calling the APIs of this class, please call WebSphere Application Server CEI APIs directly.

public class ECSEmitter
extends java.lang.Object
implements com.ibm.events.emitter.Emitter

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

ECSEmitter(java.lang.String passedJndiName,
          java.lang.String \_ecsID)
Deprecated. 
ECSEmitter constructor.
    - Method Summary Methods Modifier and Type Method and Description void addUserDataEvent (java.util.Properties properties) Deprecated. Creates and sends a user data event. void close () Deprecated. Instructs the emitter to release all resources that are owned by this object and dependents. org.eclipse.hyades.logging.events.cbe.CommonBaseEvent createCommonBaseEvent (java.lang.String eventName) Deprecated. Creates an common base event via eventFactory java.lang.String getCurrentEcsID () Deprecated. Gets the current ECS ID locally stored on the ECSEmitter instance. com.ibm.events.ComponentMetaData getFilterMetaData () Deprecated. Used to obtain the filter meta data. com.ibm.events.ComponentMetaData getMetaData () Deprecated. Used to obtain the emitter component meta data. java.lang.String getParentEcsID () Deprecated. Gets the parent ECS ID locally stored on the ECSEmitter instance. Span getSpan () Deprecated. int getSynchronizationMode () Deprecated. Allows the caller to determine the current setting for synchronization in this emitter. int getTransactionMode () Deprecated. Allows the caller to determine the currently active transaction mode. boolean hasNoCorrelationData () Deprecated. boolean isSynchronizationModeSupported (int arg0) Deprecated. Allows the caller to determine if a synchronization mode is supported by this emitter. void releaseAndEndECS (java.lang.String ecsID) Deprecated. Releases the current ECSEmitter. java.lang.String sendEvent (org.eclipse.hyades.logging.events.cbe.CommonBaseEvent arg0) Deprecated. Sends an event to the Event Bus. java.lang.String sendEvent (org.eclipse.hyades.logging.events.cbe.CommonBaseEvent cbe, int synchMode, int txMod) Deprecated. Sends an event to the Event Bus overriding the default emitter behavior with the passed parameters. java.lang.String[] sendEvents (org.eclipse.hyades.logging.events.cbe.CommonBaseEvent[] arg0) Deprecated. Sends an array of events to the Event Bus. java.lang.String[] sendEvents (org.eclipse.hyades.logging.events.cbe.CommonBaseEvent[] cbes, int synchMode, int txMode) Deprecated. Sends an array of events to the Event Bus overriding the default emitter behavior with the passed parameters. void setSynchronizationMode (int arg0) Deprecated. Sets the default synchronization mode to use when sending events to the Event Bus. void setTempCurrentEcsID (java.lang.String newCurEcsID) Deprecated. Overrides the content of the current ECS id that is set in the emitted CBEs. void setTempParentEcsID (java.lang.String newParEcsID) Deprecated. Overrides the value of the parent ECS id that is set in the emitted CBEs. void setTransactionMode (int arg0) Deprecated. Sets the transaction mode to use when sending events to the Event Bus.

### Method Summary

| Modifier and Type                                     | Method and Description                                                                                                                                                                                                                             |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                                  | addUserDataEvent(java.util.Properties properties) Deprecated.  Creates and sends a user data event.                                                                                                                                                |
| void                                                  | close() Deprecated.  Instructs the emitter to release all resources that are owned by this object and dependents.                                                                                                                                  |
| org.eclipse.hyades.logging.events.cbe.CommonBaseEvent | createCommonBaseEvent(java.lang.String eventName) Deprecated.  Creates an common base event via eventFactory                                                                                                                                       |
| java.lang.String                                      | getCurrentEcsID() Deprecated.  Gets the current ECS ID locally stored on the ECSEmitter instance.                                                                                                                                                  |
| com.ibm.events.ComponentMetaData                      | getFilterMetaData() Deprecated.  Used to obtain the filter meta data.                                                                                                                                                                              |
| com.ibm.events.ComponentMetaData                      | getMetaData() Deprecated.  Used to obtain the emitter component meta data.                                                                                                                                                                         |
| java.lang.String                                      | getParentEcsID() Deprecated.  Gets the parent ECS ID locally stored on the ECSEmitter instance.                                                                                                                                                    |
| Span                                                  | getSpan() Deprecated.                                                                                                                                                                                                                              |
| int                                                   | getSynchronizationMode() Deprecated.  Allows the caller to determine the current setting for synchronization in this emitter.                                                                                                                      |
| int                                                   | getTransactionMode() Deprecated.  Allows the caller to determine the currently active transaction mode.                                                                                                                                            |
| boolean                                               | hasNoCorrelationData() Deprecated.                                                                                                                                                                                                                 |
| boolean                                               | isSynchronizationModeSupported(int arg0) Deprecated.  Allows the caller to determine if a synchronization mode is supported by this emitter.                                                                                                       |
| void                                                  | releaseAndEndECS(java.lang.String ecsID) Deprecated.  Releases the current ECSEmitter.                                                                                                                                                             |
| java.lang.String                                      | sendEvent(org.eclipse.hyades.logging.events.cbe.CommonBaseEvent arg0) Deprecated.  Sends an event to the Event Bus.                                                                                                                                |
| java.lang.String                                      | sendEvent(org.eclipse.hyades.logging.events.cbe.CommonBaseEvent cbe,          int synchMode,          int txMod) Deprecated.  Sends an event to the Event Bus overriding the default emitter behavior with the passed parameters.                  |
| java.lang.String[]                                    | sendEvents(org.eclipse.hyades.logging.events.cbe.CommonBaseEvent[] arg0) Deprecated.  Sends an array of events to the Event Bus.                                                                                                                   |
| java.lang.String[]                                    | sendEvents(org.eclipse.hyades.logging.events.cbe.CommonBaseEvent[] cbes,           int synchMode,           int txMode) Deprecated.  Sends an array of events to the Event Bus overriding the default emitter behavior with the passed parameters. |
| void                                                  | setSynchronizationMode(int arg0) Deprecated.  Sets the default synchronization mode to use when sending events to the Event Bus.                                                                                                                   |
| void                                                  | setTempCurrentEcsID(java.lang.String newCurEcsID) Deprecated.  Overrides the content of the current ECS id that is set in the emitted CBEs.                                                                                                        |
| void                                                  | setTempParentEcsID(java.lang.String newParEcsID) Deprecated.  Overrides the value of the parent ECS id that is set in the emitted CBEs.                                                                                                            |
| void                                                  | setTransactionMode(int arg0) Deprecated.  Sets the transaction mode to use when sending events to the Event Bus.                                                                                                                                   |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait