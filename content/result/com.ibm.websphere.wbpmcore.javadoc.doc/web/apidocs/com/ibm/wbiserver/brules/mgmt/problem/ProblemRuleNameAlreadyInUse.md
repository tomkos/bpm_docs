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

## Class ProblemRuleNameAlreadyInUse

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemRuleNameAlreadyInUse

- All Implemented Interfaces:
java.io.Serializable

public class ProblemRuleNameAlreadyInUse
extends Problem
implements java.io.Serializable
Problem class representing the error that the name of the new rule being added to the
 rule block is already in use for another rule in that rule block.
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

ProblemRuleNameAlreadyInUse(java.lang.String newRuleName,
                           Rule existingRuleUsingName,
                           RuleBlock ruleBlock)
Constructor for the ProblemRuleNameAlreadyInUse class.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getErrorMessage () Rule getExistingRuleUsingName () Get the existing rule that is already using the name. java.lang.String getNewRuleName () Get the name of the new rule that is in error. RuleBlock getRuleBlock () Get the rule block to which the rule was being added.

### Method Summary

| Modifier and Type   | Method and Description                                                           |
|---------------------|----------------------------------------------------------------------------------|
| java.lang.String    | getErrorMessage()                                                                |
| Rule                | getExistingRuleUsingName() Get the existing rule that is already using the name. |
| java.lang.String    | getNewRuleName() Get the name of the new rule that is in error.                  |
| RuleBlock           | getRuleBlock() Get the rule block to which the rule was being added.             |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait