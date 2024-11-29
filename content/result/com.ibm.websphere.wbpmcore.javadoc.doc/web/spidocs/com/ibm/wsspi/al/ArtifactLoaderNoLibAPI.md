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

## Interface ArtifactLoaderNoLibSPI

- All Superinterfaces:
ArtifactLoader

public interface ArtifactLoaderNoLibSPI
extends ArtifactLoader
This class is the interface (spi) for the basic functionality provided by Artifactloader.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String COPYRIGHT

### Field Summary

| Modifier and Type       | Field and Description   |
|-------------------------|-------------------------|
| static java.lang.String | COPYRIGHT               |

- Fields inherited from interface com.ibm.wsspi.al.ArtifactLoader
INSTANCE

- Method Summary Methods Modifier and Type Method and Description java.util.Collection queryURLsSingleScopeNoLib (java.lang.String artifactType, java.lang.String targetNamespace, java.lang.Object scope) Return a Collection of URLs that are mapped to the artifact type and contribute to the specified target namespace.

### Method Summary

| Modifier and Type    | Method and Description                                                                                                                                                                                                                                                                   |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| java.util.Collection | queryURLsSingleScopeNoLib(java.lang.String artifactType,                          java.lang.String targetNamespace,                          java.lang.Object scope) Return a Collection of URLs that are mapped to the artifact type  and contribute to the specified target namespace. |

    - Methods inherited from interface com.ibm.wsspi.al.ArtifactLoader
queryTNSs, queryURLs, queryURLsSingleScope