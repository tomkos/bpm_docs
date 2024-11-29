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

## Class ProblemTemplateNotAssociatedWithRuleSet

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemTemplateNotAssociatedWithRuleSet

- All Implemented Interfaces:
java.io.Serializable

public class ProblemTemplateNotAssociatedWithRuleSet
extends Problem
implements java.io.Serializable
Problem class representing the error that the template associated with the specified rule
 is not associated with the ruleset to which the rule is being added.
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

ProblemTemplateNotAssociatedWithRuleSet(TemplateInstanceRule ruleBeingAdded,
                                       RuleSet ruleSet)
Constructor for the ProblemTemplateNotAssociatedWithRuleSet class.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getErrorMessage () TemplateInstanceRule getRuleBeingAdded () Get the rule being added to the ruleset. RuleSet getRuleSet () Get the ruleset to which the rule was being added.

### Method Summary

| Modifier and Type    | Method and Description                                          |
|----------------------|-----------------------------------------------------------------|
| java.lang.String     | getErrorMessage()                                               |
| TemplateInstanceRule | getRuleBeingAdded() Get the rule being added to the ruleset.    |
| RuleSet              | getRuleSet() Get the ruleset to which the rule was being added. |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait