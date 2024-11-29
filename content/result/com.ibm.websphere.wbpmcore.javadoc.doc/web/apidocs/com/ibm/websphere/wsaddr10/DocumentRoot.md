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

## Interface DocumentRoot

- All Superinterfaces: commonj.sdo.DataObject, java.io.Serializable public interface DocumentRoot extends commonj.sdo.DataObject begin-user-doc A representation of the model object 'Document Root '. end-user-doc The following features are supported:

```
public interface DocumentRoot
extends commonj.sdo.DataObject
```

The following features are supported:
 
Mixed
XMLNS Prefix Map
XSI Schema Location
Action
Endpoint Reference
Fault To
From
Message ID
Metadata
Problem Action
Problem Header QName
Problem IRI
Reference Parameters
Relates To
Reply To
Retry After
To
Is Reference Parameter

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description AttributedURIType getAction () Returns the value of the 'Action ' containment reference. EndpointReferenceType getEndpointReference () Returns the value of the 'Endpoint Reference ' containment reference. EndpointReferenceType getFaultTo () Returns the value of the 'Fault To ' containment reference. EndpointReferenceType getFrom () Returns the value of the 'From ' containment reference. AttributedURIType getMessageID () Returns the value of the 'Message ID ' containment reference. MetadataType getMetadata () Returns the value of the 'Metadata ' containment reference. commonj.sdo.Sequence getMixed () Returns the value of the 'Mixed ' attribute list. ProblemActionType getProblemAction () Returns the value of the 'Problem Action ' containment reference. AttributedQNameType getProblemHeaderQName () Returns the value of the 'Problem Header QName ' containment reference. AttributedURIType getProblemIRI () Returns the value of the 'Problem IRI ' containment reference. ReferenceParametersType getReferenceParameters () Returns the value of the 'Reference Parameters ' containment reference. RelatesToType getRelatesTo () Returns the value of the 'Relates To ' containment reference. EndpointReferenceType getReplyTo () Returns the value of the 'Reply To ' containment reference. AttributedUnsignedLongType getRetryAfter () Returns the value of the 'Retry After ' containment reference. AttributedURIType getTo () Returns the value of the 'To ' containment reference. java.util.Map getXMLNSPrefixMap () Returns the value of the 'XMLNS Prefix Map ' map. java.util.Map getXSISchemaLocation () Returns the value of the 'XSI Schema Location ' map. boolean isIsReferenceParameter () Returns the value of the 'Is Reference Parameter ' attribute. boolean isSetIsReferenceParameter () Returns whether the value of the 'Is Reference Parameter ' attribute is set. void setAction (AttributedURIType value) Sets the value of the 'Action ' containment reference. void setEndpointReference (EndpointReferenceType value) Sets the value of the 'Endpoint Reference ' containment reference. void setFaultTo (EndpointReferenceType value) Sets the value of the 'Fault To ' containment reference. void setFrom (EndpointReferenceType value) Sets the value of the 'From ' containment reference. void setIsReferenceParameter (boolean value) Sets the value of the 'Is Reference Parameter ' attribute. void setMessageID (AttributedURIType value) Sets the value of the 'Message ID ' containment reference. void setMetadata (MetadataType value) Sets the value of the 'Metadata ' containment reference. void setProblemAction (ProblemActionType value) Sets the value of the 'Problem Action ' containment reference. void setProblemHeaderQName (AttributedQNameType value) Sets the value of the 'Problem Header QName ' containment reference. void setProblemIRI (AttributedURIType value) Sets the value of the 'Problem IRI ' containment reference. void setReferenceParameters (ReferenceParametersType value) Sets the value of the 'Reference Parameters ' containment reference. void setRelatesTo (RelatesToType value) Sets the value of the 'Relates To ' containment reference. void setReplyTo (EndpointReferenceType value) Sets the value of the 'Reply To ' containment reference. void setRetryAfter (AttributedUnsignedLongType value) Sets the value of the 'Retry After ' containment reference. void setTo (AttributedURIType value) Sets the value of the 'To ' containment reference. void unsetIsReferenceParameter () Unsets the value of the 'Is Reference Parameter ' attribute.

### Method Summary

