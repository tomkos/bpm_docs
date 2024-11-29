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

## Class ArtifactURIResolver

- java.lang.Object
    - org.eclipse.emf.common.notify.impl.AdapterImpl
        - com.ibm.wsspi.ar.ArtifactURIResolver

- All Implemented Interfaces:
org.eclipse.emf.common.notify.Adapter, org.eclipse.emf.common.notify.Adapter.Internal, org.eclipse.wst.wsdl.internal.util.WSDLModelLocator, org.eclipse.xsd.util.XSDSchemaLocationResolver

public class ArtifactURIResolver
extends org.eclipse.emf.common.notify.impl.AdapterImpl
implements org.eclipse.xsd.util.XSDSchemaLocationResolver, org.eclipse.wst.wsdl.internal.util.WSDLModelLocator
Resolves the federated view of a WSDL and XSD based on the URI.  A federated
 view of a WSDL merges all the WSDL documents that participate in the same
 target namespace into one view and ensures the ResourceSet contains the
 models for the WSDLs as well as all the referenced XSDs.
Since:
6.0.0.0

- ======== NESTED CLASS SUMMARY ======== =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Nested Class Summary Nested Classes Modifier and Type Class and Description protected static class ArtifactURIResolver.ResolverFactory

### Nested Class Summary

| Modifier and Type      | Class and Description               |
|------------------------|-------------------------------------|
| protected static class | ArtifactURIResolver.ResolverFactory |

    - Nested classes/interfaces inherited from interface org.eclipse.emf.common.notify.Adapter
org.eclipse.emf.common.notify.Adapter.Internal

- Field Summary Fields Modifier and Type Field and Description static java.lang.String COPYRIGHT

### Field Summary

| Modifier and Type       | Field and Description   |
|-------------------------|-------------------------|
| static java.lang.String | COPYRIGHT               |

    - Fields inherited from class org.eclipse.emf.common.notify.impl.AdapterImpl
target

- Constructor Summary

Constructors 

Constructor and Description

ArtifactURIResolver()

- Method Summary Methods Modifier and Type Method and Description static org.eclipse.emf.common.notify.AdapterFactory getFactory () Return the custom AdapterFactoryImpl for XSDSchemaLocationResolver. boolean isAdapterForType (java.lang.Object type) java.lang.String resolveSchemaLocation (org.eclipse.xsd.XSDSchema xsdSchema, java.lang.String namespaceURI, java.lang.String schemaLocationURI) java.lang.String resolveURI (java.lang.String baseURI, java.lang.String namespaceURI, java.lang.String location) Locates the document given the target namespace.

### Method Summary

| Modifier and Type                                   | Method and Description                                                                                                                                                  |
|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static org.eclipse.emf.common.notify.AdapterFactory | getFactory() Return the custom AdapterFactoryImpl for XSDSchemaLocationResolver.                                                                                        |
| boolean                                             | isAdapterForType(java.lang.Object type)                                                                                                                                 |
| java.lang.String                                    | resolveSchemaLocation(org.eclipse.xsd.XSDSchema xsdSchema,                      java.lang.String namespaceURI,                      java.lang.String schemaLocationURI) |
| java.lang.String                                    | resolveURI(java.lang.String baseURI,           java.lang.String namespaceURI,           java.lang.String location) Locates the document given the target namespace.     |

    - Methods inherited from class org.eclipse.emf.common.notify.impl.AdapterImpl
getTarget, notifyChanged, setTarget, unsetTarget
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait