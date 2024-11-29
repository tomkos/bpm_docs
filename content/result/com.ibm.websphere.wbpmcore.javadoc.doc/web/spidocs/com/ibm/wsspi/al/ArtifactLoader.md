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

## Interface ArtifactLoader

- All Known Subinterfaces:
ArtifactLoaderNoLibSPI

public interface ArtifactLoader
This class is the interface (spi) for the basic functionality provided by Artifactloader.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static ArtifactLoader
INSTANCE
Provides access to the implementation of the artifact loader.
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.util.Collection
queryTNSs(java.lang.String artifactType,
         java.lang.Object scope)
Returns a Collection of target namespaces as Strings that are mapped to
 the artifact type.

java.util.Collection
queryURLs(java.lang.String artifactType,
         java.lang.String targetNamespace,
         java.lang.Object scope)
Returns a Collection of URLs that are mapped to the artifact type and
 contribute to the specified target namespace.

java.util.Collection
queryURLsSingleScope(java.lang.String artifactType,
                    java.lang.String targetNamespace,
                    java.lang.Object scope)
Return a Collection of URLs that are mapped to the artifact type
 and contribute to the specified target namespace.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- INSTANCE
static final ArtifactLoader INSTANCE
Provides access to the implementation of the artifact loader.

- Method Detail

### Method Detail

    - queryURLs
java.util.Collection queryURLs(java.lang.String artifactType,
                             java.lang.String targetNamespace,
                             java.lang.Object scope)
Returns a Collection of URLs that are mapped to the artifact type and
 contribute to the specified target namespace.  The target namespace
 can be specified, "*" can be used to indicate all, or the value can be
 "null" which indicates the null target namespace.  This query is
 semantically equivalent to the following SQL queries:

 select url from artifactType where targetNamespace="targetNamespace"

 select url from artifactType where targetNamespace="null"

 select url from artifactType where targetNamespace="*"

In the WBI runtime, the scope indicates the class loader to run the
 query in.  The parameter can have three potential values, null, an
 object that is an instance of ClassLoader, or an object that is not an
 instance of ClassLoader.  In the case of null, the scope is set to the
 current class loader.  If a non-class loader instance is passed, that
 object's class loader is used to define the scope.  If a class loader
 instance is passed, that object is used to define the scope.
Parameters:artifactType - Specifies one of the set of possible artifact
 types supported by the artifact loader (e.g. xsd, wsdl, rol, rel, reli,
 sel, brg, etc).targetNamespace - Specifies the target namespace to use for the
 query.  The string "null" represents the null target namespace, and the
 string "*" represents all target namespaces. In the case of SCDL artifact
 types, this parameter specifies the name of the SCDL artifacts.scope - The scope to begin the query for the artifact.  Null
 indicates the current scope.  An instance of ClassLoader indicates that
 class loader's scope.  An instance that is not of type ClassLoader, is
 used to obtain its class loader and that class loader is used to
 determine the scope.
Returns:A collection of java.net.URLs
    - queryURLsSingleScope
java.util.Collection queryURLsSingleScope(java.lang.String artifactType,
                                        java.lang.String targetNamespace,
                                        java.lang.Object scope)
Return a Collection of URLs that are mapped to the artifact type
 and contribute to the specified target namespace.  The target
 namespace can be specified, "*" can be used to
 indicate all, or the value can be "null" which
 indicates the null target namespace.  This query is semantically
 equivalent to the following SQL queries:

 select url from artifactType where targetNamespace="targetNamespace"

 select url from artifactType where targetNamespace="null"

 select url from artifactType where targetNamespace="*"

In contrast to queryURLs, if no artifacts of the
 specified type are located in the defined scope (or the default
 scope if null was specified), the method immedately returns an
 empty collection.
Parameters:artifactType - Specifies one of the set of possible artifact
 types supported by the artifact loader (e.g. xsd, wsdl, rol, rel, reli,
 sel, brg, etc).targetNamespace - Specifies the target namespace to use for the
 query. "null" is the null target namespace, and "*" for all target
 namespaces. In the case of SCDL artifact types, this parameter specifies
 the name of the SCDL artifacts.scope - The scope to begin the query for the artifact.  The
 value null indicates the current scope.
Returns:A collection of java.net.URLs
    - queryTNSs
java.util.Collection queryTNSs(java.lang.String artifactType,
                             java.lang.Object scope)
Returns a Collection of target namespaces as Strings that are mapped to
 the artifact type.  This query is semantically equivalent to the
 following SQL query:

 select targetNamespace from artifactType
 

 In the case of SCDL artifact types, this query returns a Collection of
 names of the found SCDL artifacts.
Parameters:artifactType - Specifies one of the set of possible artifact
 types supported by the artifact loader (e.g. xsd, wsdl, rol, rel, reli,
 sel, brg, etc).scope - The scope to begin the query for the artifact.  Null
 indicates the current scope.  An instance of ClassLoader indicates that
 class loader's scope.  An instance that is not of type ClassLoader, is
 used to obtain its class loader and that class loader is used to
 determine the scope.
Returns:a collection of targetNamespace Strings.