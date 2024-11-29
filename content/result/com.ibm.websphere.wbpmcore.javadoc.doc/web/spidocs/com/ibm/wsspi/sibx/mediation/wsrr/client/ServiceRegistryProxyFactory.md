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

## Class ServiceRegistryProxyFactory

- java.lang.Object
    - com.ibm.wsspi.sibx.mediation.wsrr.client.ServiceRegistryProxyFactory

- public class ServiceRegistryProxyFactory
extends java.lang.Object
A Factory used to access the ServiceRegistryProxy class

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description ServiceRegistryProxy getDefaultServiceRegistryProxy () Gets the ServiceRegistryProxy instance for the default Service Registry. static ServiceRegistryProxyFactory getInstance () Returns the singleton instance of the ServiceRegistryProxyFactory ServiceRegistryProxy getServiceRegistryProxy (java.lang.String registryName) Gets the ServiceRegistryProxy instance for the named Service Registry.

### Method Summary

| Modifier and Type                  | Method and Description                                                                                                        |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| ServiceRegistryProxy               | getDefaultServiceRegistryProxy() Gets the ServiceRegistryProxy instance for the default Service Registry.                     |
| static ServiceRegistryProxyFactory | getInstance() Returns the singleton instance of the ServiceRegistryProxyFactory                                               |
| ServiceRegistryProxy               | getServiceRegistryProxy(java.lang.String registryName) Gets the ServiceRegistryProxy instance for the named Service Registry. |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait