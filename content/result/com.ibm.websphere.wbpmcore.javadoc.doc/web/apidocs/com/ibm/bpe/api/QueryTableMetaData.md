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

## Interface QueryTableMetaData

- All Superinterfaces:
java.io.Serializable

public interface QueryTableMetaData
extends java.io.Serializable
Provides the meta data of a query table.
Since:
6.2.0.1

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

java.util.List
getAttributeMetaData()
Returns information about the attributes that are defined on the query table.

AuthorizationInfo
getAuthorizationInfo()
Returns information about the authorization that is defined for the query table.

java.lang.String
getDescription(java.util.Locale locale)
Returns the description of the query table in the requested locale.

java.lang.String
getDisplayName(java.util.Locale locale)
Returns the display name of the query table in the requested locale.

java.util.List
getKeyAttributeInfo()
Returns information about the key attributes of the query table.

QueryTableKind
getKind()
Returns the kind of the query table.

java.util.Locale
getLocale()
Returns the locale that is calculated for the system variable $LOCALE.

java.util.Locale[]
getLocales()
Returns the locales of available display names and descriptions.

java.lang.String
getName()
Returns the name of the query table.

java.lang.String
getPrimaryQueryTableName()
Returns the name of the primary query table.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getName
java.lang.String getName()
Returns the name of the query table.
 For example, the name of a predefined query table like TASK or
 the name of a composite or supplemental query table whose name format is PREFIX.NAME.
Returns:The name of the query table.
    - getPrimaryQueryTableName
java.lang.String getPrimaryQueryTableName()
Returns the name of the primary query table.
 For example, the name of a predefined query table like TASK.
Returns:The name of the primary query table.
    - getKind
QueryTableKind getKind()
Returns the kind of the query table.
Returns:The kind of the query table. Refer to QueryTableKind.
    - getDisplayName
java.lang.String getDisplayName(java.util.Locale locale)
Returns the display name of the query table in the requested locale.
 If there is no display name for the particular locale, the best available
 match is returned.
 
Parameters:locale - The locale for which the display name is to be provided.
Returns:The display name of the query table.
    - getDescription
java.lang.String getDescription(java.util.Locale locale)
Returns the description of the query table in the requested locale.
 If there is no description for the particular locale, the best available
 match is returned.
 
Parameters:locale - The locale for which the description is to be provided.
Returns:The description of the query table.
    - getLocales
java.util.Locale[] getLocales()
Returns the locales of available display names and descriptions.
 Returns an empty array when there are no display names and descriptions.
Returns:The locales of the display names and descriptions.
    - getLocale
java.util.Locale getLocale()
Returns the locale that is calculated for the system variable $LOCALE.
Returns:The locale that is set for $LOCALE.
    - getKeyAttributeInfo
java.util.List getKeyAttributeInfo()
Returns information about the key attributes of the query table.
 
Returns:A list of AttributeInfo objects that describe the key attributes of the query table.
    Refer to AttributeInfo.
    - getAttributeMetaData
java.util.List getAttributeMetaData()
Returns information about the attributes that are defined on the query table.
 
Returns:A list of AttributeMetaData objects that describe the selected attributes of the query table.
    Refer to AttributeMetaData.
    - getAuthorizationInfo
AuthorizationInfo getAuthorizationInfo()
Returns information about the authorization that is defined for the query table.
 
Returns:The authorization information - refer to AuthorizationInfo.