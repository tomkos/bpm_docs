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

## Interface MessageWrapper

- public interface MessageWrapper
The MessageWrapper interface is used to wrap Service Data Objects (SDO) and their Web client settings.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
(C) Copyright IBM Corporation 2005.
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getContextRoot()
Returns the context root for the customized JSP.

java.lang.String
getFaultName()
Returns the fault name.

java.lang.Object
getMessage()
Returns the message.

java.lang.String
getUrl()
Returns the URL of the customized JSP.

void
setContextRoot(java.lang.String contextRoot)
Sets the context root for the customized JSP.

void
setFaultName(java.lang.String faultName)
Sets the fault name.

void
setMessage(java.lang.Object message)
Sets the message.

void
setUrl(java.lang.String url)
Sets the URL of the customized JSP.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
(C) Copyright IBM Corporation 2005.
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getContextRoot
java.lang.String getContextRoot()
Returns the context root for the customized JSP.
Returns:The context root.
    - setContextRoot
void setContextRoot(java.lang.String contextRoot)
Sets the context root for the customized JSP.
Parameters:contextRoot - The context root.
    - getUrl
java.lang.String getUrl()
Returns the URL of the customized JSP.
Returns:The URL.
    - setUrl
void setUrl(java.lang.String url)
Sets the URL of the customized JSP.
Parameters:url - The URL.
    - getMessage
java.lang.Object getMessage()
Returns the message.
Returns:The message.
    - setMessage
void setMessage(java.lang.Object message)
Sets the message.
Parameters:message - The message.
    - getFaultName
java.lang.String getFaultName()
Returns the fault name.
Returns:The fault name.
    - setFaultName
void setFaultName(java.lang.String faultName)
Sets the fault name.
Parameters:faultName - The fault name.