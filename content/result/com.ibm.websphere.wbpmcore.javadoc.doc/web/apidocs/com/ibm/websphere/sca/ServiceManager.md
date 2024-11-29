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

## Class ServiceManager

- java.lang.Object
    - com.ibm.websphere.sca.ServiceManager

- public class ServiceManager
extends java.lang.Object
Represents a lookup scope for locating SCA services. ServiceManager provides methods to locate a service given an SCA service reference. It also provides methods to
 bind an SCA reference to an endpoint. From inside a service component, ServiceManager allows you to get a handle to the current service component metadata and
 create an endpoint reference for this component.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static ServiceManager
INSTANCE
The default ServiceManager instance.
    - Constructor Summary

Constructors 

Constructor and Description

ServiceManager()
Constructs a new ServiceManager.

ServiceManager(java.io.InputStream inputStream)
Constructs a new ServiceManager from an InputStream.
    - Method Summary Methods Modifier and Type Method and Description EndpointReference createEndpointReference (InterfaceType interfaceType) Creates an endpoint reference for one of interfaces exposed by the current service component. Component getComponent () Returns the Component object representing the current SCDL component. commonj.sdo.Sequence getEndpointReferenceParameters () Returns the endpoint reference parameters associated with the current invocation. commonj.sdo.Sequence getEndpointReferenceProperties () Returns the endpoint reference properties associated with the current invocation. java.lang.Object getService (Reference reference, EndpointReference endpointReference) Locates the given service reference, binds the service reference to the given endpoint, and returns a proxy to the target service. java.lang.Object getService (java.lang.String referenceName, EndpointReference endpointReference) Locates the named service reference, binds the service reference to the given endpoint, and returns a proxy to the target service. java.lang.Object locateService (Reference reference) Locates the service wired to the given reference and returns a proxy to the service. java.lang.Object locateService (java.lang.String referenceName) Locates the service wired to the named reference and returns a proxy to the service.

### Method Summary

| Modifier and Type    | Method and Description                                                                                                                                                                                                       |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EndpointReference    | createEndpointReference(InterfaceType interfaceType) Creates an endpoint reference for one of interfaces exposed by the current service component.                                                                           |
| Component            | getComponent() Returns the Component object representing the current SCDL component.                                                                                                                                         |
| commonj.sdo.Sequence | getEndpointReferenceParameters() Returns the endpoint reference parameters associated with the current invocation.                                                                                                           |
| commonj.sdo.Sequence | getEndpointReferenceProperties() Returns the endpoint reference properties associated with the current invocation.                                                                                                           |
| java.lang.Object     | getService(Reference reference,           EndpointReference endpointReference) Locates the given service reference, binds the service reference to the given endpoint, and returns a proxy to the target service.            |
| java.lang.Object     | getService(java.lang.String referenceName,           EndpointReference endpointReference) Locates the named service reference, binds the service reference to the given endpoint, and returns a proxy to the target service. |
| java.lang.Object     | locateService(Reference reference) Locates the service wired to the given reference and returns a proxy to the service.                                                                                                      |
| java.lang.Object     | locateService(java.lang.String referenceName) Locates the service wired to the named reference and returns a proxy to the service.                                                                                           |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait