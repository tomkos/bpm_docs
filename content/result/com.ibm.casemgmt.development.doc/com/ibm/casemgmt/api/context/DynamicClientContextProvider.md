- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class DynamicClientContextProvider

- java.lang.Object
    - com.ibm.casemgmt.api.context.DynamicClientContextProvider

- public abstract class DynamicClientContextProvider
extends java.lang.Object
Allows the client context to be generated based on a particular object being processed,
 currently a particular LaunchStep or WorkItem object.  A concrete implementation
 of this class is provided to the CaseMgmtContext object through its setDynamicClientContextProvider()
 method.
 
 A class overrides this class and overrides any methods for the particular object types
 it wants to support.

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

DynamicClientContextProvider()
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description java.util.Map<java.lang.String,java.lang.Object> getContextForLaunchStep (LaunchStep launchStep) Generates client context applicable to a particular LaunchStep object. java.util.Map<java.lang.String,java.lang.Object> getContextForWorkItem (WorkItem workItem) Generates client context applicable to a particular WorkItem object.

### Method Summary

| Modifier and Type                                | Method and Description                                                                                                |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| java.util.Map<java.lang.String,java.lang.Object> | getContextForLaunchStep(LaunchStep launchStep) Generates client context applicable to a particular LaunchStep object. |
| java.util.Map<java.lang.String,java.lang.Object> | getContextForWorkItem(WorkItem workItem) Generates client context applicable to a particular WorkItem object.         |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait