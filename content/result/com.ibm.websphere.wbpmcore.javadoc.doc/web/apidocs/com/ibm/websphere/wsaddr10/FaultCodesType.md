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
- Enum Constants |
- Field |
- Method

- Detail:
- Enum Constants |
- Field |
- Method

## Enum FaultCodesType

- java.lang.Object
    - java.lang.Enum<FaultCodesType>
        - com.ibm.websphere.wsaddr10.FaultCodesType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<FaultCodesType>, org.eclipse.emf.common.util.Enumerator

public enum FaultCodesType
extends java.lang.Enum<FaultCodesType>
implements org.eclipse.emf.common.util.Enumerator

 A representation of the literals of the enumeration 'Fault Codes Type',
 and utility methods for working with them.

- =========== ENUM CONSTANT SUMMARY =========== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

TNS\_ACTION\_MISMATCH\_LITERAL
The 'Tns Action Mismatch' literal object.

TNS\_ACTION\_NOT\_SUPPORTED\_LITERAL
The 'Tns Action Not Supported' literal object.

TNS\_DESTINATION\_UNREACHABLE\_LITERAL
The 'Tns Destination Unreachable' literal object.

TNS\_DUPLICATE\_MESSAGE\_ID\_LITERAL
The 'Tns Duplicate Message ID' literal object.

TNS\_ENDPOINT\_UNAVAILABLE\_LITERAL
The 'Tns Endpoint Unavailable' literal object.

TNS\_INVALID\_ADDRESS\_LITERAL
The 'Tns Invalid Address' literal object.

TNS\_INVALID\_ADDRESSING\_HEADER\_LITERAL
The 'Tns Invalid Addressing Header' literal object.

TNS\_INVALID\_CARDINALITY\_LITERAL
The 'Tns Invalid Cardinality' literal object.

TNS\_INVALID\_EPR\_LITERAL
The 'Tns Invalid EPR' literal object.

TNS\_MESSAGE\_ADDRESSING\_HEADER\_REQUIRED\_LITERAL
The 'Tns Message Addressing Header Required' literal object.

TNS\_MISSING\_ADDRESS\_IN\_EPR\_LITERAL
The 'Tns Missing Address In EPR' literal object.
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT 

static int
TNS\_ACTION\_MISMATCH
The 'Tns Action Mismatch' literal value.

static int
TNS\_ACTION\_NOT\_SUPPORTED
The 'Tns Action Not Supported' literal value.

static int
TNS\_DESTINATION\_UNREACHABLE
The 'Tns Destination Unreachable' literal value.

static int
TNS\_DUPLICATE\_MESSAGE\_ID
The 'Tns Duplicate Message ID' literal value.

static int
TNS\_ENDPOINT\_UNAVAILABLE
The 'Tns Endpoint Unavailable' literal value.

static int
TNS\_INVALID\_ADDRESS
The 'Tns Invalid Address' literal value.

static int
TNS\_INVALID\_ADDRESSING\_HEADER
The 'Tns Invalid Addressing Header' literal value.

static int
TNS\_INVALID\_CARDINALITY
The 'Tns Invalid Cardinality' literal value.

static int
TNS\_INVALID\_EPR
The 'Tns Invalid EPR' literal value.

static int
TNS\_MESSAGE\_ADDRESSING\_HEADER\_REQUIRED
The 'Tns Message Addressing Header Required' literal value.

static int
TNS\_MISSING\_ADDRESS\_IN\_EPR
The 'Tns Missing Address In EPR' literal value.

static java.util.List<FaultCodesType>
VALUES
A public read-only list of all the 'Relationship Type' enumerators.
    - Method Summary Methods Modifier and Type Method and Description static FaultCodesType get (int value) Returns the 'Relationship Type ' literal with the specified integer value. static FaultCodesType get (java.lang.String literal) Returns the 'Relationship Type ' literal with the specified literal value. static FaultCodesType getByName (java.lang.String name) Returns the 'Relationship Type ' literal with the specified name. java.lang.String getLiteral () java.lang.String getName () int getValue () java.lang.String toString () Returns the literal value of the enumerator, which is its string representation. static FaultCodesType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static FaultCodesType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type       | Method and Description                                                                                  |
|-------------------------|---------------------------------------------------------------------------------------------------------|
| static FaultCodesType   | get(int value) Returns the 'Relationship Type' literal with the specified integer value.                |
| static FaultCodesType   | get(java.lang.String literal) Returns the 'Relationship Type' literal with the specified literal value. |
| static FaultCodesType   | getByName(java.lang.String name) Returns the 'Relationship Type' literal with the specified name.       |
| java.lang.String        | getLiteral()                                                                                            |
| java.lang.String        | getName()                                                                                               |
| int                     | getValue()                                                                                              |
| java.lang.String        | toString() Returns the literal value of the enumerator, which is its string representation.             |
| static FaultCodesType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.          |
| static FaultCodesType[] | values() Returns an array containing the constants of this enum type, in the order they are declared.   |

    - Methods inherited from class java.lang.Enum
clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait