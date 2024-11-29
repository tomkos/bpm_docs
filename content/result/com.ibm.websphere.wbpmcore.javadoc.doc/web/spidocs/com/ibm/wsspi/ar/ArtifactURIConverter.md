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

## Class ArtifactURIConverter

- java.lang.Object
    - org.eclipse.emf.ecore.resource.impl.URIConverterImpl
        - com.ibm.wsspi.ar.ArtifactURIConverter

- All Implemented Interfaces:
com.ibm.ws.ar.util.ARImplConstants, com.ibm.ws.ar.util.ARPIIMessages, ARConstants, org.eclipse.emf.ecore.resource.URIConverter

public class ArtifactURIConverter
extends org.eclipse.emf.ecore.resource.impl.URIConverterImpl
implements com.ibm.ws.ar.util.ARImplConstants
Extension into EMF to support loading resources using the "wbi\_artifact:/"
 and "archive:/" protocols which gives a single federated view of a WSDL
 document within an EAR file.

- ======== NESTED CLASS SUMMARY ======== =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Nested Class Summary

### Nested Class Summary

    - Nested classes/interfaces inherited from class org.eclipse.emf.ecore.resource.impl.URIConverterImpl
org.eclipse.emf.ecore.resource.impl.URIConverterImpl.Archive, org.eclipse.emf.ecore.resource.impl.URIConverterImpl.PlatformResourceOutputStream, org.eclipse.emf.ecore.resource.impl.URIConverterImpl.URIMap, org.eclipse.emf.ecore.resource.impl.URIConverterImpl.WorkbenchHelper
    - Nested classes/interfaces inherited from interface org.eclipse.emf.ecore.resource.URIConverter
org.eclipse.emf.ecore.resource.URIConverter.Cipher, org.eclipse.emf.ecore.resource.URIConverter.Readable, org.eclipse.emf.ecore.resource.URIConverter.ReadableInputStream, org.eclipse.emf.ecore.resource.URIConverter.Writeable, org.eclipse.emf.ecore.resource.URIConverter.WriteableOutputStream

- Field Summary Fields Modifier and Type Field and Description static java.lang.String COPYRIGHT static ArtifactURIConverter INSTANCE

### Field Summary

| Modifier and Type           | Field and Description   |
|-----------------------------|-------------------------|
| static java.lang.String     | COPYRIGHT               |
| static ArtifactURIConverter | INSTANCE                |

    - Fields inherited from class org.eclipse.emf.ecore.resource.impl.URIConverterImpl
uriMap, workspaceRoot
    - Fields inherited from interface com.ibm.ws.ar.util.ARPIIMessages
ALLOGGER, ARTIFACTLOADER\_FILENOTFOUND, ARTIFACTLOADER\_INCORRECT\_URL, ARTIFACTLOADER\_IO\_FAILURE, ARTIFACTLOADER\_OPENFAILURE, ARTIFACTLOADER\_PROTOCOL\_REG\_FAILURE, BUNDLE, RES\_BUNDLE
    - Fields inherited from interface com.ibm.wsspi.ar.ARConstants
HTTP, SCHEMA, WSDL, XSD
    - Fields inherited from interface org.eclipse.emf.ecore.resource.URIConverter
URI\_MAP

- Constructor Summary

Constructors 

Modifier
Constructor and Description

protected 
ArtifactURIConverter()
Default constructor

- Method Summary Methods Modifier and Type Method and Description protected java.io.InputStream connectInputStream (java.net.URL url) java.io.InputStream createInputStream (org.eclipse.emf.common.util.URI uri)

### Method Summary

| Modifier and Type             | Method and Description                                 |
|-------------------------------|--------------------------------------------------------|
| protected java.io.InputStream | connectInputStream(java.net.URL url)                   |
| java.io.InputStream           | createInputStream(org.eclipse.emf.common.util.URI uri) |

    - Methods inherited from class org.eclipse.emf.ecore.resource.impl.URIConverterImpl
createArchive, createArchiveInputStream, createArchiveOutputStream, createFileInputStream, createFileOutputStream, createOutputStream, createPlatformResourceInputStream, createPlatformResourceOutputStream, createURLInputStream, createURLOutputStream, getInternalURIMap, getURIMap, isArchiveScheme, normalize
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait