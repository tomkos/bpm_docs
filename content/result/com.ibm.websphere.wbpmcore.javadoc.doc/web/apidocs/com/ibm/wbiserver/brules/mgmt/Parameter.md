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

## Interface Parameter

- All Superinterfaces:
java.io.Serializable

public interface Parameter
extends java.io.Serializable
This interface represents one template parameter.  Each parameter has a name, a data type,
 and an optional constraint.  The constraint, if present, specifies constraints on the
 value for this parameter.  For example, the constraint may specify that a numeric 
 parameter must be within the range from 0 to 100.
 
 A method is provided to create a new ParameterValue object to represent
 a value for this parameter.  This method would be used when new parameter values need
 to be specified when creating a new template instance.  There is also a method to 
 validate that a given value is valid for this parameter given the data type and 
 any defined constraints.

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

ParameterValue
createParameterValue(java.lang.String value)
Create a new ParameterValue object for the parameter represented by this
 object.

Constraint
getConstraint()
Get the constraints, if any, for the values for this variable.

ParameterDataType
getDataType()
Get the data type of this variable.

Template
getDefiningTemplate()
Get the template in which this parameter is defined.

java.lang.String
getDescription()
Get the description associated with this parameter.

java.lang.String
getDisplayName()
Get the display name for this parameter.

java.lang.String
getName()
Get the name of this variable.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getName
java.lang.String getName()
Get the name of this variable.
Returns:The name of this variable.
    - getDescription
java.lang.String getDescription()
Get the description associated with this parameter.
Returns:The description associated with this parameter.  May be null.
    - getDisplayName
java.lang.String getDisplayName()
Get the display name for this parameter.  The display name may have been
 specified during development of the parameter to give a name that is more
 understandable to the business user.
Returns:the display name of this parameter.  May be null.
    - getDataType
ParameterDataType getDataType()
Get the data type of this variable.
Returns:The data type of this variable.
    - getConstraint
Constraint getConstraint()
Get the constraints, if any, for the values for this variable.
Returns:The Constraint object that specifies the constraints for the value
 for this variable or null if there are no constraints.
    - getDefiningTemplate
Template getDefiningTemplate()
Get the template in which this parameter is defined.
Returns:The template in which this parameter is defined.
    - createParameterValue
ParameterValue createParameterValue(java.lang.String value)
                                    throws ValidationException
Create a new ParameterValue object for the parameter represented by this
 object.  The new object represents the specified value for this parameter.  This method 
 can be used to create ParameterValue objects to be used when creating a 
 template instances based on a particular template.  The specified value is checked to 
 ensure that it is valid for this parameter given the parameter's data type and any 
 defined constraints.  The value must be convertible, using standard Java methods, to 
 the type of the parameter.  For example, if the type of the parameter is double, then 
 it must be possible to convert the valueto a Java double using the 
 Double.valueOf() method.  Note that for boolean types the only allowed
 values are the strings "true" and "false", all lower case.
Parameters:value - The value for the template parameter in string form.  This value must be
 convertible, using standard Java methods, to the type of the parameter.  null is not 
 allowed unless the type of the parameter is string.
Returns:A new ParameterValue representing the specified value for the 
 specified parameter.
Throws:
ValidationException - if any validation errors are detected as defined above.
java.lang.IllegalArgumentException - if the specified value is null and the type of the
 parameter is not string.
ChangesNotAllowedException - if changes related to this object are temporarily 
 disallowed while other changes are being published.