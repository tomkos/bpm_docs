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

## Class ArtifactResouceFactoryImpl

- java.lang.Object
    - org.eclipse.emf.ecore.resource.impl.ResourceFactoryImpl
        - com.ibm.wsspi.ar.ArtifactResouceFactoryImpl

- All Implemented Interfaces:
ARConstants, org.eclipse.emf.ecore.resource.Resource.Factory

public class ArtifactResouceFactoryImpl
extends org.eclipse.emf.ecore.resource.impl.ResourceFactoryImpl
implements ARConstants
Extension to EMF to support loading WSDL and XSD documents within an EAR
 file.  Since a the files in an EAR are physically a JAR within a JAR,
 we also support a custom scheme, "archive:/" which can open streams and
 within these nested JARs. To configure a ResourceSet for the ArtifactResolver 
 use the following steps:

   Resource.Factory rf = ArtifactResouceFactoryImpl.INSTANCE;
         Resource.Factory.Registry registry = resourceSet.getResourceFactoryRegistry ();

        // Register the resource factory for wbi\_artifact protocol
        registry.getProtocolToFactoryMap ().put (
                                ArtifactResourceFactoryImpl.WBI\_ARTIFACT\_PROTOCOL, rf);
        registry.getExtensionToFactoryMap ().put ("xsd", rf);
        registry.getExtensionToFactoryMap ().put ("wsdl", rf);
        resourceSet.getAdapterFactories ().add (ArtifactURIResolver.getFactory ());
        resourceSet.setURIConverter (ArtifactURIConverter.INSTANCE);
        

 If a WSDL target namespace is spread across several documents the elements
 are merged into a single model.

- ======== NESTED CLASS SUMMARY ======== =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Nested Class Summary

### Nested Class Summary

    - Nested classes/interfaces inherited from interface org.eclipse.emf.ecore.resource.Resource.Factory
org.eclipse.emf.ecore.resource.Resource.Factory.Descriptor, org.eclipse.emf.ecore.resource.Resource.Factory.Registry

- Field Summary Fields Modifier and Type Field and Description static ArtifactResouceFactoryImpl INSTANCE static java.lang.String WBI\_ARTIFACT\_PROTOCOL

### Field Summary

| Modifier and Type                 | Field and Description   |
|-----------------------------------|-------------------------|
| static ArtifactResouceFactoryImpl | INSTANCE                |
| static java.lang.String           | WBI\_ARTIFACT\_PROTOCOL   |

    - Fields inherited from interface com.ibm.wsspi.ar.ARConstants
HTTP, SCHEMA, WSDL, XSD

- Constructor Summary

Constructors 

Modifier
Constructor and Description

protected 
ArtifactResouceFactoryImpl()

- Method Summary Methods Modifier and Type Method and Description org.eclipse.emf.ecore.resource.Resource createResource (org.eclipse.emf.common.util.URI uri)

### Method Summary

| Modifier and Type                       | Method and Description                              |
|-----------------------------------------|-----------------------------------------------------|
| org.eclipse.emf.ecore.resource.Resource | createResource(org.eclipse.emf.common.util.URI uri) |

    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait