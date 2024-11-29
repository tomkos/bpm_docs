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

## Interface ArtifactLocator

- public interface ArtifactLocator
This interface specifies the contract that the Locators need to implement.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
Copyright information for this class/interface
    - Method Summary

Methods 

Modifier and Type
Method and Description

LocatorDefinition
getLocatorDefinition()
Returns the configuration of this Locator, as assembled by the
 environment.

void
initialize(java.util.Map bootstrapContext,
          LocatorDefinition definition)
Configure thyself for use given the bootstrapContext (a Map of environment-
 specific context) and one's configuration information from the
 LocatorDefinition.

java.util.Collection
query(java.lang.String mime,
     java.lang.String targetNamespace)
Query the locator for any artifacts matching the specified mime-type and
 target namespace.

java.util.Collection
queryTargetNamespaces(java.lang.String mime)
Query the locator for all target namespaces defined by artifacts of the
 specified mime-type in the path associated with this locator instance.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
Copyright information for this class/interface
See Also:Constant Field Values

- Method Detail

### Method Detail

    - initialize
void initialize(java.util.Map bootstrapContext,
              LocatorDefinition definition)
Configure thyself for use given the bootstrapContext (a Map of environment-
 specific context) and one's configuration information from the
 LocatorDefinition.  When this method is complete, the
 implementing ArtifactLocator is prepared to process any query.
Parameters:bootstrapContext - Map of environment-specific context.definition - The configuation assmbled from the system environment.
    - query
java.util.Collection query(java.lang.String mime,
                         java.lang.String targetNamespace)
Query the locator for any artifacts matching the specified mime-type and
 target namespace.  Any artifacts that match are returned in a Collection
 of URLs.  Locator implementation will return the artifacts that are visible
 to it and that match namespace and mime criterion.
 Note that passing a targetNamespace of "*" will return all
 artifacts matching the specified mime-type.
Parameters:mime - The mime-type of the artifacts being locatedtargetNamespace - The target namespace of the artifacts being located
Returns:A collection of URLs
    - queryTargetNamespaces
java.util.Collection queryTargetNamespaces(java.lang.String mime)
Query the locator for all target namespaces defined by artifacts of the
 specified mime-type in the path associated with this locator instance.
Parameters:mime - The mime-type of the artifacts being located
Returns:A collection of TNS Strings
    - getLocatorDefinition
LocatorDefinition getLocatorDefinition()
Returns the configuration of this Locator, as assembled by the
 environment.
Returns:A LocatorDefinition which represents this Locator's configuration.