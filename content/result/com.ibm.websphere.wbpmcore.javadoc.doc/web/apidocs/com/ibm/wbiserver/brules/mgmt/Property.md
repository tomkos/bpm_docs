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

## Interface Property

- All Superinterfaces:
BusinessRuleChangeDetector, java.io.Serializable

All Known Subinterfaces:
SystemDefinedProperty, UserDefinedProperty

public interface Property
extends BusinessRuleChangeDetector, java.io.Serializable
This interface represents one property associated with some element of the API.  A property
 is simply a name-value pair.  Both the name and the value are strings.  The name cannot be
 null and must contain at least one non-whitespace character.  The property value obtained 
 from a Property object will never be null.  A property with a null value is 
 defined to be the same as the an undefined property.  Hence, null is not allowed as the 
 value of a property.  If you want to make a property undefined, the property should be 
 removed from the property list that contains it.
 
 Two types of properties are supported: system-defined properties and user-defined 
 properties.  System-defined properties are defined by the system and their value cannot be 
 changed.  User-defined properties are defined by the user of the API.  A user-defined 
 property's value  is completely defined by the user and can be changed.  Other than checking 
 for null, no validation is performed on the value when it is changed.  System-defined 
 properties are represented by subclass SystemDefinedProperty.  
 User-defined properties are represented by subclass 
 UserDefinedProperty.
 
 There are several system-defined properties.  The property names for all system-defined 
 properties are defined in constants in this interface.  The javadoc for each constant gives
 a description of the property.  In general, property names beginning with the string 
 "IBMSystem" are reserved for future system-defined properties and should not be used as 
 names for user-defined properties.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static java.lang.String
PROPERTY\_NAME\_\_DISPLAY\_NAME
The name of the system-defined property containing the display name of the object.

static java.lang.String
PROPERTY\_NAME\_\_NAME
The name of the system-defined property containing the name of the object.

static java.lang.String
PROPERTY\_NAME\_\_SHELL
The name of the system-defined property containing the value on whether the object
 is a shell object or not.

static java.lang.String
PROPERTY\_NAME\_\_TARGET\_NAME\_SPACE
The name of the system-defined property containing the target namespace of the object.

static java.lang.String
PROPERTY\_NAME\_\_UUID
The name of the system-defined property containing the universally unique
 identifier of the object.

static java.lang.String
PROPERTY\_NAME\_\_VERSION
The name of the system-defined property containing the version of the object.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getName () Get the name of this property. java.lang.String getValue () Get the value of this property.

### Method Summary

| Modifier and Type   | Method and Description                     |
|---------------------|--------------------------------------------|
| java.lang.String    | getName() Get the name of this property.   |
| java.lang.String    | getValue() Get the value of this property. |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges