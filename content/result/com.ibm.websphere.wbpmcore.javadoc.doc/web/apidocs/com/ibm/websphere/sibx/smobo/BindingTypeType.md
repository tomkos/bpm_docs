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

## Enum BindingTypeType

- java.lang.Object
    - java.lang.Enum<BindingTypeType>
        - com.ibm.websphere.sibx.smobo.BindingTypeType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<BindingTypeType>, org.eclipse.emf.common.util.Enumerator

public enum BindingTypeType
extends java.lang.Enum<BindingTypeType>
implements org.eclipse.emf.common.util.Enumerator

 A representation of the literals of the enumeration 'Binding Type Type',
 and utility methods for working with them.
 
 Note that these literals are only of use to the custom mediation writer and cannot
 be used in filter primitive expressions.

- =========== ENUM CONSTANT SUMMARY =========== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

EIS\_LITERAL
The 'EIS' literal object

GENERIC\_JMS\_LITERAL
The 'Generic JMS' literal object

HTTP\_LITERAL
The 'HTTP' literal object

JMS\_LITERAL
The 'JMS' literal object

MQ\_LITERAL
The 'MQ' literal object

MQJMS\_LITERAL
The 'MQJMS' literal object

NOT\_SET\_LITERAL
The 'Not Set' literal object

SCA\_LITERAL
The 'SCA' literal object

SLSB\_LITERAL
The 'SLSB' literal object

WEB\_SERVICE\_LITERAL
The 'Web Service' literal object

WEB\_SERVICE\_SOAP\_1\_1\_LITERAL
The 'WEB\_SERVICE\_SOAP\_1\_1' literal object

WEB\_SERVICE\_SOAP\_1\_2\_LITERAL
The 'WEB\_SERVICE\_SOAP\_1\_2' literal object
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT 

static int
EIS
The 'EIS' literal value

static int
GENERIC\_JMS
The 'Generic JMS' literal value

static int
HTTP
The 'HTTP' literal value

static int
JMS
The 'JMS' literal value

static int
MQ
The 'MQ' literal value

static int
MQJMS
The 'MQJMS' literal value

static int
NOT\_SET
The 'Not Set' literal value

static int
SCA
The 'SCA' literal value

static int
SLSB
The 'SLSB' literal value

static java.util.List<BindingTypeType>
VALUES
A public read-only list of all the 'Binding Type Type' enumerators

static int
WEB\_SERVICE
The 'Web Service' literal value

static int
WEB\_SERVICE\_SOAP\_1\_1
The 'WEB\_SERVICE\_SOAP\_1\_1' literal value

static int
WEB\_SERVICE\_SOAP\_1\_2
The 'WEB\_SERVICE\_SOAP\_1\_2' literal value
    - Method Summary Methods Modifier and Type Method and Description static BindingTypeType get (int value) Returns the 'Binding Type Type ' literal with the specified integer value static BindingTypeType get (java.lang.String literal) Returns the 'Binding Type Type ' literal with the specified literal value static BindingTypeType getByName (java.lang.String name) Returns the 'Binding Type Type ' literal with the specified name java.lang.String getLiteral () java.lang.String getName () int getValue () java.lang.String toString () Returns the literal value of the enumerator, which is its string representation static BindingTypeType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static BindingTypeType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type        | Method and Description                                                                                 |
|--------------------------|--------------------------------------------------------------------------------------------------------|
| static BindingTypeType   | get(int value) Returns the 'Binding Type Type' literal with the specified integer value                |
| static BindingTypeType   | get(java.lang.String literal) Returns the 'Binding Type Type' literal with the specified literal value |
| static BindingTypeType   | getByName(java.lang.String name) Returns the 'Binding Type Type' literal with the specified name       |
| java.lang.String         | getLiteral()                                                                                           |
| java.lang.String         | getName()                                                                                              |
| int                      | getValue()                                                                                             |
| java.lang.String         | toString() Returns the literal value of the enumerator, which is its string representation             |
| static BindingTypeType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.         |
| static BindingTypeType[] | values() Returns an array containing the constants of this enum type, in the order they are declared.  |

    - Methods inherited from class java.lang.Enum
clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait