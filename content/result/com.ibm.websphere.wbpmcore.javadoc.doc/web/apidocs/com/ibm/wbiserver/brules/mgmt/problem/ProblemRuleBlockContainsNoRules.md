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

## Class ProblemRuleBlockContainsNoRules

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemRuleBlockContainsNoRules

- All Implemented Interfaces:
java.io.Serializable

public class ProblemRuleBlockContainsNoRules
extends Problem
implements java.io.Serializable
Problem class representing the error that the rule block contains no rules.  A rule block
 must contain at least one rule.
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

ProblemRuleBlockContainsNoRules(RuleBlock ruleBlock)
Constructor for the ProblemRuleBlockContainsNoRules class.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getErrorMessage () RuleBlock getRuleBlock () Get the rule block that contains no rules.

### Method Summary

| Modifier and Type   | Method and Description                                    |
|---------------------|-----------------------------------------------------------|
| java.lang.String    | getErrorMessage()                                         |
| RuleBlock           | getRuleBlock() Get the rule block that contains no rules. |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait