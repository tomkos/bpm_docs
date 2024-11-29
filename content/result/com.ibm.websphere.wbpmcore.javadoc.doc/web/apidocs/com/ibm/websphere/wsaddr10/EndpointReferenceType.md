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

## Interface EndpointReferenceType

- All Superinterfaces: commonj.sdo.DataObject, java.io.Serializable public interface EndpointReferenceType extends commonj.sdo.DataObject begin-user-doc A representation of the model object 'Endpoint Reference Type '. end-user-doc The following features are supported:

```
public interface EndpointReferenceType
extends commonj.sdo.DataObject
```

The following features are supported:
 
Address
Reference Parameters
Metadata
Any
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
    - Method Summary Methods Modifier and Type Method and Description AttributedURIType getAddress () Returns the value of the 'Address ' containment reference. commonj.sdo.Sequence getAny () Deprecated. commonj.sdo.Sequence getAnyAttribute () Deprecated. MetadataType getMetadata () Returns the value of the 'Metadata ' containment reference. ReferenceParametersType getReferenceParameters () Returns the value of the 'Reference Parameters ' containment reference. void setAddress (AttributedURIType value) Sets the value of the 'Address ' containment reference. void setMetadata (MetadataType value) Sets the value of the 'Metadata ' containment reference. void setReferenceParameters (ReferenceParametersType value) Sets the value of the 'Reference Parameters ' containment reference.

### Method Summary

| Modifier and Type       | Method and Description                                                                                                    |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------|
| AttributedURIType       | getAddress() Returns the value of the 'Address' containment reference.                                                    |
| commonj.sdo.Sequence    | getAny() Deprecated.                                                                                                      |
| commonj.sdo.Sequence    | getAnyAttribute() Deprecated.                                                                                             |
| MetadataType            | getMetadata() Returns the value of the 'Metadata' containment reference.                                                  |
| ReferenceParametersType | getReferenceParameters() Returns the value of the 'Reference Parameters' containment reference.                           |
| void                    | setAddress(AttributedURIType value) Sets the value of the 'Address' containment reference.                                |
| void                    | setMetadata(MetadataType value) Sets the value of the 'Metadata' containment reference.                                   |
| void                    | setReferenceParameters(ReferenceParametersType value) Sets the value of the 'Reference Parameters' containment reference. |

- Methods inherited from interface commonj.sdo.DataObject
createDataObject, createDataObject, createDataObject, createDataObject, createDataObject, createDataObject, delete, detach, get, get, get, getBigDecimal, getBigDecimal, getBigDecimal, getBigInteger, getBigInteger, getBigInteger, getBoolean, getBoolean, getBoolean, getByte, getByte, getByte, getBytes, getBytes, getBytes, getChangeSummary, getChar, getChar, getChar, getContainer, getContainmentProperty, getDataGraph, getDataObject, getDataObject, getDataObject, getDate, getDate, getDate, getDouble, getDouble, getDouble, getFloat, getFloat, getFloat, getInstanceProperties, getInstanceProperty, getInt, getInt, getInt, getList, getList, getList, getLong, getLong, getLong, getProperty, getRootObject, getSequence, getSequence, getSequence, getSequence, getShort, getShort, getShort, getString, getString, getString, getType, isSet, isSet, isSet, set, set, set, setBigDecimal, setBigDecimal, setBigDecimal, setBigInteger, setBigInteger, setBigInteger, setBoolean, setBoolean, setBoolean, setByte, setByte, setByte, setBytes, setBytes, setBytes, setChar, setChar, setChar, setDataObject, setDataObject, setDataObject, setDate, setDate, setDate, setDouble, setDouble, setDouble, setFloat, setFloat, setFloat, setInt, setInt, setInt, setList, setList, setList, setLong, setLong, setLong, setShort, setShort, setShort, setString, setString, setString, unset, unset, unset