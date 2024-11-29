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

## Interface UnmodifiableProperty

- public interface UnmodifiableProperty
Represents a non-modifiable interface to a property.  This interface
 allows the value and other attributes of the property to be accessed
 but the value cannot be modified.
 
 This interface can be obtained from a Case Manager Java API object,
 such as a Case object, when there is no intent to modify the properties
 of the object. In that scenario some communication to the server can be 
 optimized. In particular, communication with an external data service
 can be deferred until there is an intent to modify the object.
 
 Most of the methods on this interface correspond to non-modifying methods
 on the CaseMgmtProperty class. Some methods on that class
 are only applicable when communication with an external data service
 has occurred, such as the hasDependentProperties method.  
 Such communication does not occur until there is an 
 intent to modify the properties of the object. Therefore those methods
 are not included on this interface.

ID status:
ID review by David Newhall

- ========== METHOD SUMMARY ===========
    - Method Summary

All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description

com.filenet.api.constants.Cardinality
getCardinality()
Corresponds to the getCardinality method on
 CaseMgmtProperty.

CaseMgmtChoiceList
getChoiceList()
Corresponds to the getChoiceList method on
 CaseMgmtProperty.

java.lang.Object
getDefaultValue()
Corresponds to the getDefaultValue method on
 CaseMgmtProperty.

java.lang.String
getDescription()
Corresponds to the getDescription method on
 CaseMgmtProperty.

java.lang.String
getDisplayName()
Corresponds to the getDisplayName method on
 CaseMgmtProperty.

java.lang.Integer
getMaximumLength()
Corresponds to the getMaximumLength method on
 CaseMgmtProperty.

java.lang.Object
getMaximumValue()
Corresponds to the getMaximumValue method on
 CaseMgmtProperty.

java.lang.Object
getMinimumValue()
Corresponds to the getMinimumValue method on
 CaseMgmtProperty.

java.lang.Object
getOriginalValue()
Corresponds to the getOriginalValue method on
 CaseMgmtProperty.

CaseMgmtPropertyState
getOriginalValueState()
Corresponds to the getOriginalValueState method on
 CaseMgmtProperty.

com.filenet.api.constants.TypeID
getPropertyType()
Corresponds to the getPropertyType method on
 CaseMgmtProperty.

boolean
getRequiresUniqueElements()
Corresponds to the getRequiresUniqueElements method on
 CaseMgmtProperty.

com.filenet.api.constants.PropertySettability
getSettability()
Corresponds to the getSettability method on
 CaseMgmtProperty.

java.lang.String
getSymbolicName()
Corresponds to the getSymbolicName method on
 CaseMgmtProperty.

java.lang.Object
getValue()
Corresponds to the getValue method on
 CaseMgmtProperty.

CaseMgmtPropertyState
getValueState()
Corresponds to the getValueState method on
 CaseMgmtProperty.

boolean
isHidden()
Corresponds to the isHidden method on
 CaseMgmtProperty.

boolean
isInherited()
Corresponds to the isInherited method on
 CaseMgmtProperty.

boolean
isOrderable()
Corresponds to the isOrderable method on
 CaseMgmtProperty.

boolean
isQueryable()
Corresponds to the isQueryable method on
 CaseMgmtProperty.

boolean
isRequired()
Corresponds to the isRequired method on
 CaseMgmtProperty.

boolean
isSelectable()
Corresponds to the isSelectable method on
 CaseMgmtProperty.

boolean
isSystemOwned()
Corresponds to the isSystemOwned method on
 CaseMgmtProperty.

- ============ METHOD DETAIL ==========
    - Method Detail

### Method Detail

- getSymbolicName
java.lang.String getSymbolicName()
Corresponds to the getSymbolicName method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- getValue
java.lang.Object getValue()
Corresponds to the getValue method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- getValueState
CaseMgmtPropertyState getValueState()
Corresponds to the getValueState method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- getOriginalValue
java.lang.Object getOriginalValue()
Corresponds to the getOriginalValue method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- getOriginalValueState
CaseMgmtPropertyState getOriginalValueState()
Corresponds to the getOriginalValueState method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- getDisplayName
java.lang.String getDisplayName()
Corresponds to the getDisplayName method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- getDescription
java.lang.String getDescription()
Corresponds to the getDescription method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- getPropertyType
com.filenet.api.constants.TypeID getPropertyType()
Corresponds to the getPropertyType method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- getCardinality
com.filenet.api.constants.Cardinality getCardinality()
Corresponds to the getCardinality method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- getRequiresUniqueElements
boolean getRequiresUniqueElements()
Corresponds to the getRequiresUniqueElements method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- getSettability
com.filenet.api.constants.PropertySettability getSettability()
Corresponds to the getSettability method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- isRequired
boolean isRequired()
Corresponds to the isRequired method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- isQueryable
boolean isQueryable()
Corresponds to the isQueryable method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- isSelectable
boolean isSelectable()
Corresponds to the isSelectable method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- isOrderable
boolean isOrderable()
Corresponds to the isOrderable method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- isHidden
boolean isHidden()
Corresponds to the isHidden method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- isInherited
boolean isInherited()
Corresponds to the isInherited method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- isSystemOwned
boolean isSystemOwned()
Corresponds to the isSystemOwned method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- getDefaultValue
java.lang.Object getDefaultValue()
Corresponds to the getDefaultValue method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- getMaximumValue
java.lang.Object getMaximumValue()
Corresponds to the getMaximumValue method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- getMinimumValue
java.lang.Object getMinimumValue()
Corresponds to the getMinimumValue method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- getMaximumLength
java.lang.Integer getMaximumLength()
Corresponds to the getMaximumLength method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall

- getChoiceList
CaseMgmtChoiceList getChoiceList()
Corresponds to the getChoiceList method on
 CaseMgmtProperty.

ID status:
ID review by David Newhall