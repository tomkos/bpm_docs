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

## Interface CorrelationPropertyInstanceData

- All Superinterfaces:
java.io.Serializable

public interface CorrelationPropertyInstanceData
extends java.io.Serializable
Provides information about a property of a correlation set instance.
Since:
7.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getJavaTypeName()
Returns the name of the Java type.

java.lang.String
getMessageTypeName()
Returns the type of the message that defines the correlation property.

java.lang.String
getMessageTypeNamespace()
Returns the namespace of the message that defines the correlation property.

java.lang.String
getPartName()
Returns the part of the message that defines the correlation property.

java.lang.String
getPropertyName()
Returns the name of the correlation property.

java.lang.String
getQueryExpression()
Returns the query expression that defines the correlation property.

java.io.Serializable
getValue()
Returns the value of the correlation property.

java.lang.String
getXSDTypeName()
Returns the name of the XSD type.

java.lang.String
getXSDTypeNamespace()
Returns the name of the namespace of an XSD type.

void
setValue(java.io.Serializable propertyValue)
Sets the value of the correlation property.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getPropertyName
java.lang.String getPropertyName()
Returns the name of the correlation property.
Returns:The name of the correlation property.
    - getJavaTypeName
java.lang.String getJavaTypeName()
Returns the name of the Java type.
Returns:The name of the Java type.
    - getXSDTypeNamespace
java.lang.String getXSDTypeNamespace()
Returns the name of the namespace of an XSD type.
Returns:The name of the namespace of an XSD type.
    - getXSDTypeName
java.lang.String getXSDTypeName()
Returns the name of the XSD type.
Returns:The name of the XSD type.
    - getValue
java.io.Serializable getValue()
Returns the value of the correlation property.
Returns:The value of the correlation property. Returns null when the associated correlation set instance is not initialized.
    - setValue
void setValue(java.io.Serializable propertyValue)
              throws InvalidPropertyAliasTypeException
Sets the value of the correlation property.
Parameters:propertyValue - The value of the correlation property.
Throws:
InvalidPropertyAliasTypeException
    - getMessageTypeNamespace
java.lang.String getMessageTypeNamespace()
Returns the namespace of the message that defines the correlation property.
Returns:The namespace of the message that defines the correlation property.
    Returns null when the associated correlation set instance is retrieved related to a specific message type.
    - getMessageTypeName
java.lang.String getMessageTypeName()
Returns the type of the message that defines the correlation property.
Returns:The type of the message that defines the correlation property.
    Returns null when the associated correlation set instance is retrieved related to a specific message type.
    - getPartName
java.lang.String getPartName()
Returns the part of the message that defines the correlation property.
Returns:The part of the message that defines the correlation property.
    Returns null when the associated correlation set instance is retrieved related to a specific message type.
    - getQueryExpression
java.lang.String getQueryExpression()
Returns the query expression that defines the correlation property.
Returns:The query expression that defines the correlation property.
    Returns null when the associated correlation set instance is retrieved related to a specific message type.