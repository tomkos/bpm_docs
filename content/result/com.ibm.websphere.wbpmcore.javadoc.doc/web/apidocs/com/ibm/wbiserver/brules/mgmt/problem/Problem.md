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

## Class Problem

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem

- All Implemented Interfaces:
java.io.Serializable

Direct Known Subclasses:
ProblemBusRuleNotInAvailTargetList, ProblemCaseEdgeChildNodeMissing, ProblemCaseEdgesAreMissing, ProblemCaseEdgeValueDefinitionMissing, ProblemDuplicatePropertyName, ProblemInvalidActionValueTemplate, ProblemInvalidAttemptToSetValueTemplateInstance, ProblemInvalidBooleanValue, ProblemInvalidConditionValueTemplate, ProblemNoTemplatesAvailableForNewActionNodes, ProblemOperationContainsNoTargets, ProblemOverlappingRanges, ProblemParmNotDefinedInTemplate, ProblemParmValueListContainsUnexpectedValue, ProblemRootNodeIsMissing, ProblemRuleBlockContainsNoRules, ProblemRuleNameAlreadyInUse, ProblemStartDateAfterEndDate, ProblemTargetBusRuleNotSet, ProblemTemplateNotAssociatedWithRuleSet, ProblemTemplateParameterNotSpecified, ProblemTNSAndNameAlreadyInUse, ProblemTreeActionTermIsMissing, ProblemTreeConditionIsMissing, ProblemTypeConversionError, ProblemValueTemplateInstanceIsMissing, ProblemValueViolatesParmConstraints, ProblemWrongNumberOfParameterValues, ProblemWrongOperationForOpSelectionRecord

public abstract class Problem
extends java.lang.Object
implements java.io.Serializable
This class represents one problem found during validation.  This is an abstract base class.
 Specific problems are represented by specific subclasses.
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

Problem(ValidationError errorType)
    - Method Summary Methods Modifier and Type Method and Description abstract java.lang.String getErrorMessage () ValidationError getErrorType () Get the error type for this problem.

### Method Summary

| Modifier and Type         | Method and Description                              |
|---------------------------|-----------------------------------------------------|
| abstract java.lang.String | getErrorMessage()                                   |
| ValidationError           | getErrorType() Get the error type for this problem. |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait