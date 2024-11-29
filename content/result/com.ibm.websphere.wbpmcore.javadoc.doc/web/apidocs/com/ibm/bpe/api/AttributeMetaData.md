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

## Interface AttributeMetaData

- All Superinterfaces:
AttributeInfo, java.io.Serializable

public interface AttributeMetaData
extends AttributeInfo
Returns the meta data of a query table attribute.
Since:
6.2.0.1

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getDescription (java.util.Locale locale) Returns the description of the attribute in the requested locale. java.lang.String getDisplayName (java.util.Locale locale) Returns the display name of the attribute in the requested locale.

### Method Summary

| Modifier and Type   | Method and Description                                                                                     |
|---------------------|------------------------------------------------------------------------------------------------------------|
| java.lang.String    | getDescription(java.util.Locale locale) Returns the description of the attribute in the requested locale.  |
| java.lang.String    | getDisplayName(java.util.Locale locale) Returns the display name of the attribute in the requested locale. |

- Methods inherited from interface com.ibm.bpe.api.AttributeInfo
getName, getSourceAttributeName, getSourceQueryTableIdentifier, getSourceQueryTableName, getType, isArray