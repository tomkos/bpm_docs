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

## Interface MQRFH2Group

- public interface MQRFH2Group begin-user-doc A representation of the model object 'MQRFH2 Group '. end-user-doc The following features are supported: See Also: WMQStructuresPackage.getMQRFH2Group()

```
public interface MQRFH2Group
```

The following features are supported:
 
Name
Rfh2 Contents
Group
Property

- ========== METHOD SUMMARY ===========
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.util.List
getGroup()
Returns the value of the 'Group' containment reference list.

java.lang.String
getName()
Returns the value of the 'Name' attribute

java.util.List
getProperty()
Returns the value of the 'Property' containment reference list.

commonj.sdo.Sequence
getRfh2Contents()
Returns the value of the 'Rfh2 Contents' attribute list

void
setName(java.lang.String value)
Sets the value of the 'Name' attribute

- ============ METHOD DETAIL ==========
    - Method Detail

### Method Detail

- getName
java.lang.String getName()
Returns the value of the 'Name' attribute.
 

 If the meaning of the 'Name' attribute isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Name' attribute.See Also:setName(String), 
WMQStructuresPackage.getMQRFH2Group\_Name()

- setName
void setName(java.lang.String value)
Sets the value of the 'Name' attribute.
 

Parameters:value - the new value of the 'Name' attribute.See Also:getName()

- getRfh2Contents
commonj.sdo.Sequence getRfh2Contents()
Returns the value of the 'Rfh2 Contents' attribute list.
 

 If the meaning of the 'Rfh2 Contents' attribute list isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Rfh2 Contents' attribute list.See Also:WMQStructuresPackage.getMQRFH2Group\_Rfh2Contents()

- getGroup
java.util.List getGroup()
Returns the value of the 'Group' containment reference list.
 The list contents are of type MQRFH2Group.
 

 If the meaning of the 'Group' containment reference list isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Group' containment reference list.See Also:WMQStructuresPackage.getMQRFH2Group\_Group()

- getProperty
java.util.List getProperty()
Returns the value of the 'Property' containment reference list.
 The list contents are of type MQRFH2Property.
 

 If the meaning of the 'Property' containment reference list isn't clear,
 there really should be more of a description here...
 

Returns:the value of the 'Property' containment reference list.See Also:WMQStructuresPackage.getMQRFH2Group\_Property()