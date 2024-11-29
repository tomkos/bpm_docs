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

## Interface RelatesToType

- All Superinterfaces: commonj.sdo.DataObject, java.io.Serializable public interface RelatesToType extends commonj.sdo.DataObject begin-user-doc A representation of the model object 'Relates To Type '. end-user-doc The following features are supported:

```
public interface RelatesToType
extends commonj.sdo.DataObject
```

The following features are supported:
 
Value
Relationship Type
Any Attribute

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description commonj.sdo.Sequence getAnyAttribute () Deprecated. java.lang.Object getRelationshipType () Returns the value of the 'Relationship Type ' attribute. java.lang.String getValue () Returns the value of the 'Value ' attribute. boolean isSetRelationshipType () Returns whether the value of the 'Relationship Type ' attribute is set. void setRelationshipType (java.lang.Object value) Sets the value of the 'Relationship Type ' attribute. void setValue (java.lang.String value) Sets the value of the 'Value ' attribute. void unsetRelationshipType () Unsets the value of the 'Relationship Type ' attribute.

### Method Summary

| Modifier and Type    | Method and Description                                                                           |
|----------------------|--------------------------------------------------------------------------------------------------|
| commonj.sdo.Sequence | getAnyAttribute() Deprecated.                                                                    |
| java.lang.Object     | getRelationshipType() Returns the value of the 'Relationship Type' attribute.                    |
| java.lang.String     | getValue() Returns the value of the 'Value' attribute.                                           |
| boolean              | isSetRelationshipType() Returns whether the value of the 'Relationship Type' attribute is set.   |
| void                 | setRelationshipType(java.lang.Object value) Sets the value of the 'Relationship Type' attribute. |
| void                 | setValue(java.lang.String value) Sets the value of the 'Value' attribute.                        |
| void                 | unsetRelationshipType() Unsets the value of the 'Relationship Type' attribute.                   |

- Methods inherited from interface commonj.sdo.DataObject
createDataObject, createDataObject, createDataObject, createDataObject, createDataObject, createDataObject, delete, detach, get, get, get, getBigDecimal, getBigDecimal, getBigDecimal, getBigInteger, getBigInteger, getBigInteger, getBoolean, getBoolean, getBoolean, getByte, getByte, getByte, getBytes, getBytes, getBytes, getChangeSummary, getChar, getChar, getChar, getContainer, getContainmentProperty, getDataGraph, getDataObject, getDataObject, getDataObject, getDate, getDate, getDate, getDouble, getDouble, getDouble, getFloat, getFloat, getFloat, getInstanceProperties, getInstanceProperty, getInt, getInt, getInt, getList, getList, getList, getLong, getLong, getLong, getProperty, getRootObject, getSequence, getSequence, getSequence, getSequence, getShort, getShort, getShort, getString, getString, getString, getType, isSet, isSet, isSet, set, set, set, setBigDecimal, setBigDecimal, setBigDecimal, setBigInteger, setBigInteger, setBigInteger, setBoolean, setBoolean, setBoolean, setByte, setByte, setByte, setBytes, setBytes, setBytes, setChar, setChar, setChar, setDataObject, setDataObject, setDataObject, setDate, setDate, setDate, setDouble, setDouble, setDouble, setFloat, setFloat, setFloat, setInt, setInt, setInt, setList, setList, setList, setLong, setLong, setLong, setShort, setShort, setShort, setString, setString, setString, unset, unset, unset