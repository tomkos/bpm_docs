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

## Class BindingRegistryFactory

- java.lang.Object
    - com.ibm.websphere.sca.bindingcore.BindingRegistryFactory

- public class BindingRegistryFactory
extends java.lang.Object
A Binding Registry factory which allows for the retrieval of a fully configured registry
  for the context classloader.

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

BindingRegistryFactory()
    - Method Summary Methods Modifier and Type Method and Description static void clearBindingRegistry (java.lang.ClassLoader associatedClassLoader) clear the BindingRegistry from cache when application stopped static commonj.connector.runtime.BindingRegistry getBindingRegistry (java.lang.ClassLoader associatedClassLoader) Returns the Binding Registry assocated with the specified ClassLoader protected java.util.Map getCache () static commonj.connector.runtime.BindingRegistry getInstance ()

### Method Summary

| Modifier and Type                                | Method and Description                                                                                                                |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| static void                                      | clearBindingRegistry(java.lang.ClassLoader associatedClassLoader) clear the BindingRegistry from cache when application stopped       |
| static commonj.connector.runtime.BindingRegistry | getBindingRegistry(java.lang.ClassLoader associatedClassLoader) Returns the Binding Registry assocated with the specified ClassLoader |
| protected java.util.Map                          | getCache()                                                                                                                            |
| static commonj.connector.runtime.BindingRegistry | getInstance()                                                                                                                         |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait