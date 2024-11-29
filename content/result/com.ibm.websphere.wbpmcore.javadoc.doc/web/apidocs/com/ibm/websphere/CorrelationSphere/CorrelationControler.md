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

## Class CorrelationControler

- java.lang.Object
    - com.ibm.websphere.CorrelationSphere.CorrelationControler

- public class CorrelationControler
extends java.lang.Object

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
BAI\_CORRELATION\_CONTEXT 

static java.lang.String
DELIM 

static java.lang.String
ESCAPE
    - Constructor Summary

Constructors 

Constructor and Description

CorrelationControler()
Constructor.
    - Method Summary Methods Modifier and Type Method and Description void endCorrelationSphere (java.lang.String id) Ends the current correlation sphere and its associated (nested) workarea. static javax.naming.Context getContext () Gets a context for use with JNDI lookups. java.lang.String getCurrentSphereID () Return the current correlation sphere identifier. java.lang.String getParentSphereID () Return the previous correlation sphere identifier. java.io.Serializable getProperty (java.lang.String key) Get the property with the specified key from the correlation context void openNewCorrelationSphere (java.lang.String id) Associate a new instance of a correlation sphere with the current thread. void removeProperty (java.lang.String key) Removes the property with the specified key from the correlation context void setProperty (java.lang.String key, java.io.Serializable value) Sets the property in the correlation context using the specified key and value

### Method Summary

| Modifier and Type           | Method and Description                                                                                                                                   |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                        | endCorrelationSphere(java.lang.String id) Ends the current correlation sphere and its associated  (nested) workarea.                                     |
| static javax.naming.Context | getContext() Gets a context for use with JNDI lookups.                                                                                                   |
| java.lang.String            | getCurrentSphereID() Return the current correlation sphere identifier.                                                                                   |
| java.lang.String            | getParentSphereID() Return the previous correlation sphere identifier.                                                                                   |
| java.io.Serializable        | getProperty(java.lang.String key) Get the property with the specified key from the correlation context                                                   |
| void                        | openNewCorrelationSphere(java.lang.String id) Associate a new instance of a correlation sphere with the  current thread.                                 |
| void                        | removeProperty(java.lang.String key) Removes the property with the specified key from the correlation context                                            |
| void                        | setProperty(java.lang.String key,            java.io.Serializable value) Sets the property in the correlation context using the specified key  and value |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait