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

## Class MediationFlowComponentFactory

- java.lang.Object
    - com.ibm.wsspi.sibx.mediation.flow.MediationFlowComponentFactory

- Deprecated.

public class MediationFlowComponentFactory
extends java.lang.Object
Factory for creating a MediationFlowComponent implementation.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid
Deprecated. 
 

static java.lang.String
COPYRIGHT
Deprecated.
    - Constructor Summary

Constructors 

Constructor and Description

MediationFlowComponentFactory()
Deprecated.
    - Method Summary Methods Modifier and Type Method and Description static java.util.List<java.lang.String> getFFDCData (boolean isNative, MediationFlowComponentKey key) Deprecated. Method to get FFDC data for data collector static MediationFlowComponent getMediationFlowComponent (MediationFlowComponentKey key, boolean isNativeModule) Deprecated. static void invalidateMediationFlowComponent (MediationFlowComponentKey key) Deprecated. static void returnNativeMediationFlowComponent (MediationFlowComponentKey key, MediationFlowComponent flowComponent) Deprecated. Method to return an instance of a MediationFlowComponent to the pool of flow components held for this component.

### Method Summary

| Modifier and Type                       | Method and Description                                                                                                                                                                                                                                                   |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static java.util.List<java.lang.String> | getFFDCData(boolean isNative,            MediationFlowComponentKey key) Deprecated.  Method to get FFDC data for data collector                                                                                                                                          |
| static MediationFlowComponent           | getMediationFlowComponent(MediationFlowComponentKey key,                          boolean isNativeModule) Deprecated.                                                                                                                                                    |
| static void                             | invalidateMediationFlowComponent(MediationFlowComponentKey key) Deprecated.                                                                                                                                                                                              |
| static void                             | returnNativeMediationFlowComponent(MediationFlowComponentKey key,                                   MediationFlowComponent flowComponent) Deprecated.  Method to return an instance of a MediationFlowComponent to the pool of  flow components held for this component. |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait