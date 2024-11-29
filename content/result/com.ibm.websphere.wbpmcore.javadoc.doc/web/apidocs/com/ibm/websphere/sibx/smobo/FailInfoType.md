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

## Interface FailInfoType

- public interface FailInfoType A representation of the model object 'Fail Info Type '. There are two sequences that are maintained within the Fail Info. The first is used to reflect nested exceptions. This sequence starts with the current Fail Info. Each Fail Info Type then points to a predecessor Fail Info, with the exception of the first in the chain where its predecessor will be null. The second of the two sequences represents the path through the flow that the message took before reaching the primitive at which it failed. This sequence is represented by a list of PrimitiveType elements as documented below. The following features are supported:

```
public interface FailInfoType
```

There are two sequences
 that are maintained within the Fail Info.  The first is used to reflect nested
 exceptions.  This sequence starts with the current Fail Info.  Each Fail Info Type 
 then points to a predecessor Fail Info, with the exception of the first in the chain where its
 predecessor will be null.

The second of the two sequences represents the path through the flow that the message took before
 reaching the primitive at which it failed.  This sequence is represented by a list of PrimitiveType
 elements as documented below.  

 
 The following features are supported:
 
Failure String
Origin
Invocation Path
Predecessor
Lang

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getFailureString()
Returns the value of the 'Failure String' attribute.

InvocationPathType
getInvocationPath()
Returns the value of the 'Invocation Path' containment reference.

java.lang.String
getLang()
Returns the value of the 'Lang' attribute.

java.lang.String
getOrigin()
Returns the value of the 'Origin' attribute.

FailInfoType
getPredecessor()
Returns the value of the 'Predecessor' containment reference.

void
setFailureString(java.lang.String value)
Sets the value of the 'Failure String' attribute.

void
setInvocationPath(InvocationPathType value)
Sets the value of the 'Invocation Path' containment reference.

void
setLang(java.lang.String value)
Sets the value of the 'Lang' attribute.

void
setOrigin(java.lang.String value)
Sets the value of the 'Origin' attribute.

void
setPredecessor(FailInfoType value)
Sets the value of the 'Predecessor' containment reference.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- $sccsid
static final java.lang.String $sccsid
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getFailureString
java.lang.String getFailureString()
Returns the value of the 'Failure String' attribute.
 
 A string indicating the cause of the failure.
 
Returns:the value of the 'Failure String' attribute.See Also:setFailureString(String)
    - setFailureString
void setFailureString(java.lang.String value)
Sets the value of the 'Failure String' attribute.
Parameters:value - the new value of the 'Failure String' attribute.See Also:getFailureString()
    - getOrigin
java.lang.String getOrigin()
Returns the value of the 'Origin' attribute.
 
 Name of the failing flow primitive.
 
Returns:the value of the 'Origin' attribute.See Also:setOrigin(String)
    - setOrigin
void setOrigin(java.lang.String value)
Sets the value of the 'Origin' attribute.
Parameters:value - the new value of the 'Origin' attribute.See Also:getOrigin()
    - getInvocationPath
InvocationPathType getInvocationPath()
Returns the value of the 'Invocation Path' containment reference.
Returns:the value of the 'Invocation Path' containment reference.See Also:setInvocationPath(InvocationPathType)
    - setInvocationPath
void setInvocationPath(InvocationPathType value)
Sets the value of the 'Invocation Path' containment reference.
Parameters:value - the new value of the 'Invocation Path' containment reference.See Also:getInvocationPath()
    - getPredecessor
FailInfoType getPredecessor()
Returns the value of the 'Predecessor' containment reference.
Returns:the value of the 'Predecessor' containment reference.See Also:setPredecessor(FailInfoType)
    - setPredecessor
void setPredecessor(FailInfoType value)
Sets the value of the 'Predecessor' containment reference.
Parameters:value - the new value of the 'Predecessor' containment reference.See Also:getPredecessor()
    - getLang
java.lang.String getLang()
Returns the value of the 'Lang' attribute.
 This denotes an attribute whose value
 is a language code for the natural language of the content of
 any element; its value is inherited.  This name is reserved
 by virtue of its definition in the XML specification.
Returns:the value of the 'Lang' attribute.See Also:setLang(String)
    - setLang
void setLang(java.lang.String value)
Sets the value of the 'Lang' attribute.
Parameters:value - the new value of the 'Lang' attribute.See Also:getLang()