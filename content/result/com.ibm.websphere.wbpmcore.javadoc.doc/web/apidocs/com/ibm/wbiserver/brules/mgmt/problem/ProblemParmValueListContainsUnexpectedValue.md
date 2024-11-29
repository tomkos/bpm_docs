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

## Class ProblemParmValueListContainsUnexpectedValue

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemParmValueListContainsUnexpectedValue

- All Implemented Interfaces:
java.io.Serializable

public class ProblemParmValueListContainsUnexpectedValue
extends Problem
implements java.io.Serializable
Problem class representing the error that a parameter value was specified that does not
 correspond to any parameter on the specified template.  This error can occur when an
 instance of a template is being created.
See Also:Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Constructor Summary

Constructors 

Constructor and Description

ProblemParmValueListContainsUnexpectedValue(ParameterValue unexpectedParameterValue,
                                           Template template,
                                           java.util.List<ParameterValue> parameterValueList)
Constructor for the ProblemParmValueListContainsUnexpectedValue class.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getErrorMessage () java.util.List<ParameterValue > getParameterValueList () Get the list of parameter values. Template getTemplate () Get the template that was being instantiated. ParameterValue getUnexpectedParameterValue () Get the parameter value that does not have a corresponding template parameter.

### Method Summary

| Modifier and Type              | Method and Description                                                                                       |
|--------------------------------|--------------------------------------------------------------------------------------------------------------|
| java.lang.String               | getErrorMessage()                                                                                            |
| java.util.List<ParameterValue> | getParameterValueList() Get the list of parameter values.                                                    |
| Template                       | getTemplate() Get the template that was being instantiated.                                                  |
| ParameterValue                 | getUnexpectedParameterValue() Get the parameter value that does not have a corresponding template parameter. |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait