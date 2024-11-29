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

## Interface JspLocation

- All Superinterfaces:
java.lang.Cloneable, java.io.Serializable

public interface JspLocation
extends java.io.Serializable, java.lang.Cloneable
Interface to retrieve JSP locations of a Web client setting.
 
 A <jsp> element is defined as follows:
 

<tel:webClientSettings clientType="Web Client">*
 
 <tel:customSetting name="name" value="value"?/>*
 
 <tel:jsp for="page|input|output|map|fault"
 uri="jspURI" contextRoot="contextRoot">+
 
 <tel:applyTo role="role"/>
 
</tel:jsp>
 
</tel:webClientSettings>
 
Since:
5.1

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
getApplyTo()
Returns the roles that are associated with this JSP location.

java.lang.String
getContextRoot()
Returns the context root of the JSP.

java.lang.String
getFaultName()
Returns the fault name provided that the JSP location describes a JSP for a fault.

java.net.URI
getUri()
Returns the URI of the JSP.

java.lang.String
getUriAsString()
Deprecated. 
Use method getUri() instead.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getUriAsString
java.lang.String getUriAsString()
Deprecated. Use method getUri() instead.
Returns the URI of the JSP represented as a string.
Returns:String -
    A string representation of the URI.
    - getUri
java.net.URI getUri()
Returns the URI of the JSP.
Returns:URI -
    The URI of the JSP.Since:
6.0.2
    - getContextRoot
java.lang.String getContextRoot()
Returns the context root of the JSP. Returns null when the context root is not set.
Returns:String -
    The context root of the JSP.
    - getApplyTo
java.util.List getApplyTo()
Returns the roles that are associated with this JSP location.
Returns:List -
    List of JspApplicableRoleEnum objects. Refer to JspApplicableRoleEnumSince:
6.0
    - getFaultName
java.lang.String getFaultName()
Returns the fault name provided that the JSP location describes a JSP for a fault.
 Returns null when the JSP location does not describe a fault JSP.
Returns:String -
    The fault name when the JSP location describes a fault JSP; otherwise null.Since:
6.0