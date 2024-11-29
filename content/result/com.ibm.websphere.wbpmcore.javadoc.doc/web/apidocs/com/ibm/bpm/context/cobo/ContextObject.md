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

## Interface ContextObject

- All Superinterfaces: commonj.sdo.DataObject, java.io.Serializable public interface ContextObject extends commonj.sdo.DataObject begin-user-doc A representation of the model object 'Context Object '. end-user-doc The following features are supported:

```
public interface ContextObject
extends commonj.sdo.DataObject
```

The following features are supported:
 
User Defined Context
Header Info

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description HeaderInfoType getHeaderInfo () Returns the value of the 'Header Info ' containment reference UserDefinedContextType getUserDefinedContext () Returns the value of the 'User Defined Context ' containment reference void setHeaderInfo (HeaderInfoType value) Sets the value of the 'Header Info ' containment reference void setUserDefinedContext (UserDefinedContextType value) Sets the value of the 'User Defined Context ' containment reference

### Method Summary

| Modifier and Type      | Method and Description                                                                                                 |
|------------------------|------------------------------------------------------------------------------------------------------------------------|
| HeaderInfoType         | getHeaderInfo() Returns the value of the 'Header Info' containment reference                                           |
| UserDefinedContextType | getUserDefinedContext() Returns the value of the 'User Defined Context' containment reference                          |
| void                   | setHeaderInfo(HeaderInfoType value) Sets the value of the 'Header Info' containment reference                          |
| void                   | setUserDefinedContext(UserDefinedContextType value) Sets the value of the 'User Defined Context' containment reference |

- Methods inherited from interface commonj.sdo.DataObject
createDataObject, createDataObject, createDataObject, createDataObject, createDataObject, createDataObject, delete, detach, get, get, get, getBigDecimal, getBigDecimal, getBigDecimal, getBigInteger, getBigInteger, getBigInteger, getBoolean, getBoolean, getBoolean, getByte, getByte, getByte, getBytes, getBytes, getBytes, getChangeSummary, getChar, getChar, getChar, getContainer, getContainmentProperty, getDataGraph, getDataObject, getDataObject, getDataObject, getDate, getDate, getDate, getDouble, getDouble, getDouble, getFloat, getFloat, getFloat, getInstanceProperties, getInstanceProperty, getInt, getInt, getInt, getList, getList, getList, getLong, getLong, getLong, getProperty, getRootObject, getSequence, getSequence, getSequence, getSequence, getShort, getShort, getShort, getString, getString, getString, getType, isSet, isSet, isSet, set, set, set, setBigDecimal, setBigDecimal, setBigDecimal, setBigInteger, setBigInteger, setBigInteger, setBoolean, setBoolean, setBoolean, setByte, setByte, setByte, setBytes, setBytes, setBytes, setChar, setChar, setChar, setDataObject, setDataObject, setDataObject, setDate, setDate, setDate, setDouble, setDouble, setDouble, setFloat, setFloat, setFloat, setInt, setInt, setInt, setList, setList, setList, setLong, setLong, setLong, setShort, setShort, setShort, setString, setString, setString, unset, unset, unset