| Modifier and Type          | Method and Description                                                                                                    |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------|
| AttributedURIType          | getAction() Returns the value of the 'Action' containment reference.                                                      |
| EndpointReferenceType      | getEndpointReference() Returns the value of the 'Endpoint Reference' containment reference.                               |
| EndpointReferenceType      | getFaultTo() Returns the value of the 'Fault To' containment reference.                                                   |
| EndpointReferenceType      | getFrom() Returns the value of the 'From' containment reference.                                                          |
| AttributedURIType          | getMessageID() Returns the value of the 'Message ID' containment reference.                                               |
| MetadataType               | getMetadata() Returns the value of the 'Metadata' containment reference.                                                  |
| commonj.sdo.Sequence       | getMixed() Returns the value of the 'Mixed' attribute list.                                                               |
| ProblemActionType          | getProblemAction() Returns the value of the 'Problem Action' containment reference.                                       |
| AttributedQNameType        | getProblemHeaderQName() Returns the value of the 'Problem Header QName' containment reference.                            |
| AttributedURIType          | getProblemIRI() Returns the value of the 'Problem IRI' containment reference.                                             |
| ReferenceParametersType    | getReferenceParameters() Returns the value of the 'Reference Parameters' containment reference.                           |
| RelatesToType              | getRelatesTo() Returns the value of the 'Relates To' containment reference.                                               |
| EndpointReferenceType      | getReplyTo() Returns the value of the 'Reply To' containment reference.                                                   |
| AttributedUnsignedLongType | getRetryAfter() Returns the value of the 'Retry After' containment reference.                                             |
| AttributedURIType          | getTo() Returns the value of the 'To' containment reference.                                                              |
| java.util.Map              | getXMLNSPrefixMap() Returns the value of the 'XMLNS Prefix Map' map.                                                      |
| java.util.Map              | getXSISchemaLocation() Returns the value of the 'XSI Schema Location' map.                                                |
| boolean                    | isIsReferenceParameter() Returns the value of the 'Is Reference Parameter' attribute.                                     |
| boolean                    | isSetIsReferenceParameter() Returns whether the value of the 'Is Reference Parameter' attribute is set.                   |
| void                       | setAction(AttributedURIType value) Sets the value of the 'Action' containment reference.                                  |
| void                       | setEndpointReference(EndpointReferenceType value) Sets the value of the 'Endpoint Reference' containment reference.       |
| void                       | setFaultTo(EndpointReferenceType value) Sets the value of the 'Fault To' containment reference.                           |
| void                       | setFrom(EndpointReferenceType value) Sets the value of the 'From' containment reference.                                  |
| void                       | setIsReferenceParameter(boolean value) Sets the value of the 'Is Reference Parameter' attribute.                          |
| void                       | setMessageID(AttributedURIType value) Sets the value of the 'Message ID' containment reference.                           |
| void                       | setMetadata(MetadataType value) Sets the value of the 'Metadata' containment reference.                                   |
| void                       | setProblemAction(ProblemActionType value) Sets the value of the 'Problem Action' containment reference.                   |
| void                       | setProblemHeaderQName(AttributedQNameType value) Sets the value of the 'Problem Header QName' containment reference.      |
| void                       | setProblemIRI(AttributedURIType value) Sets the value of the 'Problem IRI' containment reference.                         |
| void                       | setReferenceParameters(ReferenceParametersType value) Sets the value of the 'Reference Parameters' containment reference. |
| void                       | setRelatesTo(RelatesToType value) Sets the value of the 'Relates To' containment reference.                               |
| void                       | setReplyTo(EndpointReferenceType value) Sets the value of the 'Reply To' containment reference.                           |
| void                       | setRetryAfter(AttributedUnsignedLongType value) Sets the value of the 'Retry After' containment reference.                |
| void                       | setTo(AttributedURIType value) Sets the value of the 'To' containment reference.                                          |
| void                       | unsetIsReferenceParameter() Unsets the value of the 'Is Reference Parameter' attribute.                                   |

- Methods inherited from interface commonj.sdo.DataObject
createDataObject, createDataObject, createDataObject, createDataObject, createDataObject, createDataObject, delete, detach, get, get, get, getBigDecimal, getBigDecimal, getBigDecimal, getBigInteger, getBigInteger, getBigInteger, getBoolean, getBoolean, getBoolean, getByte, getByte, getByte, getBytes, getBytes, getBytes, getChangeSummary, getChar, getChar, getChar, getContainer, getContainmentProperty, getDataGraph, getDataObject, getDataObject, getDataObject, getDate, getDate, getDate, getDouble, getDouble, getDouble, getFloat, getFloat, getFloat, getInstanceProperties, getInstanceProperty, getInt, getInt, getInt, getList, getList, getList, getLong, getLong, getLong, getProperty, getRootObject, getSequence, getSequence, getSequence, getSequence, getShort, getShort, getShort, getString, getString, getString, getType, isSet, isSet, isSet, set, set, set, setBigDecimal, setBigDecimal, setBigDecimal, setBigInteger, setBigInteger, setBigInteger, setBoolean, setBoolean, setBoolean, setByte, setByte, setByte, setBytes, setBytes, setBytes, setChar, setChar, setChar, setDataObject, setDataObject, setDataObject, setDate, setDate, setDate, setDouble, setDouble, setDouble, setFloat, setFloat, setFloat, setInt, setInt, setInt, setList, setList, setList, setLong, setLong, setLong, setShort, setShort, setShort, setString, setString, setString, unset, unset, unset