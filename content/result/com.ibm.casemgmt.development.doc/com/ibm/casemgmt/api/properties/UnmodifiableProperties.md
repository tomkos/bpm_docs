- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Interface UnmodifiableProperties

- public interface UnmodifiableProperties
Represents a non-modifiable interface to a collection of properties.
 The UnmodifiableProperty interfaces accessed through this
 collection allow the values and other attributes of properties to be
 accessed but the values cannot be modified.
 
 This interface can be obtained from a Case Management Java API object,
 such as a Case object, when there is no intent to modify the properties 
 of the object. In that scenario some communication to the server can be 
 optimizedIn particular, communication with an external data service
 can be deferred until there is an intent to modify the object.
 
 Most of the methods on this interface correspond to non-modifying methods
 on the CaseMgmtProperties class.

ID status:
ID review by David Newhall

- ========== METHOD SUMMARY ===========
    - Method Summary

All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description

java.util.List<UnmodifiableProperty>
asList()
Corresponds to the asList method on
 CaseMgmtProperties, returning a list of UnmodifiableProperty
 objects corresponding to the properties in the collection.

UnmodifiableProperty
find(java.lang.String propertyName)
Corresponds to the find(propertyName) method on 
 CaseMgmtProperties, returning an UnmodifiableProperty
 interface corresponding to the property if it exists in the collection.

UnmodifiableProperty
get(java.lang.String propertyName)
Corresponds to the get(propertyName) method on
 CaseMgmtProperties, returning an UnmodifiableProperty
 interface corresponding to the property.

java.lang.Object
getObjectValue(java.lang.String propertyName)
Corresponds to the getObjectValue(propertyName) method on
 CaseMgmtProperties.

com.filenet.api.meta.PropertyDescription
getPropertyDescription(java.lang.String propertyName)
Corresponds to the getPropertyDescription(propertyName) method on
 CaseMgmtProperties.

boolean
isPropertyPresent(java.lang.String propertyName)
Corresponds to the isPropertyPresent(propertyName) method on
 CaseMgmtProperties.

int
size()
Corresponds to the size method on
 CaseMgmtProperties.

boolean
supportsProperty(java.lang.String propertyName)
Corresponds to the supportsProperty(propertyName) method on
 CaseMgmtProperties.

- ============ METHOD DETAIL ==========
    - Method Detail

### Method Detail

- find
UnmodifiableProperty find(java.lang.String propertyName)
Corresponds to the find(propertyName) method on 
 CaseMgmtProperties, returning an UnmodifiableProperty
 interface corresponding to the property if it exists in the collection.

ID status:
ID review by David Newhall

- get
UnmodifiableProperty get(java.lang.String propertyName)
Corresponds to the get(propertyName) method on
 CaseMgmtProperties, returning an UnmodifiableProperty
 interface corresponding to the property.

ID status:
ID review by David Newhall

- getPropertyDescription
com.filenet.api.meta.PropertyDescription getPropertyDescription(java.lang.String propertyName)
Corresponds to the getPropertyDescription(propertyName) method on
 CaseMgmtProperties.

ID status:
ID review by David Newhall

- supportsProperty
boolean supportsProperty(java.lang.String propertyName)
Corresponds to the supportsProperty(propertyName) method on
 CaseMgmtProperties.

ID status:
ID review by David Newhall

- isPropertyPresent
boolean isPropertyPresent(java.lang.String propertyName)
Corresponds to the isPropertyPresent(propertyName) method on
 CaseMgmtProperties.

ID status:
ID review by David Newhall

- getObjectValue
java.lang.Object getObjectValue(java.lang.String propertyName)
Corresponds to the getObjectValue(propertyName) method on
 CaseMgmtProperties.

ID status:
ID review by David Newhall

- asList
java.util.List<UnmodifiableProperty> asList()
Corresponds to the asList method on
 CaseMgmtProperties, returning a list of UnmodifiableProperty
 objects corresponding to the properties in the collection.

ID status:
ID review by David Newhall

- size
int size()
Corresponds to the size method on
 CaseMgmtProperties.

ID status:
ID review by David Newhall