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

## Interface RegistryAnnotationsType

- public interface RegistryAnnotationsType A representation of the model object 'Registry Annotations Type '. The following features are supported:

```
public interface RegistryAnnotationsType
```

The following features are supported:
 
Property
Classification
Relationship

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.util.List<java.lang.String>
getClassification()
Returns the value of the 'Classification' attribute list.

java.util.List<RegistryPropertyType>
getProperty()
Returns the value of the 'Property' containment reference list.

java.util.List<RegistryRelationshipType>
getRelationship()
Returns the value of the 'Relationship' containment reference list.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- $sccsid
static final java.lang.String $sccsid
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getProperty
java.util.List<RegistryPropertyType> getProperty()
Returns the value of the 'Property' containment reference list.
 The list contents are of type RegistryPropertyType.
Returns:the value of the 'Property' containment reference list.
    - getClassification
java.util.List<java.lang.String> getClassification()
Returns the value of the 'Classification' attribute list.
 The list contents are of type String.
Returns:the value of the 'Classification' attribute list.
    - getRelationship
java.util.List<RegistryRelationshipType> getRelationship()
Returns the value of the 'Relationship' containment reference list.
 The list contents are of type RegistryRelationshipType.
Returns:the value of the 'Relationship' containment reference list.