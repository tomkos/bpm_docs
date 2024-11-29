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

## Class JavaMediationDataObject

- java.lang.Object
    - com.ibm.wbiserverspi.mediation.JavaMediationDataObject

- public abstract class JavaMediationDataObject
extends java.lang.Object
This class is implemented by Java Snippets that are called by Interface
 Mediation components configured to mediate WSDL interfaces.
 
 An Interface Mediation component will call this class to perform mediation
 of a particular parameter in an interface. This is used for a DataObject
 parameter to be mediated (for example, WSDL interfaces).

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

JavaMediationDataObject()
    - Method Summary Methods Modifier and Type Method and Description com.ibm.wbiserver.relationshipservice.common.ExecutionContext getContext () abstract commonj.sdo.DataObject mediate (commonj.sdo.DataObject parameter) This method should mediate a DataObject parameter in whatever user-defined manner is needed. void setContext (com.ibm.wbiserver.relationshipservice.common.ExecutionContext arg0)

### Method Summary

| Modifier and Type                                             | Method and Description                                                                                                                 |
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| com.ibm.wbiserver.relationshipservice.common.ExecutionContext | getContext()                                                                                                                           |
| abstract commonj.sdo.DataObject                               | mediate(commonj.sdo.DataObject parameter) This method should mediate a DataObject parameter in whatever user-defined manner is needed. |
| void                                                          | setContext(com.ibm.wbiserver.relationshipservice.common.ExecutionContext arg0)                                                         |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait