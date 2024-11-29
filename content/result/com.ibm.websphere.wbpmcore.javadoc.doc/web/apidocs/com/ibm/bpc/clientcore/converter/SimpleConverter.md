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

## Interface SimpleConverter

- public interface SimpleConverter
A SimpleConverter converts an object from or to a
 String representation (without making any assumptions about the context). 
 Implement this interface to provide basic conversion between string and 
 object representations. Returns a null value to indicate error conditions:
 it is your responsibility to handle these.

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

java.lang.Object
getAsObject(java.lang.String value,
           java.util.Locale l)
Parses a string into a Java object.

java.lang.String
getAsString(java.lang.Object obj,
           java.util.Locale l)
Converts objects to a string in the specified locale.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getAsString
java.lang.String getAsString(java.lang.Object obj,
                           java.util.Locale l)
Converts objects to a string in the specified locale.
 The default time zone is used for the conversion.
Parameters:obj - The application object or datl - The target locale
Returns:A string representation of the object, or null if an error occurs
    - getAsObject
java.lang.Object getAsObject(java.lang.String value,
                           java.util.Locale l)
Parses a string into a Java object.
 The default time zone is used for the conversion.
Parameters:value - The (possibly localized) string representation of the objectl - The locale into which the string is to be translated
Returns:An object represented by the string value, or null if an error occurs.