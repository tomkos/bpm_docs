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

## Enum WSASchemaType

- java.lang.Object
    - java.lang.Enum<WSASchemaType>
        - com.ibm.websphere.sibx.smobo.WSASchemaType

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<WSASchemaType>, org.eclipse.emf.common.util.Enumerator

public enum WSASchemaType
extends java.lang.Enum<WSASchemaType>
implements org.eclipse.emf.common.util.Enumerator

 A representation of the literals of the enumeration 'WSA Schema Type',
 and utility methods for working with them.
 
 Note that these literals are only of use to the custom mediation writer and cannot
 be used in filter primitive expressions.

- =========== ENUM CONSTANT SUMMARY =========== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

HTTP\_SCHEMAS\_XMLSOAP\_ORG\_WS200408\_ADDRESSING\_LITERAL
The 'Http Schemas Xmlsoap Org Ws200408 Addressing' literal object

HTTP\_WWW\_W3\_ORG200508\_ADDRESSING\_LITERAL
The 'Http Www W3 Org200508 Addressing' literal object
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT 

static int
HTTP\_SCHEMAS\_XMLSOAP\_ORG\_WS200408\_ADDRESSING
The 'Http Schemas Xmlsoap Org Ws200408 Addressing' literal value

static int
HTTP\_WWW\_W3\_ORG200508\_ADDRESSING
The 'Http Www W3 Org200508 Addressing' literal value

static java.util.List<WSASchemaType>
VALUES
A public read-only list of all the 'WSA Schema Type' enumerators
    - Method Summary Methods Modifier and Type Method and Description static WSASchemaType get (int value) Returns the 'WSA Schema Type ' literal with the specified integer value static WSASchemaType get (java.lang.String literal) Returns the 'WSA Schema Type ' literal with the specified literal value static WSASchemaType getByName (java.lang.String name) Returns the 'WSA Schema Type ' literal with the specified name java.lang.String getLiteral () java.lang.String getName () int getValue () java.lang.String toString () Returns the literal value of the enumerator, which is its string representation static WSASchemaType valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static WSASchemaType [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type      | Method and Description                                                                                |
|------------------------|-------------------------------------------------------------------------------------------------------|
| static WSASchemaType   | get(int value) Returns the 'WSA Schema Type' literal with the specified integer value                 |
| static WSASchemaType   | get(java.lang.String literal) Returns the 'WSA Schema Type' literal with the specified literal value  |
| static WSASchemaType   | getByName(java.lang.String name) Returns the 'WSA Schema Type' literal with the specified name        |
| java.lang.String       | getLiteral()                                                                                          |
| java.lang.String       | getName()                                                                                             |
| int                    | getValue()                                                                                            |
| java.lang.String       | toString() Returns the literal value of the enumerator, which is its string representation            |
| static WSASchemaType   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static WSASchemaType[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait