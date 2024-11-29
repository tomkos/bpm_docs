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

## Class ProblemWrongNumberOfParameterValues

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemWrongNumberOfParameterValues

- All Implemented Interfaces:
java.io.Serializable

public class ProblemWrongNumberOfParameterValues
extends Problem
implements java.io.Serializable
Problem class representing the error that the number of parameter values specified does
 not equal the number of parameters.  This error can happen when creating a template
 instance rule or a template instance expression from a template and the wrong number of
 parameters is specified.
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

ProblemWrongNumberOfParameterValues(Template template,
                                   java.util.List<ParameterValue> parameterValues)
Constructor for the ProblemWrongNumberOfParameterValues class.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getErrorMessage () java.util.List<ParameterValue > getParameterValues () Get the list of parameter values specified. Template getTemplate () Get the template involved in the error.

### Method Summary

| Modifier and Type              | Method and Description                                           |
|--------------------------------|------------------------------------------------------------------|
| java.lang.String               | getErrorMessage()                                                |
| java.util.List<ParameterValue> | getParameterValues() Get the list of parameter values specified. |
| Template                       | getTemplate() Get the template involved in the error.            |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait