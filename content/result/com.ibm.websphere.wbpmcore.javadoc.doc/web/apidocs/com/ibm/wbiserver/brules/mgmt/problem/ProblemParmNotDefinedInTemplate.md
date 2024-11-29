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

## Class ProblemParmNotDefinedInTemplate

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemParmNotDefinedInTemplate

- All Implemented Interfaces:
java.io.Serializable

public class ProblemParmNotDefinedInTemplate
extends Problem
implements java.io.Serializable
Problem class representing the error that a parameter value was specified for a parameter
 that is not defined on the template for which an instance is being created.  This error occurs 
 when attempting to create an instance based on a template and one of the values specified is
 for a parameter that is not defined on this template.
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

ProblemParmNotDefinedInTemplate(Parameter parameter,
                               Template template,
                               java.util.List<ParameterValue> parameterValueList)
Constructor for the ProblemParmNotDefinedInTemplate class.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getErrorMessage () Parameter getParameter () Get the parameter that is not defined on this template. java.util.List<ParameterValue > getParameterValueList () Get the list of parameter values. Template getTemplate () Get the template that was being instantiated.

### Method Summary

| Modifier and Type              | Method and Description                                                 |
|--------------------------------|------------------------------------------------------------------------|
| java.lang.String               | getErrorMessage()                                                      |
| Parameter                      | getParameter() Get the parameter that is not defined on this template. |
| java.util.List<ParameterValue> | getParameterValueList() Get the list of parameter values.              |
| Template                       | getTemplate() Get the template that was being instantiated.            |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait